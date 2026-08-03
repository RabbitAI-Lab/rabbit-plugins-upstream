"""
ahkb_chunk_match.py — 知识元 ↔ 原始文件 Chunk 匹配引擎

功能：将知识元与原始文档 chunk 进行 TF-IDF 匹配，找到相关的原始文件和章节位置。
提供两个接口：
  1. match_unit_to_chunks() — 单个知识元匹配所有 chunk
  2. write_related_files_to_unit() — 将匹配结果写入知识元文件

在 crosslink 主循环中使用，扩展为"任务三"。
"""
import re
import os
import time as _time_


def match_unit_to_chunks(unit, all_chunks, weights=None, min_score=None, max_files=8,
                          prebuilt_unit_vec=None, prebuilt_chunk_vecs=None):
    """
    将单个知识元与所有原始文件 chunk 进行 4 维度加权匹配。

    评分维度：
      1. 内容相似性（TF-IDF 余弦） → 满分100 × wContext
      2. 标签相似性（Jaccard）       → 满分100 × wTags
      3. 标题命中（知识元名在chunk标题中出现）→ 满分100 × wTitle(=0.3)
      4. 多chunk加成（同文件N个chunk命中）→ ×(1.0~1.5)

    阈值公式（与资源匹配任务二的逻辑一致）：
      max_possible = 100×(wContext + wTags + wTitle)
      min_score    = max_possible × (1 - cLinksDensity^0.6)

    Args:
        unit: 知识元 dict，含 name, title, text, tags
        all_chunks: 所有 chunk 列表
        weights: 权重配置 {"cContext", "cTags", "cLinksDensity"}，None则用默认值
        min_score: 最低文件级匹配阈值，None则自动计算
        max_files: 最多关联多少个文件
        prebuilt_unit_vec: 预提取的知识元 TF-IDF 向量（{word: weight}），None 则现场提取
        prebuilt_chunk_vecs: 预提取的 chunk TF-IDF 向量字典 {chunk_index: {word: weight}}，None 则现场提取

    Returns:
        dict: {
            "matched":     [...],   # 达到阈值的文件（用于写入）
            "all_sorted":  [...],   # 全部候选文件（用于进度显示）
            "w_ctx":       float,
            "w_tags":      float,
            "w_title":     float,
            "threshold":   float,
        }
        每个文件条目: {file, positions, score, cs, ts, tts, n_chunks}
    """
    from ahkb_crosslink import _tfidf_similarity, _title_bigram_sim, _vec_cosine

    # ── 权重与阈值 ──
    if weights is None:
        weights = {}
    w_ctx   = weights.get("cContext", 0.5)
    w_tags  = weights.get("cTags", 0.5)
    w_title = 0.3  # 标题命中权重固定
    density = max(0.1, weights.get("cLinksDensity", 0.5))

    max_possible = 100 * w_ctx + 100 * w_tags + 100 * w_title

    if min_score is None:
        min_score = max_possible * (1 - density ** 0.6)

    # chunk 级阈值比文件级低，避免漏掉多chunk弱信号聚合
    chunk_min_score = min_score * 0.4
    if chunk_min_score < 0.5:
        chunk_min_score = 0.5

    unit_text = unit.get("text", "")
    unit_name = (unit.get("name") or "").strip().lower()
    unit_tags = [t.lower().strip() for t in unit.get("tags", []) if t.strip()]

    # ── 1. 逐chunk评分 ──
    chunk_scores = []
    _use_cached = prebuilt_unit_vec is not None and prebuilt_chunk_vecs is not None
    for _ci, ch in enumerate(all_chunks):
        ch_text     = ch.get("text", "").strip()
        ch_heading  = (ch.get("heading") or "").strip().lower()
        ch_keywords = [k.lower().strip() for k in ch.get("tags", []) if k.strip()]

        if not ch_text:
            continue

        # ① 内容相似性（0-100）
        if _use_cached and _ci in prebuilt_chunk_vecs:
            content_score = _vec_cosine(prebuilt_unit_vec, prebuilt_chunk_vecs[_ci]) * 100
        else:
            content_score = _tfidf_similarity(unit_text, ch_text) * 100

        # ② 标签相似性（0-100）
        if unit_tags and ch_keywords:
            u_set = set(unit_tags)
            c_set = set(ch_keywords)
            inter = len(u_set & c_set)
            union = len(u_set | c_set)
            tag_score = (inter / union) * 100 if union else 0
        else:
            tag_score = 0

        # ③ 标题命中（0-100）
        if unit_name and ch_heading:
            if unit_name in ch_heading:
                title_score = 100
            else:
                title_score = _title_bigram_sim(unit_name, ch_heading) * 100
        else:
            title_score = 0

        # 加权求和
        total = content_score * w_ctx + tag_score * w_tags + title_score * w_title

        if total >= chunk_min_score:
            chunk_scores.append((ch, total, content_score, tag_score, title_score))

    if not chunk_scores:
        return {"matched": [], "all_sorted": [], "w_ctx": w_ctx, "w_tags": w_tags, "w_title": w_title, "threshold": min_score}

    # ── 2. 按文件分组 ──
    file_groups = {}
    for ch, total, cs, ts, tts in chunk_scores:
        src = ch["source_file"]
        if src not in file_groups:
            file_groups[src] = {
                "file": src,
                "positions": [],
                "chunk_scores": [],
                "best_score": 0.0,
                "best_cs": 0, "best_ts": 0, "best_title": 0,
            }
        fg = file_groups[src]

        pos = ch.get("position", ch.get("heading", ""))
        if pos and pos not in fg["positions"]:
            fg["positions"].append(pos)

        fg["chunk_scores"].append((ch, total, cs, ts, tts))
        if total > fg["best_score"]:
            fg["best_score"] = total
            fg["best_cs"]   = cs
            fg["best_ts"]   = ts
            fg["best_title"] = tts

    # ── 3. 多chunk加成 ──
    for fg in file_groups.values():
        n = len(fg["chunk_scores"])
        if n > 1:
            bonus = 1.0 + 0.1 * min(n - 1, 5)
            fg["best_score"] = fg["best_score"] * bonus

    # ── 4. 排序 ──
    all_sorted = sorted(file_groups.values(), key=lambda x: -x["best_score"])

    # ── 5. 构建返回 ──
    def _build_entry(fg):
        return {
            "file": fg["file"],
            "positions": fg["positions"][:5],
            "score": round(fg["best_score"], 1),
            "cs": round(fg["best_cs"], 0),
            "ts": round(fg["best_ts"], 0),
            "tts": round(fg["best_title"], 0),
            "n_chunks": len(fg["chunk_scores"]),
        }

    matched = [_build_entry(fg) for fg in all_sorted if fg["best_score"] >= min_score][:max_files]
    all_entries = [_build_entry(fg) for fg in all_sorted]

    return {
        "matched": matched,
        "all_sorted": all_entries,
        "w_ctx": w_ctx,
        "w_tags": w_tags,
        "w_title": w_title,
        "threshold": round(min_score, 1),
    }


def build_related_files_section(matched_files, source_file=""):
    """
    构建「关联原始文件」正文章节。

    规则：
      - 第1条固定为 source_file（知识元的来源文件），不允许为空
      - 后面的条目为其他匹配的原始文件（自动去除与 source 重复的）
      - 至少有一条才返回有效章节

    Returns:
        str: 完整的 "## 关联原始文件\\n\\n- ..." 段落，source和matched都为空时返回 ""
    """
    if not source_file and not matched_files:
        return ""

    body_lines = []

    # 第1条：source 文件（使用 markdown 链接格式，便于在 HTML 中点击）
    if source_file:
        _fname = source_file.replace("\\", "/").split("/")[-1]
        body_lines.append(f"- [{_fname}]({source_file})")

    # 后续：其他匹配文件（去重 source）
    if matched_files:
        for mf in matched_files:
            mf_file = mf.get("file", "")
            positions = mf.get("positions", [])
            # 跳过与 source 相同的文件
            if mf_file and mf_file != source_file:
                pos_str = ""
                if positions:
                    pos_str = " → " + "、".join(positions[:5])
                _fname = mf_file.replace("\\", "/").split("/")[-1]
                body_lines.append(f"- [{_fname}]({mf_file}){pos_str}")

    if not body_lines:
        return ""

    return "## 关联原始文件\n\n" + "\n".join(body_lines)


def write_related_files_to_unit(unit, matched_files, dry_run=False, source_file=""):
    """
    写入/更新知识元 frontmatter 中的 related_files 字段。

    规则：
      - 第1条固定为 source_file（知识元的来源文件），score: 1.0
      - 后面的条目为其他匹配的原始文件（自动去重 source）
      - 至少有一条才写入

    Args:
        unit: 知识元 dict，含 file (Path), fm_text
        matched_files: chunk 匹配结果列表
        dry_run: 仅模拟不写入
        source_file: 知识元的 source 文件路径

    Returns:
        是否修改了 frontmatter
    """
    if not source_file and not matched_files:
        return False

    # ── 构建 related_files YAML ──
    rf_lines = []

    # 第1条：source 文件
    if source_file:
        rf_lines.append(f"  - file: \"{source_file}\"")
        rf_lines.append(f"    score: 1.0")

    # 后续：匹配文件（去重source）
    if matched_files:
        for mf in matched_files:
            mf_file = mf.get("file", "")
            if mf_file and mf_file != source_file:
                rf_lines.append(f"  - file: \"{mf_file}\"")
                if mf.get("positions"):
                    pos_str = ", ".join(mf["positions"])
                    rf_lines.append(f"    positions: [{pos_str}]")
                rf_lines.append(f"    score: {mf['score']}")

    if not rf_lines:
        return False

    related_files_block = "related_files:\n" + "\n".join(rf_lines)

    # ── 更新 frontmatter ──
    new_fm = unit["fm_text"]
    if "related_files:" in new_fm:
        new_fm = re.sub(
            r'\nrelated_files:\n(?:\s+.*\n?)*',
            '',
            new_fm
        )
    new_fm = new_fm.rstrip() + "\n" + related_files_block

    unit["fm_text"] = new_fm

    # 同时更新文件（只写 frontmatter 变更，body 不动）
    # 用临时文件+原子替换绕过 Obsidian 等软件的文件锁
    if not dry_run:
        new_content = "---\n" + new_fm.strip() + "\n---" + unit["body"]
        for _retry in range(3):
            try:
                _tmp = unit["file"].with_suffix(".md.tmp")
                _tmp.write_text(new_content, encoding="utf-8")
                os.replace(_tmp, unit["file"])
                break
            except (OSError, PermissionError):
                if _retry < 2:
                    _time_.sleep(0.5)

    return True


def get_chunk_matching_stats(all_matches):
    """汇总 chunk 匹配统计"""
    total_knowledge_units = len(all_matches)
    units_with_files = sum(1 for m in all_matches if m)
    total_file_refs = sum(len(m) for m in all_matches if m)

    return {
        "total_units": total_knowledge_units,
        "units_with_files": units_with_files,
        "total_file_refs": total_file_refs,
    }
