#!/usr/bin/env python3
"""
扫描本机各 Agent 宿主的 skill 安装目录，输出成本清单（JSON）。

只做确定性统计，不做判断。判断交给调用它的 Agent。

关键设计：**区分「装在磁盘上」和「真的进了上下文」**。
未启用的插件副本、其他宿主（Codex 等）的 skill 都在磁盘上，但不占 Claude Code
的描述预算。把它们算进去会得出「预算超支」的假警报。

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
import sys
import time
from pathlib import Path

# 覆盖优先级：数字越小越优先（enterprise > personal > project > plugin/bundled）
LEVEL_RANK = {"enterprise": 0, "personal": 1, "project": 2, "plugin": 3,
              "other-host": 8, "unknown": 9}

# Claude Code 的 skill/命令描述总预算。默认约 15000 字符（≈4000 token）。
# 超出后描述被静默丢弃，无任何告警。可用 SLASH_COMMAND_TOOL_CHAR_BUDGET 调大。
# 不同版本口径不一（另有"上下文窗口 1%"的说法），故做成可配置。
DEFAULT_DESC_BUDGET = int(os.environ.get("SLASH_COMMAND_TOOL_CHAR_BUDGET", 15000))

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
# host 为 "claude-code*" 的才可能进 Claude Code 的上下文。
DEFAULT_ROOTS = [
    ("claude-code", "~/.claude/skills"),
    ("claude-code-plugins", "~/.claude/plugins"),
    ("codex", "~/.codex/skills"),
    ("openclaw", "~/.openclaw/skills"),
    ("workbuddy", "~/.workbuddy/skills"),
    ("cc-switch", "~/.cc-switch/skills"),
    ("cursor", "~/.cursor/skills"),
    ("gemini-cli", "~/.gemini/skills"),
    ("opencode", "~/.opencode/skills"),
    ("project-local", "./.claude/skills"),
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


# ── 路径工具（分隔符无关，Windows/POSIX 通用）────────────────

def norm(p) -> str:
    """统一成正斜杠，让所有路径判断在 Windows 上也成立。"""
    return str(p).replace("\\", "/")


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
    if "/managed" in s or "/etc/" in s or "enterprise" in s:
        return "enterprise", None, None
    if s.startswith(HOME_N + "/.claude/skills"):
        return "personal", None, None
    if s.startswith(CWD_N + "/.claude/skills") or norm(skill_dir).startswith(".claude/skills"):
        return "project", None, None
    if host.startswith("claude-code"):
        return "unknown", None, None
    return "other-host", None, None


# ── 宿主配置：哪些插件启用了、每个 skill 触发过几次 ──────────

def read_host_config():
    """读 ~/.claude.json。

    Claude Code 自己就维护着两份我们需要的数据：
      enabledPlugins - 决定插件里的 skill 是否进上下文
      skillUsage     - 每个 skill 的 usageCount / lastUsedAt（精确，非估算）
    比解析 ~/.claude/projects/**/*.jsonl 又快又准。
    """
    p = Path(os.path.expanduser("~/.claude.json"))
    if not p.is_file():
        return None, {}, {}
    try:
        d = json.loads(p.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError):
        return None, {}, {}

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

    # 第一遍：收集所有 skill 名，建立稳定映射。
    # 必须先收集完再替换 —— 名字会同时出现在 name 字段和 path 字段里，
    # 只改字段不改路径等于没脱敏（`~/.claude/skills/<真名>` 照样泄露）。
    if names and name_map is not None:
        def collect(o, key=None):
            if isinstance(o, dict):
                for k, v in o.items():
                    collect(v, k)
            elif isinstance(o, list):
                for v in o:
                    collect(v, key)
            elif isinstance(o, str) and key in ("name", "dir_name", "skill"):
                name_map.setdefault(o, "skill-%03d" % (len(name_map) + 1))
        collect(obj)
        # 长名优先替换，避免短名先命中造成部分替换
        ordered = sorted(name_map.items(), key=lambda kv: -len(kv[0]))
    else:
        ordered = []

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
            for real, alias in ordered:
                if real and real in s:
                    s = s.replace(real, alias)
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
        return {s["name"]: s for s in d.get("skills", []) if s.get("loaded")}

    a, b = loaded_map(prev), loaded_map(now)
    pb = prev.get("description_budget", {}) or {}
    nb = now.get("description_budget", {}) or {}

    used_more = []
    for n in sorted(set(a) & set(b)):
        d = b[n].get("usage_count", 0) - a[n].get("usage_count", 0)
        if d:
            used_more.append({"name": n, "delta": d,
                              "now": b[n].get("usage_count", 0)})
    used_more.sort(key=lambda x: -x["delta"])

    # 上次太新不能判、这次够岁数了的
    newly_judgeable = [
        {"name": n, "usage_count": b[n].get("usage_count", 0),
         "installed_days_ago": b[n].get("installed_days_ago"),
         "verdict": "zombie" if b[n].get("usage_count", 0) == 0 else "alive"}
        for n in sorted(set(a) & set(b))
        if (a[n].get("installed_days_ago", 0) < prev.get("trigger_data", {})
            .get("zombie_min_age_days", 14)
            <= b[n].get("installed_days_ago", 0))
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
        "added_skills": sorted(set(b) - set(a)),
        "removed_skills": sorted(set(a) - set(b)),
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
    for p in skill_dir.rglob("*"):
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

def scan_skill_dir(skill_dir: Path, host: str, enabled_plugins, usage, plugins_known):
    md = skill_dir / "SKILL.md"
    if not md.is_file():
        return None
    try:
        raw = md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    fm, fm_raw, body = parse_frontmatter(raw)
    level, namespace, plugin_key = classify(skill_dir, host)

    # 是否真的进 Claude Code 的上下文
    if level in ("personal", "project", "enterprise"):
        loaded, why = True, level
    elif level == "plugin":
        if not plugins_known:
            loaded, why = False, "plugin-state-unknown"
        elif plugin_key in enabled_plugins or (namespace in enabled_plugins):
            loaded, why = True, "plugin-enabled"
        else:
            loaded, why = False, "plugin-not-enabled"
    elif level == "other-host":
        loaded, why = False, f"other-host:{host}"
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
    for p in skill_dir.rglob("*"):
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

    name = fm.get("name") or skill_dir.name
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
        "dir_name": skill_dir.name,
        "host": host,
        "level": level,
        "namespace": namespace,
        "plugin_key": plugin_key,
        "loaded": loaded,
        "loaded_reason": why,
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
    found, scanned_roots = [], []
    for host, root in roots:
        base = Path(os.path.expanduser(root))
        if not base.is_dir():
            continue
        scanned_roots.append({"host": host, "path": norm(base)})
        # skill 目录 = 直接含 SKILL.md 的目录（含插件的嵌套结构）
        for md in base.rglob("SKILL.md"):
            rec = scan_skill_dir(md.parent, host, enabled_plugins, usage, plugins_known)
            if rec:
                found.append(rec)
    return found, scanned_roots


# ── 主流程 ───────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
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
    ap.add_argument("--redact-names", action="store_true",
                    help="连 skill 名一起脱敏（换成 skill-001 这类编号）。"
                         "skill 名常常泄露业务上下文，外发前建议一并开启")
    args = ap.parse_args()

    zombie_age = args.zombie_age
    budget = args.budget
    enabled_plugins, usage, host_cfg = read_host_config()
    plugins_known = host_cfg is not None

    roots = list(DEFAULT_ROOTS) + [("custom", p) for p in args.path]
    skills, scanned = collect(roots, enabled_plugins, usage, plugins_known)

    loaded = [s for s in skills if s["loaded"]]
    # 预算和冲突只看真的进上下文的那批。这是本脚本最重要的一条口径。
    scope = skills if args.all else loaded

    # ── 同名 skill 的副本 ─────────────────────────────────
    # 按 (namespace, name) 去重：插件里的 skill 有命名空间隔离，
    # discord:access 和 telegram:access 不是冲突。
    by_key = {}
    for s in scope:
        by_key.setdefault((s["namespace"] or "", s["name"]), []).append(s)

    conflicts = []
    for (_, n), v in by_key.items():
        if len(v) < 2:
            continue
        ranked = sorted(v, key=lambda x: LEVEL_RANK.get(x["level"], 9))
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
    desc_chars = sum(len(v[0]["description"]) + len(v[0]["name"]) + 4
                     for v in unique)
    over = desc_chars - budget
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
        "scope": "all-on-disk" if args.all else "loaded-only",
        "counted_skills": len(unique),
        "budget_chars": budget,
        "used_chars": desc_chars,
        "pct_used": round(desc_chars / budget * 100, 1) if budget else None,
        "over_by_chars": max(0, over),
        "skills_possibly_dropped": at_risk,
        "longest_descriptions": [
            {"name": v[0]["name"], "chars": len(v[0]["description"])}
            for v in longest],
        "excludes_builtin_skills": True,
        "note": "预算口径随 Claude Code 版本变化（另有『上下文窗口 1%』的说法），"
                "本值取自 SLASH_COMMAND_TOOL_CHAR_BUDGET 或默认 15000，请按实际版本核对。"
                "**本数字不含 Claude Code 内置 skill**（dataviz / code-review / claude-api 等，"
                "打包在 CLI 里、磁盘上无 SKILL.md），它们同样占预算，实际用量高于此处。",
        "workaround": "SLASH_COMMAND_TOOL_CHAR_BUDGET=30000",
    }

    # ── 触发数据 ─────────────────────────────────────────
    zombies = [s for s in loaded
               if s["usage_count"] == 0 and s["installed_days_ago"] >= zombie_age]
    too_new = [s for s in loaded
               if s["usage_count"] == 0 and s["installed_days_ago"] < zombie_age]
    trigger_report = {
        "available": bool(usage),
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
    oversized = [s for s in loaded if s["tier2_core_tokens"] > args.split_threshold]
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

    out = {
        "scanned_roots": scanned,
        "total_skills_on_disk": len(skills),
        "loaded_skills": len(loaded),
        "unique_skills": len(unique),
        "plugin_state": {
            "host_config_read": plugins_known,
            "enabled_plugins": sorted(enabled_plugins),
            "note": "未启用的插件副本在磁盘上但不进上下文，不计入预算。"
                    "host_config_read=false 时无法判断，插件一律按未加载处理。",
        },
        "description_budget": budget_report,
        "trigger_data": trigger_report,
        "structure": structure_report,
        "security": security_report,
        "tier1_total_tokens": tier1_total,
        "tier1_pct_of_200k": round(tier1_total / 200000 * 100, 2),
        "conflicts": conflicts,
        "precedence_note": "覆盖优先级 enterprise > personal > project > plugin —— "
                           "personal 会盖掉 project，与多数人的直觉相反。"
                           "插件里的 skill 按 <plugin>:<name> 命名空间隔离，同名不算冲突。",
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
        print(f"已写入 {args.json}：磁盘 {len(skills)} 个 skill，"
              f"其中已加载 {len(loaded)} 个，"
              f"Tier1 合计约 {tier1_total} tokens，"
              f"描述预算 {budget_report['pct_used']}%（{budget_report['scope']}），"
              f"触发数据 {'已获取' if usage else '未获取'}，"
              f"建议拆分 {len(structure_report['oversized'])} 个，"
              f"安全告警 {security_report['flagged_count']} 条"
              f"（其中 {security_report['all_cited_count']} 个全部命中疑似引用语境，"
              f"仍需过目）")
    else:
        print(text)

    if not skills:
        print("\n未找到任何 skill。请用 --path 指定实际安装目录。",
              file=sys.stderr)


if __name__ == "__main__":
    main()
