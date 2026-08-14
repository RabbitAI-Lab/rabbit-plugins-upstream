#!/usr/bin/env python3
"""
扫描本机各 Agent 宿主的 skill 安装目录，输出成本清单（JSON）。

只做确定性统计，不做判断。判断交给调用它的 Agent。

关键设计：**按宿主隔离「装在磁盘上」和「真的进了上下文」**。
不同宿主的 skill 绝不能合并计算上下文预算或覆盖冲突。

用法:
    python3 scan.py                    # 扫描默认路径
    python3 scan.py --path <dir> ...   # 追加自定义路径
    python3 scan.py --json out.json    # 写入文件
    python3 scan.py --all              # 预算按磁盘上所有 skill 算（诊断用，默认只算已加载）
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

# Windows services and CI runners may expose cp1252 consoles. Reports and
# diagnostics are bilingual, so make redirected and interactive output stable.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

# 版本号。**必须与 Cargo.toml 的 version 一致** —— 两个实现要能被同一条
# `--version` 区分开就毫无意义了。tests/test_regressions.py 有断言钉住。
__version__ = "0.1.0"

# 覆盖优先级：数字越小越优先。只在同一宿主内比较。
#
# **按宿主而异，不能只用一张表。**
# 曾经这里是一张全局表，装的是 OpenClaw 的顺序（workspace > project >
# personal > managed），却被套用到每一个宿主。conflict_domain 只负责把
# 不同宿主分开**分组**，排序仍走这张表 —— 于是 Claude Code 的
# personal 与 project 被判反了，而这恰好是 precedence_note 自己写明、
# 且「与多数人直觉相反」的那一对：**home 目录里的副本会盖掉项目里的**。
# 判反的后果不是少一条信息，而是把诊断方向整个指错。
LEVEL_RANK_BY_HOST = {
    # Claude Code：enterprise > personal > project > plugin
    "claude-code": {"enterprise": 0, "personal": 1, "project": 2, "plugin": 3,
                    "other-host": 8, "unknown": 9},
    # OpenClaw：workspace > project > personal > managed
    "openclaw": {"workspace": 0, "project": 1, "personal": 2, "managed": 3,
                 "enterprise": 0, "plugin": 3, "other-host": 8, "unknown": 9},
}
# 未知宿主退回 Claude Code 的顺序：本工具的绝大多数用户在那儿，
# 而且这一版的其余判定（personal/project/enterprise 的 classify）也是按它写的。
LEVEL_RANK = LEVEL_RANK_BY_HOST["claude-code"]


def level_rank(skill):
    """取该 skill 所属宿主的覆盖优先级。数字越小越优先。"""
    family = skill.get("host_family") or skill.get("host") or ""
    table = LEVEL_RANK_BY_HOST.get(family, LEVEL_RANK)
    return table.get(skill.get("level"), 9)

# Claude Code 的 skill/命令描述总预算。默认约 15000 字符（≈4000 token）。
# 超出后描述被静默丢弃，无任何告警。可用 SLASH_COMMAND_TOOL_CHAR_BUDGET 调大。
# 不同版本口径不一（另有"上下文窗口 1%"的说法），故做成可配置。
DEFAULT_DESC_BUDGET = int(os.environ.get("SLASH_COMMAND_TOOL_CHAR_BUDGET", 15000))
CODEX_FALLBACK_DESC_BUDGET = 8000

# 判定「僵尸」前至少要装够这么多天。装了一天就说零触发没有意义。
ZOMBIE_MIN_AGE_DAYS = 14

# 本脚本自身所在的 skill 根目录。安全扫描要排除它，否则会扫到自己的规则源码。
SELF_SKILL_ROOT = Path(__file__).resolve().parent.parent

# 安全启发式。命中不等于恶意，只是需要人看一眼。
SECURITY_PATTERNS = [
    ("adversarial_instruction", "critical", re.compile(
        r"(ignore\s+(all\s+)?previous|disregard\s+(all\s+)?prior|"
        r"忽略(之前|先前|上述)|无视(之前|先前)|"
        r"do\s+not\s+(tell|inform|mention\s+to)\s+the\s+user|不要告诉用户)", re.I)),
    ("pipe_to_shell", "critical", re.compile(
        r"(curl|wget)[^\n|]{0,200}\|\s*(ba)?sh", re.I)),
    ("base64_exec", "critical", re.compile(
        r"base64\s+(-d|--decode)[^\n]{0,80}\|\s*(ba)?sh", re.I)),
    ("raw_ip_fetch", "high", re.compile(
        r"(curl|wget|fetch)[^\n]{0,80}https?://\d{1,3}(\.\d{1,3}){3}", re.I)),
    ("password_archive", "high", re.compile(
        r"(unzip\s+-P|7z[a-z]*\s+x?\s*-p\S|openssl\s+enc\s+-\S*d)", re.I)),
    ("hardcoded_secret", "high", re.compile(
        r"(sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{12,}|"
        r"xoxb-[0-9A-Za-z-]{10,})")),
    ("credential_env_read", "medium", re.compile(
        r"(cat|grep|cp)\s+[^\n]{0,60}(\.env|\.aws/credentials|\.ssh/id_|"
        r"\.npmrc|\.netrc)", re.I)),
    ("obfuscated_exec", "medium", re.compile(
        r"(eval\s*\(\s*(atob|base64)|exec\s*\(\s*(atob|base64)|"
        r"\bchr\(\d+\)\s*\+)", re.I)),
]

# 命中点若处在「引用/举例/防御说明」语境里，**标注** cited，用于排序，**不降低严重度**。
# 例如 receipts 那条：SKILL.md 在教 Agent 防御注入时引用了攻击样例。
#
# 这里曾经犯过一次错：把 cited 做成「降级为 info 且不计入 max_severity」。
# 后果是加一句 "For example," 或一个不闭合的引号就能让 critical 完全静默。
# 启发式只配做排序提示，不配做裁决。真正的防线是人打开那一行看一眼（findings 里有行号）。
CITATION_HINTS = re.compile(
    r"(re\.compile|regex|正则|例如|举例|比如|这类|样例|"
    r"example|such as|e\.g\.|banned|forbidden|禁止|防御|抵御|注入|injection|"
    r"prompt\s*injection|attack|攻击|不要遵从|不得执行)", re.I)
OPEN_QUOTES = ("“", "「", "『")

# 约定的参考文档目录。这些目录里的 .md 视为「触发后可能整篇读」，计入 tier2。
# 其余子目录的 .md 视为数据语料，只记字节不记 token。
DOC_DIRS = {"references", "reference", "refs", "docs", "doc"}

# 仓库元数据文件：给人看的，Agent 不会读，不计入 tier2。
# 一个开源的 skill 仓库会有这些文件，把它们算成「触发时载入」是错的。
REPO_META = {"readme.md", "license.md", "license", "changelog.md", "contributing.md",
             "code_of_conduct.md", "security.md", "notice.md", "authors.md"}

URL_RE = re.compile(r"https?://[^\s\)\]\"'>]+")
EXEC_EXT = {".sh", ".py", ".js", ".ts", ".rb", ".pl", ".ps1", ".bat", ".zsh"}

# 各宿主的常见 skill 目录。找不到的会被静默跳过。
# 同一个 host 的多个根目录按该宿主的优先级归类，绝不跨宿主比较。
DEFAULT_ROOTS = [
    ("claude-code", "./.claude/skills"),
    ("claude-code", "~/.claude/skills"),
    ("claude-code-plugins", "~/.claude/plugins"),
    ("codex", "~/.codex/skills"),
    ("openclaw", "./skills"),
    ("openclaw", "./.agents/skills"),
    ("hermes", "~/.hermes/skills"),
    ("workbuddy", "./.codebuddy/skills"),
    ("workbuddy", "./.workbuddy/skills"),
    ("workbuddy", "~/.workbuddy/skills"),
    ("cc-switch", "~/.cc-switch/skills"),
    ("cursor", "~/.cursor/skills"),
    ("gemini-cli", "~/.gemini/skills"),
    ("opencode", "~/.opencode/skills"),
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


# ── 路径工具（分隔符无关，Windows/POSIX 通用）────────────────

def safe_str(s: str) -> str:
    """把 surrogateescape 产生的代理字符换成 U+FFFD。

    非 UTF-8 的**文件名**（不是文件内容）经 os.fsdecode 会变成孤立代理字符，
    这类字符无法编码回 UTF-8：json.dumps 能产出它，写文件时却抛
    UnicodeEncodeError —— **整次扫描中断**，违反「单个 skill 的失败不得
    影响其余」（ENGINEERING §4.5）。

    往返一次即可对齐 Rust 的 String::from_utf8_lossy：先按 surrogateescape
    还原原始字节，再以 replace 解码。两个实现因此产出同一个 U+FFFD。

    macOS 的 APFS 拒绝非 UTF-8 文件名，所以这条只在 Linux 上显形 ——
    CI 的 Linux job 抓到的，本地永远撞不出。
    """
    return s.encode("utf-8", "surrogateescape").decode("utf-8", "replace")


def norm(p) -> str:
    """统一成正斜杠，让所有路径判断在 Windows 上也成立。"""
    return safe_str(str(p).replace("\\", "/"))


def find_codex_executable():
    """Prefer the native binary: npm's .cmd shim can detach under redirected stdio."""
    override = os.environ.get("SKILL_VITALS_CODEX_EXECUTABLE")
    if override:
        return override
    direct = shutil.which("codex.exe")
    if direct:
        return direct
    shim = shutil.which("codex.cmd") or shutil.which("codex")
    if not shim:
        return None
    npm_root = Path(shim).parent
    candidates = list(npm_root.glob(
        "node_modules/@openai/codex/node_modules/@openai/codex-*/vendor/**/codex.exe"))
    return str(candidates[0]) if candidates else shim


def read_codex_runtime(cwd: Path, timeout=20):
    """Read Codex's authoritative skill catalog through app-server skills/list."""
    state = {"available": False, "source": "codex app-server skills/list",
             "cwd": norm(cwd.resolve()), "skills": [], "errors": []}
    exe = find_codex_executable()
    if not exe:
        state["errors"].append("codex executable not found")
        return state
    messages = [
        {"method": "initialize", "id": 1, "params": {"clientInfo": {
            "name": "skill-vitals", "title": "Skill Vitals", "version": "0.1.0"}}},
        {"method": "initialized", "params": {}},
        {"method": "skills/list", "id": 2, "params": {
            "cwds": [str(cwd.resolve())], "forceReload": True}},
    ]
    lines = []
    initialized_ready = threading.Event()
    response_ready = threading.Event()
    try:
        command = ([sys.executable, exe] if Path(exe).suffix.lower() == ".py" else [exe])
        proc = subprocess.Popen(command + ["app-server", "--stdio"], stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                bufsize=1, cwd=str(cwd))
        def read_responses():
            for line in proc.stdout:
                lines.append(line)
                try:
                    response_id = json.loads(line).get("id")
                    if response_id == 1:
                        initialized_ready.set()
                    elif response_id == 2:
                        response_ready.set()
                except json.JSONDecodeError:
                    pass
        reader = threading.Thread(target=read_responses, daemon=True)
        reader.start()
        proc.stdin.write(json.dumps(messages[0], separators=(",", ":")) + "\n")
        proc.stdin.flush()
        if not initialized_ready.wait(min(timeout, 5)):
            proc.kill()
            proc.wait(5)
            state["errors"].append("app-server initialize timed out")
            return state
        for message in messages[1:]:
            proc.stdin.write(json.dumps(message, separators=(",", ":")) + "\n")
            proc.stdin.flush()
        response_ready.wait(timeout)
        proc.terminate()
        try:
            proc.wait(5)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(5)
        reader.join(2)
    except (OSError, subprocess.SubprocessError) as exc:
        state["errors"].append(f"app-server failed: {exc}")
        return state
    response = None
    for line in lines:
        try:
            message = json.loads(line)
        except json.JSONDecodeError:
            continue
        if message.get("id") == 2:
            response = message
            break
    if response is None:
        detail = proc.stderr.read().strip()[-500:] or f"exit={proc.returncode}, no skills/list response"
        state["errors"].append(detail)
        return state
    if response.get("error"):
        state["errors"].append(str(response["error"]))
        return state
    entries = response.get("result", {}).get("data", [])
    for entry in entries:
        if norm(entry.get("cwd", "")) != state["cwd"]:
            continue
        state["skills"].extend(entry.get("skills", []))
        state["errors"].extend(str(e) for e in entry.get("errors", []))
    state["available"] = True
    state["executable"] = norm(exe)
    return state


def apply_codex_runtime(skills, runtime):
    """Add runtime-only skills and overlay authoritative Codex metadata by path."""
    by_path = {(s["host_family"], norm(Path(s["path"]).resolve())): s for s in skills}
    for meta in runtime.get("skills", []):
        md = Path(meta.get("path", ""))
        if not md.is_file():
            continue
        key = ("codex", norm(md.parent.resolve()))
        rec = by_path.get(key)
        if rec is None:
            rec = scan_skill_dir(md.parent, "codex", set(), {}, False)
            if not rec:
                continue
            skills.append(rec)
            by_path[key] = rec
        rec.update({
            "name": meta.get("name", rec["name"]),
            "description": meta.get("description", rec["description"]),
            "description_chars": len(meta.get("description", rec["description"])),
            "loaded": bool(meta.get("enabled", True)),
            "loaded_reason": "codex-app-server-enabled" if meta.get("enabled", True)
                             else "codex-app-server-disabled",
            "level": meta.get("scope", rec["level"]),
            "codex_scope": meta.get("scope"),
            "codex_interface": meta.get("interface"),
            "codex_dependencies": meta.get("dependencies"),
            "runtime_verified": True,
        })
    return skills


def read_workbuddy_builtin_roots():
    """Resolve WorkBuddy's top-level installed Skill packages from its cache."""
    marketplace = Path(os.path.expanduser(
        "~/.workbuddy/plugins/marketplaces/workbuddy-builtin"))
    manifest = marketplace / ".codebuddy-plugin" / "marketplace.json"
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    roots = []
    base = marketplace.resolve()
    cache = Path(os.path.expanduser("~/.workbuddy/plugins/cache/workbuddy-builtin"))
    for plugin in data.get("plugins", []):
        category = plugin.get("category")
        # `skill` 是顶层安装的 Skill 包；`builtin-plugin` 是随客户端打包的插件，
        # **它也会带 skill**（腾讯文档/PPTX/Docx、微信支付、表格代理等）。
        #
        # 曾经这里只取 `skill`，把 builtin-plugin 整包排除，于是 WorkBuddy
        # 运行时能调用的 18 个 skill 一个都没进报告。核对方式是拿运行时的
        # available skills 名单与磁盘逐条对照（见下面的白名单注释）。
        if category not in ("skill", "builtin-plugin"):
            continue
        source = plugin.get("source")
        if not isinstance(source, str):
            continue
        manifest_source = (marketplace / source).resolve()
        try:
            manifest_source.relative_to(base)
        except ValueError:
            continue
        package = plugin.get("name")
        version = plugin.get("version")
        cached = cache / str(package) / str(version)
        candidate = cached if (cached / "SKILL.md").is_file() else manifest_source
        meta = {
            "workbuddy_package": package,
            "workbuddy_version": version,
            "workbuddy_legacy_name": manifest_source.name,
            "workbuddy_orphan_marker": (cached / ".orphaned_at").is_file(),
        }

        if category == "skill":
            if candidate.is_dir():
                roots.append((str(candidate), dict(
                    meta, root_kind=("builtin-skill-cache" if candidate == cached
                                     else "builtin-skill-marketplace-fallback"))))
            continue

        # builtin-plugin：**正向白名单**，只有两处算顶层 skill ——
        #   <包>/<版本>/SKILL.md          包自身（tencent-docx 就是这种）
        #   <包>/<版本>/skills/*/SKILL.md  它带的 skill
        # 其余（tencent-docx 的 experts/ 等）是包内部的角色定义，运行时也不
        # 把它们当 skill 列出。**用白名单而不是排除 experts/**：只有一个包有
        # experts 目录，据此立全局规则是从单一样本推规则。
        #
        # 版本必须钉 manifest 的那个：cache 里会同时留着旧版本
        # （实测 weixinpay 1.5.111 与 1.6.107 并存），直接 glob 会数两遍。
        pkg_root = cached if cached.is_dir() else manifest_source
        if not pkg_root.is_dir():
            continue
        if (pkg_root / "SKILL.md").is_file():
            roots.append((str(pkg_root), dict(
                meta, root_kind="builtin-plugin-package", only_direct=True)))
        skills_dir = pkg_root / "skills"
        if skills_dir.is_dir():
            for child in sorted(skills_dir.iterdir(), key=norm):
                if (child / "SKILL.md").is_file():
                    roots.append((str(child), dict(
                        meta, root_kind="builtin-plugin-skill")))
    return roots


def read_workbuddy_welcome_mode():
    """Read the latest session's welcomeMode from local WorkBuddy logs."""
    logs = Path(os.path.expanduser("~/.workbuddy/logs"))
    try:
        files = sorted(logs.rglob("*.log"), key=lambda p: p.stat().st_mtime,
                       reverse=True)
    except OSError:
        return None
    pattern = re.compile(r'(?:welcomeMode[=:]|X-WorkBuddy-Welcome-Mode[\\"]*[:=][\\"]*)'
                         r'(work|design|code)', re.I)
    for path in files[:20]:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        matches = pattern.findall(text)
        if matches:
            return matches[-1].lower()
    return None


def workbuddy_skill_active(legacy_name, welcome_mode):
    """Ardot packages are injected only into WorkBuddy's design welcome mode."""
    return not (str(legacy_name).startswith("ardot-") and
                welcome_mode and welcome_mode != "design")


HOME_N = norm(Path(os.path.expanduser("~")))
CWD_N = norm(Path.cwd())

PLUGIN_PATH_RE = re.compile(r"/plugins/(cache|marketplaces)/([^/]+)/(.+?)/skills/")
# 插件目录树里的包装层，不是插件名本身
PLUGIN_WRAPPER_DIRS = {"plugins", "external_plugins", "unknown", "skills"}


def plugin_identity(path_n: str):
    """从插件路径里提取 (插件名, marketplace)。不是插件路径则返回 (None, None)。

    覆盖的实际形态：
      .../plugins/cache/<mkt>/<plugin>/unknown/skills/<skill>
      .../plugins/marketplaces/<mkt>/plugins/<plugin>/skills/<skill>
      .../plugins/marketplaces/<mkt>/external_plugins/<plugin>/skills/<skill>
    """
    m = PLUGIN_PATH_RE.search(path_n + "/")
    if not m:
        return None, None
    marketplace = m.group(2)
    middle = [x for x in m.group(3).split("/") if x and x not in PLUGIN_WRAPPER_DIRS]
    plugin = middle[-1] if middle else marketplace
    return plugin, marketplace


def classify(skill_dir: Path, host: str):
    """返回 (level, namespace, plugin_key)。

    namespace 用于去重：插件里的 skill 按 `<plugin>:<name>` 隔离，
    所以 discord 和 telegram 各有一个 `access` 并不是冲突。
    """
    s = norm(skill_dir.resolve())
    plugin, marketplace = plugin_identity(s)
    if plugin:
        return "plugin", plugin, f"{plugin}@{marketplace}"
    if host == "openclaw":
        if "/workspace/skills" in s:
            return "workspace", None, None
        if "/plugin-skills/" in s:
            return "plugin", None, None
        if s.startswith(CWD_N + "/skills"):
            return "workspace", None, None
        if s.startswith(CWD_N + "/.agents/skills"):
            return "project", None, None
        if s.startswith(HOME_N + "/.agents/skills"):
            return "personal", None, None
        if s.startswith(HOME_N + "/.openclaw/skills"):
            return "managed", None, None
        if re.match(re.escape(HOME_N) + r"/\.open[^/]*/skills(?:/|$)", s):
            return "managed", None, None
    if host == "hermes":
        return ("personal", None, None) if s.startswith(HOME_N + "/.hermes/skills") \
            else ("external", None, None)
    if host == "codex":
        return "personal", None, None
    if host == "workbuddy":
        if (s.startswith(CWD_N + "/.codebuddy/skills") or
                s.startswith(CWD_N + "/.workbuddy/skills")):
            return "project", None, None
        if s.startswith(HOME_N + "/.workbuddy/skills"):
            return "personal", None, None
        if "/.workbuddy/plugins/marketplaces/workbuddy-builtin/" in s:
            return "managed", None, None
        return "unknown", None, None
    if "/managed" in s or "/etc/" in s or "enterprise" in s:
        return "enterprise", None, None
    if s.startswith(HOME_N + "/.claude/skills"):
        return "personal", None, None
    if s.startswith(CWD_N + "/.claude/skills") or norm(skill_dir).startswith(".claude/skills"):
        return "project", None, None
    return "unknown", None, None


def read_hermes_external_dirs():
    """读取 Hermes 的 skills.external_dirs（仅支持其文档中的 YAML 列表形式）。"""
    cfg = Path(os.path.expanduser("~/.hermes/config.yaml"))
    if not cfg.is_file():
        return []
    try:
        lines = cfg.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []
    out, in_skills, in_external = [], False, False
    for line in lines:
        clean = line.split("#", 1)[0]
        if re.match(r"^skills\s*:\s*$", clean):
            in_skills, in_external = True, False
            continue
        if in_skills and re.match(r"^\S", clean):
            in_skills, in_external = False, False
        if in_skills and re.match(r"^\s+external_dirs\s*:\s*$", clean):
            in_external = True
            continue
        if in_external:
            m = re.match(r"^\s*-\s*['\"]?(.+?)['\"]?\s*$", clean)
            if m:
                out.append(os.path.expandvars(os.path.expanduser(m.group(1))))
            elif clean.strip():
                in_external = False
    return out


def read_openclaw_roots():
    """发现 OpenClaw 多实例根目录，并保留实例/配置证据。"""
    home = Path(os.path.expanduser("~"))
    roots = []
    for instance in home.glob(".open*"):
        if not instance.is_dir():
            continue
        cfg = instance / "openclaw.json"
        if not cfg.is_file():
            continue
        try:
            data = json.loads(cfg.read_text(encoding="utf-8", errors="replace"))
        except (OSError, json.JSONDecodeError):
            data = {}
        meta = {
            "instance_id": instance.name,
            "instance_root": norm(instance.resolve()),
            "config_path": norm(cfg.resolve()),
            "skill_entries": ((data.get("skills") or {}).get("entries") or {}),
            "plugin_entries": ((data.get("plugins") or {}).get("entries") or {}),
            "plugin_allow": ((data.get("plugins") or {}).get("allow") or []),
            "skills_prompt_budget_chars": (((data.get("skills") or {}).get("limits") or {})
                                             .get("maxSkillsPromptChars")),
        }
        for name, kind in (("skills", "managed"), ("plugin-skills", "plugin")):
            roots.append((str(instance / name), {**meta, "root_kind": kind}))
        workspace = (((data.get("agents") or {}).get("defaults") or {})
                     .get("workspace"))
        if isinstance(workspace, str) and workspace:
            workspace_root = Path(os.path.expandvars(os.path.expanduser(workspace))) / "skills"
            roots.append((str(workspace_root), {**meta, "root_kind": "workspace"}))
        roots.append((str(home / ".agents" / "skills"),
                      {**meta, "root_kind": "shared-user"}))
        npm_skills = find_openclaw_bundled_skills()
        if npm_skills:
            roots.append((str(npm_skills), {**meta, "root_kind": "bundled"}))
    return roots


def find_openclaw_bundled_skills():
    """Resolve bundled Skills across npm shims, direct bins, links, and pnpm."""
    exe = shutil.which("openclaw")
    if not exe:
        return None
    raw, resolved = Path(exe), Path(exe).resolve()
    candidates = []
    for anchor in (raw.parent, resolved.parent, *resolved.parents):
        candidates.extend((anchor / "node_modules" / "openclaw" / "skills",
                           anchor / "openclaw" / "skills"))
        if anchor.name == "openclaw":
            candidates.append(anchor / "skills")
    candidates.extend(raw.parent.glob(
        "node_modules/.pnpm/openclaw@*/node_modules/openclaw/skills"))
    seen = set()
    for candidate in candidates:
        key = norm(candidate)
        if key in seen:
            continue
        seen.add(key)
        if candidate.is_dir() and any(candidate.glob("*/SKILL.md")):
            return candidate.resolve()
    return None


def read_openclaw_runtime(instance_root):
    """Ask OpenClaw for the authoritative eligible catalog for one instance."""
    state = {"available": False, "source": "openclaw skills list --eligible --json",
             "skills": [], "errors": []}
    exe = shutil.which("openclaw")
    if not exe:
        state["errors"].append("openclaw executable not found")
        return state
    env = os.environ.copy()
    env["OPENCLAW_STATE_DIR"] = str(instance_root)
    workspace = Path(instance_root) / "workspace"
    try:
        proc = subprocess.run(
            [exe, "skills", "list", "--eligible", "--json", "--agent", "main"],
            cwd=str(workspace if workspace.is_dir() else instance_root), env=env,
            capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError) as exc:
        state["errors"].append(str(exc))
        return state
    if proc.returncode:
        state["errors"].append(proc.stderr.strip()[-500:] or f"exit={proc.returncode}")
        return state
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        state["errors"].append(f"invalid JSON: {exc}")
        return state
    state["skills"] = payload.get("skills", [])
    state["available"] = True
    state["instance_id"] = Path(instance_root).name
    return state


def apply_openclaw_runtime(skills, runtimes):
    """Overlay eligible/model-visible state returned by OpenClaw itself."""
    for runtime in runtimes:
        if not runtime.get("available"):
            continue
        instance_id = runtime.get("instance_id")
        by_name = {m.get("name"): m for m in runtime.get("skills", [])}
        for rec in skills:
            if rec["host_family"] != "openclaw" or rec["instance_id"] != instance_id:
                continue
            meta = by_name.get(rec["name"])
            if not meta:
                rec.update({
                    "loaded": False,
                    "discoverable": False,
                    "loaded_state": False,
                    "runtime_verified": True,
                    "loaded_reason": "openclaw-cli-not-eligible",
                })
                continue
            rec.update({
                "loaded": bool(meta.get("modelVisible", True)),
                "discoverable": True,
                "enabled_state": not bool(meta.get("disabled", False)),
                "loaded_state": bool(meta.get("modelVisible", True)),
                "runtime_verified": True,
                "loaded_reason": "openclaw-cli-eligible-model-visible",
                "runtime_status": "eligible-model-visible",
                "body_loaded_state": None,
                "openclaw_runtime": meta,
            })
    return skills


# ── 宿主配置：哪些插件启用了、每个 skill 触发过几次 ──────────

def read_host_config():
    """读 ~/.claude.json。

    Claude Code 自己就维护着两份我们需要的数据：
      enabledPlugins - 决定插件里的 skill 是否进上下文
      skillUsage     - 每个 skill 的 usageCount / lastUsedAt（精确，非估算）
    比解析 ~/.claude/projects/**/*.jsonl 又快又准。

    读不到时第三个返回值必须是 None：调用方用 `host_cfg is not None` 判定
    plugins_known。曾经这里返回 `{}`，于是「配置读不到」被当成「配置读到了、
    只是没有启用任何插件」，插件分支照常执行，enabled_plugins 又是 None ——
    在没有 ~/.claude.json 的机器上，只要磁盘上有一个插件 skill，整次扫描
    就 TypeError 崩掉。降级分支 plugin-state-unknown 早就写好了，只是走不到。
    """
    p = Path(os.path.expanduser("~/.claude.json"))
    if not p.is_file():
        return None, {}, None
    try:
        d = json.loads(p.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError):
        return None, {}, None

    enabled = set()
    found_key = False

    def absorb(v):
        nonlocal found_key
        if isinstance(v, dict):
            found_key = True
            enabled.update(k for k, on in v.items() if on)
        elif isinstance(v, list):
            found_key = True
            enabled.update(v)

    absorb(d.get("enabledPlugins"))
    for proj in (d.get("projects") or {}).values():
        if isinstance(proj, dict):
            absorb(proj.get("enabledPlugins"))

    usage = d.get("skillUsage")
    return (enabled if found_key else set()), (usage or {}), d


def lookup_usage(usage: dict, name: str, namespace):
    """skillUsage 的键可能是裸名，也可能是 `<plugin>:<skill>`。

    裸名回退可能撞上同名的其他 skill，这是已知的精度上限。
    """
    keys = ([f"{namespace}:{name}"] if namespace else []) + [name]
    for k in keys:
        v = usage.get(k)
        if isinstance(v, dict):
            return int(v.get("usageCount", 0) or 0), v.get("lastUsedAt"), k
        if isinstance(v, int):
            return v, None, k
    return 0, None, None


def days_since(ms):
    if not ms:
        return None
    return round((time.time() - ms / 1000.0) / 86400.0, 1)


# 承载名字的键。**新增任何带名字的输出字段时必须同步加进来**，
# 否则脱敏会漏掉它 —— 已经因此漏过三次了：
#   1. 名字残留在 path（只改了 name 字段）
#   2. description 自由文本清不干净（改为整体丢弃）
#   3. removed_skills 里的名字只存在于基线，当前 skills[] 里没有；
#      namespace / plugin_key / enabled_plugins 里的插件名与 marketplace 名
#      从来就不在这三个键里
# 三次是同一个失效模式：**用例只能测你想到的字段**。
# 兜底靠 tests/test_properties.py 的属性测试，不靠这份清单写全。
SKILL_NAME_KEYS = frozenset({"name", "dir_name", "skill",
                             "added_skills", "removed_skills"})
PLUGIN_NAME_KEYS = frozenset({"namespace"})
PLUGIN_KEY_KEYS = frozenset({"plugin_key", "enabled_plugins"})
# 宿主实例名。instance_id = Path(instance_root).name —— 用户机器上的目录名，
# 常常就是工作区或客户项目的名字，与 skill 名同一性质。
# 收集它之后，instance_root / config_path / conflict_domain 里嵌着的同一串
# 会被后面的单遍替换一起清掉，不必逐个字段列举。
INSTANCE_NAME_KEYS = frozenset({"instance_id"})


def redact(obj, names=False, name_map=None):
    """把输出里的可识别信息去掉，让用户能安全地把报告贴到 issue / 群里。

    体检结果最自然的用途就是拿去问人，所以必须提供一个能安全外发的形态。
    - 路径：home 目录 -> `~`，当前目录 -> `.`，兜底再抹一次用户名
    - 名称（可选）：skill 名往往泄露业务上下文（客户名、项目代号、研究方向），
      换成稳定编号后报告结构仍可读，但不再暴露你在做什么
    """
    user = os.path.basename(HOME_N.rstrip("/")) or ""

    def fix_str(s):
        for src, dst in ((HOME_N, "~"), (CWD_N, ".")):
            if src:
                s = s.replace(src, dst).replace(src.replace("/", "\\"), dst)
        if user:
            s = re.sub(r"(?i)(?<=[/\\])" + re.escape(user) + r"(?=[/\\]|$)", "<user>", s)
        return s

    # 第一遍：收集所有名字，建立稳定映射。
    # 必须先收集完再替换 —— 名字会同时出现在 name 字段和 path 字段里，
    # 只改字段不改路径等于没脱敏（`~/.claude/skills/<真名>` 照样泄露）。
    if names and name_map is not None:
        def alias(prefix):
            n = sum(1 for v in name_map.values() if v.startswith(prefix)) + 1
            return "%s-%03d" % (prefix, n)

        def collect(o, key=None):
            if isinstance(o, dict):
                for k, v in o.items():
                    collect(v, k)
            elif isinstance(o, list):
                # 列表元素继承父键：removed_skills 里是一串裸名字符串
                for v in o:
                    collect(v, key)
            elif isinstance(o, str) and o:
                if key in SKILL_NAME_KEYS:
                    name_map.setdefault(o, alias("skill"))
                elif key in PLUGIN_NAME_KEYS:
                    name_map.setdefault(o, alias("plugin"))
                elif key in INSTANCE_NAME_KEYS:
                    name_map.setdefault(o, alias("instance"))
                elif key in PLUGIN_KEY_KEYS and "@" in o:
                    # `<plugin>@<marketplace>` —— 两段都要脱敏。
                    # marketplace 常常直接就是公司名或团队名。
                    plug, _, mkt = o.partition("@")
                    if plug:
                        name_map.setdefault(plug, alias("plugin"))
                    if mkt:
                        name_map.setdefault(mkt, alias("market"))
        collect(obj)
        # 长名优先，避免短名先命中造成部分替换
        ordered = sorted(name_map.items(), key=lambda kv: -len(kv[0]))
    else:
        ordered = []

    # 一次扫过、不回头：用交替正则一遍替换完，替换产生的别名不会再被后续
    # 规则命中。曾经是 for real, alias: s = s.replace(...) 的顺序替换 ——
    # 只要有一个真名是别名的子串（比如 skill 名叫 "in"，别名 "plugin-001"），
    # 就会把已经脱敏好的部分再改一次，结果既错又不可预测。
    # 交替顺序即 ordered 的顺序（长名在前），Python 的交替是最左优先。
    name_re = re.compile("|".join(re.escape(r) for r, _ in ordered)) if ordered else None
    alias_of = dict(ordered)

    def walk(o, key=None):
        if isinstance(o, dict):
            return {k: walk(v, k) for k, v in o.items()}
        if isinstance(o, list):
            return [walk(v, key) for v in o]
        if isinstance(o, str):
            # description 是自由文本，可能含真名、雇主、客户名、项目代号。
            # 这类内容无法靠模式匹配清除，只能整体丢弃。
            # 预算数字在脱敏前就算好了，丢正文不影响任何统计。
            if names and key == "description":
                return "<redacted: %d chars>" % len(o)
            s = fix_str(o)
            if name_re is not None:
                s = name_re.sub(lambda m: alias_of[m.group(0)], s)
            return s
        return o

    return walk(obj)


def diff_against(prev_path, now):
    """和上一次扫描对比。

    本技能自己规定「装不够 N 天的不算僵尸，2–3 周后复查」，但复查时没人记得基线。
    这个函数就是让那条建议闭环的。
    """
    try:
        prev = json.loads(Path(prev_path).read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError) as e:
        return {"error": f"读不了基线文件 {prev_path}: {e}"}

    def loaded_map(d):
        return {(s.get("host_family") or s.get("host"), s.get("instance_id"),
                 s.get("namespace") or "", s["name"]): s
                for s in d.get("skills", []) if s.get("loaded")}

    a, b = loaded_map(prev), loaded_map(now)
    pb = prev.get("description_budget", {}) or {}
    nb = now.get("description_budget", {}) or {}

    used_more = []
    for key in sorted(set(a) & set(b), key=str):
        d = b[key].get("usage_count", 0) - a[key].get("usage_count", 0)
        if d:
            used_more.append({"name": key[-1], "host": key[0],
                              "instance_id": key[1], "namespace": key[2],
                              "delta": d, "now": b[key].get("usage_count", 0)})
    used_more.sort(key=lambda x: -x["delta"])

    # 上次太新不能判、这次够岁数了的
    newly_judgeable = [
        {"name": key[-1], "host": key[0], "instance_id": key[1],
         "namespace": key[2], "usage_count": b[key].get("usage_count", 0),
         "installed_days_ago": b[key].get("installed_days_ago"),
         "verdict": "zombie" if b[key].get("usage_count", 0) == 0 else "alive"}
        for key in sorted(set(a) & set(b), key=str)
        if (a[key].get("installed_days_ago", 0) < prev.get("trigger_data", {})
            .get("zombie_min_age_days", 14)
            <= b[key].get("installed_days_ago", 0))
    ]

    def sec_keys(d):
        out = set()
        for s in d.get("security", {}).get("flagged", []):
            for f in s.get("findings", []):
                out.add((s["name"], f.get("rule"), f.get("where"), f.get("line")))
        return out

    new_sec = sorted(sec_keys(now) - sec_keys(prev))

    return {
        "baseline_file": str(prev_path),
        "added_skills": [list(k) for k in sorted(set(b) - set(a), key=str)],
        "removed_skills": [list(k) for k in sorted(set(a) - set(b), key=str)],
        "usage_delta": used_more,
        "newly_judgeable": newly_judgeable,
        "budget_delta_chars": (nb.get("used_chars", 0) - pb.get("used_chars", 0)),
        "budget_pct_then_now": [pb.get("pct_used"), nb.get("pct_used")],
        "loaded_then_now": [len(a), len(b)],
        "new_security_findings": [
            {"skill": k[0], "rule": k[1], "where": k[2], "line": k[3]}
            for k in new_sec],
        "note": "usage_delta 为两次扫描之间的触发增量。newly_judgeable 是上次还太新、"
                "这次已装够天数的 —— 这批才是新的僵尸判定对象。",
    }


# ── 解析 ─────────────────────────────────────────────────

def est_tokens(text: str) -> int:
    """粗略 token 估算。中文按 ~1.5 字符/token，英文按 ~4 字符/token。

    这是估算不是精确值。需要精确值时装 tiktoken 并替换本函数。
    """
    if not text:
        return 0
    cjk = sum(1 for ch in text if "一" <= ch <= "鿿")
    other = len(text) - cjk
    return int(cjk / 1.5 + other / 4)


def parse_frontmatter(raw: str):
    """返回 (frontmatter_dict, frontmatter_raw, body)。不依赖 yaml 库。"""
    m = FRONTMATTER_RE.match(raw)
    if not m:
        return {}, "", raw
    fm_raw = m.group(1)
    body = raw[m.end():]
    fm = {}
    key = None
    for line in fm_raw.splitlines():
        if re.match(r"^\s+", line) and key:
            fm[key] += " " + line.strip()
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            fm[key] = val.strip().strip("'\"")
    return fm, fm_raw, body


# ── 安全扫描 ─────────────────────────────────────────────

def is_cited(line: str, matched: str) -> bool:
    """命中点是否**看起来**处在引用/举例/防御说明语境里。

    仅用于排序与提示，**绝不用于抑制告警**。这个判断可以被恶意 skill 轻易绕过
    （在同一行加 "For example," 或一个不闭合的引号即可），所以它不能承担安全职责。
    """
    i = line.find(matched)
    if i < 0:
        return False
    before = line[:i]
    if any(before.count(q) % 2 == 1 for q in ('"', "'", "`")):
        return True
    if any(q in before for q in OPEN_QUOTES):
        return True
    return bool(CITATION_HINTS.search(line))


def security_scan(skill_dir: Path, skill_raw: str):
    """对 SKILL.md 正文与 scripts/ 做启发式安全检查。

    命中 != 恶意。目的是把需要人工过目的地方标出来。
    """
    findings, scanned_files = [], []

    # 排除扫描器自身：否则 scan.py 里的规则定义和 SKILL.md 里的规则说明会自己命中
    try:
        if skill_dir.resolve() == SELF_SKILL_ROOT:
            return {
                "findings": [], "max_severity": "none",
                "max_severity_uncited": "none", "cited_count": 0,
                "all_findings_cited": False, "exec_scripts": [],
                "external_urls": [], "external_url_count": 0,
                "scanned_script_count": 0, "self_excluded": True,
            }
    except OSError:
        pass

    def check(text: str, where: str):
        lines = text.splitlines()
        for name, sev, pat in SECURITY_PATTERNS:
            m = pat.search(text)
            if not m:
                continue
            snippet = m.group(0)[:80].replace("\n", " ")
            line_no = text[:m.start()].count("\n") + 1
            line = lines[line_no - 1] if line_no <= len(lines) else ""
            findings.append({
                "rule": name,
                "severity": sev,               # 原始严重度，不因 cited 降级
                "cited": is_cited(line, m.group(0)),
                "where": where,
                "line": line_no,
                "match": snippet,
            })

    check(skill_raw, "SKILL.md")

    exec_scripts = []
    # 排序理由同上：findings 与 exec_scripts 的次序都跟着它走
    for p in sorted(skill_dir.rglob("*"), key=norm):
        if not p.is_file() or p.name == "SKILL.md":
            continue
        if p.suffix.lower() in EXEC_EXT:
            rel = norm(p.relative_to(skill_dir))
            try:
                mode = p.stat().st_mode
            except OSError:
                mode = 0
            exec_scripts.append({"path": rel, "executable": bool(mode & 0o111)})
            try:
                check(p.read_text(encoding="utf-8", errors="replace"), rel)
                scanned_files.append(rel)
            except OSError:
                pass

    # 拉取第三方内容：SKILL.md 正文里的外部 URL
    urls = sorted(set(URL_RE.findall(skill_raw)))
    external = [u for u in urls
                if not any(d in u for d in ("localhost", "127.0.0.1", "example.com"))]

    # 去重同规则同位置
    seen, uniq = set(), []
    for f in findings:
        k = (f["rule"], f["where"])
        if k not in seen:
            seen.add(k)
            uniq.append(f)

    def worst(fs):
        for lvl in ("critical", "high", "medium"):
            if any(f["severity"] == lvl for f in fs):
                return lvl
        return "none"

    uncited = [f for f in uniq if not f["cited"]]
    return {
        "findings": uniq,
        # 权威严重度：包含 cited 的命中。cited 只影响排序，不影响是否上报。
        "max_severity": worst(uniq),
        # 排序辅助：只看非引用语境的命中，用来决定先看谁。
        "max_severity_uncited": worst(uncited),
        "cited_count": len(uniq) - len(uncited),
        "all_findings_cited": bool(uniq) and not uncited,
        "exec_scripts": exec_scripts,
        "external_urls": external[:10],
        "external_url_count": len(external),
        "scanned_script_count": len(scanned_files),
    }


# ── 单个 skill ───────────────────────────────────────────

def scan_skill_dir(skill_dir: Path, host: str, enabled_plugins, usage, plugins_known,
                   source_meta=None):
    md = skill_dir / "SKILL.md"
    if not md.is_file():
        return None
    try:
        raw = md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    fm, fm_raw, body = parse_frontmatter(raw)
    level, namespace, plugin_key = classify(skill_dir, host)

    # 是否被所属宿主发现。Claude 插件是唯一能由本机配置精确判定启用状态的来源。
    source_meta = source_meta or {}
    enabled_state, loaded_state, runtime_verified = None, None, False
    if host in ("codex", "openclaw", "hermes", "workbuddy", "custom"):
        loaded, why = True, level if level != "unknown" else "explicit-root"
        if host == "workbuddy" and "/plugins/marketplaces/workbuddy-builtin/" in norm(skill_dir):
            why = "workbuddy-builtin-marketplace-manifest"
    elif host == "claude-code" and level in ("personal", "project", "enterprise"):
        loaded, why = True, level
    elif level == "plugin":
        if not plugins_known:
            loaded, why = False, "plugin-state-unknown"
        # `or ()` 是第二道闸：plugins_known 为真时 enabled_plugins 理应是集合，
        # 但一个 skill 的判定失败不该让整次扫描崩掉（ENGINEERING §4.5）。
        elif plugin_key in (enabled_plugins or ()) or (namespace in (enabled_plugins or ())):
            loaded, why = True, "plugin-enabled"
        else:
            loaded, why = False, "plugin-not-enabled"
    else:
        loaded, why = False, "unknown-location"

    # 附带资源。
    # 渐进式披露把正文拆到 references/ 之后，那部分成本仍然真实存在，只是变成按需载入。
    # 只算 SKILL.md 会严重低估一个「拆过的」skill —— 而拆分正是本技能推荐的做法。
    #
    # 但要区分两类附带 .md：
    #   参考文档 —— references/ 等约定目录，或与 SKILL.md 同级。Agent 会整篇读，计入 tier2。
    #   数据语料 —— 文章库、知识库、素材。Agent 只会选择性检索，**不计入 tier2**，
    #              否则一个带 857KB 文章库的 skill 会被算成 30 万 token。
    bundled, bundled_bytes = [], 0
    refs_tokens, refs_files = 0, 0
    corpus_files, corpus_bytes = 0, 0
    # 排序理由同 collect()：遍历顺序会传导到 bundled 列表与 refs 累加顺序
    for p in sorted(skill_dir.rglob("*"), key=norm):
        if not p.is_file() or p.name == "SKILL.md":
            continue
        try:
            size = p.stat().st_size
        except OSError:
            size = 0
        bundled_bytes += size
        rel = norm(p.relative_to(skill_dir))
        bundled.append({"path": rel, "bytes": size})
        if p.suffix.lower() not in (".md", ".markdown"):
            continue
        parts = rel.split("/")
        if len(parts) == 1 and p.name.lower() in REPO_META:
            continue  # README / LICENSE 等给人看的文件，不算 Agent 的载入成本
        is_doc = len(parts) == 1 or parts[0].lower() in DOC_DIRS
        if is_doc:
            try:
                refs_tokens += est_tokens(p.read_text(encoding="utf-8",
                                                      errors="replace"))
                refs_files += 1
            except OSError:
                pass
        else:
            corpus_files += 1
            corpus_bytes += size

    name = safe_str(fm.get("name") or skill_dir.name)
    if host == "openclaw":
        configured = source_meta.get("skill_entries", {}).get(name)
        if isinstance(configured, dict) and configured.get("enabled") is False:
            enabled_state, loaded_state = False, False
            loaded, why = False, "openclaw-config-disabled"
        elif isinstance(configured, dict) and configured.get("enabled") is True:
            enabled_state, loaded_state = True, None
            loaded, why = False, "openclaw-config-enabled-runtime-unverified"
        else:
            enabled_state, loaded_state = None, None
            loaded, why = False, "openclaw-discoverable-runtime-unverified"
    elif host == "workbuddy" and source_meta.get("workbuddy_package"):
        mode = source_meta.get("workbuddy_welcome_mode")
        if not workbuddy_skill_active(source_meta.get("workbuddy_legacy_name"), mode):
            loaded, why = False, f"workbuddy-mode-filtered:{mode}"
            enabled_state, loaded_state = False, False
        else:
            why = (f"workbuddy-builtin-active-mode:{mode}" if mode else
                   "workbuddy-builtin-mode-unknown")
            enabled_state, loaded_state = (True, None) if mode else (None, None)
    hits, last_ms, matched_key = lookup_usage(usage, name, namespace)

    # 装了多久。判定僵尸前必须看这个：装了一天的 skill 零触发说明不了任何事。
    try:
        born = min(skill_dir.stat().st_ctime, md.stat().st_ctime)
    except OSError:
        born = md.stat().st_mtime
    age_days = round((time.time() - born) / 86400.0, 1)

    desc = fm.get("description", "")
    return {
        "name": name,
        "dir_name": safe_str(skill_dir.name),
        "host": host,
        "host_family": "claude-code" if host.startswith("claude-code") else host,
        "level": level,
        "namespace": namespace,
        "plugin_key": plugin_key,
        "loaded": loaded,
        "loaded_reason": why,
        "installed": True,
        "discoverable": True if host == "openclaw" else loaded,
        "enabled_state": enabled_state,
        "loaded_state": loaded_state,
        "runtime_verified": runtime_verified,
        "instance_id": source_meta.get("instance_id"),
        "instance_root": source_meta.get("instance_root"),
        "config_path": source_meta.get("config_path"),
        "root_kind": source_meta.get("root_kind"),
        "conflict_domain": (f"openclaw:{source_meta.get('instance_id')}"
                            if host == "openclaw" and source_meta.get("instance_id")
                            else host),
        "path": norm(skill_dir),
        "content_hash": hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12],
        "description": desc,
        "description_chars": len(desc),
        # Tier 1：启动时常驻上下文的部分
        "tier1_tokens": est_tokens(fm_raw),
        # Tier 2：触发后才载入。
        #   core = SKILL.md 正文，**必然**载入
        #   refs = references/ 等附带 .md，按需载入
        #   max  = 全读的最坏情况
        "tier2_tokens": est_tokens(body),          # = core，保留原字段名
        "tier2_core_tokens": est_tokens(body),
        "tier2_refs_tokens": refs_tokens,
        "tier2_refs_files": refs_files,
        "tier2_max_tokens": est_tokens(body) + refs_tokens,
        "body_lines": body.count("\n") + 1 if body else 0,
        "bundled_files": len(bundled),
        "bundled_bytes": bundled_bytes,
        "data_corpus_files": corpus_files,
        "data_corpus_bytes": corpus_bytes,
        "mtime": int(md.stat().st_mtime),
        "installed_days_ago": age_days,
        "usage_count": hits,
        "last_used_days_ago": days_since(last_ms),
        "usage_key_matched": matched_key,
        "has_name": bool(fm.get("name")),
        "has_description": bool(desc),
        "security": security_scan(skill_dir, raw),
    }


def collect(roots, enabled_plugins, usage, plugins_known):
    found, scanned_roots, unreadable, seen = [], [], [], set()
    for item in roots:
        host, root = item[:2]
        source_meta = item[2] if len(item) > 2 else {}
        base = Path(os.path.expanduser(root))
        try:
            key = norm(base.resolve())
        except OSError:
            key = norm(base)
        dedupe_key = (host, source_meta.get("instance_id"), key)
        if dedupe_key in seen:
            continue
        seen.add(dedupe_key)
        if not base.is_dir():
            continue
        scanned_roots.append({"host": host, "path": norm(base),
                              "instance_id": source_meta.get("instance_id"),
                              "root_kind": source_meta.get("root_kind")})
        # skill 目录 = 直接含 SKILL.md 的目录（含插件的嵌套结构）
        #
        # **必须排序。**rglob 不保证顺序（Rust 的 walkdir 同样不保证，且与
        # rglob 不一致），而遍历顺序会一路传导到输出：排序键相同的元素之间
        # 次序会抖，更要命的是 --redact-names 的别名编号按名字**出现顺序**
        # 分配，于是同一台机器上两次扫描可以给出不同的 skill-001。
        # 按 norm() 的字符串排序而不是按 Path 排序：Path 比较的是 parts 元组，
        # "a/b" 与 "a-c" 的先后与字符串比较相反，跨语言对不上。
        # only_direct：只看这一层的 SKILL.md，不向下递归。
        # builtin-plugin 的包根用它 —— 那个目录里同时躺着 experts/ 与
        # skills/，递归会把包内部的角色定义也当成顶层 skill。
        mds = ([base / "SKILL.md"] if source_meta.get("only_direct")
               else sorted(base.rglob("SKILL.md"), key=norm))
        for md in mds:
            if not md.is_file():
                continue
            rec = scan_skill_dir(md.parent, host, enabled_plugins, usage, plugins_known,
                                 source_meta)
            if rec:
                found.append(rec)
            elif md.is_file():
                # rglob 找到了 SKILL.md，scan_skill_dir 却没产出记录 —— 只可能是
                # 读取失败（权限、IO 错误）。
                # 曾经这里直接跳过：一个权限异常的 skill 会**从报告里彻底消失**，
                # 用户看到的清点数字是错的，而且没有任何迹象表明少了东西。
                # 对一个做清点的工具，静默丢项就是错误答案。
                unreadable.append({"name": md.parent.name,
                                   "path": norm(md.parent),
                                   "host": host,
                                   "reason": "SKILL.md 存在但读不了（权限或 IO 错误）"})
    return found, scanned_roots, unreadable


# ── 主流程 ───────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", action="version",
                    version="skill-vitals %s" % __version__)
    ap.add_argument("--host", choices=("all", "claude-code", "codex", "openclaw", "hermes", "workbuddy"),
                    default="all", help="只分析一个宿主；默认按宿主分别扫描全部支持的宿主")
    ap.add_argument("--path", action="append", default=[],
                    help="额外扫描路径，可重复")
    ap.add_argument("--json", help="输出文件；省略则打印到 stdout")
    ap.add_argument("--budget", type=int, default=DEFAULT_DESC_BUDGET,
                    help=f"描述字符预算，默认 {DEFAULT_DESC_BUDGET}")
    ap.add_argument("--all", action="store_true",
                    help="预算与冲突按磁盘上所有 skill 算（诊断用；默认只算已加载的）")
    ap.add_argument("--zombie-age", type=int, default=ZOMBIE_MIN_AGE_DAYS,
                    help=f"判定僵尸所需的最小安装天数，默认 {ZOMBIE_MIN_AGE_DAYS}")
    ap.add_argument("--split-threshold", type=int, default=6000,
                    help="tier2_core_tokens 超过多少就建议拆分，默认 6000（约窗口 3%%）")
    ap.add_argument("--baseline", help="上一次的 scan JSON，用于输出变化对比")
    ap.add_argument("--redact", action="store_true",
                    help="脱敏：绝对路径里的 home 目录和用户名替换为 ~ / <user>。"
                         "打算把结果贴给别人看时用")
    ap.add_argument("--self-root",
                    help="本工具自身的 skill 目录，安全扫描会跳过它。"
                         "省略时按脚本位置推断；二进制形态下那条线断了，故可显式指定")
    ap.add_argument("--redact-names", action="store_true",
                    help="连 skill 名一起脱敏（换成 skill-001 这类编号）。"
                         "skill 名常常泄露业务上下文，外发前建议一并开启")
    args = ap.parse_args()

    # 负数一律拒绝。**不能静默接受后产出垃圾** —— `--budget -1` 曾经算出
    # `pct_used: -6300.0` 并原样打进摘要行，一个负百分比被当成测量值输出。
    # 拒绝比编一个数好：这是本工具反复申明的那条底线。
    for flag, value in (("--budget", args.budget),
                        ("--zombie-age", args.zombie_age),
                        ("--split-threshold", args.split_threshold)):
        if value is not None and value < 0:
            ap.error("%s 不能为负数（收到 %d）" % (flag, value))

    # 显式指定「自己」在哪。Python 版本来能靠 __file__ 推断，二进制形态
    # 下那条线断了（二进制装在 npm/cargo 的 bin 目录，与 skill 目录无关），
    # 所以两个实现都提供这个开关，保持命令面一致。
    # **排除是可见的**：被排除的 skill 带着 self_excluded=true 出现在报告里。
    if args.self_root:
        global SELF_SKILL_ROOT
        SELF_SKILL_ROOT = Path(args.self_root).resolve()

    zombie_age = args.zombie_age
    budget = args.budget
    enabled_plugins, usage, host_cfg = read_host_config()
    plugins_known = host_cfg is not None

    roots = list(DEFAULT_ROOTS)
    for p, meta in read_openclaw_roots():
        roots.append(("openclaw", p, meta))
    for p in read_hermes_external_dirs():
        roots.append(("hermes", p))
    workbuddy_mode, workbuddy_roots = None, []
    if os.environ.get("SKILL_VITALS_DISABLE_WORKBUDDY_BUILTINS") != "1":
        workbuddy_mode = read_workbuddy_welcome_mode()
        workbuddy_roots = read_workbuddy_builtin_roots()
        for p, meta in workbuddy_roots:
            roots.append(("workbuddy", p, {**meta,
                         "workbuddy_welcome_mode": workbuddy_mode}))
    if args.host != "all":
        roots = [r for r in roots if r[0] == args.host or
                 (args.host == "claude-code" and r[0] == "claude-code-plugins")]
    roots += [(args.host if args.host != "all" else "custom", p) for p in args.path]
    skills, scanned, unreadable = collect(roots, enabled_plugins, usage, plugins_known)
    openclaw_runtime = []
    if os.environ.get("SKILL_VITALS_DISABLE_OPENCLAW_RUNTIME") != "1" and args.host in ("all", "openclaw"):
        instance_roots = sorted({s[2].get("instance_root") for s in roots
                                 if len(s) > 2 and s[0] == "openclaw" and
                                 s[2].get("instance_root")})
        openclaw_runtime = [read_openclaw_runtime(Path(p)) for p in instance_roots]
        skills = apply_openclaw_runtime(skills, openclaw_runtime)
    codex_runtime = {"available": False, "source": "codex app-server skills/list",
                     "skills": [], "errors": ["host not selected"]}
    if os.environ.get("SKILL_VITALS_DISABLE_CODEX_RUNTIME") == "1":
        codex_runtime["errors"] = ["disabled by SKILL_VITALS_DISABLE_CODEX_RUNTIME"]
    elif args.host in ("all", "codex"):
        codex_runtime = read_codex_runtime(Path.cwd())
        if codex_runtime["available"]:
            skills = apply_codex_runtime(skills, codex_runtime)

    loaded = [s for s in skills if s["loaded"]]
    analysis_candidates = [s for s in skills if s["loaded"] or
                           (s["host_family"] == "openclaw" and s["discoverable"])]
    # 预算和冲突只看真的进上下文的那批。这是本脚本最重要的一条口径。
    scope = skills if args.all else analysis_candidates

    # ── 同名 skill 的副本 ─────────────────────────────────
    # 按 (namespace, name) 去重：插件里的 skill 有命名空间隔离，
    # discord:access 和 telegram:access 不是冲突。
    by_key = {}
    for s in scope:
        # 同名 skill 只会在同一宿主内争抢；跨宿主是独立运行时。
        by_key.setdefault((s["conflict_domain"], s["namespace"] or "", s["name"]), []).append(s)

    conflicts = []
    for (_, _, n), v in by_key.items():
        if len(v) < 2:
            continue
        ranked = sorted(v, key=level_rank)
        winner, losers = ranked[0], ranked[1:]
        identical = len({x["content_hash"] for x in v}) == 1

        if identical:
            kind, severity = "redundant", "low"
        else:
            # 被覆盖的那份比生效的更新 —— 新版本被旧版本静默盖掉
            newer_loser = max(losers, key=lambda x: x["mtime"])
            if newer_loser["mtime"] > winner["mtime"]:
                kind, severity = "shadowed_newer", "high"
            else:
                kind, severity = "intentional_override", "medium"

        conflicts.append({
            "host": winner["host_family"],
            "instance_id": winner["instance_id"],
            "conflict_domain": winner["conflict_domain"],
            "name": n,
            "kind": kind,
            "severity": severity,
            "effective": {"level": winner["level"], "path": winner["path"],
                          "hash": winner["content_hash"], "mtime": winner["mtime"]},
            "shadowed": [{"level": x["level"], "path": x["path"],
                          "hash": x["content_hash"], "mtime": x["mtime"]}
                         for x in losers],
        })
    conflicts.sort(key=lambda c: {"high": 0, "medium": 1, "low": 2}[c["severity"]])

    unique = list(by_key.values())
    tier1_total = sum(v[0]["tier1_tokens"] for v in unique)

    # ── 描述预算 ─────────────────────────────────────────
    # Claude Code 把 name+description 拼成列表注入系统提示，有硬预算。
    # 超出后静默丢弃描述（据报从调用最少的开始），无告警。
    is_codex_budget = args.host == "codex"
    effective_budget = CODEX_FALLBACK_DESC_BUDGET if is_codex_budget else budget
    desc_chars = sum(len(v[0]["description"]) + len(v[0]["name"]) + 4 +
                     (len(v[0]["path"]) + 1 if is_codex_budget else 0)
                     for v in unique)
    over = desc_chars - effective_budget
    if over > 0:
        lens = sorted((len(v[0]["description"]) for v in unique), reverse=True)
        acc, at_risk = 0, 0
        for L in lens:
            acc += L
            at_risk += 1
            if acc >= over:
                break
    else:
        at_risk = 0

    longest = sorted(unique, key=lambda v: -len(v[0]["description"]))[:5]

    budget_report = {
        "available": args.host in ("claude-code", "codex"),
        "scope": "all-on-disk" if args.all else "loaded-only",
        "counted_skills": len(unique),
        "budget_chars": effective_budget,
        "used_chars": desc_chars,
        "pct_used": round(desc_chars / effective_budget * 100, 1) if effective_budget else None,
        "over_by_chars": max(0, over),
        "skills_possibly_dropped": at_risk,
        "longest_descriptions": [
            {"name": v[0]["name"], "chars": len(v[0]["description"])}
            for v in longest],
        "excludes_builtin_skills": True,
        "policy": ("Codex initial skill list: at most 2% of model context, or 8000 chars "
                   "when context is unknown" if is_codex_budget else
                   "Claude Code SLASH_COMMAND_TOOL_CHAR_BUDGET"),
        "note": ("Codex 官方口径包含 name、description、path；本报告无法从 skills/list 获得"
                 "当前模型上下文窗口，因此采用官方 fallback 8000 字符。Codex 会先缩短描述，"
                 "仍超限时省略部分 skill 并发出警告。" if is_codex_budget else
                 "Claude Code 预算口径随版本变化；本值取自环境变量或默认 15000。"
                 "本数字不含打包在 CLI、磁盘无 SKILL.md 的内置 skill。"),
        "workaround": None if is_codex_budget else "SLASH_COMMAND_TOOL_CHAR_BUDGET=30000",
    }
    if not budget_report["available"]:
        # 这是 Claude Code 专属的配置与预算；其他宿主没有等价、可验证的阈值。
        budget_report.update({
            "scope": "not-available",
            "counted_skills": None,
            "budget_chars": None,
            "used_chars": None,
            "pct_used": None,
            "over_by_chars": None,
            "skills_possibly_dropped": None,
            "longest_descriptions": [],
            "excludes_builtin_skills": None,
            "workaround": None,
        })

    # ── 触发数据 ─────────────────────────────────────────
    trigger_available = args.host == "claude-code" and bool(usage)
    trigger_scope = loaded if trigger_available else []
    zombies = [s for s in trigger_scope
               if s["usage_count"] == 0 and s["installed_days_ago"] >= zombie_age]
    too_new = [s for s in trigger_scope
               if s["usage_count"] == 0 and s["installed_days_ago"] < zombie_age]
    trigger_report = {
        "available": trigger_available,
        "source": "~/.claude.json -> skillUsage",
        "entries_in_host_record": len(usage),
        "counts_are": "lifetime cumulative, not last-30-days",
        "zombie_min_age_days": zombie_age,
        "zombie_candidates": [
            {"name": s["name"], "path": s["path"],
             "installed_days_ago": s["installed_days_ago"],
             "tier1_tokens": s["tier1_tokens"]}
            for s in sorted(zombies, key=lambda x: -x["tier1_tokens"])],
        "too_new_to_judge": [
            {"name": s["name"], "installed_days_ago": s["installed_days_ago"]}
            for s in sorted(too_new, key=lambda x: x["installed_days_ago"])],
        "note": "零触发只有在装够 %d 天后才说明问题。too_new_to_judge 里的不要当僵尸报。"
                % zombie_age,
    }

    # ── 结构：谁该拆 ─────────────────────────────────────
    # 判据是 token 不是行数。实测同一库内密度能差 4 倍以上
    # （487 行 / 21.4 tok/行 的文件比 794 行 / 4.9 tok/行 的贵 2.7 倍），
    # 所以按行数给拆分建议会把结论给反。
    oversized = [s for s in analysis_candidates
                 if s["tier2_core_tokens"] > args.split_threshold]
    oversized.sort(key=lambda s: -s["tier2_core_tokens"])
    structure_report = {
        "split_threshold_tokens": args.split_threshold,
        "criterion": "tier2_core_tokens（SKILL.md 正文），行数仅作参考",
        "oversized": [
            {"name": s["name"], "path": s["path"],
             "tier2_core_tokens": s["tier2_core_tokens"],
             "tier2_refs_tokens": s["tier2_refs_tokens"],
             "tier2_max_tokens": s["tier2_max_tokens"],
             "body_lines": s["body_lines"],
             "tokens_per_line": round(s["tier2_core_tokens"] / max(s["body_lines"], 1), 1),
             "pct_of_200k_if_fully_read": round(s["tier2_max_tokens"] / 200000 * 100, 2)}
            for s in oversized],
        "missing_frontmatter": [
            {"name": s["name"], "path": s["path"],
             "has_name": s["has_name"], "has_description": s["has_description"]}
            for s in loaded if not (s["has_name"] and s["has_description"])],
        "already_split": [
            {"name": s["name"], "core": s["tier2_core_tokens"],
             "refs": s["tier2_refs_tokens"], "refs_files": s["tier2_refs_files"],
             "max": s["tier2_max_tokens"]}
            for s in sorted(loaded, key=lambda x: -x["tier2_refs_tokens"])
            if s["tier2_refs_tokens"] > 0],
        "large_data_corpus": [
            {"name": s["name"], "files": s["data_corpus_files"],
             "mb": round(s["data_corpus_bytes"] / 1048576, 1)}
            for s in sorted(loaded, key=lambda x: -x["data_corpus_bytes"])
            if s["data_corpus_bytes"] > 1048576],
        "note": "oversized 用 core 判定（必然载入的部分）。already_split 里 max 才是"
                "全读时的真实成本 —— 拆分降低的是**平均**成本，不是最坏成本。"
                "large_data_corpus 是子目录里的 .md 语料（文章库/知识库），"
                "按检索使用、不计入 tier2，报告里只需提一句体积。",
    }

    # ── 安全汇总 ─────────────────────────────────────────
    sev_order = {"critical": 0, "high": 1, "medium": 2, "none": 3}
    # 所有有命中的都上报，cited 与否只决定排序先后，不决定是否出现。
    flagged = [s for s in skills if s["security"]["max_severity"] != "none"]
    flagged.sort(key=lambda s: (sev_order[s["security"]["max_severity_uncited"]],
                                sev_order[s["security"]["max_severity"]],
                                not s["loaded"]))
    security_report = {
        "flagged_count": len(flagged),
        "critical_count": sum(1 for s in flagged
                              if s["security"]["max_severity"] == "critical"),
        "critical_uncited_count": sum(1 for s in flagged
                                      if s["security"]["max_severity_uncited"] == "critical"),
        "all_cited_count": sum(1 for s in flagged
                               if s["security"]["all_findings_cited"]),
        "fetches_external_count": sum(1 for s in skills
                                      if s["security"]["external_url_count"] > 0),
        "with_scripts_count": sum(1 for s in skills if s["security"]["exec_scripts"]),
        "flagged": [{"name": s["name"], "path": s["path"], "loaded": s["loaded"],
                     "severity": s["security"]["max_severity"],
                     "severity_uncited": s["security"]["max_severity_uncited"],
                     "all_findings_cited": s["security"]["all_findings_cited"],
                     "findings": s["security"]["findings"]} for s in flagged[:30]],
        "note": "启发式规则，命中不等于恶意，需人工过目；同样会漏报。扫描器自身文件已排除。"
                "`cited=true` 表示命中点看起来在引用/举例/防御说明语境里——"
                "**这只影响排序，不降低严重度、不抑制上报**。"
                "该标记可被轻易绕过（同行加 'For example,' 或一个不闭合的引号），"
                "所以绝不能拿它当作安全结论。每条命中都带行号，打开看一眼才是防线。",
    }

    # 上下文属于各自宿主，不能把 Codex、Claude Code 等的数值相加后当成一个窗口。
    host_summaries = {}
    for host in ("claude-code", "codex", "openclaw", "hermes", "workbuddy"):
        host_skills = [s for s in skills if s["host_family"] == host]
        host_loaded = [s for s in host_skills if s["loaded"]]
        host_discoverable = [s for s in host_skills if s["discoverable"]]
        summary_scope = host_discoverable if host == "openclaw" else host_loaded
        host_groups = {}
        for s in summary_scope:
            host_groups.setdefault((s["instance_id"] or "", s["namespace"] or "",
                                    s["name"]), []).append(s)
        host_unique = [sorted(group, key=level_rank)[0]
                       for group in host_groups.values()]
        # 这个宿主**有没有运行时证据可拿**。
        #
        # Claude Code / Hermes / WorkBuddy 压根没有逐 skill 的运行时接口可问，
        # Codex 与 OpenClaw 有但可能探测失败。两种情况下面的两个计数都必须是
        # **null 而不是 0** —— 0 读起来是「问到了，是零个」，而真相是「问不到」。
        #
        # 这条曾经写成 0：claude-code 那行会显示 verified_loaded=0 而
        # discoverable=31，读者以为「31 个一个都没被证实」，实际上这个字段
        # 对 Claude Code 永远不适用。同一份报告里 openclaw_instances 的
        # runtime_catalog_skills 探测不到时就是 null —— 两处不该不一致。
        runtime_evidence = (
            codex_runtime["available"] if host == "codex" else
            any(r.get("available") for r in openclaw_runtime) if host == "openclaw" else
            False)

        # 「有几个 unique skill 拿到了运行时证据」。**按组内任一副本算**：
        # 证据属于 skill，不属于某一份副本 —— Codex 按路径匹配，可能只标中
        # 被遮蔽的那份，此时说「没有证据」是错的。
        #
        # 曾经 OpenClaw 分支在这里数的是**运行时清单的条数**，与其余分支量的
        # 不是一回事（一个是「宿主说它有多少」，一个是「我们报的这些有多少有
        # 证据」）。同一个字段名下两种含义，且清单条数在
        # openclaw_instances[].runtime_catalog_skills 已经报过。现已统一。
        verified_unique = len({(s["instance_id"], s["namespace"] or "", s["name"])
                               for s in summary_scope if s["runtime_verified"]})

        host_summaries[host] = {
            "skills_on_disk": len(host_skills),
            "discoverable_skills": len(host_discoverable),
            "runtime_verified_loaded_skills": (
                sum(1 for s in host_skills if s["runtime_verified"] and s["loaded"])
                if runtime_evidence else None),
            "runtime_verified_unique_skills": verified_unique if runtime_evidence else None,
            "unique_discoverable_skills": len(host_unique),
            "tier1_total_tokens": sum(s["tier1_tokens"] for s in host_unique),
            "description_budget": ("available" if host == "claude-code" else
                                   "official-estimate" if host == "codex" and codex_runtime["available"]
                                   else "configurable" if host == "openclaw"
                                   else "not-available"),
            "trigger_data": "available" if host == "claude-code" and bool(usage) else "not-available",
        }

    openclaw_instances = {}
    for instance_id in sorted({s["instance_id"] for s in skills
                               if s["host_family"] == "openclaw" and s["instance_id"]}):
        instance_skills = [s for s in skills if s["host_family"] == "openclaw" and
                           s["instance_id"] == instance_id]
        discoverable = [s for s in instance_skills if s["discoverable"]]
        disabled = [s for s in discoverable if s["enabled_state"] is False]
        unknown = [s for s in discoverable if s["enabled_state"] is None]
        unique_names = {(s["namespace"] or "", s["name"]) for s in discoverable}
        runtime = next((r for r in openclaw_runtime
                        if r.get("instance_id") == instance_id), None)
        openclaw_instances[instance_id] = {
            "instance_root": next((s["instance_root"] for s in instance_skills
                                   if s["instance_root"]), None),
            "config_path": next((s["config_path"] for s in instance_skills
                                 if s["config_path"]), None),
            "skills_on_disk": len(instance_skills),
            "discoverable_skills": len(discoverable),
            "unique_discoverable_skills": len(unique_names),
            "explicitly_disabled": len(disabled),
            "enabled_unknown": len(unknown),
            "runtime_verified": sum(1 for s in discoverable if s["runtime_verified"]),
            "runtime_catalog_skills": (len(runtime.get("skills", []))
                                       if runtime and runtime.get("available") else None),
            "runtime_semantics": ("eligible/model-visible metadata; full SKILL.md body load unknown"
                                  if runtime and runtime.get("available") else
                                  "filesystem candidates; runtime unavailable"),
            "tier1_candidate_tokens": sum(s["tier1_tokens"] for s in discoverable),
        }

    out = {
        "scanned_roots": scanned,
        "host_selection": args.host,
        "host_summaries": host_summaries,
        "openclaw_runtime": openclaw_runtime,
        # 扫描过程中读不了的 skill。**必须显式出现**，不能静默丢掉 ——
        # 缺一项的报告有价值，少一项却不说的报告会误导清点。
        "unreadable_skills": unreadable,
        "total_skills_on_disk": len(skills),
        "loaded_skills": len(loaded),
        "unique_skills": len(unique),
        "plugin_state": {
            "host_config_read": plugins_known,
            # 同上：读不到配置时 enabled_plugins 是 None，不是空集合。
            # 两者在报告里含义完全不同，见下面的 note。
            "enabled_plugins": sorted(enabled_plugins or ()),
            "note": "未启用的插件副本在磁盘上但不进上下文，不计入预算。"
                    "host_config_read=false 时无法判断，插件一律按未加载处理。",
        },
        "codex_runtime": {
            "available": codex_runtime["available"],
            "source": codex_runtime["source"],
            "cwd": codex_runtime.get("cwd"),
            "catalog_skills": len(codex_runtime.get("skills", [])),
            "errors": codex_runtime["errors"],
            "note": "available=true 时，Codex 的发现、scope、enabled、interface、dependencies "
                    "来自官方 app-server；触发次数仍无公开的逐 skill 接口。",
        },
        "workbuddy_discovery": {
            "source": "manifest-selected top-level packages resolved in plugins/cache/workbuddy-builtin",
            "user_root": norm(Path(os.path.expanduser("~/.workbuddy/skills"))),
            "builtin_root": norm(Path(os.path.expanduser(
                "~/.workbuddy/plugins/marketplaces/workbuddy-builtin"))),
            "cache_root": norm(Path(os.path.expanduser(
                "~/.workbuddy/plugins/cache/workbuddy-builtin"))),
            "excluded_roots": ["~/.workbuddy/connectors-marketplace (catalog only)",
                               "builtin-plugin 包内部的非顶层内容（如 experts/ 下的角色定义）"],
            "welcome_mode": workbuddy_mode,
            # 数**包**，不是数 root：一个 builtin-plugin 包会展开成多个 root
            # （包自身 + skills/ 下每一个），字段名说的是 packages。
            "top_level_manifest_packages": len(
                {m.get("workbuddy_package") for _, m in workbuddy_roots
                 if m.get("workbuddy_package")}),
            "skill_roots_from_manifest": len(workbuddy_roots),
            "enabled_state": "mode-filtered manifest evidence; no public per-skill runtime API",
            "trigger_data": "not-available",
        },
        "openclaw_instances": openclaw_instances,
        "description_budget": budget_report,
        "trigger_data": trigger_report,
        "structure": structure_report,
        "security": security_report,
        "tier1_total_tokens": tier1_total,
        "tier1_pct_of_200k": round(tier1_total / 200000 * 100, 2),
        "conflicts": conflicts,
        "precedence_note": "覆盖只在同一宿主内比较。Claude Code：enterprise > personal > project > plugin；"
                           "OpenClaw：workspace > project > personal > managed。"
                           "插件里的 skill 按 <plugin>:<name> 命名空间隔离，同名不算冲突。",
        "cross_host_note": "不同宿主的上下文互不共享；请使用 host_summaries 或 --host 查看单一宿主，"
                           "不要把顶层 Tier1 或描述预算当作跨宿主总预算。",
        "skills": sorted(skills, key=lambda s: (not s["loaded"], -s["tier1_tokens"])),
    }

    if args.baseline:
        out["diff_vs_baseline"] = diff_against(args.baseline, out)

    if args.redact or args.redact_names:
        out = redact(out, names=args.redact_names, name_map={})
        out["redacted"] = {
            "paths": True,
            "names": bool(args.redact_names),
            "note": "本输出已脱敏，可安全外发。未脱敏的原始数据请重新扫描。",
        }

    text = json.dumps(out, ensure_ascii=False, indent=2)
    if args.json:
        Path(args.json).write_text(text, encoding="utf-8")
        budget_text = (f"{budget_report['pct_used']}%（{budget_report['scope']}）"
                       if budget_report["available"] else
                       "可配置（本实例未设置）" if args.host == "openclaw" else "未获取")
        active_text = (f"运行时可见（记录数）{len(loaded)} 个"
                       if args.host == "openclaw" else f"其中已加载 {len(loaded)} 个")
        print(f"已写入 {args.json}：磁盘 {len(skills)} 个 skill，"
              f"{active_text}，"
              f"Tier1 合计约 {tier1_total} tokens，"
              f"描述预算 {budget_text}，"
              f"触发数据 {'已获取' if trigger_report['available'] else '未获取'}，"
              f"建议拆分 {len(structure_report['oversized'])} 个，"
              f"安全告警 {security_report['flagged_count']} 条"
              f"（其中 {security_report['all_cited_count']} 个全部命中疑似引用语境，"
              f"仍需过目）")
    else:
        print(text)

    if unreadable:
        # 也写一份到 stderr：JSON 里那条字段只有解析输出的人会看到，
        # 而直接在终端跑的人同样需要知道清点数字是不完整的。
        print("\n注意：%d 个 skill 的 SKILL.md 读不了，未计入统计（见 "
              "unreadable_skills）：" % len(unreadable), file=sys.stderr)
        for u in unreadable[:10]:
            print("  %s" % u["path"], file=sys.stderr)

    if not skills:
        print("\n未找到任何 skill。请用 --path 指定实际安装目录。",
              file=sys.stderr)


if __name__ == "__main__":
    main()
