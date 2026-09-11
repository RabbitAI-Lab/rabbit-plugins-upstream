#!/usr/bin/env python3
"""mcp_checkup.py — static security checkup of an MCP/Agent config.

Runs 14 automated STATIC checks on a supplied MCP configuration (the JSON
document you point an MCP/Agent client at). The analysis is purely static:
it never connects to any URL inside the config, never executes anything,
and by default never leaves the machine — all checks run locally via the
bundled mcp_rules module.

The 14 automated checks cover: hardcoded cloud credentials/API keys,
arbitrary shell/command execution exposure, writable filesystem / root or
home mounts, dangerous container flags, insecure transport, over-broad
tool scopes, missing timeouts/version pins, and similar high-signal
configuration issues. The 14 checks are a triage layer — they do NOT
replace manual audit of endpoint behavior, tool implementation code, or
data-flow boundaries.

Input: a config JSON file (--config) OR a single remote endpoint URL
(--endpoint-url, wrapped as a single-server http config for static checks;
no network connection is made to that URL).

Use --online ONLY if you explicitly want the Correctover hosted service
(requires CCS_API_TOKEN in the environment). Default is local, zero network.

Exit codes: 0 = checkup ran (any risk level); 2 = usage error;
            3 = online mode returned HTTP 402 (payment required).
Risk levels CRIT/HIGH/MED/LOW are findings, not process failures.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SEV_ORDER = ("CRIT", "HIGH", "MED", "LOW")

DISCLAIMER = (
    "免责声明： 本结果由 Correctover CCS 配置体检工具自动生成，仅对本次提交的输入数据负责。 "
    "自动化检查仅为辅助手段，不构成安全保证、合规结论、审计意见或法律意见。 "
    "本工具不声称获得 OWASP、IETF 等任何标准组织的背书或认证；报告中引用的标准名称仅用于说明检查依据。 "
    "配置对应端点的实时行为、工具实现代码与数据流边界超出自动检查范围，需人工深度复核。 "
    "任何安全决策与合规判定，应以具备资质的人工审计/复核结论为最终依据。"
)


def _load_body(args) -> tuple[dict | None, int]:
    body: dict = {}
    if args.config:
        try:
            with open(args.config, encoding="utf-8") as f:
                cfg = json.load(f)
        except Exception as e:
            print(f"输入错误: 无法读取配置文件: {e}", file=sys.stderr)
            return None, 2
        if isinstance(cfg, dict) and "mcpServers" not in cfg and isinstance(cfg.get("config"), dict):
            cfg = cfg["config"]
        body["config"] = cfg
    elif args.endpoint_url:
        body["endpoint_url"] = args.endpoint_url
    elif not sys.stdin.isatty():
        try:
            cfg = json.load(sys.stdin)
            if isinstance(cfg, dict) and "mcpServers" not in cfg and isinstance(cfg.get("config"), dict):
                cfg = cfg["config"]
            body["config"] = cfg
        except Exception as e:
            print(f"输入错误: stdin 不是合法 JSON: {e}", file=sys.stderr)
            return None, 2
    else:
        print("用法: 需要 --config <json> 或 --endpoint-url <url>（或 stdin 传入配置 JSON）",
              file=sys.stderr)
        return None, 2
    return body, 0


def _run_local(body: dict) -> dict:
    import mcp_rules  # noqa: E402

    config = body.get("config")
    if isinstance(config, str):
        try:
            config = json.loads(config)
        except Exception as e:
            return {"ok": False, "error": f"config 不是合法 JSON: {e}"}

    endpoint = body.get("endpoint_url")
    if config is None and isinstance(endpoint, str) and endpoint:
        config = {"mcpServers": {"remote": {"url": endpoint, "type": "http"}}}

    if config is None:
        return {"ok": False, "error": "需要 config（MCP 配置 JSON 对象/字符串）或 endpoint_url"}

    t0 = time.perf_counter()
    report = mcp_rules.check_config(config)
    report["ok"] = True
    report["duration_ms"] = round((time.perf_counter() - t0) * 1000, 3)
    report["mode"] = "local"
    report["manual_audit_note"] = (
        "以上为 14 项自动化静态检查结果，仅为初筛。远程端点的实时行为、工具实现代码、"
        "权限边界与数据流需人工深度审计确认，详见报告免责声明。"
    )
    report["disclaimer"] = DISCLAIMER
    return report


def _run_online(body: dict, endpoint: str | None) -> tuple[dict | None, int]:
    import ccs_online_client as client  # noqa: E402

    try:
        rep = client.call("/v1/checkup/mcp", body, endpoint=endpoint)
    except client.PaymentRequiredError:
        return None, 3
    except client.CCSAPIError as e:
        print(f"服务错误: HTTP {e.status} {e.payload}", file=sys.stderr)
        return None, 2
    return rep, 0


def _render(rep: dict) -> None:
    print("=" * 64)
    print("  MCP / Agent 配置安全体检 — 静态检查报告")
    mode = "本地" if rep.get("mode") == "local" else "在线"
    print(f"  运行模式: {mode}（纯静态，不连接配置中的任何地址）")
    print("=" * 64)
    print(f"  风险等级 (risk_level): {rep.get('risk_level')}")
    s = rep.get("summary", {})
    print(f"  发现统计: CRIT={s.get('CRIT', 0)}  HIGH={s.get('HIGH', 0)}  "
          f"MED={s.get('MED', 0)}  LOW={s.get('LOW', 0)}")
    print(f"  自动检查项: {rep.get('checks_run')} 项")
    print("-" * 64)
    for sev in SEV_ORDER:
        items = [f for f in rep.get("findings", []) if f.get("severity") == sev]
        for f in items:
            print(f"  [{sev}] {f.get('title')}  ({f.get('rule_id')})")
            if f.get("server"):
                print(f"        服务器: {f.get('server')}")
            ev = f.get("evidence") or ""
            if ev:
                print(f"        依据: {str(ev)[:160]}")
            rec = f.get("remediation") or ""
            if rec:
                print(f"        建议: {rec}")
    print("-" * 64)
    print(f"  {rep.get('manual_audit_note', '')}")
    print(f"  耗时: {rep.get('duration_ms')} ms")
    print("=" * 64)
    disc = rep.get("disclaimer")
    if disc:
        print(f"\n{disc}")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="MCP/Agent 配置静态安全体检（14 项自动检查，默认本地运行，零外传）")
    ap.add_argument("-c", "--config",
                    help="MCP 配置 JSON 文件路径（mcpServers 文档）")
    ap.add_argument("-u", "--endpoint-url",
                    help="单个远程 MCP 端点 URL（包成单服务器静态检查，不发起连接）")
    ap.add_argument("--online", action="store_true",
                    help="显式使用 Correctover 在线服务体检（默认本地，不联网；在线需 CCS_API_TOKEN）")
    ap.add_argument("--endpoint", help="在线模式：覆盖 CCS 服务端点")
    ap.add_argument("--json", action="store_true", help="输出完整机器可读 JSON")
    args = ap.parse_args()

    body, code = _load_body(args)
    if code:
        return code

    if args.online:
        rep, code = _run_online(body, args.endpoint)
        if code:
            return code
    else:
        rep = _run_local(body)
        if rep.get("ok") is False:
            print(f"错误: {rep.get('error')}", file=sys.stderr)
            return 2

    if args.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
    else:
        _render(rep)
    return 0


if __name__ == "__main__":
    sys.exit(main())
