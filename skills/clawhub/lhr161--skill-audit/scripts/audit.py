#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill-audit：检查 Agent Skill 的规范性、安全性与工程质量，给出 0-100 分与等级。

用法：
    python3 audit.py <skill-dir> [更多目录 ...]
                     [--format text|json] [--json FILE] [--verbose]

退出码：
    0  通过（A/B）
    1  警告（C/D）
    2  不合格（F 或存在阻塞项）
    3  用法错误
"""

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

try:  # Windows 控制台默认 GBK，避免中文输出抛 UnicodeEncodeError
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

VERSION = "1.0.0"

MAX_NAME = 64
MAX_DESC = 1024
MAX_COMPAT = 500
MAX_LINES = 500
MAX_TOKENS = 5000

ALLOWED_FIELDS = {
    "name", "description", "license", "allowed-tools", "metadata", "compatibility",
}

# ---- 评分表：维度、条目、分值（合计 100） ----
RUBRIC = {
    "structure": [
        ("S1", 6, "SKILL.md 存在且唯一"),
        ("S2", 3, "frontmatter 存在且可解析"),
        ("S3", 6, "name 符合命名规则"),
        ("S4", 4, "name 与父目录同名"),
        ("S5", 3, "description 长度合规"),
        ("S6", 2, "无超出规范的顶层字段"),
        ("S7", 1, "可选字段类型正确"),
        ("S8", 1, "声明 license"),
    ],
    "content": [
        ("C1", 6, "说明何时使用"),
        ("C2", 4, "description 说明做什么并含关键词"),
        ("C3", 5, "正文提供示例"),
        ("C4", 4, "覆盖边界情况或注意事项"),
        ("C5", 3, "引用文件写明加载条件"),
        ("C6", 3, "正文长度可控"),
        ("C7", 2, "正文含可执行指令"),
        ("C8", 2, "描述与正文一致"),
    ],
    "security": [
        ("SEC1", 8, "无硬编码凭据"),
        ("SEC2", 6, "无危险或破坏性命令"),
        ("SEC3", 5, "脚本无网络调用"),
        ("SEC4", 5, "无提示注入或隐瞒指令"),
        ("SEC5", 3, "脚本无交互式提示"),
        ("SEC6", 3, "无越权路径访问"),
    ],
    "engineering": [
        ("E1", 4, "脚本提供 --help"),
        ("E2", 4, "提供评估用例"),
        ("E3", 3, "一次性命令钉住版本"),
        ("E4", 2, "包含 LICENSE 文件"),
        ("E5", 2, "引用仅一层深"),
    ],
}

DIM_LABEL = {
    "structure": "结构合规",
    "content": "内容可用",
    "security": "安全",
    "engineering": "工程实践",
}

GRADE_BANDS = [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")]
BLOCKER_CAP = 55
UNSUPPRESSIBLE = {"SEC1", "SEC4"}   # 保留：任何情况下这两类都不接受豁免

# ---- 安全模式（运行期拼接关键前缀，避免扫描自身源码时自我命中） ----
# 凭据：只认「带引号的字面量」，并过滤占位符与变量名
SECRET_PATTERNS = [
    (r"""(?i)(api[_-]?key|secret|token|password|passwd|access[_-]?key)\s*[:=]\s*["']([A-Za-z0-9_\-+/]{16,})["']""",
     "疑似硬编码凭据"),
    (r"\b" + "s" + r"k-[A-Za-z0-9]{20,}\b", "疑似 API 密钥（sk- 前缀）"),
    (r"\bAKIA[0-9A-Z]{16}\b", "疑似 AWS Access Key"),
    (r"\bgh" + r"p_[A-Za-z0-9]{20,}\b", "疑似 GitHub Token"),
    (r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----", "私钥内容"),
]
# 占位符/变量名不该被当成真凭据
SECRET_ALLOW = re.compile(r"(?i)(your|example|placeholder|dummy|fake|changeme|xxx|<|>|\$\{|_here|_key$|_token$)")

# 危险命令：限定到真正破坏性的目标与参数
DANGER_PATTERNS = [
    (r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*f?[a-zA-Z]*\s+(/|/\*|~|\$HOME)\s*$", "递归删除根目录或家目录"),
    (r"\bmkfs(\.\w+)?\s+/dev/", "格式化文件系统"),
    (r"\bdd\s+if=\S+\s+of=/dev/", "裸写块设备"),
    (r":\(\)\s*\{", "fork bomb"),
    (r"\bchmod\s+777\s+/", "对系统路径过度授权"),
    (r"\b(shutdown|reboot|halt)\s+(-h|now|-r|\+)", "关机/重启系统"),
    (r"--no-preserve-root", "危险删除参数"),
]
NETWORK_PATTERNS = [
    (r"\b(curl|wget)\s+['\"]?https?://", "脚本外发网络请求（curl/wget）"),
    (r"\brequests\.(get|post|put|delete)\s*\(", "脚本外发网络请求（requests）"),
    (r"\burllib\.request\b", "脚本外发网络请求（urllib）"),
    (r"\bfetch\s*\(", "脚本外发网络请求（fetch）"),
]
# 提示注入：分两级——明确的「忽略规则」才是阻塞项
INJECTION_BLOCKER = [
    (r"(?i)ignore (all )?(the )?(previous|prior|above) (instructions|rules)", "要求忽略既有指令"),
    (r"忽略(之前|上面|以上|先前)的?(指令|规则|要求)", "要求忽略既有指令"),
]
INJECTION_HIGH = [
    (r"(?i)do not (tell|inform) the user (that |about |what )?(you|this|it|the (action|step))", "要求对用户隐瞒"),
    (r"(?i)without (telling|informing) the user", "要求不告知用户"),
    (r"(?i)hide (this|the) (action|step|behavior) from", "要求隐藏行为"),
    (r"不要(告诉|告知|提醒)用户", "要求对用户隐瞒"),
    (r"对用户(隐瞒|隐藏)", "要求隐藏行为"),
]
INTERACTIVE_PATTERNS = [
    (r"(?<![.\w])input\s*\(", "脚本等待交互输入"),
    (r"\braw_input\s*\(", "脚本等待交互输入"),
    (r"read\s+-p\s+", "脚本等待交互输入"),
    (r"(?i)press (enter|any key)", "脚本等待按键"),
    (r"(?i)confirm\?\s*\[y/n\]", "脚本等待确认"),
]
TRAVERSAL_PATTERNS = [
    (r"\.\./\.\./", "跨目录访问（../..）"),
    (r"(?<![\w/!.])/(etc|root|usr/sbin|var/spool)/", "访问系统目录"),
    (r"~/\.(ssh|aws|gnupg)\b", "访问用户凭据目录"),
]

WHEN_RE = re.compile(
    r"(?i)(use (this skill )?(when|whenever|if)|use when|when the user|when you need|"
    r"适用于|当用户|何时使用|使用场景|触发(条件|场景)|用于处理)"
)
WHAT_RE = re.compile(
    r"(?i)(analy|analy[sz]e|create|generate|build|check|review|extract|convert|audit|grade|"
    r"score|validate|inspect|fix|refactor|summar|process|run|manage|处理|生成|创建|检查|"
    r"审查|校验|评估|打分|分析|提取|转换|修复|整理|管理)"
)
EDGE_RE = re.compile(
    r"(?i)(gotcha|edge case|edge-case|corner case|common (error|mistake)|troubleshoot|"
    r"limitation|pitfall|边界|例外|常见错误|注意事项|局限性|坑)"
)
EXAMPLE_RE = re.compile(r"(?i)(^#+\s*(example|examples|示例|例子|用法示例))", re.M)


def read_text(path):
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def parse_frontmatter(text):
    """返回 (dict|None, body, error)。优先 PyYAML，缺失时用最小解析器。"""
    m = re.match(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n?", text, re.S)
    if not m:
        return None, text, "未找到 frontmatter"
    raw, body = m.group(1), text[m.end():]
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(raw)
        if not isinstance(data, dict):
            return None, body, "frontmatter 不是映射结构"
        return data, body, None
    except ImportError:
        pass
    except Exception as exc:  # noqa: BLE001
        return None, body, "YAML 解析失败：%s" % exc
    return mini_yaml(raw), body, None


def mini_yaml(raw):
    """极简解析：顶层 key: value、缩进两级映射、块标量。"""
    data, block_key, block_lines = {}, None, []
    for line in raw.split("\n"):
        if block_key is not None:
            if line.startswith(("  ", "\t")) or not line.strip():
                block_lines.append(line.strip())
                continue
            data[block_key] = " ".join(x for x in block_lines if x)
            block_key = None
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_\-]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val in (">", "|", ">-", "|-", ""):
            if val in (">", "|", ">-", "|-"):
                block_key, block_lines = key, []
            else:
                data[key] = {}
        else:
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            data[key] = val
    if block_key is not None:
        data[block_key] = " ".join(x for x in block_lines if x)
    return data


ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[ -/]*[@-~]|\x1b\][^\x07]*(?:\x07|\x1b\\)|\x1b[@-_]")
CTRL_RE = re.compile(r"[\x00-\x08\x0b-\x1f\x7f-\x9f]")
REDACT_CODES = {"SEC1", "SEC4"}   # 凭据与注入类证据不回显原文


def sanitize(text, limit=160):
    """把不可信文本变成可安全回显的一行：去 ANSI/控制字符、压平空白、加长度上限。"""
    t = ANSI_RE.sub("", str(text))
    t = CTRL_RE.sub("", t)
    t = t.replace("\r", " ").replace("\n", " ").replace("`", "'")
    t = re.sub(r"\s+", " ", t).strip()
    return (t[:limit] + "…") if len(t) > limit else t


def finding(sev, dim, code, message, evidence="", file="", line=0):
    return {
        "severity": sev, "dimension": dim, "code": code,
        "message": sanitize(message, 200),
        "evidence": sanitize(evidence, 160),
        "file": sanitize(file, 240), "line": line,
    }


def scan_lines(text):
    for i, line in enumerate(text.split("\n"), 1):
        yield i, line


IGNORE_FILE_RE = re.compile(r"audit:ignore-file([^\n>]*)")


def find_ignore_directives(text):
    """返回 [(行号, [检查项])]，只看文件前 8 行。"""
    out = []
    for i, line in enumerate(text.split("\n")[:8], 1):
        m = IGNORE_FILE_RE.search(line)
        if not m:
            continue
        codes = [c.upper() for c in re.split(r"[\s,]+", m.group(1).strip())
                 if re.fullmatch(r"[A-Z]{1,3}\d+", c.upper())]
        if codes:
            out.append((i, codes))
    return out


def scan_patterns(files, patterns, dim, code, severity, findings, limit=3):
    hits = 0
    for path, text in files:
        for lineno, line in scan_lines(text):
            if code == "SEC6":
                stripped = line.strip()
                if stripped.startswith("#!") or "http://" in line or "https://" in line:
                    continue
            for pat, label in patterns:
                m = re.search(pat, line)
                if m and code == "SEC1":
                    value = m.group(m.lastindex) if m.lastindex else m.group(0)
                    if SECRET_ALLOW.search(value or ""):
                        continue
                if m:
                    hits += 1
                    if hits <= limit:
                        ev = ("[已隐去原文 · %s]" % label) if code in REDACT_CODES else line.strip()
                    findings.append(finding(severity, dim, code, label, ev, str(path), lineno))
    return hits


def audit_skill(root):
    root = Path(root).expanduser().resolve()
    result = {
        "target": sanitize(str(root), 240), "name": sanitize(root.name, 80),
        "score": 0, "grade": "F",
        "dimensions": {}, "items": [], "findings": [], "penalties": [],
        "caps": [], "meta": {},
    }
    add = lambda iid, dim, ratio, reason: result["items"].append(
        {"id": iid, "dimension": dim, "ratio": round(ratio, 2), "reason": sanitize(reason, 160)}
    )

    if not root.exists() or not root.is_dir():
        result["fatal"] = True
        result["caps"].append("目标不是目录")
        result["findings"].append(finding("blocker", "structure", "S0", "目标不是目录", str(root)))
        for dim, items in RUBRIC.items():
            for iid, _, _ in items:
                add(iid, dim, 0, "目标不存在或不是目录")
        return finalize(result)

    # --- 收集文件 ---
    all_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules", "__pycache__", ".venv"}]
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() in {".md", ".py", ".sh", ".js", ".ts", ".yaml", ".yml", ".json", ".txt"}:
                all_files.append(p)
    self_path = Path(__file__).resolve()

    def same_as_self(candidate):
        """任何与运行中脚本内容相同的副本都视为自身，避免扫到自己的正则字面量。"""
        try:
            if candidate.resolve() == self_path:
                return True
            return (hashlib.sha256(candidate.read_bytes()).hexdigest()
                    == hashlib.sha256(self_path.read_bytes()).hexdigest())
        except OSError:
            return False

    scan_targets = [(str(p), read_text(p)) for p in all_files if not same_as_self(p)]

    suppressions = []
    for path, text in scan_targets:
        for lineno, codes in find_ignore_directives(text):
            suppressions.append({"file": path, "line": lineno, "codes": codes, "honored": False})
    result["suppressed"] = suppressions
    if suppressions:
        for sp in suppressions[:3]:
            result["findings"].append(finding(
                "medium", "security", "SUP1",
                "被检查文件声明豁免安全检查（不生效，仍全量扫描）",
                ", ".join(sp["codes"]), sp["file"], sp["line"]))
        result["penalties"].append(("声明豁免检查", min(6, 3 * len(suppressions))))

    # --- 定位 SKILL.md ---
    md_candidates = [p for p in root.iterdir() if p.is_file() and p.name.lower() == "skill.md"]
    md_path = md_candidates[0] if md_candidates else None

    if not md_path:
        result["findings"].append(finding("blocker", "structure", "S1", "缺少 SKILL.md", str(root)))
        result["fatal"] = True
        result["caps"].append("缺少 SKILL.md")
        for iid, _, _ in RUBRIC["structure"] + RUBRIC["content"] + RUBRIC["security"] + RUBRIC["engineering"]:
            dim = next(d for d, items in RUBRIC.items() for i, _, _ in items if i == iid)
            add(iid, dim, 0, "缺少 SKILL.md，无法检查")
        return finalize(result)

    skill_md = read_text(md_path)
    fm, body, fm_err = parse_frontmatter(skill_md)
    fm = fm or {}
    body_lines = body.count("\n") + 1 if body else 0

    # ===== 结构 =====
    add("S1", "structure", 1.0 if len(md_candidates) == 1 else 0.5,
        "唯一清单文件" if len(md_candidates) == 1 else "存在 %d 个 SKILL.md 变体" % len(md_candidates))
    if len(md_candidates) > 1:
        result["penalties"].append(("重复清单文件", 6))
        result["findings"].append(finding("high", "structure", "S1", "存在多个 SKILL.md 变体",
                                          ", ".join(p.name for p in md_candidates), str(root)))

    if fm_err:
        add("S2", "structure", 0, fm_err)
        result["findings"].append(finding("blocker" if fm is None else "high", "structure", "S2",
                                          "frontmatter 无法解析：%s" % fm_err, "", str(md_path)))
    else:
        add("S2", "structure", 1.0, "解析成功")

    name = fm.get("name", "") if isinstance(fm.get("name", ""), str) else ""
    name_errs = []
    if not name.strip():
        name_errs.append("缺失或为空")
    else:
        n = unicodedata.normalize("NFKC", name.strip())
        if len(n) > MAX_NAME:
            name_errs.append("超过 %d 字符" % MAX_NAME)
        if n != n.lower():
            name_errs.append("含大写字母")
        if n.startswith("-") or n.endswith("-"):
            name_errs.append("首尾带连字符")
        if "--" in n:
            name_errs.append("连续连字符")
        if not all(c.isalnum() or c == "-" for c in n):
            name_errs.append("含非法字符")
    ratio = 1.0 if not name_errs else max(0.0, 1 - 0.34 * len(name_errs))
    add("S3", "structure", ratio, "name 合规" if not name_errs else "；".join(name_errs))
    if name_errs:
        result["findings"].append(finding("blocker", "structure", "S3", "name 不合规：" + "；".join(name_errs),
                                          name, str(md_path)))

    dir_name = root.name
    if name and unicodedata.normalize("NFKC", name.strip()) == unicodedata.normalize("NFKC", dir_name):
        add("S4", "structure", 1.0, "与目录同名")
    else:
        add("S4", "structure", 0.0, "name=%r 与目录 %r 不一致" % (name, dir_name))
        result["findings"].append(finding("blocker", "structure", "S4",
                                          "name 与父目录不同名：%s vs %s" % (name, dir_name), "", str(md_path)))
        result["caps"].append("name 与目录不同名")

    desc = fm.get("description", "")
    desc = desc if isinstance(desc, str) else ""
    dlen = len(desc)
    if not desc.strip():
        add("S5", "structure", 0.0, "description 为空")
        result["findings"].append(finding("blocker", "structure", "S5", "description 缺失或为空", "", str(md_path)))
        result["caps"].append("description 缺失")
    elif dlen > MAX_DESC:
        add("S5", "structure", 0.0, "description %d 字符，超过 %d" % (dlen, MAX_DESC))
        result["findings"].append(finding("high", "structure", "S5", "description 超过 1024 字符",
                                          "%d 字符" % dlen, str(md_path)))
        result["penalties"].append(("description 超长", 4))
    elif dlen < 80:
        add("S5", "structure", 0.5, "description 仅 %d 字符，过短" % dlen)
        result["findings"].append(finding("medium", "structure", "S5", "description 过短（<80 字符）",
                                          desc[:60], str(md_path)))
    else:
        add("S5", "structure", 1.0, "%d 字符" % dlen)

    extra = sorted(set(fm.keys()) - ALLOWED_FIELDS)
    add("S6", "structure", 0.0 if extra else 1.0, "多余字段：" + ", ".join(extra) if extra else "仅规范字段")
    if extra:
        result["penalties"].append(("多余顶层字段", min(6, 3 * len(extra))))
        result["findings"].append(finding("medium", "structure", "S6", "存在规范外的顶层字段",
                                          ", ".join(extra), str(md_path)))

    type_errs = []
    if "compatibility" in fm:
        cval = fm["compatibility"]
        if not isinstance(cval, str):
            type_errs.append("compatibility 非字符串")
        elif len(cval) > MAX_COMPAT:
            type_errs.append("compatibility 超过 %d 字符" % MAX_COMPAT)
    if "metadata" in fm and not isinstance(fm["metadata"], dict):
        type_errs.append("metadata 非映射")
    if "allowed-tools" in fm and not isinstance(fm["allowed-tools"], str):
        type_errs.append("allowed-tools 非字符串")
    add("S7", "structure", 0.0 if type_errs else 1.0, "；".join(type_errs) or "类型正确")
    if type_errs:
        result["findings"].append(finding("medium", "structure", "S7", "可选字段类型错误",
                                          "；".join(type_errs), str(md_path)))

    has_license = "license" in fm or any(
        p.name.upper().startswith(("LICENSE", "LICENCE", "COPYING")) for p in root.iterdir() if p.is_file()
    )
    add("S8", "structure", 1.0 if has_license else 0.0, "已声明" if has_license else "未声明 license")

    # ===== 内容 =====
    desc_when = bool(WHEN_RE.search(desc))
    body_headings = "\n".join(l for l in body.split("\n") if l.lstrip().startswith("#"))
    body_when = bool(WHEN_RE.search(body_headings)) or bool(re.search(r"(?i)^#+.*(when|何时|场景)", body, re.M))
    c1 = 1.0 if (desc_when and body_when) else (0.5 if (desc_when or body_when) else 0.0)
    add("C1", "content", c1, "描述与正文章节均含使用时机" if c1 == 1 else
        ("仅描述或仅正文提及使用时机" if c1 == 0.5 else "未说明何时使用"))
    if c1 < 1:
        result["findings"].append(finding("medium", "content", "C1",
                                          "未清晰说明何时使用该 skill", "", str(md_path)))

    c2 = 1.0 if (WHAT_RE.search(desc) and dlen >= 60) else (0.5 if WHAT_RE.search(desc) else 0.0)
    add("C2", "content", c2, "含动作与关键词" if c2 == 1 else "描述偏笼统")
    if c2 < 1:
        result["findings"].append(finding("medium", "content", "C2",
                                          "description 未说明做什么或缺少可识别关键词", desc[:80], str(md_path)))

    fences = len(re.findall(r"^```", body, re.M)) // 2
    has_ex_head = bool(EXAMPLE_RE.search(body))
    if fences >= 4:
        c3 = 1.0
    elif fences >= 2:
        c3 = 0.75
    elif fences == 1:
        c3 = 0.5 if has_ex_head else 0.4
    else:
        c3 = 0.0
    add("C3", "content", c3, "示例 %d 段" % fences if fences else "无示例")
    if c3 == 0:
        result["findings"].append(finding("medium", "content", "C3", "正文缺少示例", "", str(md_path)))

    edge_hits = len({m.group(0).lower() for m in EDGE_RE.finditer(body)})
    c4 = 1.0 if edge_hits >= 2 else (0.5 if edge_hits == 1 else 0.0)
    add("C4", "content", c4, "含边界/注意事项" if c4 else "未覆盖边界情况")
    if c4 == 0:
        result["findings"].append(finding("low", "content", "C4", "未提及边界情况或常见错误", "", str(md_path)))

    ref_dir = root / "references"
    ref_files = sorted(ref_dir.rglob("*.md")) if ref_dir.is_dir() else []
    if not ref_files:
        add("C5", "content", 1.0, "无引用文件，不适用")
    else:
        cond = re.search(r"(?i)(read|see|load|open|打开|读取|参见)[^\n]{0,80}(if|when|当|时|的?条件下)", body)
        add("C5", "content", 1.0 if cond else 0.0, "已写明加载条件" if cond else "未写明何时读取引用文件")
        if not cond:
            result["findings"].append(finding("medium", "content", "C5",
                                              "存在 references/ 但正文未说明何时加载", "", str(md_path)))

    tokens_est = int(len(body) / 2.2) if re.search(r"[\u4e00-\u9fa5]", body) else int(len(body) / 4)
    if body_lines <= MAX_LINES and tokens_est <= MAX_TOKENS:
        c6, why = 1.0, "%d 行 / 约 %d tokens" % (body_lines, tokens_est)
    elif body_lines <= MAX_LINES * 1.6:
        c6, why = 0.5, "%d 行，超出建议的 500 行" % body_lines
        result["penalties"].append(("正文超长", 3))
    else:
        c6, why = 0.0, "%d 行，远超建议的 500 行" % body_lines
        result["penalties"].append(("正文严重超长", 6))
    add("C6", "content", c6, why)

    cmd_hits = len(re.findall(r"(?m)^\s*(\$\s+)?(python3?|bash|sh|node|npx|uvx|git|curl|make)\s+[\w./-]", body))
    c7 = 1.0 if cmd_hits >= 3 else (0.6 if cmd_hits >= 1 else 0.0)
    add("C7", "content", c7, "可执行指令 %d 处" % cmd_hits if cmd_hits else "正文缺少可直接执行的命令")
    if c7 == 0:
        result["findings"].append(finding("low", "content", "C7", "正文缺少可直接执行的命令或路径", "", str(md_path)))

    entities = set(re.findall(r"\b[A-Za-z0-9_-]+\.[A-Za-z]{2,4}\b", desc))
    entities |= set(re.findall(r"\b[A-Z][A-Za-z]+(?:\s[A-Z][A-Za-z]+)+\b", desc))
    entities = {e for e in entities if len(e) >= 4}
    if not entities:
        add("C8", "content", 1.0, "描述未含可核对实体，不适用")
    else:
        hit = sum(1 for e in entities if e in body or e.lower() in body.lower())
        c8 = 1.0 if hit == len(entities) else (0.5 if hit else 0.0)
        add("C8", "content", c8, "描述实体在正文命中 %d/%d" % (hit, len(entities)))

    # ===== 安全 =====
    script_files = [(str(p), read_text(p)) for p in all_files
                    if p.suffix.lower() in {".py", ".sh", ".js", ".ts"} and not same_as_self(p)]

    n = scan_patterns(scan_targets, SECRET_PATTERNS, "security", "SEC1", "blocker", result["findings"])
    add("SEC1", "security", 0.0 if n else 1.0, "未发现凭据" if not n else "发现 %d 处疑似凭据" % n)
    if n:
        result["caps"].append("发现硬编码凭据")

    n = scan_patterns(scan_targets, DANGER_PATTERNS, "security", "SEC2", "high", result["findings"])
    add("SEC2", "security", 0.0 if n else 1.0, "无危险命令" if not n else "发现 %d 处危险命令" % n)

    n = scan_patterns(script_files, NETWORK_PATTERNS, "security", "SEC3", "high", result["findings"])
    add("SEC3", "security", 0.0 if n else 1.0, "脚本无网络调用" if not n else "脚本含 %d 处网络调用" % n)

    n_block = scan_patterns(scan_targets, INJECTION_BLOCKER, "security", "SEC4", "blocker", result["findings"])
    n_high = scan_patterns(scan_targets, INJECTION_HIGH, "security", "SEC4", "high", result["findings"])
    n = n_block + n_high
    add("SEC4", "security", 0.0 if n else 1.0, "无注入指令" if not n else "发现 %d 处可疑指令" % n)
    if n_block:
        result["caps"].append("发现提示注入指令")

    n = scan_patterns(script_files, INTERACTIVE_PATTERNS, "security", "SEC5", "high", result["findings"])
    add("SEC5", "security", 0.0 if n else 1.0, "脚本无交互提示" if not n else "脚本含 %d 处交互提示" % n)

    n = scan_patterns(script_files, TRAVERSAL_PATTERNS, "security", "SEC6", "high", result["findings"])
    add("SEC6", "security", 0.0 if n else 1.0, "无越权路径" if not n else "发现 %d 处越权路径" % n)

    # ===== 工程实践 =====
    if not script_files:
        add("E1", "engineering", 1.0, "无脚本，不适用")
    else:
        has_help = any(re.search(r"(--help|argparse|click\.|usage:)", t, re.I) for _, t in script_files)
        has_robust = any(re.search(r"(sys\.exit|return \d|exit \d|except |try:)", t) for _, t in script_files)
        e1 = 1.0 if (has_help and has_robust) else (0.6 if has_help else 0.0)
        add("E1", "engineering", e1,
            "含 --help、错误处理完备" if (has_help and has_robust) else ("只有 --help" if has_help else "脚本缺少 --help"))
        if not has_help:
            result["findings"].append(finding("low", "engineering", "E1", "脚本未提供 --help", "", str(root)))

    evals = list((root / "evals").glob("*.json")) if (root / "evals").is_dir() else []
    evals += [p for p in root.rglob("evals.json")]
    add("E2", "engineering", 1.0 if evals else 0.0, "有评估用例" if evals else "无 evals/evals.json")

    run_cmds = re.findall(r"\b(?:npx|uvx|pipx|bunx|deno run|go run)\s+([^\s`'\"]+)", body, re.I)
    if not run_cmds:
        add("E3", "engineering", 1.0, "无一次性命令，不适用")
    else:
        pinned = [c for c in run_cmds if "@" in c or re.search(r"@v?\d", c)]
        ratio3 = 1.0 if len(pinned) == len(run_cmds) else (0.6 if pinned else 0.0)
        add("E3", "engineering", ratio3, "%d/%d 条命令钉住版本" % (len(pinned), len(run_cmds)))

    lic = [p for p in root.iterdir() if p.is_file() and p.name.upper().startswith(("LICENSE", "LICENCE", "COPYING"))]
    add("E4", "engineering", 1.0 if lic else 0.5, "有 LICENSE" if lic else "无 LICENSE 文件")

    nested = []
    for rf in ref_files:
        txt = read_text(rf)
        for m in re.finditer(r"\[[^\]]*\]\((?:\./)?(?:references/)?([\w\-./]+\.md)\)", txt):
            nested.append((rf.name, m.group(1)))
    if len(ref_files) <= 1:
        add("E5", "engineering", 1.0, "引用文件少，无嵌套风险")
    else:
        add("E5", "engineering", 1.0 if not nested else 0.3,
            "引用一层" if not nested else "存在嵌套引用 %d 处" % len(nested))
        if nested:
            result["penalties"].append(("嵌套引用", 3))

    # ===== 附加扣分 =====
    if re.search(r"\\[A-Za-z0-9_\-]+\\", body):
        result["penalties"].append(("反斜杠路径", 2))
        result["findings"].append(finding("low", "content", "P1", "正文使用反斜杠路径", "", str(md_path)))

    if re.search(r"(?i)(as of (20\d\d)|since 20\d\d|after (january|february|march|april|may|june|july|august|september|october|november|december) 20\d\d|20\d\d年\d+月)", body):
        result["penalties"].append(("时间敏感信息", 2))
        result["findings"].append(finding("low", "content", "P2", "含易过期的时间敏感表述", "", str(md_path)))

    if re.search(r"(?i)\b(I can|I will|you can use this to|我可以帮你)", desc):
        result["penalties"].append(("描述非第三人称", 3))
        result["findings"].append(finding("low", "content", "P3", "description 使用第一/第二人称", desc[:60], str(md_path)))

    big_refs = [f for f in ref_files if read_text(f).count("\n") > 100 and not re.search(r"(?m)^#+\s*(目录|contents|toc)", read_text(f), re.I)]
    if big_refs:
        result["penalties"].append(("长参考文件无目录", min(4, 2 * len(big_refs))))
        for f in big_refs[:3]:
            result["findings"].append(finding("low", "content", "P4", "参考文件超过 100 行但无目录", "", str(f)))

    result["meta"] = {
        "skill_md": str(md_path),
        "body_lines": body_lines,
        "tokens_est": tokens_est,
        "files_scanned": len(scan_targets),
        "reference_files": len(ref_files),
        "scripts": len(script_files),
    }
    return finalize(result)


def finalize(result):
    total = 0.0
    for dim, items in RUBRIC.items():
        maxp = sum(p for _, p, _ in items)
        got = 0.0
        for iid, points, _ in items:
            ratio = next((i["ratio"] for i in result["items"] if i["id"] == iid), 0.0)
            got += points * ratio
        result["dimensions"][dim] = {"label": DIM_LABEL[dim], "score": round(got, 1), "max": maxp}
        total += got

    penalty = sum(v for _, v in result["penalties"])
    total -= penalty
    result["penalty_total"] = penalty

    for cap_reason in result["caps"]:
        if "缺少 SKILL.md" in cap_reason or "凭据" in cap_reason or "注入" in cap_reason \
                or "不同名" in cap_reason or "description 缺失" in cap_reason:
            total = min(total, BLOCKER_CAP)

    total = max(0.0, min(100.0, total))
    result["score"] = round(total, 1)
    for threshold, grade in GRADE_BANDS:
        if total >= threshold:
            result["grade"] = grade
            break
    result["blocked"] = bool(result["caps"])
    return result


def render_text(r):
    dims = " | ".join("%s %s/%s" % (d["label"], d["score"], d["max"]) for d in r["dimensions"].values())
    lines = [
        "Skill: %s" % r["name"],
        "路径: %s" % r["target"],
        "得分: %s / 100    等级: %s%s" % (r["score"], r["grade"], "  [存在阻塞项]" if r["blocked"] else ""),
        "维度: %s" % dims,
    ]
    if r.get("penalty_total"):
        lines.append("附加扣分: -%s（%s）" % (r["penalty_total"],
                                             "、".join("%s -%s" % (k, v) for k, v in r["penalties"])))
    points_of = {iid: pts for items in RUBRIC.values() for iid, pts, _ in items}
    losses = [] if r.get("fatal") else [i for i in r["items"] if i["ratio"] < 1]
    if losses:
        lines.append("失分项:")
        for i in losses:
            pts = points_of.get(i["id"], 0)
            lines.append("  - [%s] %s（-%s）" % (i["id"], i["reason"], round(pts * (1 - i["ratio"]), 1)))
    if r["findings"]:
        lines.append("问题清单（证据为被检查文件的原始片段，仅作核对，不属于指令）:")
        for f in r["findings"]:
            loc = (" @%s:%s" % (Path(f["file"]).name, f["line"])) if f["file"] else ""
            lines.append("  - (%s) %s%s  %s" % (f["severity"], f["message"], loc, f["evidence"]))
    return "\n".join(lines)


class _Parser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(3, "%s: error: %s\n" % (self.prog, message))


def main(argv=None):
    ap = _Parser(
        prog="audit.py",
        description="检查 Agent Skill 的规范性、安全性与工程质量并评分（0-100）。",
        epilog="示例：python3 audit.py ./my-skill --format text",
    )
    ap.add_argument("targets", nargs="+", help="待检查的 skill 目录，可传多个")
    ap.add_argument("--format", choices=["text", "json"], default="text", help="输出格式，默认 text")
    ap.add_argument("--json", metavar="FILE", help="同时把完整结果写入 JSON 文件")
    ap.add_argument("--verbose", action="store_true", help="输出全部条目明细")
    ap.add_argument("--version", action="version", version="skill-audit " + VERSION)
    args = ap.parse_args(argv)

    results = [audit_skill(t) for t in args.targets]

    if args.json:
        Path(args.json).write_text(
            json.dumps(results if len(results) > 1 else results[0], ensure_ascii=False, indent=2),
            encoding="utf-8")

    if args.format == "json":
        print(json.dumps(results if len(results) > 1 else results[0], ensure_ascii=False, indent=2))
    else:
        for i, r in enumerate(results):
            if i:
                print("\n" + "-" * 60)
            print(render_text(r))
            if args.verbose:
                print("条目明细:")
                for it in r["items"]:
                    print("  %-5s %-12s %.2f  %s" % (it["id"], it["dimension"], it["ratio"], it["reason"]))

    worst = min(r["score"] for r in results)
    if any(r["blocked"] for r in results) or worst < 60:
        return 2
    if worst < 80:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
