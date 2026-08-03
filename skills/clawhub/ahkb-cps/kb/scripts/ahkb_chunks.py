"""
ahkb_chunks.py — 原始文档 Chunk 存储与索引模块

功能：
  1. 保存提取后的 chunk 到 chunks/ 目录（每个原始文件一个 JSON）
  2. 维护 chunks/index.json 全局索引
  3. 提供加载和检索接口

设计原则：
  - 所有格式的 chunk 统一结构，匹配引擎只认 chunk.text，不关心原始格式
  - 一个原始文件 → 一个 JSON 文件，方便检索时一次性读取上下文
  - 全局索引用内存热加载，提升匹配效率
"""
import json
import datetime
import hashlib
from pathlib import Path
from ahkb_trash import _trash_file


def _chunks_dir(workspace):
    """chunks 目录路径"""
    d = Path(workspace) / "chunks"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _index_path(workspace):
    """索引文件路径"""
    return _chunks_dir(workspace) / "index.json"


def _safe_filename(source_file):
    """将 source_file 路径转为安全的 JSON 文件名"""
    # 例如 "原始文件/大系统观/BSV_core_knowledge_base.md" → "BSV_core_knowledge_base.md.json"
    p = Path(source_file)
    name = p.stem + p.suffix  # 保留完整文件名（含扩展名，如 .md）
    # 替换不安全字符
    safe = "".join(c if c.isalnum() or c in '._- ()' else '_' for c in name)
    return safe + ".json"


def save_chunks(extracted_data, source_file, workspace):
    """
    从提取结果保存 chunk 到 chunks/ 目录。

    Args:
        extracted_data: extract_xxx() 返回的 dict，含 chunks、full_text 等
        source_file: 相对于 workspace 的源文件路径，如 "原始文件/大系统观/xxx.md"
        workspace: 工作空间根目录

    Returns:
        dict: {saved, chunk_count, chunk_file}
    """
    now_str = datetime.datetime.now().isoformat(timespec="seconds")

    # ── 构建 chunk 记录 ──
    chunks_out = []
    for i, ch in enumerate(extracted_data.get("chunks", [])):
        text = ch.get("text", "").strip()
        heading = ch.get("heading", "").strip()
        position = ch.get("source_position", ch.get("heading", ""))

        # 计算 heading_level
        h_level = ch.get("level", 0)
        if not h_level:
            # 根据 type 推断
            ctype = ch.get("type", "")
            if ctype == "slide":
                h_level = 2  # PPT每页相当于 H2
            elif ctype == "page":
                h_level = 3
            elif ctype == "sheet":
                h_level = 2
            else:
                h_level = 1

        word_count = len(text.replace("\n", "").replace(" ", ""))

        # 提取关键词（简单 TF 前5，实际匹配用 jieba）
        tags = []
        if len(text) > 20:
            try:
                import jieba.analyse
                tags = jieba.analyse.extract_tags(text, topK=5, withWeight=False)
            except Exception:
                pass

        chunks_out.append({
            "chunk_id": f"{Path(source_file).stem}-{i+1:03d}",
            "heading": heading if heading else "(无标题)",
            "heading_level": h_level,
            "position": position if position else heading,
            "word_count": word_count,
            "tags": tags,
            "text": text,
        })

    # ── 保存 chunk JSON ──
    chunk_json = {
        "source_file": source_file,
        "format": extracted_data.get("type", "unknown"),
        "last_updated": now_str,
        "total_word_count": sum(c["word_count"] for c in chunks_out),
        "chunk_count": len(chunks_out),
        "full_text": extracted_data.get("full_text", ""),
        "chunks": chunks_out,
    }

    chunk_dir = _chunks_dir(workspace)
    fname = _safe_filename(source_file)
    chunk_path = chunk_dir / fname

    chunk_path.write_text(
        json.dumps(chunk_json, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    # ── 更新全局索引 ──
    _update_index(workspace, source_file, chunks_out, chunk_json)

    return {
        "saved": True,
        "chunk_count": len(chunks_out),
        "chunk_file": str(chunk_path.relative_to(workspace)),
    }


def _update_index(workspace, source_file, chunks, chunk_json):
    """更新全局索引 index.json"""
    idx_path = _index_path(workspace)
    now_str = datetime.datetime.now().isoformat(timespec="seconds")

    # 读取已有索引
    index = {"updated": now_str, "chunks": [], "files": [], "file_chunk_map": {}}
    if idx_path.exists():
        try:
            index = json.loads(idx_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    # 移除该文件原有的 chunk 条目
    old_chunk_ids = set()
    if source_file in index.get("file_chunk_map", {}):
        old_chunk_ids = set(
            index["chunks"][i]["chunk_id"]
            for i in index["file_chunk_map"][source_file]
            if 0 <= i < len(index["chunks"])
        )
    index["chunks"] = [c for c in index["chunks"] if c.get("chunk_id") not in old_chunk_ids]

    # 添加新 chunk 条目（不含 text 正文，只存元数据）
    start_idx = len(index["chunks"])
    for i, ch in enumerate(chunks):
        index["chunks"].append({
            "chunk_id": ch["chunk_id"],
            "source_file": source_file,
            "heading": ch["heading"],
            "position": ch["position"],
            "word_count": ch["word_count"],
            "tag_count": len(ch.get("tags", [])),
        })

    # 更新 file_chunk_map
    index["file_chunk_map"][source_file] = list(range(start_idx, start_idx + len(chunks)))

    # 更新文件列表
    if source_file not in index["files"]:
        index["files"].append(source_file)

    index["updated"] = now_str

    idx_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


def load_chunk_index(workspace):
    """加载全局 chunk 索引（只含元数据，不含正文）"""
    idx_path = _index_path(workspace)
    if not idx_path.exists():
        return {"chunks": [], "files": [], "file_chunk_map": {}}
    try:
        return json.loads(idx_path.read_text(encoding="utf-8"))
    except Exception:
        return {"chunks": [], "files": [], "file_chunk_map": {}}


def load_all_chunks_with_text(workspace):
    """
    加载所有 chunk（含正文），用于跨文档匹配。

    Returns:
        list[dict]: 每个元素含 chunk_id, source_file, heading, position, word_count, text
    """
    idx = load_chunk_index(workspace)
    chunk_dir = _chunks_dir(workspace)
    all_chunks = []

    # 缓存已加载的 JSON 文件，避免重复读取
    file_cache = {}
    for ci, meta in enumerate(idx.get("chunks", [])):
        source_file = meta.get("source_file", "")
        if source_file not in file_cache:
            json_path = chunk_dir / _safe_filename(source_file)
            if json_path.exists():
                try:
                    file_cache[source_file] = json.loads(json_path.read_text(encoding="utf-8"))
                except Exception:
                    file_cache[source_file] = {"chunks": []}
            else:
                file_cache[source_file] = {"chunks": []}

        # 在同文件的 chunks 中查找对应 chunk
        source_chunks = file_cache[source_file].get("chunks", [])
        chunk = None
        for sc in source_chunks:
            if sc.get("chunk_id") == meta.get("chunk_id"):
                chunk = sc
                break

        if chunk:
            all_chunks.append({
                "chunk_id": chunk.get("chunk_id", ""),
                "source_file": source_file,
                "heading": meta.get("heading", ""),
                "position": meta.get("position", ""),
                "word_count": meta.get("word_count", 0),
                "text": chunk.get("text", ""),
            })

    return all_chunks


def load_chunks_for_file(source_file, workspace):
    """加载某个原始文件的所有 chunk（含正文）"""
    chunk_dir = _chunks_dir(workspace)
    json_path = chunk_dir / _safe_filename(source_file)
    if not json_path.exists():
        return {"source_file": source_file, "chunks": [], "full_text": ""}
    try:
        return json.loads(json_path.read_text(encoding="utf-8"))
    except Exception:
        return {"source_file": source_file, "chunks": [], "full_text": ""}


def remove_file_chunks(source_file, workspace):
    """删除某个原始文件的所有 chunk 记录"""
    chunk_dir = _chunks_dir(workspace)
    json_path = chunk_dir / _safe_filename(source_file)
    if json_path.exists():
        _trash_file(json_path, workspace)

    idx_path = _index_path(workspace)
    if idx_path.exists():
        try:
            index = json.loads(idx_path.read_text(encoding="utf-8"))
            old_ids = set()
            if source_file in index.get("file_chunk_map", {}):
                old_ids = set(
                    index["chunks"][i]["chunk_id"]
                    for i in index["file_chunk_map"].get(source_file, [])
                    if 0 <= i < len(index["chunks"])
                )
            index["chunks"] = [c for c in index["chunks"] if c.get("chunk_id") not in old_ids]
            index["file_chunk_map"].pop(source_file, None)
            if source_file in index.get("files", []):
                index["files"].remove(source_file)
            idx_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass

    return {"removed": source_file}


def purge_all_chunks(workspace):
    """清空所有 chunk 数据"""
    chunk_dir = _chunks_dir(workspace)
    idx_path = _index_path(workspace)

    # 重置索引
    idx_path.write_text(json.dumps({
        "updated": datetime.datetime.now().isoformat(timespec="seconds"),
        "chunks": [],
        "files": [],
        "file_chunk_map": {},
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    # 删除所有 chunk JSON
    for f in chunk_dir.glob("*.json"):
        if f.name != "index.json":
            _trash_file(f, workspace)

    return {"purged": True}


def get_chunk_stats(workspace):
    """获取 chunk 存储统计"""
    idx = load_chunk_index(workspace)
    chunk_dir = _chunks_dir(workspace)

    total_size = 0
    for f in chunk_dir.glob("*.json"):
        try:
            total_size += f.stat().st_size
        except Exception:
            pass

    return {
        "total_chunks": len(idx.get("chunks", [])),
        "total_files": len(idx.get("files", [])),
        "total_size_bytes": total_size,
        "total_size_mb": round(total_size / 1024 / 1024, 2),
    }
