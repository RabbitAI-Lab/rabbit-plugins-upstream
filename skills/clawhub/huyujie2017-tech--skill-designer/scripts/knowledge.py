#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
knowledge.py — 知识库统一门面（ADR-001 阶段0 · 契约层 / local 后端）

为什么需要这个文件（阶段0 措施 0.1 + 0.2）
────────────────────────────────────────────────────────────────────
重构前，「知识怎么被检索到」这件事是**隐式**的：

  · SKILL.md 的路由表把「用户意图 → references/xxx.md 路径」写死在 markdown 里（30+ 处），
    agent 只能靠人读各文件头部的「加载条件」自行判断该开哪一份；
  · 召回的粒度是**文件**（22 份顶层 + 10 份分片），召不到**条目**（147 条 D 里挑 2 条）；
  · 条目库的四方一致性（分片实际条数 = 视图一声明 = 速查表行数 = 头部计数）至今
    依靠人工脚本 outputs/_verify_library2.py 跑——跨落点漂移已复发三次。

本文件把「知识接口」显式化为 4 件契约，阶段0 只实现 local 后端：

  ① ID 契约      D-NNN / DP-XXX / L-NN 永久稳定，作为**唯一引用键**（路径退居实现细节）
  ② Manifest     **条目粒度**索引（id/block/themes/title/abstract/tags/hash），可整份常驻上下文
  ③ 检索契约     index / get / search / verify / stats 五动作，本地与远程**同签名**
  ④ 完整性契约   逐条 sha256 + 库版本，防「权威源被改而索引没跟上」

阶段0 的硬边界（不可越界）
────────────────────────────────────────────────────────────────────
  **本文件不搬动、不改写任何权威源。**
  Manifest 是**派生索引**，随时可重生成；get() 直接从权威 markdown 切片返回正文。
  因此全库**不存在第二份内容**——遵守 DP-204（单一事实源）/ DP-209（权威源唯一化）。
  把权威源上移到结构化数据、让 markdown 变成生成物，是**阶段 1** 的事。

失败语义（DP-210 失败即熔断，不得向右兜底）
────────────────────────────────────────────────────────────────────
  索引缺失 / 正文与索引 hash 不符 / ID 编号断裂 → **硬失败（退出码 1）**，
  并给出一个可执行动作；绝不用模型记忆或旧数据「凑」出结果。
  视图漂移等不阻断使用的偏差 → 仅警告（退出码 2），与 check_blueprint 缺口语义一致。

用法
────────────────────────────────────────────────────────────────────
    python scripts/knowledge.py index  [--write] [--compact] [--out <路径>] [--json]
    python scripts/knowledge.py get    D-133 [--format md|json]
    python scripts/knowledge.py search --block B07 [--theme T4] [--tag 路由] [--text 加载] [--limit 5] [--json] [--ids-only]
    python scripts/knowledge.py verify [--strict] [--json]
    python scripts/knowledge.py stats  [--dead-after 10] [--json]
    python scripts/knowledge.py selftest   # 契约层反向测试（改判据后必跑，L11）

两层索引（实测体量，勿混用）
────────────────────────────────────────────────────────────────────
    机器件  scripts/library_manifest.json  176 条 ≈ 109 KB ≈ 50 K token  → 只给 verify/工具读，**绝不进上下文**
    上下文件 `index --compact`            176 条 ≈ 11.7 KB ≈ 4.5 K token → 可给 agent 看；默认不落盘、按需生成

    为什么分两层：DP-207（有限资源分层承载）。ADR-001 曾估「manifest ≈1.5–2K token 可整份常驻」，
    实测高出一倍有余 → 结论改为「**不整份常驻，按需 search 取切片**」（见 outputs/arch-refactor-20260911/ 勘误）。
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys
from pathlib import Path

from errors import enable_utf8, fail, warn

# ───────────────────────────── 常量 / 契约 ─────────────────────────────

SCHEMA_VERSION = "1.0"
MANIFEST_REL = Path("scripts") / "library_manifest.json"
TELEMETRY_REL = Path("scripts") / "library_telemetry.json"

BLOCK_IDS = [f"B{i:02d}" for i in range(1, 11)]
BLOCK_NAMES = {
    "B01": "条件", "B02": "事实", "B03": "观点", "B04": "问题", "B05": "分析",
    "B06": "决策", "B07": "计划", "B08": "行动", "B09": "结果", "B10": "复盘",
}

RE_SHARD = Path("references") / "blocks"
SHARD_FMT = "design-blocks-b{:02d}.md"
PRINCIPLES_REL = Path("references") / "design-principles-library.md"
LESSONS_REL = Path("references") / "lessons.md"
LIBRARY_REL = Path("references") / "design-blocks-library.md"

RE_ENTRY_HEAD = re.compile(r"^###\s+(D-\d+)\s*·\s*(.+?)\s*$", re.M)
RE_DP_HEAD = re.compile(r"^###\s+(DP-\d+)\s*·\s*(.+?)\s*$", re.M)
RE_L_HEAD = re.compile(r"^###\s+(L\d+)\s*·\s*(.+?)\s*$", re.M)
RE_ANY_H3 = re.compile(r"^###\s+.*$", re.M)
# 条目级 h3：**只有**「### <ID> · 标题」才是条目边界。
# 为什么不能用任意 h3 当边界：实测 D-106 正文内部含 `### 检查清单（按「时机 × 角度」分组）`
# 与 `#### A. 任务前…` 两级小标题——用 RE_ANY_H3 作边界会把正文**从那里截断**，
# 后续内容既不属于本条也不属于任何条（静默丢失）。阶段0 的 manifest 一直带着这个洞，
# 直到阶段1 编译器做「生成物 diff」才把它照出来（**命令输出 ≠ 实际生效**的又一实证）。
RE_ENTRY_H3 = re.compile(r"^###\s+(?:D-\d{3}|DP-\d{3}|L\d+)\s*·", re.M)
# 正文结束边界 = ① 下一个**条目级** h3  ② 下一处 `##` 段级标题。
# 只写 ① 会漏掉「最后一个条目吞到文件尾」——实测 DP-211 与 L12 的正文把文末
# `## 归档区` 一并吞下，编译器渲染时与骨架重复输出（生成物多出一份归档区）。
# 加上 ② 即解决；实测 10 个分片里 `^##` 行数为 0，不会误伤正文。
RE_BODY_END = re.compile(r"^(?:###\s+(?:D-\d{3}|DP-\d{3}|L\d+)\s*·|##\s)", re.M)
# ───────────────────── 解析：字段键识别 + KV 提取 ─────────────────────

RE_KV = re.compile(r"\*\*([^*\n]{1,14})\*\*")
# 字段键的前缀只允许出现结构符（行首 / 列表符 / 引用符 / 分隔符）；
# 含实义文字的前缀说明这是**行内加粗**，不是字段键。
RE_STRUCT_PREFIX = re.compile(r"^[\s\-*>｜|]*$")


def _field_keys(line: str) -> list:
    """挑出本行真正的「字段键」** 匹配，排除行内加粗。

    为什么必须区分：`- **要点**：施工图 = 选框架 → **五段骨架逐段填出** → 资源分配。`
    里有 **两处** `**…**`——后者是行内强调。若一并当字段键，`要点` 的值会被
    截断成半句（实测 D-062 的 abstract 因此只剩 25 个字符），而 abstract 是
    agent 判断「这条相不相关」的第一信号，截断直接拉低召回质量。
    """
    keys = []
    for m in RE_KV.finditer(line):
        prefix = line[:m.start()]
        cut = max(prefix.rfind("｜"), prefix.rfind("|"))
        seg = prefix[cut + 1:] if cut >= 0 else prefix
        if RE_STRUCT_PREFIX.match(seg):
            keys.append(m)
    return keys


def parse_fields(block_text: str) -> dict:
    """把「**键**：值」式行解析成字典（含多行字段的值续行）。

    同一条目的字段有三种写法，都要接住：
        - **主题** T8 工程·脚本·性能                   （无冒号、带列表符）
        - **落位** B03 观点 ｜ **主题** T1 模式与类型    （同一行两个字段）
          **要点**：……                                 （无列表符）
    """
    out: dict[str, str] = {}
    raw_lines = block_text.split("\n")
    for i, line in enumerate(raw_lines):
        keys = _field_keys(line)
        if not keys:
            continue
        for j, m in enumerate(keys):
            key = m.group(1).strip()
            seg_end = keys[j + 1].start() if j + 1 < len(keys) else len(line)
            val = line[m.end():seg_end].strip().lstrip("：:").strip().rstrip("｜|").strip()
            if j == len(keys) - 1:            # 末字段：并入后续非字段行（多行值续行）
                rest = []
                k = i + 1
                while k < len(raw_lines) and len(rest) < 6:
                    nxt = raw_lines[k]
                    stripped = nxt.strip()
                    if (not stripped or _field_keys(nxt)
                            or stripped.startswith(("---", "#", "|"))):
                        break
                    rest.append(stripped)
                    k += 1
                if rest:
                    val = (val + " " + " ".join(rest)).strip()
            if key and val and key not in out:
                out[key] = val
    return out

# ───────────────────────────── 基础 IO / 正文规范化 ─────────────────────────────

def read_text(path: Path) -> str:
    return io.open(path, encoding="utf-8").read()


def norm_body(text: str) -> str:
    """正文规范化：统一换行、去行尾空白、去首尾空行与尾部 --- 分隔线。

    为什么必须规范化：hash 要跨平台稳定（Windows 的 \\r\\n 会让同一份文件
    在两个平台上算出不同 hash，完整性契约当场失效）。
    """
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and (not lines[-1].strip() or lines[-1].strip() == "---"):
        lines.pop()
    return "\n".join(lines)


def sha256_of(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def first_sentence(text: str, limit: int = 120) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"[`*]", "", text)
    if len(text) <= limit:
        return text
    cut = text[:limit]
    for sep in ("。", "；", "，", " "):
        idx = cut.rfind(sep)
        if idx > limit * 0.5:
            return cut[:idx] + "…"
    return cut + "…"


# ───────────────────────────── 解析：三个来源 ─────────────────────────────

def slice_body(text: str, head_start: int) -> str:
    """取条目正文：从标题行之后，到**下一个条目级 h3 或段级 h2** 或文末。

    边界必须用 RE_BODY_END（详见其定义处的两段说明）：
      · 不能用「任意 ###」——正文内部的小标题（如 `### 检查清单`）会被误当边界而截断正文；
      · 也不能只用「条目级 ###」——最后一个条目的正文会吞掉文末的 `## 归档区`。
    """
    nl = text.find("\n", head_start)
    nxt = RE_BODY_END.search(text, nl + 1)
    end = nxt.start() if nxt else len(text)
    return text[nl + 1:end]


def parse_shard(path: Path, block_id: str) -> list[dict]:
    text = read_text(path)
    heads = list(RE_ENTRY_HEAD.finditer(text))
    out = []
    for i, m in enumerate(heads):
        body = norm_body(slice_body(text, m.start()))
        f = parse_fields(body)
        themes = re.findall(r"\bT(\d{1,2})\b", f.get("主题", "")) or re.findall(r"\bT(\d{1,2})\b", f.get("落位", ""))
        tags = re.findall(r"`([^`]+)`", f.get("标签", ""))
        out.append({
            "id": m.group(1),
            "kind": "entry",
            "block": block_id,
            "blocks": [block_id],
            "themes": [f"T{t}" for t in dict.fromkeys(themes)],
            "title": m.group(2).strip(),
            "abstract": first_sentence(f.get("要点") or f.get("触发信号") or m.group(2)),
            "tags": [t.strip() for t in tags if t.strip()],
            "trigger": first_sentence(f.get("触发信号", ""), 90),
            "source": str(path.relative_to(path.parents[2])).replace("\\", "/"),
            "anchor": f"### {m.group(1)} · {m.group(2).strip()}",
            "line": text.count("\n", 0, m.start()) + 1,
            "hash": sha256_of(body),
            "origin": first_sentence(f.get("来源", ""), 80),
            "explains": [],
        })
    return out


def parse_principles(path: Path) -> list[dict]:
    text = read_text(path)
    heads = list(RE_DP_HEAD.finditer(text))
    out = []
    for m in heads:
        body = norm_body(slice_body(text, m.start()))
        f = parse_fields(body)
        blocks = list(dict.fromkeys(re.findall(r"\bB\d{2}\b", f.get("落地要点", ""))))
        # explains：只认条目区「来源」行里的显式 D-NNN（速查表那一列用的是压缩写法，
        # 如「D-027 404 405 407 409」是 A-4xx 系列的简记，不可直接当 ID 用）
        explains = list(dict.fromkeys(re.findall(r"\bD-\d{3}\b", f.get("来源", ""))))
        out.append({
            "id": m.group(1),
            "kind": "principle",
            "block": blocks[0] if blocks else "",
            "blocks": blocks,
            "themes": [],
            "title": m.group(2).strip(),
            "abstract": first_sentence(f.get("原则概述") or m.group(2)),
            "tags": [t.strip() for t in re.split(r"[/、]", f.get("适用场景", "").split("触发信号")[0].lstrip("标签 ").strip()) if t.strip()],
            "trigger": first_sentence(f.get("适用场景", ""), 90),
            "source": str(path.relative_to(path.parents[1])).replace("\\", "/"),
            "anchor": f"### {m.group(1)} · {m.group(2).strip()}",
            "line": text.count("\n", 0, m.start()) + 1,
            "hash": sha256_of(body),
            "origin": first_sentence(f.get("来源", ""), 80),
            "explains": explains,
        })
    return out


def parse_lessons(path: Path) -> list[dict]:
    text = read_text(path)
    heads = list(RE_L_HEAD.finditer(text))
    out = []
    for m in heads:
        body = norm_body(slice_body(text, m.start()))
        f = parse_fields(body)
        blocks = list(dict.fromkeys(re.findall(r"\bB\d{2}\b", f.get("触发格", ""))))
        mref = re.search(r"引用[：:]\s*(\d+)", body)
        out.append({
            "id": m.group(1),
            "kind": "lesson",
            "block": blocks[0] if blocks else "",
            "blocks": blocks,
            "themes": [],
            "title": m.group(2).strip(),
            "abstract": first_sentence(f.get("规则") or m.group(2)),
            "tags": [],
            "trigger": first_sentence(f.get("信号", ""), 90),
            "source": str(path.relative_to(path.parents[1])).replace("\\", "/"),
            "anchor": f"### {m.group(1)} · {m.group(2).strip()}",
            "line": text.count("\n", 0, m.start()) + 1,
            "hash": sha256_of(body),
            "origin": first_sentence(f.get("来源", ""), 80),
            "explains": [],
            "refs": int(mref.group(1)) if mref else 0,   # lessons 自带的引用计数（机器写回）
        })
    return out


# ───────────────────────────── 索引构建 ─────────────────────────────

def build_manifest(root: Path) -> dict:
    """从权威源重建 manifest。**读权威源，不写权威源。**"""
    entries: list[dict] = []
    for i, block_id in enumerate(BLOCK_IDS, start=1):
        shard = root / RE_SHARD / SHARD_FMT.format(i)
        if not shard.is_file():
            continue
        entries.extend(parse_shard(shard, block_id))
    entries.extend(parse_principles(root / PRINCIPLES_REL))
    entries.extend(parse_lessons(root / LESSONS_REL))

    counts = {"entry": 0, "principle": 0, "lesson": 0}
    blocks: dict[str, int] = {}
    for e in entries:
        counts[e["kind"]] = counts.get(e["kind"], 0) + 1
        if e["kind"] == "entry":
            blocks[e["block"]] = blocks.get(e["block"], 0) + 1

    # 库版本 = kb-<权威源最新修改日>.<条目总数>
    mtimes = []
    for rel in [PRINCIPLES_REL, LESSONS_REL, LIBRARY_REL] + \
               [RE_SHARD / SHARD_FMT.format(i) for i in range(1, 11)]:
        p = root / rel
        if p.is_file():
            mtimes.append(p.stat().st_mtime)
    day = "0000.00.00"
    if mtimes:
        import datetime
        day = datetime.date.fromtimestamp(max(mtimes)).strftime("%Y.%m.%d")

    lib_version = f"kb-{day}.{len(entries)}"
    return {
        "schemaVersion": SCHEMA_VERSION,
        "libraryVersion": lib_version,
        "counts": counts,
        "blocks": {b: blocks.get(b, 0) for b in BLOCK_IDS},
        "total": len(entries),
        "entries": entries,
    }


def manifest_path(root: Path) -> Path:
    return root / MANIFEST_REL


def load_manifest(root: Path):
    p = manifest_path(root)
    if not p.is_file():
        return None
    try:
        return json.loads(read_text(p))
    except (ValueError, OSError):
        return None


# ───────────────────────────── local 后端 ─────────────────────────────

class LocalBackend:
    """本地后端：manifest 常驻、正文按需从权威源切片。

    与未来 RemoteBackend **同签名**（index/get/search/verify），
    这样阶段 2 切后端时主流程一行不用改（ADR-001 §5.2 契约③）。
    """

    def __init__(self, root: Path):
        self.root = root

    # -- ② Manifest --------------------------------------------------
    def index(self) -> dict:
        return build_manifest(self.root)

    # -- ③ get -------------------------------------------------------
    def get(self, eid: str) -> dict | None:
        rebuilt = build_manifest(self.root)
        for e in rebuilt["entries"]:
            if e["id"].lower() == eid.lower():
                src = self.root / e["source"]
                text = read_text(src)
                m = re.search(r"^###\s+" + re.escape(e["id"]) + r"\s*·.*$", text, re.M)
                if not m:
                    return None
                body = norm_body(slice_body(text, m.start()))
                return {"id": e["id"], "kind": e["kind"], "block": e["block"],
                        "title": e["title"], "version": rebuilt["libraryVersion"],
                        "body": body, "hash": sha256_of(body)}
        return None

    # -- ③ search ----------------------------------------------------
    def search(self, block=None, theme=None, tag=None, text=None, limit=5) -> list[dict]:
        mf = build_manifest(self.root)
        tokens = [t for t in re.split(r"\s+", (text or "").strip()) if t]
        hits = []
        for e in mf["entries"]:
            if block and e["block"] != block.upper() and block.upper() not in e["blocks"]:
                continue
            if theme and theme.upper() not in [t.upper() for t in e["themes"]]:
                continue
            if tag and not any(tag in t for t in e["tags"]):
                continue
            if tokens:
                blob = " ".join([e["id"], e["title"], e["abstract"], e["trigger"],
                                 " ".join(e["tags"]), " ".join(e["themes"]), e.get("origin", "")])
                # 正文也参与匹配（权威源实时读，不落第二份拷贝）
                body = self.get(e["id"]) or {}
                blob += " " + body.get("body", "")
                if not all(t in blob for t in tokens):
                    continue
            hits.append(e)
        out = []
        for e in hits[: max(limit, 0) or None]:
            out.append({"id": e["id"], "kind": e["kind"], "block": e["block"],
                        "title": e["title"], "abstract": e["abstract"]})
        return out

    # -- ④ verify ----------------------------------------------------
    def verify(self, strict: bool = False) -> dict:
        """四类检查，全部机器可判（对齐 DP-211：验收先问执行者能力）。"""
        report = {"hard": [], "soft": [], "checks": []}

        mf_disk = load_manifest(self.root)
        if mf_disk is None:
            report["hard"].append("E008 manifest 缺失或 JSON 不可解析 → 跑 `sd_cli knowledge index --write`")
            report["checks"].append(("C0 manifest 可读", False, "缺失/损坏"))
            return report
        report["checks"].append(("C0 manifest 可读", True, f"{mf_disk.get('total')} 条"))

        if mf_disk.get("schemaVersion") != SCHEMA_VERSION:
            report["hard"].append(
                f"E008 schemaVersion 不匹配（索引 {mf_disk.get('schemaVersion')} / 本脚本 {SCHEMA_VERSION}）"
                " → 重新生成索引（索引与脚本版本必须同代）")
            report["checks"].append(("C0 schema 同代", False, "schemaVersion 不一致"))
            return report
        report["checks"].append(("C0 schema 同代", True, SCHEMA_VERSION))

        # C1 索引与权威源一致
        # 为什么比「整条指纹」而不是只比正文 hash：正文切片**不含标题行**（标题在
        # `### D-NNN · X` 里，属结构不属正文），所以只比 hash 会漏掉「改标题 / 改落位 /
        # 改主题 / 改标签」这类改动——反向测试夹具 ② 实测抓到过这个洞（索引撒谎而 verify 全绿）。
        # 唯一排除的字段是 `line`：在条目上方插入文字会合法地平移行号，不算内容改动。
        FINGERPRINT_KEYS = ("id", "kind", "block", "blocks", "themes", "title", "abstract",
                            "tags", "trigger", "source", "anchor", "hash", "origin",
                            "explains", "refs")

        def _fp(e: dict) -> str:
            payload = {k: e.get(k) for k in FINGERPRINT_KEYS}
            return hashlib.sha256(
                json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
            ).hexdigest()

        rebuilt = build_manifest(self.root)
        old = {e["id"]: e for e in mf_disk["entries"]}
        new = {e["id"]: e for e in rebuilt["entries"]}
        appended = sorted(set(new) - set(old))
        removed = sorted(set(old) - set(new))
        changed = sorted(i for i in set(old) & set(new) if _fp(old[i]) != _fp(new[i]))
        if appended or removed or changed:
            det = []
            if appended:
                det.append(f"新增 {len(appended)}：{' '.join(appended[:5])}")
            if removed:
                det.append(f"消失 {len(removed)}：{' '.join(removed[:5])}")
            if changed:
                det.append(f"内容改动 {len(changed)}：{' '.join(changed[:5])}")
            report["hard"].append("E009 索引与权威源不一致（" + "；".join(det) +
                                  "）→ 跑 `sd_cli knowledge index --write` 重建；若正文是被手工改的，先看 git diff")
            report["checks"].append(("C1 索引↔权威源指纹", False, "；".join(det)))
        else:
            report["checks"].append(("C1 索引↔权威源指纹", True, f"{len(new)} 条逐条一致（含标题/落位/标签/摘要）"))

        # C2 ID 编号空间完整性（I2 不变量）
        gaps = []
        d_ids = sorted(int(i[2:]) for i in new if i.startswith("D-"))
        if d_ids:
            gaps += [f"D-{i:03d}" for i in range(1, max(d_ids) + 1) if i not in set(d_ids)]
        for prefix in ("DP-", "L"):
            ids = sorted(int(re.sub(r"\D", "", i)) for i in new if i.startswith(prefix))
            if not ids:
                continue
            # DP 允许按百位分段（0xx / 1xx / 2xx 各自连续），L 连续
            series: dict[int, list[int]] = {}
            for v in ids:
                series.setdefault(v // 100, []).append(v)
            for _, vals in series.items():
                for v in range(vals[0], vals[-1] + 1):
                    if v not in set(vals):
                        gaps.append(f"{prefix}{v}" if prefix == "L" else f"{prefix}{v:03d}")
        dupes = sorted({e["id"] for e in rebuilt["entries"] if
                        sum(1 for x in rebuilt["entries"] if x["id"] == e["id"]) > 1})
        if gaps or dupes:
            det = []
            if gaps:
                det.append("缺号：" + " ".join(gaps[:8]) + ("…" if len(gaps) > 8 else ""))
            if dupes:
                det.append("重复：" + " ".join(dupes[:8]))
            report["hard"].append("E010 ID 编号空间断裂（" + "；".join(det) +
                                  "）→ ID 永久稳定不得重编号，补条目或修正编号后重建索引")
            report["checks"].append(("C2 ID 编号空间", False, "；".join(det)))
        else:
            report["checks"].append(("C2 ID 编号空间", True,
                                     f"D-001~D-{max(d_ids):03d} 连续 / 无重复（含 DP・L）"))

        # C3 条目库四方一致性（把 outputs/_verify_library2.py 的人工核对升为一等命令）
        c3 = verify_library_views(self.root, rebuilt)
        if c3["fail"]:
            report["soft"].append("E011 条目库视图不一致：" + "；".join(c3["fail"]) +
                                  " → 人工脚本核对（阶段1 编译器落地后由生成器保证）")
            report["checks"].append(("C3 条目库四方一致性", False, "；".join(c3["fail"])))
        else:
            report["checks"].append(("C3 条目库四方一致性", True, c3["ok"]))

        # C4 设计观层引用完整性（DP.explains 指向的 D 必须存在）
        known = set(new)
        dangling = []
        for e in rebuilt["entries"]:
            for t in e.get("explains", []):
                if t not in known:
                    dangling.append(f"{e['id']}→{t}")
        if dangling:
            report["soft"].append("E012 设计观层引用了不存在的条目：" + " ".join(dangling[:6]) +
                                  " → 修正 DP 来源行或补该条目")
            report["checks"].append(("C4 DP 引用可解析", False, " ".join(dangling[:6])))
        else:
            n = sum(len(e.get("explains", [])) for e in rebuilt["entries"])
            report["checks"].append(("C4 DP 引用可解析", True, f"{n} 条引用全部命中"))

        # C5 生成物 ↔ 权威源（阶段1 起 md 全部是 library/*.json 的生成物）
        # 为什么必须单列这一项：C1 比的是「索引 ↔ md」，它**防不住"有人直接手改 md"**——
        # md 一改，重算索引又自洽了（C1 复绿），于是"权威源唯一"名存实亡。
        # C5 才是 md 已降级为生成物之后的真正守卫：md 必须**逐字节等于**权威源的渲染结果。
        try:
            import importlib
            import sys as _sys
            _sys.path.insert(0, str(Path(__file__).resolve().parent))
            cl = importlib.import_module("compile_library")
            if not (self.root / "library" / "entries.json").is_file():
                report["hard"].append(
                    "E013 权威源 library/*.json 缺失（阶段1 起它必须随包发布，否则 md 无法回编译）"
                    " → 跑 `python scripts/library_extract.py` 重建，或检查发布白名单是否漏了 library/")
                report["checks"].append(("C5 生成物↔权威源", False, "权威源缺失"))
            else:
                rendered = cl.render_all(self.root)
                drift = [str(rel) for rel, txt in rendered.items()
                         if (self.root / rel).is_file() and read_text(self.root / rel) != txt]
                missing = [str(rel) for rel in rendered if not (self.root / rel).is_file()]
                if drift or missing:
                    det = []
                    if drift:
                        det.append(f"被手改 {len(drift)} 份：{' '.join(drift[:3])}")
                    if missing:
                        det.append(f"缺失 {len(missing)} 份：{' '.join(missing[:3])}")
                    report["hard"].append(
                        "E013 生成物与权威源不一致（" + "；".join(det) +
                        "）→ md 已是生成物，**改内容请改 library/*.json 后重编译**："
                        "`python scripts/compile_library.py --write`")
                    report["checks"].append(("C5 生成物↔权威源", False, "；".join(det)))
                else:
                    report["checks"].append(
                        ("C5 生成物↔权威源", True, f"{len(rendered)} 份生成物逐字节等于权威源渲染结果"))
        except Exception as e:                     # 权威源不可读 = 硬失败，不得静默跳过
            report["hard"].append(f"E013 生成物一致性无法核对（{type(e).__name__}: {e}）→ 检查 library/ 与 scripts/compile_library.py")
            report["checks"].append(("C5 生成物↔权威源", False, f"{type(e).__name__}"))

        if strict and report["soft"]:
            report["hard"] += [s + "（--strict 下升级为硬失败）" for s in report["soft"]]
            report["soft"] = []
        return report


# ───────────────────────────── 条目库视图一致性 ─────────────────────────────

RE_VIEW1_COUNT = re.compile(r"^\|\s*\*\*(B\d\d)[^*]*\*\*\s*\|\s*\[[^\]]+\]\([^)]+\)\s*\|\s*(\d+)\s*\|", re.M)
RE_VIEW1_IDS = re.compile(r"^\|\s*\*\*(B\d\d)\*\*\s*\|\s*([^|]+)\|", re.M)
RE_QUICK = re.compile(r"^\|\s*\*{0,2}(D-\d+)\*{0,2}\s*\|\s*([^|]+?)\s*\|\s*(B\d\d)\s*\|\s*(T\d+)\s*\|", re.M)
RE_THEME = re.compile(r"^\|\s*\*\*(T\d+)[^*]*\*\*\s*\|\s*([^|]+)\|", re.M)
RE_HEADCOUNT = re.compile(r"(\d+)\s*条可复用设计积木")
RE_SHARDCOUNT = re.compile(r"共\s*(\d+)\s*条")


def verify_library_views(root: Path, manifest: dict) -> dict:
    lib_p = root / LIBRARY_REL
    if not lib_p.is_file():
        return {"fail": [], "ok": "无 design-blocks-library.md（跳过）"}
    import collections
    lib = read_text(lib_p)
    fail_msgs, ok_msgs = [], []

    shard_counts = collections.Counter(e["block"] for e in manifest["entries"] if e["kind"] == "entry")
    shard_ids = collections.defaultdict(set)
    for e in manifest["entries"]:
        if e["kind"] == "entry":
            shard_ids[e["block"]].add(e["id"])

    v1_counts = {m.group(1): int(m.group(2)) for m in RE_VIEW1_COUNT.finditer(lib)}
    v1_ids = {}
    for m in RE_VIEW1_IDS.finditer(lib):
        v1_ids[m.group(1)] = set(re.findall(r"\bD-\d{3}\b", m.group(2)))

    quick_rows = list(RE_QUICK.finditer(lib))
    quick_ids = {m.group(1) for m in quick_rows}
    quick_block = {m.group(1): m.group(3) for m in quick_rows}

    # 头部计数
    head = RE_HEADCOUNT.search(lib)
    head_count = int(head.group(1)) if head else None

    # 分片自身声明的「共 N 条」
    for i, b in enumerate(BLOCK_IDS, start=1):
        shard = root / RE_SHARD / SHARD_FMT.format(i)
        if not shard.is_file():
            continue
        m = RE_SHARDCOUNT.search(read_text(shard).split("\n\n")[1] if "\n\n" in read_text(shard) else "")
        if not m:
            m = RE_SHARDCOUNT.search(read_text(shard)[:1200])
        actual = shard_counts.get(b, 0)
        if m and int(m.group(1)) != actual:
            fail_msgs.append(f"{b} 分片标题「共 {m.group(1)} 条」≠ 实际 {actual}")
        if b in v1_counts and v1_counts[b] != actual:
            fail_msgs.append(f"{b} 视图一声明 {v1_counts[b]} ≠ 实际 {actual}")
        if b in v1_ids and len(v1_ids[b]) != actual:
            fail_msgs.append(f"{b} 视图一 ID 列表 {len(v1_ids[b])} 个 ≠ 实际 {actual}")
        if b in v1_ids:
            only_shard = shard_ids.get(b, set()) - v1_ids[b]
            only_view = v1_ids[b] - shard_ids.get(b, set())
            if only_shard:
                fail_msgs.append(f"{b} 分片有而视图一无：{' '.join(sorted(only_shard)[:4])}")
            if only_view:
                fail_msgs.append(f"{b} 视图一有而分片无：{' '.join(sorted(only_view)[:4])}")

    total_entries = sum(shard_counts.values())
    if head_count is not None and head_count != total_entries:
        fail_msgs.append(f"头部计数 {head_count} ≠ 分片合计 {total_entries}")
    if len(quick_rows) != total_entries:
        fail_msgs.append(f"速查表 {len(quick_rows)} 行 ≠ 分片合计 {total_entries}")
    if quick_ids != set().union(*shard_ids.values()) if shard_ids else False:
        miss = set().union(*shard_ids.values()) - quick_ids
        extra = quick_ids - set().union(*shard_ids.values())
        if miss:
            fail_msgs.append(f"速查表漏 {len(miss)}：{' '.join(sorted(miss)[:5])}")
        if extra:
            fail_msgs.append(f"速查表多 {len(extra)}：{' '.join(sorted(extra)[:5])}")
    # 速查表落位列 vs 分片归属
    for e in manifest["entries"]:
        if e["kind"] == "entry" and e["id"] in quick_block and quick_block[e["id"]] != e["block"]:
            fail_msgs.append(f"{e['id']} 速查表落位 {quick_block[e['id']]} ≠ 分片 {e['block']}")

    # 视图二：主题覆盖
    theme_ids = {}
    for m in RE_THEME.finditer(lib):
        theme_ids[m.group(1)] = set(re.findall(r"\bD-\d{3}\b", m.group(2)))
    for t, ids in theme_ids.items():
        unknown = ids - quick_ids
        if unknown:
            fail_msgs.append(f"视图二 {t} 含速查表外条目：{' '.join(sorted(unknown)[:4])}")

    if not fail_msgs:
        ok_msgs.append(f"10 格逐格核对通过，合计 {total_entries}，"
                       f"速查表 {len(quick_rows)} 行 / 头部计数 {head_count}，双向无孤儿")
    return {"fail": fail_msgs, "ok": "；".join(ok_msgs)}


# ───────────────────────────── 遥测（阶段1 · K3 落地） ─────────────────────────────

def load_telemetry(root: Path) -> dict | None:
    p = root / TELEMETRY_REL
    if not p.is_file():
        return None
    try:
        return json.loads(read_text(p))
    except (ValueError, OSError):
        return None


def tick(root: Path, eid: str) -> None:
    """命中计数 +1（机器写回，**同会话幂等**）。

    为什么把「存活度」落到这里：项目自己的 L9 判定——**设计期全 ✓ 不能证明活得下去**。
    而 147 条 D 此前**零命中计数**，无法回答「这条到底有没有用」。本函数让
    `knowledge get` 成为唯一可信的命中信号（**取正文才算命中**；search 只返候选、不算）。

    幂等怎么做的：会话 id 取自环境变量 `SD_KNOWLEDGE_SESSION`（未设则不幂等，每次都 +1）。
    同一会话内重复取同一条 → 只计一次。理由：一次设计任务里反复 `get D-133` 是
    「同一次使用」，计 N 次会把「使用率」变成「调用频率」，指标会失真。
    """
    import datetime
    tel = load_telemetry(root) or {"schemaVersion": SCHEMA_VERSION, "entries": {}}
    tel.setdefault("entries", {})
    rec = tel["entries"].setdefault(eid, {"hits": 0, "lastHit": None, "lastSession": None})
    session = os.environ.get("SD_KNOWLEDGE_SESSION", "")
    if session and rec.get("lastSession") == session:
        return                                     # 同会话已计过 → 幂等跳过
    rec["hits"] = int(rec.get("hits", 0)) + 1
    rec["lastHit"] = datetime.datetime.now().replace(microsecond=0).isoformat()
    rec["lastSession"] = session or None
    tel["libraryVersion"] = (load_manifest(root) or {}).get("libraryVersion", "")
    p = root / TELEMETRY_REL
    p.parent.mkdir(parents=True, exist_ok=True)
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(tel, ensure_ascii=False, indent=1) + "\n")


# ───────────────────────────── 后端路由（阶段1 · pay skill 衔接位） ─────────────────────────────

def resolve_backend(root: Path, mode: str):
    """→ (backend, fallback_backend)。失败时抛 RemoteNotConfigured，由调用方转 E014。

    **熔断语义（DP-210）**：`remote` 模式**绝不**静默回落本地；`auto` 模式才回落，
    且回落时**必须打印告警**——否则远程长期故障而用户浑然不觉（"看起来成功"最危险）。
    """
    from knowledge_remote import (make_backend, RemoteNotConfigured,  # 延迟导入，避免循环
                                RemoteVersionTooOld)
    m = mode or "local"
    if m == "local":
        return LocalBackend(root), None
    return make_backend(root, m)               # remote / auto


def _warn_fallback(mode: str, err: Exception) -> None:
    warn(f"[{mode}] 远程增强服务不可用（{type(err).__name__}）→ 已回落本地同版本索引；"
         f"本地缺失的条目会熔断报缺口，**不会**用模型记忆补。", script="knowledge")


# ───────────────────────────── CLI 动作 ─────────────────────────────

def render_compact(mf: dict) -> str:
    """紧凑索引（上下文件）：只留 id / 格 / 主题 / 标题，markdown 表形态。

    **为什么必须与机器 manifest 分开**（实测数据，见 outputs/arch-refactor-20260911/）：
      机器 manifest（含 hash/source/anchor/abstract）176 条 = 109 KB ≈ 50 K token
      ——那是「校验件」，**绝不能进上下文**；
      本紧凑索引 176 条 = 11.7 KB ≈ 4.5 K token —— 这才是可给 agent 看的「上下文件」。
    这正是 DP-207「有限资源分层承载：一等放规则，二等放实例，第三层留可跑断言」在
    知识库自身上的落地；也只是「一等」——**默认不常驻**，按需 `search` 取相关切片更省。
    """
    lines = [f"<!-- 知识库紧凑索引 · {mf['libraryVersion']} · {mf['total']} 条"
             f"（D {mf['counts'].get('entry', 0)} / DP {mf['counts'].get('principle', 0)}"
             f" / L {mf['counts'].get('lesson', 0)}）· 由 knowledge.py 生成，勿手改 -->",
             "",
             "| ID | 格 | 主题 | 标题 |",
             "|---|---|---|---|"]
    for e in mf["entries"]:
        lines.append(f"| {e['id']} | {e['block'] or '-'} | {'/'.join(e['themes']) or '-'} | {e['title']} |")
    return "\n".join(lines) + "\n"


def cmd_index(root: Path, write: bool, as_json: bool, compact: bool, out: str,
              mode: str = "local") -> int:
    mf = None
    if mode in ("remote", "auto"):
        from knowledge_remote import RemoteNotConfigured, RemoteUnavailable, RemoteVersionTooOld
        try:
            b, _ = resolve_backend(root, mode)
            if b.__class__.__name__ == "RemoteBackend":
                mf = b.index()
                print(f"（来源：远程增强服务 · {mf.get('libraryVersion', '?')}）")
        except RemoteNotConfigured as err:
            if mode == "remote":
                return fail("E014", detail=str(err), script="knowledge")
        except RemoteVersionTooOld as err:
            if mode == "remote":
                return fail("E016", detail=str(err), script="knowledge")
        except RemoteUnavailable as err:
            if mode == "remote":
                return fail("E014", detail=str(err), script="knowledge")
            warn(f"[auto] 远程索引不可用（{type(err).__name__}）→ 回落本地重建", script="knowledge")
    if mf is None:
        mf = build_manifest(root)
    if write:
        p = manifest_path(root)
        p.parent.mkdir(parents=True, exist_ok=True)
        with io.open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(mf, ensure_ascii=False, indent=2) + "\n")
        print(f"✅ 已写入 {p.relative_to(root)}（{mf['total']} 条 / {mf['libraryVersion']}）")
    if out:
        p = Path(out)
        p.parent.mkdir(parents=True, exist_ok=True)
        with io.open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(render_compact(mf))
        print(f"✅ 已写入紧凑索引 {p}（{len(render_compact(mf).encode('utf-8'))/1024:.1f} KB）")
    if compact:
        print(render_compact(mf), end="")
        return 0
    if as_json:
        print(json.dumps(mf, ensure_ascii=False, indent=2))
    elif not write:
        c = mf["counts"]
        print(f"{mf['libraryVersion']}  合计 {mf['total']} 条"
              f"（做法 D {c.get('entry', 0)} / 设计观 DP {c.get('principle', 0)} / 教训 L {c.get('lesson', 0)}）")
        for b in BLOCK_IDS:
            print(f"  {b} {BLOCK_NAMES[b]:<4} {mf['blocks'][b]:>3} 条")
    return 0


def cmd_get(root: Path, eid: str, fmt: str, mode: str = "local", no_tick: bool = False) -> int:
    """取正文。命中即计数（遥测）——**只有真取了正文才算命中**。"""
    from knowledge_remote import (PayRequired, RemoteNotConfigured, RemoteUnavailable,
                                  RemoteVersionTooOld,
                                  RemoteIntegrityError, pay_hook)
    try:
        b, fb = resolve_backend(root, mode)
    except RemoteNotConfigured as err:
        return fail("E014", detail=str(err), script="knowledge")
    except RemoteVersionTooOld as err:
        return fail("E016", detail=str(err), script="knowledge")

    item = None
    try:
        item = b.get(eid)
    except PayRequired as pr:
        # **衔接位**：不自行支付（计费改造由 skill-paid 单独做）；钩子未接管 → 熔断
        if pay_hook(pr.eid, pr.payment_code, pr.out_trade_no) == 0:
            item = b.retry_get(eid, pr.out_trade_no)
        else:
            return fail("E014", detail=f"{eid} 在远程付费层且尚未授权", script="knowledge")
    except (RemoteUnavailable, RemoteIntegrityError) as err:
        if fb is None:
            return fail("E014", detail=f"{type(err).__name__}: {err}", script="knowledge")
        _warn_fallback(mode, err)
        item = fb.get(eid)

    if not item:
        return fail("E001", detail=f"知识条目 {eid} 不存在于权威源", script="knowledge")
    if not no_tick and item.get("source") != "remote":
        tick(root, item["id"])
    if fmt == "json":
        print(json.dumps(item, ensure_ascii=False, indent=2))
    else:
        print(f"# {item['id']} · {item['title']}\n"
              f"<!-- kind={item['kind']} block={item['block'] or '-'} "
              f"version={item['version']} hash={item['hash']} source={item.get('source', 'local')} -->\n")
        print(item["body"])
    return 0


def cmd_search(root: Path, args, mode: str = "local") -> int:
    from knowledge_remote import (RemoteNotConfigured, RemoteUnavailable,
                                  RemoteIntegrityError, RemoteVersionTooOld)
    try:
        b, fb = resolve_backend(root, mode)
    except RemoteNotConfigured as err:
        return fail("E014", detail=str(err), script="knowledge")
    except RemoteVersionTooOld as err:
        return fail("E016", detail=str(err), script="knowledge")
    try:
        hits = b.search(block=args.block, theme=args.theme, tag=args.tag,
                        text=args.text, limit=args.limit)
    except (RemoteUnavailable, RemoteIntegrityError) as err:
        if fb is None:
            return fail("E014", detail=f"{type(err).__name__}: {err}", script="knowledge")
        _warn_fallback(mode, err)
        hits = fb.search(block=args.block, theme=args.theme, tag=args.tag,
                         text=args.text, limit=args.limit)
    if args.json or not hits:
        print(json.dumps({"ids": [h["id"] for h in hits], "hits": hits,
                          "total": len(hits)}, ensure_ascii=False, indent=2))
    elif args.ids_only:
        print(" ".join(h["id"] for h in hits))
    else:
        print(f"命中 {len(hits)} 条（只返轻量元数据，正文用 `knowledge get <ID>` 取）：")
        for h in hits:
            print(f"  {h['id']:<8} [{h.get('block') or '--'}] {h['title']}")
            if h.get("abstract"):
                print(f"           {h['abstract']}")
    return 0


def cmd_verify(root: Path, strict: bool, as_json: bool, mode: str = "local") -> int:
    from knowledge_remote import RemoteNotConfigured, RemoteUnavailable, RemoteVersionTooOld
    if mode in ("remote", "auto"):
        try:
            b, _ = resolve_backend(root, mode)
            if hasattr(b, "verify") and b.__class__.__name__ == "RemoteBackend":
                rep = b.verify(strict=strict)
                print(json.dumps(rep, ensure_ascii=False, indent=2) if as_json else f"远程核对：{rep}")
                return 0
        except RemoteNotConfigured:
            if mode == "remote":
                return fail("E014", detail="远程未配置，无法远程核对", script="knowledge")
        except RemoteVersionTooOld as err:
            if mode == "remote":
                return fail("E016", detail=str(err), script="knowledge")
        except RemoteUnavailable as err:
            if mode == "remote":
                return fail("E014", detail=str(err), script="knowledge")
            warn(f"[auto] 远程核对不可用（{type(err).__name__}）→ 回落本地核对", script="knowledge")
    b = LocalBackend(root)
    rep = b.verify(strict=strict)
    if as_json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
    else:
        print("知识库完整性核对（ADR-001 契约④ · I2 不变量）")
        for name, ok, detail in rep["checks"]:
            print(f"  {'✅' if ok else '❌'} {name}：{detail}")
        for s in rep["soft"]:
            print(f"  ⚠️  {s}")
        for h in rep["hard"]:
            print(f"  ❌ {h}")
        if not rep["hard"] and not rep["soft"]:
            print("  → 全绿：索引与权威源一致，编号空间完整，条目库视图自洽")
    if rep["hard"]:
        code = "E013" if any("E013" in x for x in rep["hard"]) else (
            "E009" if any("E009" in x for x in rep["hard"]) else "E008")
        return fail(code, detail="见上方逐项报告", script="knowledge")
    return 2 if rep["soft"] else 0


def cmd_stats(root: Path, dead_after: int, as_json: bool, tiers: bool = False) -> int:
    if tiers:
        p = root / "library" / "tier_policy.json"
        if not p.is_file():
            return fail("E001", detail="library/tier_policy.json 缺失", script="knowledge")
        tp = json.loads(read_text(p))
        mf = load_manifest(root)
        if as_json:
            print(json.dumps({"tierPolicy": tp, "totalEntries": (mf or {}).get("total")},
                             ensure_ascii=False, indent=2))
            return 0
        print(f"免费 / 付费分层（策略源：library/tier_policy.json · 冻结基线 {tp.get('frozenBaseline')}）")
        for key in ("free", "paid"):
            t = tp["tiers"][key]
            print(f"\n  【{key.upper()}】{t['name']}")
            print(f"    规则：{t['rule']}")
            for i in t["includes"]:
                print(f"      · {i}")
        print(f"\n  不可收回的存量（neverPaid）：")
        for i in tp["entryTierRule"]["neverPaid"]:
            print(f"      · {i}")
        print(f"\n  防缩水判据：{tp['reductionBan']['rule']}")
        if mf:
            print(f"  当前条目总数（免费层基线）：{mf['total']} 条 · {mf['libraryVersion']}")
        return 0

    mf = load_manifest(root)
    if mf is None:
        return fail("E008", detail="manifest 缺失", script="knowledge")
    tel = load_telemetry(root)
    entries = mf["entries"]
    # 注意：遥测是**嵌套**结构 {"entries": {id: {hits, lastHit, lastSession}}}，
    # 不是扁平的 {id: {...}}——阶段0 的占位实现按扁平读过，若不改会让"存活度"永远显示
    # 全部条目零命中（把有命中的也说成死的，属"看起来正常"的错误输出）。
    recs = (tel or {}).get("entries", {})
    zero = [e["id"] for e in entries if not recs.get(e["id"], {}).get("hits")]
    out = {
        "libraryVersion": mf["libraryVersion"],
        "counts": mf["counts"],
        "blocks": mf["blocks"],
        "telemetry": "enabled" if tel is not None else "disabled",
        "zeroHit": len(zero),
        "zeroHitIds": zero,
    }
    if as_json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0
    c = mf["counts"]
    print(f"{mf['libraryVersion']}  合计 {mf['total']} 条"
          f"（D {c.get('entry', 0)} / DP {c.get('principle', 0)} / L {c.get('lesson', 0)}）")
    for b in BLOCK_IDS:
        print(f"  {b} {BLOCK_NAMES[b]:<4} {mf['blocks'][b]:>3} 条")
    if tel is None:
        # 诚实性硬约束：没有遥测就说没有，绝不用 hits=0 冒充「死条目」
        print(f"\n⚠️  命中遥测未启用（阶段1 · K3 落地后可用）：{TELEMETRY_REL}"
              " 不存在 → **无法判定死条目**，不输出 --dead-after 清单。")
        print("    当前可用的近邻证据：lessons 自带引用计数（机器写回，见 lessons.md）——"
              f"12 条中 {sum(1 for e in entries if e['kind'] == 'lesson' and e.get('refs', 0) == 0)} 条为 0 次引用。")
        return 2
    dead = zero          # 与 zeroHitIds 同一定义（同一事实只算一次，DP-204）
    hit = len(entries) - len(dead)
    print(f"\n存活度：{hit} 条有命中 / {len(dead)} 条零命中（共 {len(entries)} 条）")
    print(f"  判据：`knowledge get <ID>` 自动计数（**取正文才算命中**；search 只返候选不计，"
          f"同会话幂等）。规则：连续 {dead_after} 个设计任务未命中 → 移入归档区。")
    print(f"  零命中前 40 条：")
    for i in dead[:40]:
        print(f"    {i}")
    if len(dead) > 40:
        print(f"    …（其余 {len(dead) - 40} 条略）")
    return 0


# ───────────────────── 契约层反向测试（L11：验收要固化成一条命令） ─────────────────────

def _stage_sandbox(sb: Path, _shutil) -> None:
    """把「跑得起来的一套最小仓库」拷进临时目录（临时目录而非 outputs/ 夹具，见 §9.1）。"""
    (sb / "references" / "blocks").mkdir(parents=True, exist_ok=True)
    (sb / "scripts").mkdir(parents=True, exist_ok=True)
    for f in (self_root / RE_SHARD).glob("*.md"):
        _shutil.copy2(f, sb / RE_SHARD / f.name)
    for rel in (LIBRARY_REL, PRINCIPLES_REL, LESSONS_REL):
        _shutil.copy2(self_root / rel, sb / rel)
    for f in (self_root / "scripts").glob("*.py"):
        _shutil.copy2(f, sb / "scripts" / f.name)
    # ⚠ library/ 必须一起带进沙箱（v3.18.0 修）：C5 要拿权威源回核生成物。
    # 漏了它 → 基线自带 E013 ⇒ 五个坏样本全部「没被拦住」，反向测试变成永远红。
    # 这正是 L11 的活例：**检查项新增后没回扫既有夹具**，红的是夹具不是被测对象。
    # （staging/ 是开发态隔离区，不带。）
    for f in (self_root / "config.json",):
        if f.is_file():
            _shutil.copy2(f, sb / f.name)
    libsrc = self_root / "library"
    if libsrc.is_dir():
        for f in libsrc.rglob("*"):
            if f.is_file() and "staging" not in f.relative_to(libsrc).parts \
                    and "__pycache__" not in f.parts:
                dst = sb / "library" / f.relative_to(libsrc)
                dst.parent.mkdir(parents=True, exist_ok=True)
                _shutil.copy2(f, dst)


def _selftest_case(name: str, mutate, expect_code: str, reindex: bool = False) -> dict:
    """在**临时目录**里构造坏样本并跑 verify。

    为什么用临时目录而不是 outputs/_fixture_*/：那个约定正是 ADR-001 §9.1
    指出的问题源（outputs/ 已堆 6 个遗留夹具，与"产物范围门禁 D-146"相悖）。
    契约层夹具**包含在一条命令里**，不需要在仓库里留下任何痕迹。

    reindex=True 的含义：构造完成后**先重建索引再验**——用来把「索引过期」
    （E009）这一噪音源排除掉，从而**单独隔离**出要测的那条不变量。
    不这么做，E009 会先亮并掩盖掉真正的信号（反向测试第一版就在此踩坑：
    删末尾条目想测 E010，实际只报 E009，因为"末尾被删"根本形不成内部缺号）。
    """
    import shutil as _shutil
    import subprocess as _sp
    import tempfile as _tf

    with _tf.TemporaryDirectory(prefix="sd_kfix_") as td:
        sb = Path(td)
        _stage_sandbox(sb, _shutil)

        def _kb(*cmd):
            return _sp.run([sys.executable, str(sb / "scripts" / "knowledge.py"), *cmd],
                           cwd=sb, capture_output=True, text=True, encoding="utf-8")

        def _verify():
            p = _kb("verify")
            return p.returncode, (p.stdout or "") + (p.stderr or "")

        _kb("index", "--write")
        rc0, _ = _verify()
        try:
            mutate(sb)
        except Exception as e:                      # 夹具自身失效要显式暴露，不静默
            return {"case": name, "baseline_clean": rc0 == 0, "exit": None,
                    "expected": expect_code, "code_found": False, "pass": False,
                    "snippet": [f"夹具构造失败：{e}"]}
        if reindex:
            _kb("index", "--write")
        rc, out = _verify()
        return {"case": name, "baseline_clean": rc0 == 0, "exit": rc,
                "expected": expect_code, "code_found": expect_code in out,
                "pass": rc0 == 0 and rc != 0 and (expect_code in out),
                "snippet": [l for l in out.splitlines() if l.strip()][-5:]}


def _selftest_backend_case(name: str, setup, argv: list, expect: str, must_fail: bool) -> dict:
    """在临时仓库里跑一条**指定后端**的 knowledge 命令，验远程衔接语义。

    为什么这组必须有：阶段1 新增的三条远程语义（未配置→熔断 / auto→回落 / 版本协商→熔断）
    若无人验证，就只是三行注释——L11「实现完 ≠ 会生效」的同款。且**正向也要验**：
    `auto` 未配置时必须**成功**（免费层正常路径），把它写成失败会是另一个方向的错。
    """
    import os as _os
    import shutil as _shutil
    import subprocess as _sp
    import tempfile as _tf

    with _tf.TemporaryDirectory(prefix="sd_kbe_") as td:
        sb = Path(td)
        _stage_sandbox(sb, _shutil)
        extra_env: dict = {}
        if setup:
            try:
                # setup 可返回额外环境变量（如给 remote 模式一个地址）。
                # **不改 os.environ**：改全局会污染后续用例，让"第 N 个案例莫名绿/红"。
                extra_env = setup(sb) or {}
            except Exception as e:                  # 夹具自身失效要显式暴露，不静默
                return {"case": name, "expected": expect, "exit": None, "must_fail": must_fail,
                        "pass": False, "snippet": [f"夹具构造失败：{e}"]}
        env = dict(_os.environ)
        for k in ("KNOWLEDGE_REMOTE_URL", "KNOWLEDGE_REMOTE_TOKEN"):
            env.pop(k, None)                        # 隔离宿主环境，保证「未配置」是真未配置
        env.update(extra_env)
        p = _sp.run([sys.executable, str(sb / "scripts" / "knowledge.py"), *argv],
                    cwd=sb, capture_output=True, text=True, encoding="utf-8", env=env)
        out = (p.stdout or "") + (p.stderr or "")
        ok = (p.returncode != 0) == must_fail and (expect in out)
        return {"case": name, "expected": expect, "exit": p.returncode, "must_fail": must_fail,
                "pass": ok, "snippet": [l for l in out.splitlines() if l.strip()][-4:]}


def _m_flow_too_new(sb: Path) -> dict:
    """把远程要求的最低流程版本抬到远超本地 → 触发版本协商熔断。

    同时给一个**必然不可达**的服务地址：这样才走得到「协商」那一步
    （否则 RemoteBackend 先因未配置报 E014，测的就不是协商了）。
    地址用 `127.0.0.1:9`（discard 端口，必然拒连）——不会真的联网。
    """
    p = sb / "library" / "remote_config.json"
    cfg = json.loads(p.read_text(encoding="utf-8"))
    cfg.setdefault("versionNegotiation", {})["minFlowVersion"] = "99.0.0"
    p.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"KNOWLEDGE_REMOTE_URL": "http://127.0.0.1:9/__never__"}


def _m_missing(sb: Path):
    (sb / MANIFEST_REL).unlink()


def _m_tamper(sb: Path):
    """只改**标题行**、不动正文 → 专门检验指纹比对（只比正文 hash 会漏掉它）。"""
    f = sb / RE_SHARD / "design-blocks-b07.md"
    t = read_text(f).replace("### D-065 ·", "### D-065 · TAMPERED ", 1)
    io.open(f, "w", encoding="utf-8", newline="\n").write(t)


def _m_gap(sb: Path):
    """删掉**中间**一条（D-146）→ 编号空间出现内部缺号（末尾条目不构成缺号）。"""
    f = sb / RE_SHARD / "design-blocks-b10.md"
    t = read_text(f)
    t2 = re.sub(r"\n### D-146 ·[\s\S]*?(?=\n### )", "\n", t, count=1)
    if t2 == t:
        raise AssertionError("未匹配到 D-146——夹具失效（编号或分片变动后需同步）")
    io.open(f, "w", encoding="utf-8", newline="\n").write(t2)


def _m_viewdrift(sb: Path):
    """从速查表删掉一行 → 条目库四方一致性断裂。

    正则必须兼容 `**D-146**`（速查表里新条目是加粗的、老条目不是）——
    这正是本项目记录过的 grep 坑：只写 `^\\|\\s*D-\\d+\\s*\\|` 会漏掉全部加粗行。
    """
    f = sb / LIBRARY_REL
    t = read_text(f)
    t2 = re.sub(r"^\|\s*\*{0,2}D-146\*{0,2}\s*\|[^\n]*\n", "", t, count=1, flags=re.M)
    if t2 == t:
        raise AssertionError("未匹配到速查表 D-146 行——夹具失效")
    io.open(f, "w", encoding="utf-8", newline="\n").write(t2)


def _m_dangling(sb: Path):
    """把一条 DP 的支撑条目改成不存在的 D-999。"""
    f = sb / PRINCIPLES_REL
    t = read_text(f)
    t2 = t.replace("支撑条目 **D-143 D-145 D-146 D-147**", "支撑条目 **D-143 D-999 D-146 D-147**", 1)
    if t2 == t:
        raise AssertionError("未匹配到 DP-211 支撑条目行——夹具失效")
    io.open(f, "w", encoding="utf-8", newline="\n").write(t2)


def cmd_selftest(as_json: bool) -> int:
    cases = [
        ("① manifest 缺失", _m_missing, "E008", False),
        ("② 权威源被篡改（仅改标题）", _m_tamper, "E009", False),
        ("③ ID 内部缺号（已重建索引）", _m_gap, "E010", True),
        ("④ 条目库视图漂移（已重建索引）", _m_viewdrift, "E011", True),
        ("⑤ 设计观引用悬空（已重建索引）", _m_dangling, "E012", True),
    ]
    results = [_selftest_case(n, m, c, r) for n, m, c, r in cases]

    # 远程衔接语义（阶段1 措施 1.6）——四条：两条必须熔断、两条必须成功
    bcases = [
        ("⑥ 远程未配置 + remote → 熔断给动作",
         None, ["get", "D-133", "--backend", "remote"], "E014", True),
        ("⑦ 远程未配置 + auto → 静默回落本地（须成功）",
         None, ["get", "D-133", "--backend", "auto"], "D-133", False),
        ("⑧ 版本协商不过 + remote → 熔断（E016）",
         _m_flow_too_new, ["get", "D-133", "--backend", "remote"], "E016", True),
        ("⑨ 版本协商不过 + auto → 回落本地 + 告警（须成功）",
         _m_flow_too_new, ["get", "D-133", "--backend", "auto"], "版本协商未通过", False),
    ]
    for n, m, argv, exp, mf in bcases:
        results.append(_selftest_backend_case(n, m, argv, exp, mf))

    if as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0 if all(r["pass"] for r in results) else 1
    print("knowledge 契约层反向测试（坏样本必须被**分别**拦住——危险形态是静默放行，不是报错）")
    for r in results:
        kind = "应失败" if r.get("must_fail", True) else "应成功"
        print(f"  {'✅' if r['pass'] else '❌'} {r['case']:<28} 期望含「{r['expected']}」"
              f" / 退出码 {r['exit']} / {kind}")
        if not r["pass"]:
            for l in r["snippet"]:
                print(f"       | {l}")
    ok = sum(1 for r in results if r["pass"])
    if ok != len(results):
        print(f"\n❌ {len(results) - ok}/{len(results)} 个坏样本没被正确拦住——契约层存在静默放行，不可发布")
        return 1
    print(f"\n✅ {len(results)}/{len(results)} 个坏样本均被正确拦住（错误码相符）")
    return 0


# ───────────────────────────── 入口 ─────────────────────────────

def find_root() -> Path:
    return Path(__file__).resolve().parent.parent


self_root = find_root()   # 供 selftest 定位权威源（其余动作走显式 root）


def main(argv=None) -> int:
    enable_utf8()
    ap = argparse.ArgumentParser(
        description="知识库统一门面（ADR-001 阶段0 · local 后端）：ID/manifest/检索/完整性 四件契约",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=None, help="skill-designer 根目录（默认自动推断）")
    sub = ap.add_subparsers(dest="action", required=True)

    p = sub.add_parser("index", help="重建条目粒度索引（派生，可随时重跑）")
    p.add_argument("--write", action="store_true", help="写入 scripts/library_manifest.json（机器件，含 hash）")
    p.add_argument("--compact", action="store_true", help="输出紧凑索引（上下文件，id/格/主题/标题）")
    p.add_argument("--out", default="", help="把紧凑索引落盘到指定路径（一般不必，按需 search 更省）")
    p.add_argument("--json", action="store_true", help="输出完整 manifest")
    p.add_argument("--backend", choices=("local", "remote", "auto"), default="",
                   help="知识后端：local（默认）/ remote（远程增强服务）/ auto（远程优先+本地兜底）")

    p = sub.add_parser("get", help="按 ID 取条目正文（从权威源实时切片，不落第二份）")
    p.add_argument("eid", help="条目 ID，如 D-133 / DP-209 / L12")
    p.add_argument("--format", choices=("md", "json"), default="md")
    p.add_argument("--no-tick", action="store_true", dest="no_tick",
                   help="不计入命中遥测（机器批量调用时用，避免把调用频率误当使用率）")
    p.add_argument("--backend", choices=("local", "remote", "auto"), default="")

    p = sub.add_parser("search", help="检索条目（只返轻量元数据，不返正文）")
    p.add_argument("--block", help="按积木格过滤，如 B07")
    p.add_argument("--theme", help="按主题过滤，如 T4")
    p.add_argument("--tag", help="按标签过滤（子串匹配）")
    p.add_argument("--text", help="全文关键词（空格=AND）")
    p.add_argument("--limit", type=int, default=5, help="最多返回条数（默认 5）")
    p.add_argument("--ids-only", action="store_true", help="机器消费：只输出 ID 空格分隔")
    p.add_argument("--json", action="store_true")
    p.add_argument("--backend", choices=("local", "remote", "auto"), default="")

    p = sub.add_parser("verify", help="完整性核对（索引↔权威源 / ID 编号 / 视图一致性）")
    p.add_argument("--strict", action="store_true", help="警告升级为失败")
    p.add_argument("--json", action="store_true")
    p.add_argument("--backend", choices=("local", "remote", "auto"), default="")

    p = sub.add_parser("stats", help="知识库统计与存活度（遥测未启用时如实说明）")
    p.add_argument("--dead-after", type=int, default=10, dest="dead_after")
    p.add_argument("--tiers", action="store_true", help="显示免费/付费分层策略与其机器判据")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("selftest", help="契约层反向测试：三种坏样本是否被分别拦住（改判据后必跑）")
    p.add_argument("--json", action="store_true")

    args = ap.parse_args(argv)
    root = Path(args.root).resolve() if args.root else find_root()

    if args.action == "index":
        return cmd_index(root, args.write, args.json, args.compact, args.out,
                         mode=getattr(args, "backend", ""))
    if args.action == "get":
        return cmd_get(root, args.eid, args.format, mode=getattr(args, "backend", ""),
                       no_tick=getattr(args, "no_tick", False))
    if args.action == "search":
        return cmd_search(root, args, mode=getattr(args, "backend", ""))
    if args.action == "verify":
        return cmd_verify(root, args.strict, args.json, mode=getattr(args, "backend", ""))
    if args.action == "stats":
        return cmd_stats(root, args.dead_after, args.json, tiers=getattr(args, "tiers", False))
    if args.action == "selftest":
        return cmd_selftest(args.json)
    return fail("E005", detail=f"未知动作 {args.action}", script="knowledge")


if __name__ == "__main__":
    sys.exit(main())
