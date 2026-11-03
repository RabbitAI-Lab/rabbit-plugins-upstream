#!/usr/bin/env python3
"""attack_defend.py — 攻击防御（默认 dry-run）

用法:
    python attack_defend.py --input monitor-result.json --target <...> --dry-run [--apply] [--action block|harden|alert] [--output defend-result.json]
    python attack_defend.py --rollback defend-result.json --target <...> --apply

封禁操作生成回滚命令。默认白名单保护内网网段。
"""

import argparse
import json
import os
import re
import shlex
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common
from _common import run_cmd, emit_json, log, parse_target, write_audit

DEFAULT_WHITELIST = ["127.0.0.0/8", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"]
SEV_ORDER = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1, "INFO": 0}


def detect_firewall(target):
    """检测可用的防火墙后端。返回 (backend, available) 或 (None, [])。"""
    checks = [
        ("firewalld", "systemctl is-active firewalld 2>/dev/null | grep -q active && which firewall-cmd"),
        ("ufw", "which ufw 2>/dev/null && ufw status 2>/dev/null | grep -q 'Status: active'"),
        ("iptables", "which iptables 2>/dev/null && iptables -L -n 2>/dev/null | head -1"),
        ("nftables", "which nft 2>/dev/null"),
    ]
    for name, cmd in checks:
        r = run_cmd(target, cmd, timeout=10)
        if r["rc"] == 0:
            return name
    return None


def ip_in_whitelist(ip, whitelist):
    """判断 IP 是否在白名单内（支持任意前缀长度的 IPv4/IPv6 CIDR 与单 IP）。

    委托 _common.cidr_match：/24、/32、/25 等任意前缀都能正确匹配，
    非法条目跳过而非静默判 False。
    """
    return _common.cidr_match(ip, whitelist)


def block_ip(target, ip, backend, dry_run):
    """封禁单个 IP，返回 (commands, rollback_commands, ok)。"""
    if backend == "firewalld":
        cmd = f"firewall-cmd --add-source={shlex.quote(ip)} --zone=drop --permanent && firewall-cmd --reload"
        rb = f"firewall-cmd --remove-source={shlex.quote(ip)} --zone=drop --permanent && firewall-cmd --reload"
    elif backend == "ufw":
        cmd = f"ufw deny from {shlex.quote(ip)}"
        rb = f"ufw delete deny from {shlex.quote(ip)}"
    elif backend == "iptables":
        cmd = f"iptables -I INPUT -s {shlex.quote(ip)} -j DROP"
        rb = f"iptables -D INPUT -s {shlex.quote(ip)} -j DROP"
    elif backend == "nftables":
        cmd = f"nft add rule inet filter input ip saddr {shlex.quote(ip)} drop"
        rb = f"nft delete rule inet filter input ip saddr {shlex.quote(ip)} drop"
    else:
        return [], [], False
    if dry_run:
        return [f"[DRY-RUN] {cmd}"], [rb], True
    r = run_cmd(target, cmd, timeout=15)
    return [cmd], [rb], r["rc"] == 0


def do_block(target, monitor, dry_run, threshold, whitelist, explicit_ips):
    """执行封禁动作。"""
    backend = detect_firewall(target)
    if not backend:
        return {"action": "block", "status": "failed",
                "message": "无可用防火墙后端（firewalld/ufw/iptables/nftables）"}

    thresh_val = SEV_ORDER.get(threshold.upper(), 3)
    candidate_ips = set()
    for ev in monitor.get("events", []):
        if SEV_ORDER.get(ev.get("severity", "INFO"), 0) >= thresh_val:
            ip = ev.get("source_ip")
            if ip:
                candidate_ips.add((ip, ev.get("type", "unknown"), ev.get("severity", "INFO")))
    for ip in explicit_ips:
        candidate_ips.add((ip, "explicit", "HIGH"))

    blocked, skipped = [], []
    rollback_cmds = []
    for ip, reason, sev in sorted(candidate_ips):
        if ip_in_whitelist(ip, whitelist):
            skipped.append({"ip": ip, "reason": "in_whitelist"})
            continue
        cmds, rb, ok = block_ip(target, ip, backend, dry_run)
        if ok:
            blocked.append({"ip": ip, "reason": reason, "severity": sev})
            rollback_cmds.extend(rb)
            if not dry_run:
                write_audit(target, f"DEFEND ACTION=block IP={ip} REASON={reason} DRY_RUN=false")
        else:
            skipped.append({"ip": ip, "reason": "block_failed"})

    return {
        "action": "block", "backend": backend, "blocked_ips": blocked,
        "skipped_ips": skipped, "rollback_commands": rollback_cmds, "dry_run": dry_run,
        "status": "ok" if blocked or not candidate_ips else "no_candidates",
    }


SSHD_CONF = "/etc/ssh/sshd_config"


def do_harden(target, dry_run):
    """加固配置（低风险子集）。返回操作记录。

    实现 4 类加固：
      1. SSH 禁用空口令（PermitEmptyPasswords no）
      2. SSH 禁用 root 密码登录（PermitRootLogin prohibit-password，仍允许密钥）
      3. 内核参数：禁用 ICMP 重定向
      4. 内核参数：禁用源路由
    改动 sshd_config 前先备份（cp -a，时间戳后缀），备份失败则中止 SSH 项；
    所有变更都给出回滚命令，reload 兼容 sshd/ssh 两种服务名。
    """
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    bak = f"{SSHD_CONF}.guard-bak.{ts}"
    ops, rollback = [], []
    state = {"backup": None, "backup_failed": False}

    def _do(op, cmd, audit_tag):
        if dry_run:
            ops.append({"op": op, "command": f"[DRY-RUN] {cmd}", "applied": False})
            return
        rr = run_cmd(target, cmd, timeout=15)
        ops.append({"op": op, "command": cmd, "applied": rr["rc"] == 0,
                    "stderr": rr["stderr"][:200] if rr["rc"] != 0 else ""})
        write_audit(target, f"DEFEND ACTION=harden OP={audit_tag} DRY_RUN=false")

    def _ensure_backup():
        """改动 sshd_config 前备份一次。返回 False 表示必须中止 SSH 项。"""
        if state["backup_failed"]:
            return False
        if state["backup"]:
            return True
        cmd = f"cp -a {shlex.quote(SSHD_CONF)} {shlex.quote(bak)}"
        if dry_run:
            ops.append({"op": "backup_sshd_config", "command": f"[DRY-RUN] {cmd}", "applied": False})
        else:
            rr = run_cmd(target, cmd, timeout=10)
            if rr["rc"] != 0:
                state["backup_failed"] = True
                ops.append({"op": "backup_sshd_config", "command": cmd, "applied": False,
                            "stderr": rr["stderr"][:200]})
                return False
        state["backup"] = bak
        rollback.append(f"cp {shlex.quote(bak)} {shlex.quote(SSHD_CONF)} && {_common.RELOAD_SSHD}")
        return True

    # 1. SSH 禁用空口令
    r = run_cmd(target, f"grep -q 'PermitEmptyPasswords yes' {SSHD_CONF} 2>/dev/null", timeout=5)
    if r["rc"] == 0 and _ensure_backup():
        _do("ssh_no_empty_pass",
            f"sed -i 's/^PermitEmptyPasswords yes/PermitEmptyPasswords no/' {SSHD_CONF} "
            f"&& {_common.RELOAD_SSHD}",
            "ssh_no_empty_pass")

    # 2. SSH 禁用 root 密码登录（prohibit-password = 仅密钥）
    r = run_cmd(target, f"grep -q '^PermitRootLogin yes' {SSHD_CONF} 2>/dev/null", timeout=5)
    if r["rc"] == 0 and _ensure_backup():
        _do("ssh_no_root_password",
            f"sed -i 's/^PermitRootLogin yes/PermitRootLogin prohibit-password/' {SSHD_CONF} "
            f"&& {_common.RELOAD_SSHD}",
            "ssh_no_root_password")

    # 3. 内核参数：禁用 ICMP 重定向
    for param in ["net.ipv4.conf.all.accept_redirects", "net.ipv4.conf.default.accept_redirects"]:
        _do("sysctl_no_redirect", f"sysctl -w {param}=0", f"sysctl_no_redirect:{param}")
        rollback.append(f"sysctl -w {param}=1")

    # 4. 内核参数：禁用源路由
    for param in ["net.ipv4.conf.all.accept_source_route", "net.ipv4.conf.default.accept_source_route"]:
        _do("sysctl_no_source_route", f"sysctl -w {param}=0", f"sysctl_no_source_route:{param}")
        rollback.append(f"sysctl -w {param}=1")

    if state["backup_failed"]:
        status, message = "failed", f"备份 {SSHD_CONF} 失败，SSH 加固项已中止"
    elif not ops:
        status, message = "no_candidates", "未发现需要加固的项"
    else:
        status, message = "ok", f"{len(ops)} 项加固操作"

    return {
        "action": "harden", "operations": ops,
        "backup_files": [state["backup"]] if state["backup"] else [],
        "rollback_commands": rollback, "dry_run": dry_run,
        "status": status, "message": message,
    }


def do_rollback(target, rollback_file, apply):
    """执行回滚。"""
    if not os.path.exists(rollback_file):
        return {"action": "rollback", "status": "failed", "message": f"文件不存在: {rollback_file}"}
    with open(rollback_file, "r", encoding="utf-8") as f:
        prev = json.load(f)
    cmds = prev.get("rollback_commands", [])
    executed = []
    for cmd in reversed(cmds):
        if apply:
            r = run_cmd(target, cmd, timeout=15)
            executed.append({"command": cmd, "ok": r["rc"] == 0})
            write_audit(target, f"DEFEND ACTION=rollback CMD={cmd[:80]}")
        else:
            executed.append({"command": f"[DRY-RUN] {cmd}", "ok": True})
    return {"action": "rollback", "executed": executed, "dry_run": not apply, "status": "ok"}


def main():
    parser = argparse.ArgumentParser(description="攻击防御（默认 dry-run）")
    parser.add_argument("--input", help="monitor-result.json 路径")
    parser.add_argument("--target", required=True, help="local 或 ssh://user@host[:port]")
    parser.add_argument("--apply", action="store_true", help="真正执行（默认 dry-run）")
    parser.add_argument("--action", default="block", choices=["block", "harden", "alert"])
    parser.add_argument("--block-threshold", default="high", choices=["high", "medium"])
    parser.add_argument("--whitelist", help="白名单 IP/网段（逗号分隔），覆盖默认")
    parser.add_argument("--ips", help="显式指定封禁 IP（逗号分隔）")
    parser.add_argument("--rollback", help="回滚指定 defend-result.json")
    parser.add_argument("--output", help="输出 JSON 文件路径")
    args = parser.parse_args()

    dry_run = not args.apply
    try:
        parse_target(args.target)
    except ValueError as e:
        log(str(e), "ERROR")
        sys.exit(2)

    if args.rollback:
        result = do_rollback(args.target, args.rollback, args.apply)
    else:
        if not args.input:
            log("需要 --input 或 --rollback", "ERROR")
            sys.exit(2)
        if not os.path.exists(args.input):
            log(f"输入文件不存在: {args.input}", "ERROR")
            sys.exit(2)
        with open(args.input, "r", encoding="utf-8") as f:
            monitor = json.load(f)

        whitelist = (args.whitelist.split(",") if args.whitelist else DEFAULT_WHITELIST)
        explicit = [i.strip() for i in args.ips.split(",")] if args.ips else []

        if args.action == "block":
            if not dry_run and not _common.is_root(args.target):
                log("封禁需要 root 权限，切换 dry-run", "WARN")
                dry_run = True
            result = do_block(args.target, monitor, dry_run, args.block_threshold, whitelist, explicit)
        elif args.action == "harden":
            result = do_harden(args.target, dry_run)
        else:
            write_audit(args.target, f"DEFEND ACTION=alert EVENTS={len(monitor.get('events', []))}")
            result = {"action": "alert", "events": len(monitor.get("events", [])),
                      "status": "ok", "message": "已记录告警，未执行封禁/加固"}

    result["timestamp"] = datetime.now(timezone.utc).isoformat()
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        log(f"结果已写入 {args.output}")
    emit_json(result)
    log(f"防御完成: action={result.get('action')} status={result.get('status')}")


if __name__ == "__main__":
    main()
