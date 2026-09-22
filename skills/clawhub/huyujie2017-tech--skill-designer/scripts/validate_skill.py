#!/usr/bin/env python3
"""
validate_skill.py — 静态验证脚本（skill-designer 的机器强制验证）

把 test-playbook §六 的「静态验证清单」从"AI/人勾选"升级为"脚本机器判定"，
兑现 P28「硬性交给自动化，软性留给人/LLM」。设计遵循脚本四原则：
自愈性 / 结构化输出 / 幂等性 / 安全边界。

检查项（对齐 test-playbook §六 6 步 + P32 安全）：
  [硬性] 1. frontmatter YAML 有效（含 name + description）
           + **description 英文冒号守卫**：skillhub 按首个英文冒号截断 description，
             "Use when:" / "Do NOT use for:" 会让触发词后半段整段丢失（机器可判 → FAIL）
  [硬性] 2. name 与目录名一致
  [硬性] 3. 引用完整性：references/ assets/ scripts/ 链接可解析
  [硬性] 4. 长度检查：body < 5000 词（P11 三层披露）+ 建议 ≤500 行（P35 路由器契约）
  [半软] 5. description 五件事启发式检查（WHAT/WHEN/NEGATIVE/TRIGGER → WARN，不 FAIL）
  [安全] 6. 无 XML 角括号 / 无保留词 claude·anthropic / 无硬编码密钥（WARN）
  [硬性] 7. 目录内不允许 README.md（Anthropic 规范：面向用户的文档不放 skill 包）
  [半软] 8. 孤儿引用（存在但 SKILL.md 未链接）
  [半软] 9. references 渐进披露元数据（加载条件/核心主题/命中标签/不回答）
  [半软] 10. references/README.md 体量列与实际行数漂移（索引是 agent 估算
              加载成本的依据，漂移 >5 行会系统性误导路由决策）
  [半软] 11. SKILL.md 内嵌「目录自述图」与实际文件树一致性
  [半软] 12. 纪律可触线性：重复/探索类纪律（重试/回退/反复/再试…）必须带可数上限
              ——模糊规则等于没有规则（取自 westock-data D-052 / 元设计 DP-201）

**严格度判据**：机器可判项（1/2/3/4/7）→ FAIL 硬卡；需人工复核的启发式项
（5/8/9/10/11/12 + 6 的密钥类）→ WARN。**判据是「是否机器可判」，不是「是否历史产物」**
（取自 westock-data D-030「可验证性决定严格度」）。

软性项（逻辑连贯性、语义触发质量、工作流合理性）由 AI/人裁定，脚本不判。

用法：
    python scripts/validate_skill.py <skill_dir>
    python scripts/validate_skill.py <skill_dir> --json     # 结构化输出（供 AI 解析）
    python scripts/validate_skill.py <skill_dir> --fix      # 自动修复（README 迁移）+ 修复报告
    python scripts/validate_skill.py <skill_dir> --diag     # 软性项结构化诊断（症状/根因/修复三字段）
    python scripts/validate_skill.py --self                 # 校验 skill-designer 自身
    python scripts/validate_skill.py --self --full          # 追加端到端用户场景回归（25 用例，发布前跑）

退出码：0 = 全过；1 = 有硬性 FAIL；2 = 仅 WARN（可发布但建议处理）。
"""

import re
import sys
import json
from functools import lru_cache
from pathlib import Path
from typing import Optional

# ─── 常量 ───
DESC_MAX = 1024          # description ≤1024 字符（开放标准硬限制）
WORD_MAX = 5000          # body < 5000 词（P11）
LINE_MAX = 500           # 建议 ≤500 行（P35 路由器契约）
NEGATIVE_PATTERNS = [    # 负向边界信号（描述五件事之 NEGATIVE）
    r"do\s*not\s*use", r"don'?t\s+use", r"not\s+for", r"不用于", r"不使用", r"何时不使用",
]
WHEN_PATTERNS = [        # 触发信号（描述五件事之 WHEN）
    r"when\s+the\s+user", r"when\s+.*trigger", r"use\s+when", r"何时使用", r"触发", r"当用户",
]
SECRET_PATTERNS = [      # 疑似硬编码密钥
    r"(?i)(api[_-]?key|secret|token|password|passwd)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}",
]

# 安全扫描与孤儿引用检查只关心这些文本类文件
TEXT_SUFFIXES = {".md", ".py", ".sh", ".json", ".yaml", ".yml", ".env", ".txt"}
# 不需要进入的目录（避免大项目误扫）
SKIP_DIRS = {"node_modules", ".git", "__pycache__", ".venv", "venv", ".pytest_cache", "dist", "build"}

GREEN, RED, YELLOW, CYAN, RESET = "\033[92m", "\033[91m", "\033[93m", "\033[96m", "\033[0m"


def _tag(ok: bool) -> str:
    return f"{GREEN}PASS{RESET}" if ok else f"{RED}FAIL{RESET}"


def _warn() -> str:
    return f"{YELLOW}WARN{RESET}"


# ─── frontmatter 解析（依赖-free，退化安全） ───
def parse_frontmatter(content: str):
    """返回 (fm_dict, error)。不依赖 pyyaml；仅提取 name/description 等标量字段。
    description 支持 | 多行块。若装了 pyyaml 则优先用。"""
    text = content.lstrip()
    if not text.startswith("---"):
        return None, "无 frontmatter（必须以 --- 开头）"
    m = re.match(r"^---[ \t]*\r?\n(.*?)\r?\n---", text, re.DOTALL)
    if not m:
        return None, "frontmatter 格式无效（缺闭合 ---）"
    block = m.group(1)
    try:
        import yaml  # type: ignore
        fm = yaml.safe_load(block)
        if isinstance(fm, dict):
            return fm, None
        return None, "frontmatter 必须是 YAML 字典"
    except ImportError:
        pass
    except Exception as e:
        # pyyaml 装了但解析失败 → 走退化逻辑并报告
        return _parse_fm_loose(block, str(e))
    return _parse_fm_loose(block, None)


def _parse_fm_loose(block: str, yaml_err):
    fm, err = {}, None
    if yaml_err:
        err = f"YAML 解析失败（{yaml_err}）；退化用启发式提取"
    lines = block.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2).strip()
        if key == "description" and (val == "|" or val == ">" or val.startswith("|") or val.startswith(">")):
            # 收集后续缩进多行
            collected = []
            j = i + 1
            while j < len(lines) and (lines[j].startswith("  ") or lines[j].startswith("\t") or not lines[j].strip()):
                if lines[j].strip():
                    collected.append(lines[j].strip())
                j += 1
            fm[key] = "\n".join(collected)
            i = j
            continue
        fm[key] = val
        i += 1
    return fm, err


# ─── 文件内容缓存与受控目录扫描 ───
class SkillContext:
    """缓存 SKILL.md 内容与文件清单，避免重复 I/O 与大目录盲目扫描。"""

    def __init__(self, skill_dir: Path):
        self.skill_dir = skill_dir
        self.skill_md = skill_dir / "SKILL.md"
        self._content: Optional[str] = None
        self._files: Optional[list[Path]] = None

    @property
    def content(self) -> str:
        if self._content is None:
            self._content = self.skill_md.read_text(encoding="utf-8-sig", errors="replace") if self.skill_md.exists() else ""
        return self._content

    def text_files(self) -> list[Path]:
        """只返回关心的文本文件；跳过 node_modules/.git/__pycache__ 等大目录。"""
        if self._files is not None:
            return self._files
        files: list[Path] = []
        # 顺序扫描 references/ scripts/ assets/ 及根目录，减少全量 rglob
        for sub in ("references", "scripts", "assets", "."):
            d = self.skill_dir / sub
            if not d.is_dir():
                continue
            # 根目录下不再递归子目录（避免扫到 dist/ 等构建产物）
            if sub == ".":
                for f in d.iterdir():
                    if f.is_file() and f.suffix in TEXT_SUFFIXES:
                        files.append(f)
                continue
            for f in d.rglob("*"):
                if f.is_file() and f.suffix in TEXT_SUFFIXES and f.stat().st_size < 5 * 1024 * 1024:
                    files.append(f)
        self._files = files
        return files

    def read(self, f: Path) -> Optional[str]:
        """安全读取文本文件；结果不做缓存（安全扫描已够快）。"""
        try:
            return f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return None


# ─── 各检查项（统一接收 ctx） ───
def check_frontmatter(ctx: SkillContext):
    content = ctx.content
    fm, err = parse_frontmatter(content)
    if fm is None:
        return False, err or "frontmatter 无效"
    issues = []
    name = str(fm.get("name", "")).strip()
    desc = str(fm.get("description", "")).strip()
    if not name:
        issues.append("缺 name 字段")
    elif not re.match(r"^[a-z0-9-]+$", name):
        issues.append(f"name '{name}' 非 kebab-case（仅小写/数字/连字符）")
    if not desc:
        issues.append("缺 description 字段")
    elif len(desc) > DESC_MAX:
        issues.append(f"description 超长（{len(desc)} > {DESC_MAX}）")
    # 英文冒号截断守卫（机器可判 → FAIL 硬卡）：
    # skillhub 解析器按**首个英文冒号**截断 description，"Use when:" / "Do NOT use for:"
    # 会让其后半段触发词**整段丢失**（发布后实测确认）。只扫 value，"description:" 这个键不在其内。
    bad_colon = re.findall(r"[A-Za-z][A-Za-z ]*:\s", desc)
    if bad_colon:
        issues.append(
            f"description 含 {len(bad_colon)} 处英文冒号（如 {bad_colon[:3]}）——"
            "skillhub 按首个英文冒号截断，触发词后半段将整段丢失；改用中文冒号「：」"
        )
    # 安全：XML 角括号 / 保留词（P32）
    if re.search(r"<\w+", content[:600]):
        issues.append("frontmatter 含疑似 XML 标签")
    lower_name = name.lower()
    if "claude" in lower_name or "anthropic" in lower_name:
        issues.append(f"name 含保留词 claude/anthropic")
    return (not issues), ("; ".join(issues) if issues else f"name={name or '(缺)'}, description={len(desc)} 字符")


def check_name_dir(ctx: SkillContext):
    """name 与目录名一致——两种合法安装布局都接受。

    - WorkBuddy 平铺安装：目录名 == frontmatter `name`
    - SkillHub 安装：目录名 == `slug`（`@namespace/slug` 布局），此时 name 与目录名本就不同

    只认「目录名 == name」会在 SkillHub 标准安装路径下必然误报：
    用户 `skillhub install` 后跑 `--self` 直接红一项，而内容其实完全合规。
    """
    fm, _ = parse_frontmatter(ctx.content)
    if fm is None:
        return True, "frontmatter 无效（跳过）"
    name = str(fm.get("name", "")).strip()
    if not name:
        return True, "无 name 字段（跳过）"
    dir_name = ctx.skill_dir.name
    if name == dir_name:
        return True, f"name='{name}' = 目录名"
    # SkillHub 安装布局：目录取 slug，以 config.json 的 slug 为准
    slug = ""
    cfg = ctx.skill_dir / "config.json"
    if cfg.exists():
        try:
            slug = str(json.loads(cfg.read_text(encoding="utf-8-sig", errors="replace")).get("slug", "")).strip()
        except Exception:
            slug = ""
    if slug and slug == dir_name:
        return True, f"name='{name}' / 目录='{dir_name}'（SkillHub 安装布局，目录取 slug）"
    return False, f"name='{name}' vs 目录='{dir_name}'（config.json slug={slug or '(无或缺失)'} 也对不上）"


def check_references(ctx: SkillContext):
    content = ctx.content
    refs = set()
    # markdown 链接 [text](path)
    for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", content):
        p = m.group(1).split("#")[0].split("?")[0].strip()
        if p and not p.startswith("http") and not p.startswith("mailto"):
            refs.add(p)
    # wikilink [[path]]
    for m in re.finditer(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]", content):
        p = m.group(1).strip()
        if p:
            refs.add(p)
    # 裸路径 references/ assets/ scripts/ xxx
    for m in re.finditer(r"(?:references|assets|scripts)/[A-Za-z0-9_./\-一-鿿]+\.(?:md|py|json|txt|png|jpg|svg|xlsx|html)", content):
        refs.add(m.group(0))
    # 过滤掉常见非文件引用
    skip_names = {"anthropic", "claude", "example.com", "schema.md"}
    refs = {r for r in refs if Path(r).name not in skip_names}
    if not refs:
        return True, "无文件引用（简单 skill 视为 OK）"
    missing, empty = [], []
    for ref in sorted(refs):
        cand = ctx.skill_dir / ref
        if not cand.exists():
            # 尝试从 SKILL.md 所在位置解析（引用可能相对 references/ 内部）
            cand2 = (ctx.skill_md.parent / ref).resolve()
            cand = cand2 if cand2.exists() else cand
        if not cand.exists():
            missing.append(ref)
        elif cand.stat().st_size == 0:
            empty.append(ref)
    if missing or empty:
        msg = []
        if missing:
            msg.append(f"缺 {len(missing)} 个引用: {', '.join(missing[:3])}")
        if empty:
            msg.append(f"空文件: {', '.join(empty[:3])}")
        return False, "; ".join(msg)
    return True, f"{len(refs)} 个引用均可解析"


def check_length(ctx: SkillContext):
    content = ctx.content
    words = [w for w in content.split() if w.strip()]
    lines = content.count("\n") + 1
    issues = []
    if len(words) > WORD_MAX:
        issues.append(f"body {len(words)} 词 > {WORD_MAX}（P11 三层披露）")
    if lines > LINE_MAX:
        issues.append(f"body {lines} 行 > 建议 {LINE_MAX}（P35 路由器契约，可拆 references）")
    if issues:
        return False, "; ".join(issues)
    return True, f"{len(words)} 词 / {lines} 行"


def check_description_five(ctx: SkillContext):
    fm, _ = parse_frontmatter(ctx.content)
    if fm is None:
        return True, "frontmatter 无效（跳过）"
    desc = str(fm.get("description", "")).lower()
    if not desc:
        return True, "无 description（跳过）"
    warns = []
    # WHAT: 有实际功能描述
    if len(desc) < 50:
        warns.append("description 过短，可能缺 WHAT/WHEN")
    # WHEN: 触发信号
    if not any(re.search(p, desc) for p in WHEN_PATTERNS):
        warns.append("未见 WHEN 触发信号（when/触发/当用户）")
    # NEGATIVE: 负向边界
    if not any(re.search(p, desc) for p in NEGATIVE_PATTERNS):
        warns.append("未见 NEGATIVE 负向边界（do not use/不用于）")
    # TRIGGER 词：给几条具体说法（有引号/破折号/列表信号）
    if not re.search(r"(“|”|「|」|'\w+|\"\w+|- |：)", str(fm.get("description", ""))):
        warns.append("未见触发词示例（建议列 3-5 个具体说法）")
    return (not warns), ("；".join(warns) if warns else "五件事启发式检查通过（WHAT/WHEN/NEGATIVE/触发词均命中）")


def check_security(ctx: SkillContext):
    content = ctx.content
    issues = []
    if re.search(r"<\w+", content[:600]):
        issues.append("frontmatter 含 XML 标签")
    if re.search(r"(?i)\b(claude|anthropic)\b", content[:600]):
        issues.append("frontmatter 含保留词 claude/anthropic")
    # 硬编码密钥（WARN）— 只扫描受控文本文件清单，避免全目录 rglob
    for f in ctx.text_files():
        if f.name == "SKILL.md":
            txt = content
        else:
            txt = ctx.read(f)
            if txt is None:
                continue
        for pat in SECRET_PATTERNS:
            m = re.search(pat, txt)
            if m:
                issues.append(f"疑似硬编码密钥（{f.name}）: {m.group(0)[:40]}")
                break  # 每文件只报一条，防噪音
    return (not issues), ("; ".join(issues) if issues else "无 XML/保留词/疑似密钥")


def check_no_readme(ctx: SkillContext):
    readme = ctx.skill_dir / "README.md"
    if readme.exists():
        return False, "README.md 不应放在 skill 包内（Anthropic 规范：改放 references/ 或删除）"
    return True, "无 README.md（合规）"


def check_orphan_refs(ctx: SkillContext):
    """孤儿引用检测：references/ scripts/ assets/ 里的文件，SKILL.md 正文未提及（文件名或 stem 未出现）。半软项。"""
    content = ctx.content
    orphans = []
    for f in ctx.text_files():
        rel = str(f.relative_to(ctx.skill_dir))
        # 只检查子目录中的文件（根目录文件不算"被引用"）
        # 注意：Windows 下 relative_to 产出反斜杠，必须先归一再切分，
        # 否则 parts 恒为 1 项 → 整个检查静默空转（本地假绿、Linux 评审侧 FAIL）。
        parts = rel.replace("\\", "/").split("/")
        if len(parts) < 2 or parts[0] not in ("references", "scripts", "assets"):
            continue
        if f.stem in content or f.name in content:
            continue
        # 同族豁免：分片/分册（design-blocks-b01.md、designer-guide-A.md）由其
        # 父索引（design-blocks-library / designer-guide）代表可达性。
        # 要求 SKILL.md 逐一提及 10 个分片，既违反渐进披露，也破坏「索引是唯一
        # 入口」的单一事实源（DP-204）。父索引被提及即视为整族可达。
        family = re.sub(r"[-_](?:b\d{1,2}|[A-Z])$", "", f.stem)
        if family != f.stem and family and family in content:
            continue
        orphans.append(rel)
    if orphans:
        return False, f"孤儿引用（存在但 SKILL.md 未链接）: {', '.join(orphans[:6])}"
    return True, "无孤儿引用"


# references 渐进披露元数据的四键（与 references/README.md 口径一致）
REF_FM_KEYS = ("加载条件", "核心主题", "命中标签", "不回答")


def check_ref_frontmatter(ctx: SkillContext):
    """references 是否都带渐进披露元数据。半软项：不达标 WARN，不 FAIL。

    为什么要有这一项：本 skill 全篇教别人做 progressive disclosure 与索引机制，
    若自己的 references 没写「加载条件 / 命中标签」，索引就无从路由——
    这是元 skill 最容易「说一套做一套」的地方，必须用机器兜住而不是靠自觉。
    """
    ref_dir = ctx.skill_dir / "references"
    if not ref_dir.is_dir():
        return True, "无 references/ 目录（跳过）"
    mds = sorted(ref_dir.glob("*.md"))
    if not mds:
        return True, "references/ 为空（跳过）"

    lack = []
    for f in mds:
        text = ctx.read(f) or ""
        if not text.startswith("---\n"):
            lack.append(f.name)
            continue
        end = text.find("\n---\n", 4)
        block = text[4:end] if end > 0 else ""
        if not all(k in block for k in REF_FM_KEYS):
            lack.append(f.name)

    if lack:
        tail = "…" if len(lack) > 3 else ""
        return False, (f"{len(lack)}/{len(mds)} 份缺元数据（{', '.join(lack[:3])}{tail}）"
                       f"——索引无法按「加载条件/命中标签」路由")
    return True, f"{len(mds)} 份 references 均有元数据（{'/'.join(REF_FM_KEYS)}）"


def check_index_drift(ctx: SkillContext):
    """references/README.md 体量列 vs 实际行数。半软项：漂移 >5 行 WARN。

    为什么要有这一项：体量列是 agent 估算「加载这个文件要花多少 token」的唯一依据，
    漂移会系统性误导路由决策（本项目曾 14/17 份漂移、最重 3.4×）。
    与第 9 项同属元 skill「说一套做一套」的机器兜底：第 9 项管索引元数据，本项管索引数据。
    """
    ref_dir = ctx.skill_dir / "references"
    readme = ref_dir / "README.md"
    if not readme.is_file():
        return True, "无 references/README.md（跳过）"
    text = ctx.read(readme) or ""
    rows = 0
    drifted = []
    for m in re.finditer(r"\[`([A-Za-z0-9_\-]+\.md)`\]", text):
        name = m.group(1)
        f = ref_dir / name
        if not f.is_file():
            continue  # 索引指向的文件缺失由第 3 项引用完整性管
        row_start = text.rfind("\n", 0, m.start()) + 1
        row_end = text.find("\n", m.end())
        row = text[row_start:row_end if row_end > 0 else len(text)]
        w = re.search(r"(\d+)\s*行\s*/", row)  # 只认 canonical 体量列「N 行 / ~M 词」，
        # 防止描述列里的「实际 120 行」等散数被误当体量（反向测试抓过此坑）
        if not w:
            continue  # 该行没有体量列（如分组标题），不算漂移
        rows += 1
        actual = (ctx.read(f) or "").count("\n") + 1
        claimed = int(w.group(1))
        if abs(claimed - actual) > 5:
            drifted.append(f"{name}(索引 {claimed} / 实际 {actual})")
    if not rows:
        return True, "索引无体量列（跳过）"
    if drifted:
        return False, f"{len(drifted)} 份体量漂移: {', '.join(drifted[:4])}——索引会误导加载成本估算"
    return True, f"{rows} 份索引体量与实际行数一致（±5 行内）"


def check_frontmatter_quotes(ctx: SkillContext):
    """frontmatter 引号卫生（D-128 · 移植自姊妹分支 v4.4.0 的第 11 项）。

    两类同源的冒号坑，都必须拦在上传之前：
      ① 裸冒号「: 」且值未加引号 → YAML 解析直接失败（FAIL）
      ② 英文冒号（即便加了引号）→ 部分平台解析器按首个英文冒号截断，
         表现为「技能莫名不触发」，症状极具误导性（WARN）
    本 skill 自己踩过 ②：3.13.1 实测 description 里的 `Use when:` / `Do NOT use for:`
    导致发布后触发词后半段整段丢失。

    ⚠ 与第 1 项的分工：**description 的英文冒号由第 1 项 FAIL 硬卡**（本 skill 的严格度判据
    「是否机器可判 → FAIL」，比姊妹分支的 WARN 更严），故本项对 description 只查「裸冒号」
    （YAML 必炸那一类，第 1 项的正则漏得掉），不重复报英文冒号——避免同一问题两个条目
    给出不同严重级。
    """
    text = ctx.content.lstrip()
    if not text.startswith("---"):
        return True, "无 frontmatter（跳过）"
    m = re.match(r"^---[ \t]*\r?\n(.*?)\r?\n---", text, re.DOTALL)
    if not m:
        return True, "frontmatter 格式无效（跳过，见第 1 项）"
    block = m.group(1)

    hard, soft = [], []
    for line in block.split("\n"):
        # 缩进行属于多行块标量（| / >）的内容，其冒号不参与 YAML 键解析
        if not line.strip() or line[0] in " \t-":
            continue
        mm = re.match(r"^([A-Za-z_][\w.-]*)\s*:\s*(.*)$", line)
        if not mm:
            continue
        key, val = mm.group(1), mm.group(2).strip()
        if not val or val in ("|", ">", "|-", ">-", "[", "{"):
            continue
        quoted = val[:1] in ("'", '"')
        # ① 裸冒号：未加引号的值里出现「: 」→ YAML 必炸
        if not quoted and re.search(r":\s+", val):
            hard.append(f"{key} 值含裸冒号且未加引号")
        # ② 英文冒号：去掉 URL 协议后仍含 ':' → 平台截断风险
        #    （description 的英文冒号已由第 1 项 FAIL 硬卡，此处跳过以免重复报）
        if key == "description":
            continue
        probe = re.sub(r"(?i)https?://", "", val)
        if ":" in probe:
            soft.append(f"{key} 值含英文冒号（建议改中文全角「：」）")

    if hard:
        return False, "; ".join(hard) + " → YAML 解析必失败，整值加引号即可；改完再上传", "fail"
    if soft:
        return False, "; ".join(soft) + " → 平台解析器可能按首个英文冒号截断该值（description 被截断时表现为触发词整段丢失，实测）", "warn"
    return True, "引号卫生通过（无裸冒号；description 的英文冒号由第 1 项把关）"


def check_dir_map(ctx: SkillContext):
    """第 11 项：SKILL.md 内嵌「目录自述图」与实际文件树一致性。半软项：WARN。

    为什么要有这一项：目录自述图（文件树 + 每文件一句话职责，条目 40）是 agent
    免 ls 猜测的直接依据；图里写了不存在的文件 = 又一处「说一套做一套」，
    且比索引体量漂移更误导（agent 会直接去找那个文件）。
    识别规则：fenced code block 中含 ├──/└── 树形字符即视为自述图，逐条目
    核对路径真实存在（目录名带 / 时按目录核对）。路径按缩进深度还原嵌套
    （每层 4 字符：`│   ` 或空格），子条目拼接父目录链——反向测试抓过
    「扁平 join 根目录导致嵌套文件误报」的坑。
    """
    text = ctx.content
    checked = 0
    missing = []
    for m in re.finditer(r"```[^\n]*\n(.*?)```", text, re.DOTALL):
        block = m.group(1)
        if "├──" not in block and "└──" not in block:
            continue  # 普通代码块，不是文件树
        stack = []  # 按深度记录当前目录链（如 ["references"]）
        for line in block.splitlines():
            starts = [i for i in (line.find("├──"), line.find("└──")) if i >= 0]
            if not starts:
                continue
            start = min(starts)
            depth = start // 4
            rest = line[start + 4:].split()
            if not rest:
                continue
            name = rest[0].rstrip("/").lstrip("./")
            if not name or name in (".", ".."):
                continue
            # 纯装饰边框线（如 ASCII 框图 `└───────┘`）不含任何字母数字，不是文件树条目
            if not any(ch.isalnum() for ch in name):
                continue
            parts = stack[:depth] + [name]
            checked += 1
            if not (ctx.skill_dir / "/".join(parts)).exists():
                missing.append("/".join(parts))
            if rest[0].endswith("/"):
                # 目录条目：记录进路径栈，供其子条目拼接
                del stack[depth:]
                stack.insert(depth, name)
    if checked == 0:
        return True, "SKILL.md 无目录自述图（跳过）"
    if missing:
        return False, (f"目录自述图 {len(missing)}/{checked} 个条目不存在于实际文件树"
                       f"（{', '.join(missing[:4])}）——自述图必须与实际一致")
    return True, f"目录自述图 {checked} 个条目全部真实存在"


# ─── 第 12 项：可触线规则（取自 westock-data D-052 / 元设计 DP-201）───
# 重复/探索类动作的"无上限信号词"——出现这些词就必须配数字上限
REPEAT_SIGNALS = ("重试", "回退", "反复", "再试", "多试", "盲试", "不断", "循环",
                  "一直", "多次", "重跑", "死磕", "继续试")
# 可数上限的合法写法
LIMIT_PAT = re.compile(r"(≤\s*\d+|≥\s*\d+|>=\s*\d+|至多\s*\d+|最多\s*\d+|不超过\s*\d+"
                       r"|\d+\s*(?:次|轮|份|遍|条|步))")
# 豁免①：元规则行——本条规则自身在讲"必须带上限"，不是重复动作纪律（反向测试抓出的假阳性）
META_RULE_PAT = re.compile(r"(数字上限|可数上限|触线)")
# 豁免②：参数化上限行——含 CLI flag（如 --retries/--backoff），上限由参数给出，同样可触线
FLAG_PAT = re.compile(r"--[A-Za-z][A-Za-z0-9_-]*")


def check_touchable_rules(ctx: SkillContext):
    """第 12 项：重复/探索类纪律是否带可数上限。半软项：WARN，不 FAIL。

    为什么要有这一项：**模糊规则等于没有规则**——「连续 ≥3 次写入必须批量」
    agent 能自检是否触线，「注意性能、尽量批量」无法执行（best-practices-library
    实证）。本 skill 曾长期主路由 **0 条**可触线规则——教别人这条却自己没做到，
    是「说一套做一套」的又一处；v3.6.0 补了 4 条 + 本项机器兜底。

    判据（机器可判）：命中重复类信号词（重试/回退/反复/再试/盲试…）的行，
    必须同时出现数字上限（≤N / 至多 N / N 次…），否则视为不可触线的模糊纪律。
    只扫主路由 SKILL.md（agent 必读层）；references 展开处由人工守。
    """
    text = ctx.content or ""
    stripped = text.lstrip()
    m = re.match(r"^---[ \t]*\r?\n.*?\r?\n---", stripped, re.DOTALL)
    scan = stripped[m.end():] if m else stripped  # 剥掉 frontmatter（散文不算纪律）

    bad, total = [], 0
    for lineno, line in enumerate(scan.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if not any(k in s for k in REPEAT_SIGNALS):
            continue
        total += 1
        # 三种"已触线"：写死数字上限 / 元规则自身 / 上限参数化（CLI flag）
        if LIMIT_PAT.search(s) or META_RULE_PAT.search(s) or FLAG_PAT.search(s):
            continue
        bad.append(f"L{lineno}: {s[:56]}")

    if total == 0:
        return True, "主路由无重复/探索类纪律（跳过）"
    if bad:
        return False, (f"{len(bad)}/{total} 条重复类纪律无可数上限——agent 无法自检是否触线"
                       f"（首例 {bad[0]}）；应写成「至多 N 次/轮/份 + 到顶后动作」")
    return True, f"{total} 条重复/探索类纪律均带可数上限（≤N / 至多 N / N 次…）"


# ─── 第 13 项：版本双落点一致性 ───
# 从 frontmatter **原始文本**提取，不走 YAML 解析：YAML 会把 `3.10` 解析成 float 3.1，
# 导致与 config.json 的 "3.10" 比对时误报（版本末位 0 是最易踩的坑）。
FM_VERSION_PAT = re.compile(r"^version:[ \t]*([^\s#]+)", re.M)


def _fm_block(text: str) -> str:
    """取出 frontmatter 原始块（含分隔线）；无则空串。"""
    stripped = (text or "").lstrip()
    m = re.match(r"^---[ \t]*\r?\n.*?\r?\n---", stripped, re.DOTALL)
    return m.group(0) if m else ""


def _fm_version(text: str) -> str:
    m = FM_VERSION_PAT.search(_fm_block(text))
    return m.group(1).strip().strip("\"'") if m else ""


def check_version_sync(ctx: SkillContext):
    """第 13 项：version 双落点（SKILL.md frontmatter ↔ config.json）一致性。**机器可判 → FAIL**。

    为什么要有这一项（v3.10.0 补）：本 skill 长期有「version 双落点必同改」的纪律，
    但它**只写在 AI 的私人记忆里**——SKILL.md / references / 脚本三处 grep `version`
    全 0 命中。smart-charts-8.1.1 至少把这条写进 `__init__.py` 注释（意图可发现），
    我们连声称都没有 → **知识没进系统，换个会话就丢**。
    正对照（DP-204）也给出了解法层级：**能机器校验就别靠人记住同步**。

    判据：两处都有值时必须字符串相等；任一缺失 → 无法判定，跳过（不误伤无 config.json 的 skill）。
    附加提示（不影响判定）：若存在 dist/<x>/，其 SKILL.md 版本落后于源则提示发布前同步。
    """
    v_skill = _fm_version(ctx.content)
    cfg = ctx.skill_dir / "config.json"
    v_cfg = ""
    if cfg.exists():
        try:
            v_cfg = str(json.loads(cfg.read_text(encoding="utf-8-sig", errors="replace")).get("version", "")).strip()
        except Exception:
            v_cfg = ""
    if not v_skill and not v_cfg:
        return True, "两处均无 version 字段（跳过）"
    if not v_cfg:
        return True, f"SKILL.md={v_skill}；无 config.json 可比对（跳过）"
    if not v_skill:
        return True, f"config.json={v_cfg}；SKILL.md frontmatter 无 version（跳过）"
    if v_skill != v_cfg:
        return False, (f"版本双落点不一致：SKILL.md={v_skill} vs config.json={v_cfg}"
                       f"——发布前必须同改（本条纪律此前只存在于 AI 记忆，v3.10.0 起机器兜底）")
    note = ""
    dist = ctx.skill_dir / "dist"
    if dist.is_dir():
        for sub in sorted(dist.iterdir()):
            if not sub.is_dir():
                continue
            d_skill = sub / "SKILL.md"
            if not d_skill.exists():
                break
            try:
                dv = _fm_version(d_skill.read_text(encoding="utf-8-sig", errors="replace"))
            except Exception:
                dv = ""
            if dv and dv != v_skill:
                note = f"；⚠ dist/{sub.name}={dv} 落后于源 {v_skill}（发布前 prepare_release + 全量同步）"
            break
    return True, f"版本双落点一致：SKILL.md = config.json = {v_skill}{note}"


def check_blueprint_fields(ctx: SkillContext):
    """第 14 项：蓝图字段单一事实源（blocks.py ↔ blueprint-template.md）。**机器可判 → FAIL**。

    DP-204「能引用就别同步」落地的机器兜底：fields 的唯一事实源 = scripts/blocks.py，
    模板每格「填空字段」段由 gen_blueprint_fields.py 生成（FIELDS 标记包裹）。
    两套骨架靠人工同步时 G1 事故三次复发（v3.4.0 B01 证据来源 / v3.7.0 B07 ④分发与安装）
    ——能机器校验就别靠人记住同步。

    仅当目标包自带该脚本与两份文件时才跑（他包 / 精简布局跳过，不误伤）。
    """
    gen = ctx.skill_dir / "scripts" / "gen_blueprint_fields.py"
    blocks_py = ctx.skill_dir / "scripts" / "blocks.py"
    tpl = ctx.skill_dir / "references" / "blueprint-template.md"
    if not (gen.exists() and blocks_py.exists() and tpl.exists()):
        return True, "非本生产线布局（缺 blocks.py / blueprint-template.md / 生成器），跳过"
    import subprocess
    try:
        p = subprocess.run([sys.executable, str(gen), "--check"],
                           capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=120,
                           cwd=str(ctx.skill_dir))
    except Exception as e:
        return False, f"gen_blueprint_fields.py 执行异常: {e}"
    out = re.sub(r"\x1b\[[0-9;]*m", "", (p.stdout or ""))  # 纪律：解析 CLI 输出先脱 ANSI
    lines = [l.strip() for l in out.splitlines() if l.strip()]
    if p.returncode == 0:
        tail = lines[-1] if lines else ""
        return True, f"蓝图字段单一事实源一致（blocks.py 生成模板字段段）{('：' + tail) if tail else ''}"
    drift = [l for l in lines if "仅模板有" in l or "仅 blocks.py 有" in l][:4]
    detail = "；".join(drift) if drift else (lines[-1] if lines else "无输出")
    return False, (f"蓝图字段漂移（blocks.py ↔ blueprint-template.md）→ 改 blocks.py 后跑 "
                   f"gen_blueprint_fields.py --write：{detail}")


def run_e2e_user_tests() -> tuple[int, int, str]:
    """--full 追加项：跑端到端用户场景回归（scripts/run_user_tests.py 25 个真实用例）。

    为什么接进闭环：**静态全过 ≠ 能用**（v3.9.0 实证：静态 12/0/0 仍实测挖出多个 bug）。
    run_user_tests.py 能跑通 25 个用例，但此前 validate 不调用它、SKILL.md 也无入口
    → **测试存在却不在闭环、agent 也读不到**（与 smart-charts 的 D3「自检脚本主路由
    无入口」是同一个病）。--full 把它接回来，默认不跑（约 1–3 分钟，留给发布前）。

    返回 (passed, failed, err)；未执行/解析失败时 passed=-1（视为失败但不掩盖原因）。
    """
    script = Path(__file__).resolve().parent / "run_user_tests.py"
    if not script.exists():
        return -1, -1, f"未找到 {script.name}"
    try:
        import subprocess
        p = subprocess.run([sys.executable, str(script), "--json"],
                           capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=1800)
    except Exception as e:
        return -1, -1, f"执行异常: {e}"
    raw = (p.stdout or "").strip()
    try:
        # run_user_tests --json 输出带 indent=2（多行），必须整体解析；
        # 只取最后一行会拿到孤立的 `}` —— 反向测试（--full 实跑）抓出的解析 bug。
        data = json.loads(raw[raw.index("{"):])
        return int(data.get("passed", 0)), int(data.get("failed", 0)), ""
    except Exception:
        return -1, -1, f"输出解析失败（rc={p.returncode}，首行：{raw.splitlines()[:1]}）"


def soft_diag(skill_dir: Path):
    """软性项结构化诊断（--diag）：触发质量 / 工作流 / 逻辑连贯性，输出 症状/根因/修复建议 三字段，供 AI 直接消费执行。"""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return {"skill": skill_dir.name, "error": "无 SKILL.md"}
    ctx = SkillContext(skill_dir)
    content = ctx.content
    fm, _ = parse_frontmatter(content)
    desc = str(fm.get("description", "")) if fm else ""
    desc_low = desc.lower()

    diag = []

    # 1. 触发质量：pushy 强触发句
    if re.search(r"make\s+sure\s+to\s+use\s+this\s+skill", desc, re.IGNORECASE):
        diag.append({"dim": "触发质量", "status": "ok", "symptom": "", "cause": "", "fix": "description 含 pushy 强触发句"})
    else:
        diag.append({"dim": "触发质量", "status": "warn",
                     "symptom": "description 缺 pushy 强触发句",
                     "cause": "仅靠明确关键词召回，用户模糊表达（如'把这件事教给 AI'）召回弱",
                     "fix": "在 description 追加 Make sure to use this skill whenever the user wants to ... even without saying ..."})

    # 2. 触发质量：NEGATIVE 负向边界
    if any(re.search(p, desc_low) for p in NEGATIVE_PATTERNS):
        diag.append({"dim": "触发质量", "status": "ok", "symptom": "", "cause": "", "fix": "description 含 NEGATIVE 负向边界"})
    else:
        diag.append({"dim": "触发质量", "status": "warn",
                     "symptom": "description 缺 NEGATIVE 负向边界",
                     "cause": "无 Do NOT use for 类边界，易误触发",
                     "fix": "追加 Do NOT use for: <3-5 个易混场景>"})

    # 3. 工作流：流程恢复 / checkpoint 机制
    if re.search(r"flow-recovery|checkpoint|断点续跑", content):
        diag.append({"dim": "工作流", "status": "ok", "symptom": "", "cause": "", "fix": "含流程恢复 / checkpoint 机制"})
    else:
        diag.append({"dim": "工作流", "status": "warn",
                     "symptom": "主流水线无 checkpoint / 断点续跑机制",
                     "cause": "引导流程卡壳 / 中断时无自动恢复，需用户介入",
                     "fix": "每格收尾落盘 checkpoint 快照，卡壳走 flow-recovery 恢复动作"})

    # 4. 逻辑连贯性：无法自动判
    diag.append({"dim": "逻辑连贯性", "status": "manual",
                 "symptom": "脚本无法自动判定",
                 "cause": "属语义 / 逻辑层面，需 AI 或人裁定",
                 "fix": "走 test-playbook 触发测试 + 效果测试双跑"})

    return {"skill": skill_dir.name, "soft_diag": diag}


def apply_fixes(skill_dir: Path, results):
    """--fix：对可自动修复项执行动作，输出修复报告（fixed=已自动修 / manual_review=需人工确认）。"""
    fixed, manual = [], []
    ctx = SkillContext(skill_dir)

    # ① README 迁移（明确、安全、可逆）
    readme = skill_dir / "README.md"
    if readme.exists():
        target = skill_dir / "references" / "README.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        readme.rename(target)
        fixed.append({"item": "README.md 在包内", "action": "已迁移到 references/README.md"})

    # ② 孤儿引用：生成建议链接 patch（不自动改导航表，交 AI/人确认插入位置）
    content = ctx.content
    for f in ctx.text_files():
        rel = str(f.relative_to(skill_dir))
        parts = rel.replace("\\", "/").split("/")  # 兼容 Windows 反斜杠，否则静默空转
        if len(parts) < 2 or parts[0] not in ("references", "scripts", "assets"):
            continue
        if f.stem in content or f.name in content:
            continue
        family = re.sub(r"[-_](?:b\d{1,2}|[A-Z])$", "", f.stem)
        if family != f.stem and family and family in content:
            continue
        manual.append({"item": f"孤儿引用 {rel}",
                       "action": "在 SKILL.md 导航表加一行加载条件",
                       "patch": f"| {f.stem} | {parts[0]}/{f.name} | 何时加载：______ |"})

    # ③ name 与目录不一致：二选一提示（不自动改，需用户决策）
    for r in results:
        if r["check"].startswith("2") and r["status"] == "fail":
            manual.append({"item": "name 与目录不一致",
                           "action": "二选一：改 frontmatter name，或改目录名（二者必须一致）"})

    # ④ description 五件事不全：起草补全（交用户确认）
    for r in results:
        if r["check"].startswith("5") and r["status"] in ("warn", "fail"):
            manual.append({"item": "description 五件事不全",
                           "action": "基于 frontmatter 已有内容起草补全，交用户确认"})

    return {"skill": skill_dir.name, "fixed": fixed, "manual_review": manual}


# ─── 主流程 ───
def validate_skill(skill_dir: Path, as_json: bool = False):
    skill_md = skill_dir / "SKILL.md"
    if not skill_dir.is_dir() or not skill_md.exists():
        return None, f"不是有效 skill 目录（缺 SKILL.md）: {skill_dir}"

    ctx = SkillContext(skill_dir)
    checks = [
        ("1. frontmatter 有效", check_frontmatter),
        ("2. name 与目录一致", check_name_dir),
        ("3. 引用完整性", check_references),
        ("4. 长度(body<5K/≤500行)", check_length),
        ("5. description 五件事", check_description_five),
        ("6. 安全(密钥/XML/保留词)", check_security),
        ("7. 无 README.md", check_no_readme),
        ("8. 孤儿引用", check_orphan_refs),
        ("9. references 元数据", check_ref_frontmatter),
        ("10. 索引体量漂移", check_index_drift),
        ("11. 目录自述图一致性", check_dir_map),
        ("12. 纪律可触线性", check_touchable_rules),
        ("13. 版本双落点一致", check_version_sync),
        ("14. 蓝图字段单一事实源", check_blueprint_fields),
        ("15. frontmatter 引号卫生", check_frontmatter_quotes),
    ]
    results = []
    n_pass = n_fail = n_warn = 0
    for label, fn in checks:
        try:
            res = fn(ctx)
            # v3.15.0：允许检查函数返回三元组 (ok, msg, severity) 自报严重级（移植自姊妹分支 v4.4.0）；
            # 老函数返回二元组的行为不变（向后兼容）
            if isinstance(res, tuple) and len(res) == 3:
                ok, msg, forced = res
            else:
                ok, msg = res
                forced = None
        except Exception as e:
            ok, msg, forced = False, f"脚本异常: {e}", None
        # 严格度判据 = **该项是否机器可判**（取自 westock-data D-030「可验证性决定严格度」）：
        #   机器可判（1/2/3/4/7/13/14）→ FAIL 硬卡；
        #   需人工复核的启发式项（5/6 密钥类/8/9/10/11/12）→ WARN 放行但提示。
        # 注意：判据**不是**「是否历史产物」——历史产物若机器可判，照样该 FAIL。
        severity = "fail"
        if ok:
            severity = "pass"
            n_pass += 1
        elif forced in ("warn", "fail"):
            severity = forced
            n_warn += 1 if forced == "warn" else 0
            n_fail += 1 if forced == "fail" else 0
        elif label.startswith(("5", "8", "9", "10", "11", "12")) or (label.startswith("6") and "疑似硬编码" in msg and "XML" not in msg and "保留词" not in msg):
            severity = "warn"
            n_warn += 1
        else:
            n_fail += 1
        results.append({"check": label, "status": severity, "message": msg})

    if as_json:
        return {"skill": skill_dir.name, "results": results,
                "pass": n_pass, "warn": n_warn, "fail": n_fail}, None

    print(f"\n{'='*60}")
    print(f"Skill 静态验证: {CYAN}{skill_dir.name}{RESET}")
    print(f"{'='*60}")
    for r in results:
        tag = {"pass": _tag(True), "fail": _tag(False), "warn": _warn()}[r["status"]]
        print(f"  [{tag}] {r['check']:28s} — {r['message']}")
    summary = f"\n  结果: {n_pass} 过 / {n_warn} 警 / {n_fail} 败"
    if n_fail == 0:
        print(f"  {GREEN}硬性检查全过{RESET}{summary}")
    else:
        print(f"  {RED}{n_fail} 项硬性失败{RESET}{summary}")
        print("  -> 软性项（逻辑/触发质量/工作流）需 AI/人裁定；硬性项改完再跑。")
    if n_warn:
        print(f"  {YELLOW}WARN 项建议处理：可发布但先看说明。{RESET}")
    return results, None


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    do_fix = "--fix" in args
    do_diag = "--diag" in args
    do_full = "--full" in args
    args = [a for a in args if a not in ("--json", "--fix", "--diag", "--full")]

    # Windows 控制台统一 UTF-8 输出，避免 GBK 乱码
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    if not args:
        print(__doc__)
        return 1

    if args[0] == "--self":
        skill_dir = Path(__file__).resolve().parent.parent  # skill-designer 根
    else:
        skill_dir = Path(args[0]).resolve()

    # --diag：软性项结构化诊断（不跑硬性检查，直接输出三字段诊断）
    if do_diag:
        print(json.dumps(soft_diag(skill_dir), ensure_ascii=False, indent=2))
        return 0

    out, err = validate_skill(skill_dir, as_json)
    if err:
        print(err)
        return 1

    # --fix：对可自动修复项执行动作 + 输出修复报告
    if do_fix:
        report = apply_fixes(skill_dir, out)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    # --full：静态之外追加端到端用户场景回归（不计入 13 项，单列一行）
    e2e = None
    if do_full:
        e2e = run_e2e_user_tests()
        if e2e[0] < 0:
            print(f"  [{_warn()}] {'端到端用户场景回归':26s} — 未执行：{e2e[2]}")
        else:
            print(f"  [{_tag(e2e[1] == 0)}] {'端到端用户场景回归':26s} "
                  f"— {e2e[0]} 通过 / {e2e[1]} 失败（run_user_tests，--full）")
    e2e_ok = (e2e is None) or (e2e[0] >= 0 and e2e[1] == 0)

    if as_json:
        if e2e is not None:
            out["e2e_user_tests"] = {"passed": e2e[0], "failed": e2e[1], "error": e2e[2]}
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0 if (out["fail"] == 0 and e2e_ok) else 1
    # 非 JSON 模式：out 是 results 列表
    n_fail = sum(1 for r in out if r["status"] == "fail") + (0 if e2e_ok else 1)
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
