#!/usr/bin/env python3
"""
absorb_intake.py — 吸收流水线 S0–S3（ADR-001 §6.2 / §7 措施 1.4）

定位
   把上游 skill-rebuild 产出的吸收切片（absorbed.json）**安全地**并入权威源。
   本文件属**开发态**（低频、可能失败重试、要人拍板），与运行态的设计流程
   物理隔离（ADR-001 §6.3 K1：**运行态不得依赖开发态**）——设计流程一次都不调用它。

四段流水线
   S0 采集  三查门禁 → 候选落 library/staging/<slug>/（与权威库物理隔离，不合规**打回不代填**）
   S1 归并  dedup_index 查重 → 命中即不收；同一 (格,主题) 同源单点 ≥3 条 → 提示升维为 DP
   S2 编译  compile_library --write（扫描器 fail-closed）+ knowledge index --write
   S3 发布  knowledge verify + 台账（新增 ID 清单 / 处置统计）

用法
   python scripts/absorb_intake.py --from <absorbed.json>            # 只出裁决表，不落盘（默认）
   python scripts/absorb_intake.py --from <absorbed.json> --stage    # 跑到 S0：候选入 staging/
   python scripts/absorb_intake.py --from <absorbed.json> --commit   # S1–S3：并入权威源并编译
   python scripts/absorb_intake.py --replay <absorbed.json>          # 重放测试（只读，验收 1.4）
   python scripts/absorb_intake.py --check-dedup                     # 登记册健康 + 全样本登记覆盖率
   python scripts/absorb_intake.py --self-test                       # 反向测试：坏样本必须被拦住

退出码
   0 = 成功；1 = 业务失败（有打回 / 无候选 / 重放不一致）；2 = 仅警告；3 = 门禁拦截（fail-closed）

为什么「打回不代填」是 P0
   intake 若替上游补全缺失字段，就等于把「证据不足」洗成「证据齐备」——下游再也看不出
   这条知识的证据其实是编的。宁要诚实的不收，不要伪造的收录。
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from errors import enable_utf8  # noqa: E402
from knowledge import BLOCK_IDS, read_text  # noqa: E402

enable_utf8()

LIB_REL = Path("library")
STAGING_REL = LIB_REL / "staging"
DEDUP_REL = LIB_REL / "dedup_index.json"
ENTRIES_REL = LIB_REL / "entries.json"
SAMPLES_REL = Path("example") / "design-blocks"

# S0 三查①的「四要素」——与上游 absorb_export.py 的 REQUIRED 同代（DP-204 单一事实源：
# 这里是**消费侧**副本，改动须两侧同步；已在 --check-dedup 里做一致性告警）
REQUIRED = ("name", "block", "trigger", "evidence", "point")

VERDICT_ENUM = ("already-covered", "applied-not-new", "out-of-scope", "over-engineering")
VERDICT_ZH = {
    "already-covered": "已收录",
    "applied-not-new": "属应用非新机制",
    "out-of-scope": "场景不相关",
    "over-engineering": "过度设计",
}

# S0 三查③：证据可溯源 = 正文里出现**可定位锚点**。
# 必须同时认两种真实形态（实测踩过：只认反引号会把 15/15 全部误判成「无可溯源证据」）：
#   ① 反引号包裹：`` `tencent-news/SKILL.md:39-46` ``（库内条目的写法）
#   ② 裸路径：`tencent-news/SKILL.md:39-46`（吸收切片的写法——切片是压缩表达，更少格式化）
# 行号形态也要认全：`:39-46` / `:81,87` / `:81` / 无行号。
RE_EXT = r"(?:md|py|sh|ps1|json|html?|js|ts|tsx|svg|ya?ml|toml|cfg|ini|txt)"
RE_BACKTICK = re.compile(r"`([^`\n]{1,120})`")
RE_PATHISH = re.compile(rf"^[\w./\\-]+\.{RE_EXT}(?::\d+(?:[-–,]\d+)*)?$", re.I)
RE_BARE = re.compile(rf"[\w][\w./\\-]*\.{RE_EXT}(?::\d+(?:[-–,]\d+)*)?", re.I)

# 从库内条目 body 抽「- **字段**：值」
RE_FIELD = re.compile(r"^-\s*\*\*([^*\n]+)\*\*\s*[：:]\s*(.*)$", re.M)


# ───────────────────────────── 通用 ─────────────────────────────

def field_of(body: str, key: str) -> str:
    for k, v in RE_FIELD.findall(body):
        if k.strip() == key:
            return v.strip()
    return ""


def _norm_path(s: str) -> str:
    """锚点归一到「路径本身」：去行号、统一分隔符与小写。

    为什么不把行号纳入比较：吸收切片与入库条目对同一证据的行号写法会不同
    （切片 `:81` + `L87`，库内合并成 `:81,87`），把行号当判据会产生大量假不一致。
    行号仍是可读的定位信息，只是**不参与机器等价判定**。
    """
    return s.split(":")[0].replace("\\", "/").strip().lower()


def anchors_of(text: str) -> set[str]:
    """抽出文本里的可定位锚点（归一化为路径）。同时认反引号形态与裸路径形态。"""
    out: set[str] = set()
    t = text or ""
    for span in RE_BACKTICK.findall(t):
        s = span.strip()
        if RE_PATHISH.match(s):
            out.add(_norm_path(s))
    for m in RE_BARE.finditer(t):
        out.add(_norm_path(m.group(0)))
    return {a for a in out if a}


def fingerprint(text: str) -> str:
    """能力指纹：去空白 / 去标点后的字符集合，用于查重的粗匹配兜底。"""
    return re.sub(r"[\s\W_]+", "", (text or "").lower())


def load_json(path: Path):
    return json.loads(read_text(path))


def load_dedup(root: Path) -> dict:
    p = root / DEDUP_REL
    if not p.is_file():
        raise SystemExit(f"❌ 登记册缺失：{p}（吸收查重没有它就只能靠人读文档，K1 不成立）")
    try:
        return load_json(p)
    except (ValueError, OSError) as e:
        raise SystemExit(f"❌ dedup_index.json 不可解析：{type(e).__name__}: {e}")


def library_ids(root: Path) -> dict[str, dict]:
    """**全编号空间**（D-NNN + DP-NNN + L-N）→ 条目。

    ⚠ 这里踩过一次真坑：初版只读 `entries.json`，于是重放测试把已入库的
    DP-209/210/211 报成「不在库」（0/3）——查重表少了编号空间，错误方向还是
    「谎报缺失」。吸收切片可以带三类 ID，索引就必须覆盖三类（DP-209 权威源唯一化）。
    """
    out: dict[str, dict] = {}
    for f in ("entries.json", "principles.json", "lessons.json"):
        p = root / LIB_REL / f
        if not p.is_file():
            continue
        for e in load_json(p)["entries"]:
            out[e["id"]] = e
    return out


# ───────────────────────────── S0 采集（三查门禁） ─────────────────────────────

def s0_intake(absorbed: dict) -> tuple[list[dict], list[dict]]:
    """三查门禁 → (候选, 打回)。**打回只给理由，不代填任何字段。**"""
    cands: list[dict] = []
    rejects: list[dict] = []
    for i, h in enumerate(absorbed.get("highlights", [])):
        raw_id = str(h.get("id", "")).strip()
        why: list[str] = []
        # 查① 四要素齐全
        for k in REQUIRED:
            if not str(h.get(k, "")).strip():
                why.append(f"缺必填字段 {k}")
        # 查② block ∈ B01–B10
        if h.get("block") not in BLOCK_IDS:
            why.append(f"block 非法：{h.get('block')!r}（应为 B01–B10）")
        # 查③ 证据可溯源（必须有可定位锚点，不接受「据观察」这类无锚点证据）
        if not anchors_of(str(h.get("evidence", ""))):
            why.append("证据无可定位锚点（反引号路径[.ext][:行]），无法溯源")
        if not raw_id:
            why.append("缺 id（ID 由人拍板，不机器分配）")
        if why:
            rejects.append({"index": i, "id": raw_id or f"<#{i}>",
                            "name": str(h.get("name", ""))[:60],
                            "stage": "S0", "reason": "；".join(why)})
            continue
        cands.append({
            "id": raw_id, "block": h["block"], "theme": h.get("theme", ""),
            "title": h["name"], "trigger": h["trigger"], "evidence": h["evidence"],
            "point": h["point"], "bypass": h.get("bypass", ""),
            "anchors": sorted(anchors_of(h["evidence"])),
        })
    return cands, rejects


def s0_stage(root: Path, absorbed: dict, cands: list[dict], rejects: list[dict]) -> Path:
    """把候选落进 library/staging/<slug>/（**物理隔离**：编译器不读它，权威库不受污染）。"""
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", str(absorbed.get("skill", "unknown"))).strip("-") or "unknown"
    d = root / STAGING_REL / slug
    d.mkdir(parents=True, exist_ok=True)
    payload = {
        "skill": absorbed.get("skill", ""), "source": absorbed.get("source", ""),
        "sampledAt": absorbed.get("sampledAt", ""), "modes": absorbed.get("modes", ""),
        "stagedAt": today(), "candidates": cands, "rejects": rejects,
    }
    (d / "candidates.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return d


def today() -> str:
    import datetime
    return datetime.date.today().isoformat()


# ───────────────────────────── S1 归并（查重 + 升维） ─────────────────────────────

def match_signatures(text: str, signatures: list[dict]) -> list[dict]:
    low = (text or "").lower()
    hits = []
    for s in signatures:
        for sig in s.get("signals", []):
            if sig and str(sig).lower() in low:
                hits.append(s)
                break
    return hits


def s1_merge(cands: list[dict], dedup: dict, lib: dict[str, dict]) -> list[dict]:
    """逐条裁决：dedup 命中 / 已在库 / 待收录。"""
    sigs = dedup.get("signatures", [])
    verdicts: list[dict] = []
    for c in cands:
        text = f"{c['title']}\n{c.get('trigger','')}\n{c.get('point','')}"
        hits = match_signatures(text, sigs)
        if c["id"] in lib:
            verdicts.append({"id": c["id"], "verdict": "already-in-library",
                             "detail": f"库中已有同 ID（{lib[c['id']]['title'][:36]}）→ 不收，勿重复收录",
                             "equivalent": [c["id"]], "signatureKeys": []})
            continue
        if hits:
            eq = sorted({i for h in hits for i in h.get("equivalent", [])})
            verdicts.append({
                "id": c["id"], "verdict": "dedup-hit",
                "detail": "命中登记册：" + " / ".join(h["label"] for h in hits),
                "equivalent": eq, "signatureKeys": [h["key"] for h in hits]})
            continue
        verdicts.append({"id": c["id"], "verdict": "accept",
                         "detail": "登记册未命中同类能力 → 可收录（仍需人工拍板 要点/标签/抗绕过性）",
                         "equivalent": [], "signatureKeys": []})
    return verdicts


def promotion_groups(cands: list[dict], accepted_ids: set[str]) -> list[dict]:
    """DP-204 归并判据：同一 (格, 主题) 出现 ≥3 条同源单点条目 ⇒ 应考虑升维为 DP 条目。

    为什么这是「归并」而不是「再补几条」：多项缺口若指向同一 archetype，
    散点补条目会让库越长越碎，而问题下一次仍然复发——正确动作是提炼一条设计观。
    """
    buckets: dict[tuple[str, str], list[str]] = {}
    for c in cands:
        if c["id"] not in accepted_ids:
            continue
        buckets.setdefault((c["block"], c.get("theme", "")), []).append(c["id"])
    return [{"block": b, "theme": t, "ids": ids, "suggestion": "考虑提炼为 1 条 DP 条目"}
            for (b, t), ids in sorted(buckets.items()) if len(ids) >= 3]


# ───────────────────────────── S2 编译 / S3 发布 ─────────────────────────────

def s2_compile(root: Path) -> tuple[int, str]:
    import compile_library
    rc, written, issues, _notes = compile_library.write_all(root)
    if rc != 0:
        return rc, "；".join(issues[:5])
    return 0, f"已重编译 {len(written)} 份视图"


def s3_publish(root: Path) -> tuple[int, str]:
    import knowledge
    mf = knowledge.build_manifest(root)
    knowledge.manifest_path(root).write_text(
        json.dumps(mf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    rep = knowledge.LocalBackend(root).verify()
    if rep["hard"]:
        return 1, "；".join(rep["hard"][:3])
    return 0, f"索引 {mf['total']} 条 / {mf['libraryVersion']}；verify 全绿（C0–C5）"


# ───────────────────────────── 登记册健康检查 ─────────────────────────────

def check_dedup(root: Path, verbose: bool = True) -> tuple[list[str], list[str]]:
    """→ (错误, 警告)。等价物解析不到 = 登记腐烂（对齐 i3_allowlist 的失效检测）。"""
    dedup = load_dedup(root)
    lib = library_ids(root)
    sigs = dedup.get("signatures", [])
    errors: list[str] = []
    warns: list[str] = []

    keys = [s.get("key", "") for s in sigs]
    dup = sorted({k for k in keys if keys.count(k) > 1})
    if dup:
        errors.append(f"key 重复：{' '.join(dup)}")

    for s in sigs:
        key = s.get("key", "<无 key>")
        v = s.get("verdict", "")
        if v not in VERDICT_ENUM:
            errors.append(f"{key}：verdict 非法 {v!r}（应为 {VERDICT_ENUM}）")
            continue
        if v in ("already-covered", "applied-not-new"):
            eq, refs = s.get("equivalent", []), s.get("equivalentRef", [])
            if not eq and not refs:
                errors.append(f"{key}：verdict={v} 但 equivalent/equivalentRef 全空 → 等价物无法核对")
            for i in eq:
                if i not in lib:
                    errors.append(f"{key}：等价条目 {i} 在当前库中不存在 → 登记腐烂（E015）")
            for r in refs:
                if not (root / r).is_file():
                    errors.append(f"{key}：等价文件 {r} 不存在 → 登记腐烂（E015）")
        else:
            if not str(s.get("reason", "")).strip():
                errors.append(f"{key}：verdict={v} 必须写明 reason")
        if s.get("provenance") == "reconstructed" and not str(s.get("source", "")).strip():
            warns.append(f"{key}：provenance=reconstructed 但未注明来源 → 无法审计登记依据")

    # 全样本登记覆盖率：所有 absorbed.json 的 notAbsorbed 都该在册
    unregistered: list[str] = []
    if (root / SAMPLES_REL).is_dir():
        for p in sorted((root / SAMPLES_REL).glob("*/absorbed.json")):
            try:
                data = load_json(p)
            except (ValueError, OSError):
                warns.append(f"{p.relative_to(root)} 不可解析，跳过覆盖率核对")
                continue
            for na in data.get("notAbsorbed", []):
                if not match_signatures(str(na.get("item", "")) + " " + str(na.get("reason", "")), sigs):
                    unregistered.append(f"{p.parent.name}: {na.get('item','')[:40]}")
    if unregistered:
        warns.append(f"有 {len(unregistered)} 条历史「不收」未在登记册中："
                     + "；".join(unregistered[:6]) + " → 补进 dedup_index.json")

    if verbose:
        print(f"=== 登记册健康检查（{DEDUP_REL}）===")
        print(f"  登记项 {len(sigs)} 条；等价条目引用 "
              f"{sum(len(s.get('equivalent', [])) for s in sigs)} 个 / "
              f"等价文件引用 {sum(len(s.get('equivalentRef', [])) for s in sigs)} 个")
        for e in errors:
            print(f"  ❌ {e}")
        for w in warns:
            print(f"  ⚠️  {w}")
        if not errors and not warns:
            print("  ✅ 全部登记可解析、无腐烂、历史不收项已全部在册")
    return errors, warns


# ───────────────────────────── 重放测试（验收 1.4） ─────────────────────────────

REPLAY_MACHINE_FIELDS = ("block", "theme", "title")

# 定稿期的**规范化差异**（不是内容差异）——判据沿用 compile_library.classify_diff 的思路：
# 先规范化再比，残余才算实质差异。实测来源（v3.18.0 重放，逐条查因后归纳）：
#   · 加引号/书名号：切片 `别质疑` → 库内 `『别质疑』`
#   · 枚举分隔符：切片 `A / B / C` → 库内 `ABC` 直接并列
#   · 补目录限定：切片锚点 `SKILL.md` → 库内 `tencent-news/SKILL.md`（**更精确**，不是丢失）
# 注意只归一**呈现层**字符；中英文逗号与「、」不在此列（它们可能承载真实句读差异）。
RE_NORM_STRIP = re.compile(r"[『』「」“”\"'`*（）()【】\[\]\s/／\\·|｜]+")


def norm_text(s: str) -> str:
    return RE_NORM_STRIP.sub("", s or "")


def anchor_key(path: str) -> str:
    return path.replace("\\", "/").rsplit("/", 1)[-1].lower()


def cmd_replay(root: Path, absorbed_path: Path, as_json: bool) -> int:
    """重放本轮吸收，与现有库**逐字段**比对，并如实区分「机器可重放」与「人工润色层」。

    这个分级是刻意的：吸收切片是**压缩表达**，入库条目是**改写定稿**。
    谎称「重放逐字一致」会掩盖人工润色的真实工作量；反过来，只说「不一致」又丢掉了
    真正可机器验证的那部分（id/格/主题/标题/触发信号/证据锚点）。故分两级报。
    """
    absorbed = load_json(absorbed_path)
    lib = library_ids(root)
    dedup = load_dedup(root)

    rows: list[dict] = []
    for h in absorbed.get("highlights", []):
        e = lib.get(h.get("id", ""))
        row = {"id": h.get("id", ""), "inLibrary": bool(e)}
        if not e:
            rows.append(row)
            continue
        row["block"] = h.get("block") == e["block"]
        row["theme"] = [h.get("theme", "")] == e["themes"]
        row["title"] = h.get("name", "") == e["title"]
        st, lt = str(h.get("trigger", "")), field_of(e["body"], "触发信号")
        row["triggerExact"] = st.strip() == lt.strip()
        row["triggerNorm"] = norm_text(st) == norm_text(lt)
        ea, la = anchors_of(h.get("evidence", "")), anchors_of(field_of(e["body"], "证据"))
        lb = {anchor_key(x) for x in la}
        row["anchorStrict"] = bool(ea) and ea <= la
        row["anchorBase"] = bool(ea) and all(anchor_key(x) in lb for x in ea)
        row["pointExact"] = str(h.get("point", "")).strip() == field_of(e["body"], "要点").strip()
        rows.append(row)

    pr: list[dict] = []
    for p in absorbed.get("principles", []):
        e = lib.get(p.get("id", ""))
        pr.append({"id": p.get("id", ""), "inLibrary": bool(e),
                   "explains": sorted(e.get("explains", [])) if e else [],
                   "declared": sorted(p.get("explains", []))})

    na_total = len(absorbed.get("notAbsorbed", []))
    na_reg = sum(1 for na in absorbed.get("notAbsorbed", [])
                 if match_signatures(str(na.get("item", "")) + " " + str(na.get("reason", "")),
                                     dedup.get("signatures", [])))

    n = len(rows)
    covered = sum(1 for r in rows if r["inLibrary"])
    cnt = lambda k: sum(1 for r in rows if r.get(k))  # noqa: E731
    machine_ok = sum(1 for r in rows if all(r.get(k) for k in REPLAY_MACHINE_FIELDS))
    pr_ok = sum(1 for r in pr if r["inLibrary"])

    result = {
        "sample": absorbed.get("skill", ""), "highlights": n,
        "covered": covered, "machineReplay": {k: cnt(k) for k in REPLAY_MACHINE_FIELDS},
        "triggerExact": cnt("triggerExact"), "triggerNorm": cnt("triggerNorm"),
        "anchorStrict": cnt("anchorStrict"), "anchorBase": cnt("anchorBase"),
        "pointExact": cnt("pointExact"),
        "principles": len(pr), "principlesCovered": pr_ok,
        "notAbsorbed": na_total, "notAbsorbedRegistered": na_reg,
    }

    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"=== 吸收重放测试：{result['sample']} ===")
        print(f"  ① 收录一致性：{covered}/{n} 条 highlight 已在库"
              f"（原则 {pr_ok}/{len(pr)} 已在库）")
        print(f"  ② 机器可重放字段（逐字一致）：")
        for k in REPLAY_MACHINE_FIELDS:
            print(f"       {k:<8} {result['machineReplay'][k]}/{n}")
        print(f"  ③ 规范化后等价（差异仅为定稿期规范化：加引号 / 补目录限定）：")
        print(f"       trigger 逐字 {result['triggerExact']}/{n}"
              f" → 规范化后 {result['triggerNorm']}/{n}")
        print(f"       证据锚点 严格路径包含 {result['anchorStrict']}/{n}"
              f" → basename 层包含 {result['anchorBase']}/{n}")
        print(f"  ④ 人工润色层（**不可机器重放**，如实标注）：")
        print(f"       要点逐字一致 {result['pointExact']}/{n}"
              f" → 入库时经改写定稿，吸收切片只是压缩表达")
        print(f"  ⑤ 不收项登记覆盖率：{na_reg}/{na_total}"
              f"（dedup_index 命中；未登记者会在 --check-dedup 报出）")

        bad = [r["id"] for r in rows if not all(r.get(k) for k in REPLAY_MACHINE_FIELDS)]
        if bad:
            print(f"\n  ⚠️  机器可重放字段不一致 {len(bad)} 条：{' '.join(bad)}")
        miss = [r["id"] for r in rows if r["inLibrary"] and not r.get("anchorBase")]
        if miss:
            print(f"  ❌ 锚点无法对应 {len(miss)} 条：{' '.join(miss)}（证据可能指向了切片里没有的文件）")
        tbad = [r["id"] for r in rows if r["inLibrary"] and not r.get("triggerNorm")]
        if tbad:
            print(f"  ❌ 触发信号规范化后仍不一致 {len(tbad)} 条：{' '.join(tbad)}")
        for p in pr:
            if p["inLibrary"] and p["declared"] and p["declared"] != p["explains"]:
                print(f"  ⚠️  {p['id']} explains 不一致：切片 {p['declared']} vs 库 {p['explains']}")

    # 判据：收录集合 + 机器可重放字段 + trigger 规范化等价 + 锚点可对应 + 原则 + 不收登记 六项全过。
    # 刻意**不**要求要点逐字一致——那本就属人工改写定稿，把它写成门禁等于用不可能的标准
    # 制造「永远红」，下次就会有人去放宽它（门禁腐烂的典型路径）。
    ok = (covered == n and machine_ok == n and result["triggerNorm"] == n
          and result["anchorBase"] == n and pr_ok == len(pr) and na_reg == na_total)
    if not ok:
        print("\n❌ 重放存在不一致——逐条查因后再改库（不得为了让测试变绿而改判据）")
        return 1
    print("\n✅ 重放一致：收录集合、格/主题/标题、触发信号（规范化等价）、证据锚点（可对应）、"
          "原则引用、不收项登记全部对上")
    return 0


# ───────────────────────────── 反向测试 ─────────────────────────────

def _bad_samples() -> list[tuple[str, dict, str]]:
    """坏样本 → (名字, absorbed 片段, 期望在 S0 被拦的理由关键词)。"""
    good = {"id": "D-999", "name": "X", "block": "B01", "theme": "T1",
            "trigger": "t", "evidence": "`a/b.md:1` 里写了 x", "point": "p", "bypass": ""}
    return [
        ("缺证据", {**good, "evidence": ""}, "缺必填字段 evidence"),
        ("证据无锚点", {**good, "evidence": "据观察，效果很好"}, "无可定位锚点"),
        ("block 非法", {**good, "block": "B11"}, "block 非法"),
        ("缺 id", {**good, "id": ""}, "缺 id"),
        ("缺要点", {**good, "point": ""}, "缺必填字段 point"),
    ]


def cmd_self_test(as_json: bool) -> int:
    """反向测试：**危险形态是静默放行，不是报错**（DP-208 / L11）。"""
    cases = []
    for name, bad, expect in _bad_samples():
        cands, rejects = s0_intake({"highlights": [bad]})
        got = rejects[0]["reason"] if rejects else ""
        ok = (not cands) and (expect in got)
        cases.append({"case": name, "expect": expect, "got": got or "<静默放行！>", "ok": ok})
    # 正样本必须被放行（否则门禁过严 = 也会被绕过）
    good = {"highlights": [{"id": "D-999", "name": "X", "block": "B01", "theme": "T1",
                            "trigger": "t", "evidence": "`a/b.md:1` 写了 x",
                            "point": "p", "bypass": "rule"}]}
    c, r = s0_intake(good)
    cases.append({"case": "正样本应放行", "expect": "通过", "got": "通过" if (c and not r) else "被误拦",
                  "ok": bool(c) and not r})
    if as_json:
        print(json.dumps(cases, ensure_ascii=False, indent=2))
    else:
        print("=== absorb_intake 反向测试（坏样本必须被 S0 拦住）===")
        for c_ in cases:
            print(f"  {'✅' if c_['ok'] else '❌'} {c_['case']:<14} 期望「{c_['expect']}」→ 实际「{c_['got']}」")
    n_ok = sum(1 for c_ in cases if c_["ok"])
    print(f"\n{'✅' if n_ok == len(cases) else '❌'} 反向测试 {n_ok}/{len(cases)}")
    return 0 if n_ok == len(cases) else 3


# ───────────────────────────── CLI ─────────────────────────────

def cmd_intake(root: Path, path: Path, stage: bool, commit: bool, as_json: bool) -> int:
    absorbed = load_json(path)
    cands, rejects = s0_intake(absorbed)
    lib = library_ids(root)
    dedup = load_dedup(root)
    verdicts = s1_merge(cands, dedup, lib)
    accepted = {v["id"] for v in verdicts if v["verdict"] == "accept"}
    groups = promotion_groups(cands, accepted)

    out = {"source": str(path), "skill": absorbed.get("skill", ""),
           "s0": {"candidates": len(cands), "rejects": rejects},
           "s1": {"verdicts": verdicts, "promotionHints": groups}}
    rc = 0
    if as_json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"=== 吸收流水线：{absorbed.get('skill','?')} ===")
        print(f"── S0 采集（三查门禁）──")
        print(f"  候选 {len(cands)} 条 / 打回 {len(rejects)} 条（打回**只给理由，不代填**）")
        for r_ in rejects:
            print(f"    ❌ {r_['id']}：{r_['reason']}")
        print(f"── S1 归并（dedup_index 查重）──")
        for v in verdicts:
            mark = {"accept": "🟢 可收录", "dedup-hit": "🔁 命中登记",
                    "already-in-library": "✅ 已在库"}[v["verdict"]]
            print(f"    {mark} {v['id']}：{v['detail']}")
        if groups:
            print(f"── 归并判据提示（DP-204：同源单点 ≥3 ⇒ 考虑升维，不散点补）──")
            for g in groups:
                print(f"    ⬆️ {g['block']}/{g['theme']} 有 {len(g['ids'])} 条："
                      f"{' '.join(g['ids'])} → {g['suggestion']}")
        print(f"\n  小结：可收录 {len(accepted)} / 命中登记 {sum(1 for v in verdicts if v['verdict']=='dedup-hit')}"
              f" / 已在库 {sum(1 for v in verdicts if v['verdict']=='already-in-library')}"
              f" / 打回 {len(rejects)}")

    if rejects:
        rc = 1
    if stage:
        d = s0_stage(root, absorbed, cands, rejects)
        print(f"\n── S0 落盘：{d.relative_to(root)}（与权威库物理隔离，编译器不读）")
    if commit:
        if rejects or not accepted:
            print("\n❌ S2 拒绝编译：存在打回项或无可收录项（fail-closed，不写任何生成物）")
            return 1
        rc2, msg = s2_compile(root)
        print(f"── S2 编译：{'✅' if rc2 == 0 else '❌'} {msg}")
        if rc2 != 0:
            return 3
        rc3, msg3 = s3_publish(root)
        print(f"── S3 发布：{'✅' if rc3 == 0 else '❌'} {msg3}")
        if rc3 != 0:
            return 1
        print("\n⚠️ 注意：候选**未自动并入 library/entries.json**——要点/标签/抗绕过性属人工判断，"
              "机器不代填（P0 诚实性）。补全字段后重跑同命令。")
    return rc


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="吸收流水线 S0–S3（ADR-001 措施 1.4）")
    ap.add_argument("--from", dest="src", help="absorbed.json 路径（上游 skill-rebuild 产出）")
    ap.add_argument("--stage", action="store_true", help="跑到 S0：候选落 library/staging/")
    ap.add_argument("--commit", action="store_true", help="跑 S2–S3（编译 + 发布门禁）")
    ap.add_argument("--replay", metavar="FILE", help="重放测试：与现有库逐字段比对（只读）")
    ap.add_argument("--check-dedup", action="store_true", help="登记册健康检查 + 全样本登记覆盖率")
    ap.add_argument("--self-test", action="store_true", help="反向测试（坏样本必须被拦）")
    ap.add_argument("--json", action="store_true", help="JSON 输出")
    ap.add_argument("--root", default=None)
    args = ap.parse_args(argv)
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent

    if args.self_test:
        return cmd_self_test(args.json)
    if args.check_dedup:
        e, w = check_dedup(root, verbose=not args.json)
        if args.json:
            print(json.dumps({"errors": e, "warnings": w}, ensure_ascii=False, indent=2))
        return 3 if e else (2 if w else 0)
    if args.replay:
        return cmd_replay(root, Path(args.replay), args.json)
    if not args.src:
        ap.error("需要 --from <absorbed.json>（或 --replay / --check-dedup / --self-test）")
    return cmd_intake(root, Path(args.src), args.stage, args.commit, args.json)


if __name__ == "__main__":
    raise SystemExit(main())
