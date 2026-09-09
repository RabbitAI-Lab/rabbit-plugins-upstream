#!/usr/bin/env python3
"""mcp_rules.py — 14 static security checks for MCP / Agent server configurations.

This module performs STATIC analysis only. It never connects to the supplied
URL, never executes anything, and never leaves the process. It is designed to
be imported by the online checkup API and reused by offline tooling.

Scope: the 14 automated checks below are a lightweight triage layer. They are
NOT a full security assessment and do not replace manual code review / deep
audit work. Nothing here is endorsed by OWASP, IETF or any standards body.
"""
from __future__ import annotations

import re
from typing import Any

SEVERITY_ORDER = {"CRIT": 0, "HIGH": 1, "MED": 2, "LOW": 3, "INFO": 4}

# --------------------------------------------------------------------------- #
# Rule catalogue — 14 automated static checks
# --------------------------------------------------------------------------- #
RULES: list[dict] = [
    {
        "id": "MCP-001",
        "severity": "CRIT",
        "title": "云凭证 / 云密钥直接硬编码在配置中",
        "basis": "配置文本中出现云平台 Access Key（如 LTAI 前缀、AKIA 前缀等）特征串",
        "remediation": "立即作废并轮换该密钥；改用短期临时凭证/角色；密钥仅存放于密钥管理服务，环境变量注入。",
    },
    {
        "id": "MCP-002",
        "severity": "CRIT",
        "title": "文件系统服务器可写或挂载根目录/家目录",
        "basis": "filesystem 类服务器参数含 / ~ * 等宽路径，或未限制只读",
        "remediation": "将可访问目录收敛到项目工作目录；能只读则只读；禁止把根目录、家目录、密钥目录挂载给 MCP 服务器。",
    },
    {
        "id": "MCP-003",
        "severity": "CRIT",
        "title": "暴露任意 shell / 命令执行能力",
        "basis": "command 或服务器工具名中出现 bash/sh/zsh/powershell/cmd、execute_command 等",
        "remediation": "移除通用命令执行工具；如确需，改为参数级白名单命令集，并在调用前加运行时校验钩子。",
    },
    {
        "id": "MCP-004",
        "severity": "HIGH",
        "title": "工具暴露通用代码/表达式求值",
        "basis": "工具/参数中出现 eval、exec、python -c、node -e 等动态求值",
        "remediation": "移除求值型工具；用固定功能接口替代自由表达式执行。",
    },
    {
        "id": "MCP-005",
        "severity": "HIGH",
        "title": "网络/抓取类服务器缺少主机白名单（SSRF 面）",
        "basis": "fetch/http/requests/browser/curl 类服务器未配置 ALLOWED_HOSTS 等出网限制",
        "remediation": "配置出网域名白名单；阻断云元数据地址（169.254.169.254）与内网网段；对重定向目标做同样校验。",
    },
    {
        "id": "MCP-006",
        "severity": "HIGH",
        "title": "环境变量中出现通用密钥/令牌",
        "basis": "env 键名匹配 token/secret/password/api_key/auth 等敏感命名，且值非空",
        "remediation": "最小化注入给 MCP 服务器的环境变量；密钥改为运行时按需获取；定期轮换；不要把生产密钥写进可下发给 Agent 的配置。",
    },
    {
        "id": "MCP-007",
        "severity": "HIGH",
        "title": "数据库服务器未声明只读",
        "basis": "postgres/mysql/mongo/sqlite 类服务器未设置 READ_ONLY/readonly 标志",
        "remediation": "Agent 侧访问一律只读账号 + 只读连接；写操作走受控业务接口。",
    },
    {
        "id": "MCP-008",
        "severity": "HIGH",
        "title": "Git 服务器未限制推送/写权限",
        "basis": "git 类服务器参数缺少 --read-only/--no-push 等限制",
        "remediation": "以只读凭据运行 Git 服务器；禁止 Agent 直接推送/改配置。",
    },
    {
        "id": "MCP-009",
        "severity": "HIGH",
        "title": "浏览器自动化服务器可交互且无域名隔离",
        "basis": "playwright/puppeteer/browser 类服务器未配置允许域名、可用复用登录态",
        "remediation": "限制可访问域名；使用隔离浏览器上下文（无持久化 Cookie）；禁止访问内部管理后台。",
    },
    {
        "id": "MCP-010",
        "severity": "MED",
        "title": "远程端点使用明文 HTTP",
        "basis": "配置中的 URL 使用 http:// 而非 https://",
        "remediation": "改用 HTTPS；远程 MCP 必须经过 TLS，防止令牌与数据在链路中泄露/被篡改。",
    },
    {
        "id": "MCP-011",
        "severity": "MED",
        "title": "命令字符串含明显注入危险段",
        "basis": "command/args 中出现 $(...)、反引号、管道拼接用户可控变量等模式",
        "remediation": "不要把外部输入拼进 shell 命令；改用参数数组形式调用；对参数做白名单校验。",
    },
    {
        "id": "MCP-012",
        "severity": "MED",
        "title": "工具集合疑似过宽（危险工具聚类）",
        "basis": "单个配置中同时出现文件写入、命令执行、网络访问三类能力中的两类及以上",
        "remediation": "按最小权限拆分服务器；Agent 只挂载完成任务所必需的工具集。",
    },
    {
        "id": "MCP-013",
        "severity": "MED",
        "title": "远程端点指向本地回环 / 云元数据地址",
        "basis": "URL 主机为 localhost/127.0.0.1、169.254.169.254、内网 IP 段",
        "remediation": "远程 MCP 端点不得指向本机与云元数据；如为本地开发配置，上线前移除。",
    },
    {
        "id": "MCP-014",
        "severity": "LOW",
        "title": "远程包启动器未锁定版本（供应链面）",
        "basis": "npx/uvx/dlx 等运行远程包时未带固定版本号（latest 浮动）",
        "remediation": "固定包版本并记录校验值；条件允许时改为本地安装/审计后依赖，避免每次启动拉取最新代码。",
    },
]
assert len(RULES) == 14, "自动检查项必须为 14 项"

CLOUD_KEY_PATTERNS = [
    re.compile(r"\bLTAI[0-9A-Za-z]{12,}"),       # Alibaba Cloud AK id
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),          # AWS access key id
    re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b"),    # Google API key
]
SECRET_ENV_KEY = re.compile(r"(token|secret|password|passwd|api[_-]?key|apikey|auth|credential)", re.I)
SHELL_NAMES = ("bash", "sh", "zsh", "powershell", "pwsh", "cmd.exe", "cmd")
EVAL_PATTERNS = re.compile(r"(\beval\s*\(|\bexec\s*\(|python\s+-c\b|node\s+-e\b|Function\s*\()", re.I)
NETWORK_HINTS = ("fetch", "requests", "curl", "wget")
# Plain HTTP *transport* MCP servers are not outbound-fetch tools themselves;
# "browser"/"http" hints are handled separately by the browser rule / URL rules.
FETCH_TOOL_HINTS = ("fetch", "requests", "curl", "wget")
DB_HINTS = ("postgres", "mysql", "mongo", "sqlite", "database", "sql")
FS_HINTS = ("filesystem", "fs-server")
GIT_HINTS = ("git",)
BROWSER_HINTS = ("playwright", "puppeteer", "browser", "chrome")
LAUNCHER_HINTS = ("npx", "uvx", "dlx", "bunx")
INJECTION_PATTERNS = re.compile(r"(\$\(|`|&&|\|\||\s\|\s|;\s*\$\{|{{.*}}.*\bexec\b)")
_INTERNAL_HOST_RE = re.compile(
    r"^(localhost|127\.|10\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.|169\.254\.|\[?::1\]?|metadata\.google)",
    re.I,
)


def _as_text(v: Any) -> str:
    try:
        return v if isinstance(v, str) else str(v)
    except Exception:
        return ""


def _iter_server_entries(config: Any):
    """Yield (server_name, server_cfg_dict) turals from common MCP config shapes."""
    entries: list[tuple[str, dict]] = []

    def add(name: str, cfg: Any):
        if isinstance(cfg, dict):
            entries.append((str(name), cfg))

    if isinstance(config, dict):
        # Shape A: {"mcpServers": {"name": {...}}}
        for key in ("mcpServers", "servers", "mcp"):
            block = config.get(key)
            if isinstance(block, dict):
                for name, cfg in block.items():
                    add(name, cfg)
        # Shape B: top-level map of name -> server cfg
        for name, cfg in config.items():
            if isinstance(cfg, dict) and any(
                k in cfg for k in ("command", "url", "type", "transport", "args")
            ):
                add(name, cfg)
    elif isinstance(config, list):
        for i, cfg in enumerate(config):
            if isinstance(cfg, dict):
                add(cfg.get("name", f"server[{i}]"), cfg)
    return entries


def _server_text(cfg: dict) -> str:
    try:
        return str(cfg)
    except Exception:
        return ""


def _command_contains_shell(cfg: dict) -> bool:
    cmd = _as_text(cfg.get("command", "")).lower()
    base = cmd.replace("\\", "/").split("/")[-1]
    if base in SHELL_NAMES:
        return True
    for a in cfg.get("args", []) or []:
        a_base = _as_text(a).replace("\\", "/").split("/")[-1].lower()
        if a_base in SHELL_NAMES:
            return True
    return False


def _hinted(cfg: dict, name: str, hints) -> bool:
    blob = (name + " " + _as_text(cfg.get("command", "")) + " "
            + " ".join(_as_text(a) for a in (cfg.get("args") or []))).lower()
    return any(h in blob for h in hints)


def _urls_in(cfg: dict) -> list[str]:
    urls: list[str] = []
    for key in ("url", "endpoint", "serverUrl", "host"):
        v = cfg.get(key)
        if isinstance(v, str) and v:
            urls.append(v)
    return urls


def _host_of(url: str) -> str:
    m = re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://([^/]+)", url)
    return m.group(1).split(":")[0] if m else ""


def check_config(config: Any) -> dict:
    """Run the 14 static checks against a parsed MCP config.

    Returns a report dict: {checks_run, findings:[{rule_id,severity,title,
    server,evidence,basis,remediation}], summary:{CRIT,HIGH,MED,LOW}, risk_level}
    """
    findings: list[dict] = []

    def add(rule: dict, server: str, evidence: str):
        findings.append({
            "rule_id": rule["id"],
            "severity": rule["severity"],
            "title": rule["title"],
            "server": server,
            "evidence": evidence[:300],
            "basis": rule["basis"],
            "remediation": rule["remediation"],
        })

    entries = _iter_server_entries(config)

    for name, cfg in entries:
        text = _server_text(cfg)
        args = cfg.get("args") or []
        args_text = " ".join(_as_text(a) for a in args)
        env = cfg.get("env") if isinstance(cfg.get("env"), dict) else {}

        # MCP-001 cloud keys anywhere in the config text
        for pat in CLOUD_KEY_PATTERNS:
            m = pat.search(text)
            if m:
                add(RULES[0], name, f"疑似云密钥特征串: {m.group(0)[:6]}…（已脱敏）")
                break

        # MCP-002 filesystem wide access
        if _hinted(cfg, name, FS_HINTS):
            wide = any(
                _as_text(a).strip() in ("/", "~", "*", "/home", "/root", "C:\\")
                or _as_text(a).strip().endswith(":/")
                for a in args
            ) or any(a in ("~", "/", "*") for a in args)
            ro = any("read-only" in _as_text(a).lower() or "readonly" in _as_text(a).lower() for a in args)
            if wide or not ro:
                add(RULES[1], name, f"args={args_text[:120] or '(空)'}；只读标志={'有' if ro else '无'}")

        # MCP-003 shell execution
        if _command_contains_shell(cfg):
            add(RULES[2], name, f"command={_as_text(cfg.get('command'))} args={args_text[:80]}")

        # MCP-004 eval/code execution
        if EVAL_PATTERNS.search(text):
            add(RULES[3], name, "command/args 中出现 eval/exec/动态求值模式")

        # MCP-005 network without host allowlist
        if _hinted(cfg, name, FETCH_TOOL_HINTS):
            has_allowlist = any(
                k.upper() in ("ALLOWED_HOSTS", "HOST_WHITELIST", "ALLOWED_DOMAINS")
                for k in env
            ) or any("allowed-hosts" in _as_text(a).lower() for a in args)
            if not has_allowlist:
                add(RULES[4], name, "网络类服务器未发现出网主机白名单配置")

        # MCP-006 generic secrets in env
        for k, v in env.items():
            if SECRET_ENV_KEY.search(str(k)) and v not in (None, "", "${}", "changeme"):
                add(RULES[5], name, f"env 键 {k} 含非空敏感值（值不回显）")
                break

        # MCP-007 database not read-only
        if _hinted(cfg, name, DB_HINTS):
            ro = any("read_only" in str(k).lower() or "readonly" in str(k).lower() for k in env) \
                or any("readonly" in _as_text(a).lower() for a in args)
            if not ro:
                add(RULES[6], name, "数据库类服务器未发现只读标志")

        # MCP-008 git push capability
        if _hinted(cfg, name, GIT_HINTS):
            locked = any("--read-only" in _as_text(a) or "--no-push" in _as_text(a) for a in args)
            if not locked:
                add(RULES[7], name, "git 类服务器未发现 --read-only/--no-push 限制")

        # MCP-009 browser automation without isolation
        if _hinted(cfg, name, BROWSER_HINTS):
            isolated = any(
                "isolated" in _as_text(a).lower() or "allowed-origins" in _as_text(a).lower()
                or "headless" in _as_text(a).lower()
                for a in args
            ) or any("ALLOWED" in str(k).upper() for k in env)
            if not isolated:
                add(RULES[8], name, "浏览器自动化服务器未发现域名限制/隔离上下文配置")

        # URL-based checks
        for url in _urls_in(cfg):
            host = _host_of(url)
            # MCP-010 plaintext http
            if url.lower().startswith("http://"):
                add(RULES[9], name, f"端点使用明文 HTTP: {host}")
            # MCP-013 internal / metadata targets
            if host and _INTERNAL_HOST_RE.match(host):
                add(RULES[12], name, f"端点主机为回环/内网/元数据地址: {host}")

        # MCP-011 injection-prone command construction
        if INJECTION_PATTERNS.search(_as_text(cfg.get("command")) + " " + args_text):
            add(RULES[10], name, "命令/参数中出现 $(...)、反引号或管道拼接模式")

        # MCP-014 launcher without pinned version
        cmd_base = _as_text(cfg.get("command")).replace("\\", "/").split("/")[-1].lower()
        all_tokens = [cmd_base] + [_as_text(a).replace("\\", "/").split("/")[-1].lower() for a in args]
        for i, tok in enumerate(all_tokens):
            if tok in LAUNCHER_HINTS:
                # look at the next token (the package spec)
                nxt = all_tokens[i + 1] if i + 1 < len(all_tokens) else ""
                if nxt and not re.search(r"@\d", nxt) and "@" not in nxt:
                    add(RULES[13], name, f"{tok} 启动远程包未固定版本: {nxt[:60]}")
                break

        # MCP-012 capability clustering
        caps = set()
        if _command_contains_shell(cfg) or EVAL_PATTERNS.search(text):
            caps.add("exec")
        if _hinted(cfg, name, FS_HINTS) or any("write" in _as_text(t).lower() for t in args):
            caps.add("file")
        if _hinted(cfg, name, NETWORK_HINTS) or _urls_in(cfg):
            caps.add("net")
        if len(caps) >= 2:
            add(RULES[11], name, f"同一配置聚类能力: {sorted(caps)}")

    findings.sort(key=lambda f: SEVERITY_ORDER.get(f["severity"], 9))
    summary = {"CRIT": 0, "HIGH": 0, "MED": 0, "LOW": 0}
    for f in findings:
        if f["severity"] in summary:
            summary[f["severity"]] += 1

    if summary["CRIT"] > 0:
        risk = "CRIT"
    elif summary["HIGH"] > 0:
        risk = "HIGH"
    elif summary["MED"] > 0:
        risk = "MED"
    elif summary["LOW"] > 0:
        risk = "LOW"
    else:
        risk = "PASS"

    return {
        "checks_run": 14,
        "servers_scanned": len(entries),
        "findings": findings,
        "summary": summary,
        "risk_level": risk,
    }
