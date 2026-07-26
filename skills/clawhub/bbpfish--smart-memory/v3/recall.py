"""
Smart Memory v3 — 召回引擎

L1 TF-IDF 关键词召回 + L2 AND 语义全文展开。
严格按 SPEC §4.1 实现：L2 仅在 importance≥0.7 AND (retention<0.3 OR 精确命中≥2) 时触发。
"""

import hashlib
import json
import math
import os
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from typing import Optional

from .cues import CueStore
from .db import get_connection, utcnow_dt
from .manifest import ManifestStore
from .tokenizer import tokenize


# ---------------------------------------------------------------------------
# 模块级常量
# ---------------------------------------------------------------------------
DEFAULT_TOP_K = 8               # 默认召回数量
DEFAULT_RECALL_DAYS = 30        # 默认时间衰减窗口（天）
DEFAULT_MAX_DOCS = 3            # 默认 L2 展开最大文档数
L1_RELEVANCE_WEIGHT = 0.7       # L1 相关性权重
L1_DECAY_WEIGHT = 0.3           # L1 时间衰减权重
STALE_OBSERVED_PENALTY = 0.5    # stale_observed 的 score 降权系数
PRECOND_FAILED_PENALTY = 0.5    # 前置条件失败降权系数（SPEC §6.2）
PRECOND_UNKNOWN_PENALTY = 0.8   # 前置条件未知降权系数
TIME_DECAY_FLOOR = 0.1          # 时间衰减下限
TIME_DECAY_YEAR_WINDOW = 365    # 时间衰减年窗口（天）


class RecallEngine:
    """召回引擎：L1 TF-IDF 摘要召回 → L2 条件性全文展开。"""

    def __init__(self, db_path: Optional[str] = None):
        """初始化召回引擎。

        Args:
            db_path: SQLite 数据库路径，None 则使用默认单例连接。
        """
        self._store = CueStore(db_path)
        self._db_path = db_path
        self._index_cache: Optional[dict] = None

    def __repr__(self) -> str:
        return f"RecallEngine(db_path={self._db_path!r})"

    # ==================================================================
    # 公共入口
    # ==================================================================

    def recall(
        self,
        query: str,
        top: int = 8,
        days: int = 30,
        mode: str = "l1",
        skip_precond_cache: bool = False,
        include_stale: bool = False,
        max_docs: int = 3,
    ) -> dict:
        """主召回入口。

        Args:
            query: 用户查询字符串
            top: 最多返回线索数
            days: 时间衰减窗口（天）
            mode: 'l1'（仅摘要）、'l2'（条件展开）、'full'（L1+L2）
            skip_precond_cache: 跳过 precondition_cache 查询
            include_stale: 包含 stale_confirmed 卡片

        Returns:
            {
                "query": str,
                "mode": str,
                "l1_results": [{"card_id","score","title","keywords",...}, ...],
                "l2_triggered": bool,
                "l2_results": [{"card_id","title","content",...}, ...] | None,
            }
        """
        if not query or not query.strip():
            return {
                "query": query,
                "mode": mode,
                "l1_results": [],
                "l2_triggered": False,
                "l2_results": None,
            }

        # L1 TF-IDF 召回
        l1_results = self._tfidf_recall(
            query, top, days,
            skip_precond_cache=skip_precond_cache,
            include_stale=include_stale,
        )

        l2_triggered = False
        l2_results = None

        if mode in ("l2", "full"):
            # 检查 L2 展开条件（AND 语义）
            card_ids = [r["card_id"] for r in l1_results]
            l2_triggered = self._should_expand_l2(l1_results, query)

            if l2_triggered:
                l2_results = self._l2_expand(card_ids, max_docs=max_docs)

        result = {
            "query": query,
            "mode": mode,
            "l1_results": l1_results,
            "l2_triggered": l2_triggered,
            "l2_results": l2_results,
        }

        if mode == "l1":
            result["l2_results"] = None

        return result

    # ==================================================================
    # L1 TF-IDF 召回
    # ==================================================================

    def _tfidf_recall(
        self, query: str, top: int, days: int,
        skip_precond_cache: bool = False,
        include_stale: bool = False,
    ) -> list[dict]:
        """L1 阶段：TF-IDF 关键词召回，按 final_score 排序。

        final_score = relevance_score * 0.7 + time_decay * 0.3

        SPEC §3.3 retention 过滤：
        - stale_confirmed 的卡片：默认跳过，include_stale=True 时包含
        - stale_observed 的卡片：score × 0.5
        - active 的卡片：正常
        """
        query_tokens = tokenize(query)
        if not query_tokens:
            return []

        # 获取所有非 deleted 线索卡（含 stale_observed）
        all_cues = self._store.list_all()
        if not all_cues:
            return []

        # 按 status 过滤
        filtered_cues = []
        for cue in all_cues:
            status = cue.get("status", "active")
            if status == "stale_confirmed" and not include_stale:
                continue  # 跳过
            filtered_cues.append(cue)

        if not filtered_cues:
            return []

        # 构建语料库 DF（利用缓存）
        if self._index_cache is None:
            self._index_cache = self._build_index()
        corpus_df = self._index_cache["corpus_df"]
        total_docs = self._index_cache["total_docs"]

        now = utcnow_dt()

        scored = []
        for cue in filtered_cues:
            keywords = cue.get("keywords", [])
            if not isinstance(keywords, list):
                keywords = []

            relevance = _compute_tfidf(
                query_tokens, keywords, corpus_df, total_docs
            )
            if relevance <= 0:
                continue

            # 时间衰减
            decay = _compute_time_decay(cue.get("created", ""), days, now)
            final_score = relevance * L1_RELEVANCE_WEIGHT + decay * L1_DECAY_WEIGHT

            # SPEC §3.3: stale_observed 降温
            cue_status = cue.get("status", "active")
            if cue_status == "stale_observed":
                final_score *= STALE_OBSERVED_PENALTY

            # Part B: 集成 precondition_cache 读取
            if skip_precond_cache:
                precond_status = "unknown"
            else:
                precond_status = self._get_precondition_status(cue.get("id"))
            if precond_status == "failed":
                final_score *= PRECOND_FAILED_PENALTY  # SPEC §6.2
            elif precond_status == "unknown":
                final_score *= PRECOND_UNKNOWN_PENALTY  # 缓存不存在或过期

            scored.append({
                "card_id": cue.get("id"),
                "title": cue.get("title", ""),
                "keywords": keywords,
                "scene": cue.get("scene", ""),
                "docs": cue.get("docs", []),
                "score": round(final_score, 4),
                "relevance": round(relevance, 4),
                "decay": round(decay, 4),
                "importance": cue.get("importance", 0.5),
                "retention": cue.get("retention", 1.0),
                "status": cue_status,
                "precondition_status": precond_status,
            })

        # 按 final_score 降序排序
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top]

    # ==================================================================
    # Part B: precondition_cache 状态查询
    # ==================================================================

    def _get_precondition_status(self, cue_id: str) -> str:
        """查询 precondition_cache 表中该 cue 的预检状态。

        Returns:
            "passed"  — 缓存有效且 all_passed=1
            "failed"  — 缓存有效且 all_passed=0
            "unknown" — 缓存不存在或 TTL 已过期
        """
        conn = get_connection()
        row = conn.execute(
            """SELECT all_passed, evaluated_at, ttl_minutes
               FROM precondition_cache WHERE cue_id = ?""",
            (cue_id,),
        ).fetchone()

        if row is None:
            return "unknown"

        # 检查 TTL 是否过期
        try:
            evaluated_at = datetime.strptime(row["evaluated_at"], "%Y-%m-%d %H:%M:%S")
            ttl_minutes = row["ttl_minutes"]
            now = utcnow_dt()
            if (now - evaluated_at).total_seconds() > ttl_minutes * 60:
                return "unknown"
        except (ValueError, TypeError):
            return "unknown"

        return "passed" if row["all_passed"] == 1 else "failed"

    # ==================================================================
    # L2 AND 语义展开
    # ==================================================================

    def _should_expand_l2(self, l1_results: list[dict], query: str) -> bool:
        """判断是否触发 L2 展开。

        SPEC §4.1 AND 语义：
        展开 L2 ⇔ importance ≥ 0.7 AND (retention < 0.3 OR 精确命中 ≥ 2)

        迭代所有 l1_results，任一卡片满足条件即返回 True。
        "精确命中"指 query 的 token 直接出现在 keywords 列表中（不含 TF-IDF 模糊匹配）。
        """
        if not l1_results:
            return False

        query_tokens = tokenize(query)
        if not query_tokens:
            return False

        for result in l1_results:
            importance = result.get("importance", 0.0)
            if importance < 0.7:
                continue

            retention = result.get("retention", 1.0)
            if retention < 0.3:
                return True

            # 精确命中检查：query token 与 keywords 的精确匹配数
            keywords = result.get("keywords", [])
            if isinstance(keywords, list):
                kw_lower = set(k.lower() for k in keywords if isinstance(k, str))
                exact_hits = sum(1 for t in query_tokens if t.lower() in kw_lower)
                if exact_hits >= 2:
                    return True

        return False

    def _compute_redundancy(self, top2_texts: list[str]) -> float:
        """计算两条文本的 token 集合 Jaccard 相似度（交集/并集）。"""
        if len(top2_texts) < 2:
            return 0.0

        tokens_a = set(tokenize(top2_texts[0]))
        tokens_b = set(tokenize(top2_texts[1]))

        if not tokens_a or not tokens_b:
            return 0.0

        intersection = tokens_a & tokens_b
        union = tokens_a | tokens_b
        return len(intersection) / len(union)

    def _l2_expand(self, card_ids: list[str], max_docs: int = 3) -> list[dict]:
        """L2 阶段：加载匹配卡片的完整内容。

        Part C: 展开前校验 manifest checksum：
        - checksum 匹配 → 正常展开
        - checksum 不匹配 → 自动更新 manifest 后展开
        - 文件不存在 → 跳过该文档，标记 checksum_status="broken"

        Args:
            card_ids: 需要展开的卡片 ID 列表
            max_docs: 最多展开文档数（截断）
        """
        results = []
        base_dir = os.path.dirname(os.path.abspath(__file__))
        manifest_store = ManifestStore()

        for cid in card_ids:
            card = self._store.get(cid)
            if card is None:
                continue

            docs = card.get("docs", [])
            if not isinstance(docs, list):
                docs = []

            # 校验每个关联文档的 checksum
            verified_docs = []
            checksum_statuses = []

            for doc_rel in docs:
                doc_path = os.path.join(base_dir, doc_rel)
                entry = manifest_store.get_by_path(doc_rel)

                if entry is None:
                    # manifest 无记录，跳过
                    checksum_statuses.append({
                        "doc": doc_rel,
                        "status": "not_registered",
                    })
                    continue

                if not os.path.isfile(doc_path):
                    # 文件不存在
                    checksum_statuses.append({
                        "doc": doc_rel,
                        "status": "broken",
                    })
                    continue

                # 计算当前 checksum
                actual = ManifestStore.compute_checksum(doc_path)
                expected = entry.get("checksum", "")

                if actual is None:
                    checksum_statuses.append({
                        "doc": doc_rel,
                        "status": "broken",
                    })
                    continue

                if actual != expected:
                    # 不匹配 → 自动更新 manifest
                    manifest_store.update_entry(
                        entry["doc_id"],
                        {"checksum": actual},
                    )
                    checksum_statuses.append({
                        "doc": doc_rel,
                        "status": "updated",
                    })
                else:
                    checksum_statuses.append({
                        "doc": doc_rel,
                        "status": "ok",
                    })

                verified_docs.append(doc_rel)

            # 加载文档内容（SPEC §4.3：展开内容包含 frontmatter + 正文）
            doc_contents = []
            for doc_rel in verified_docs:
                doc_path = os.path.join(base_dir, doc_rel)
                try:
                    with open(doc_path, "r", encoding="utf-8") as f:
                        doc_contents.append({
                            "path": doc_rel,
                            "content": f.read(),
                        })
                except (OSError, UnicodeDecodeError):
                    # 读取失败时仍记录但内容为空
                    doc_contents.append({
                        "path": doc_rel,
                        "content": "",
                        "error": "failed to read",
                    })

            result = {
                "card_id": card.get("id"),
                "title": card.get("title", ""),
                "content": card.get("scene", ""),
                "keywords": card.get("keywords", []),
                "docs": verified_docs,
                "doc_contents": doc_contents,
                "importance": card.get("importance", 0.5),
                "retention": card.get("retention", 1.0),
            }

            if checksum_statuses:
                result["checksum_status"] = checksum_statuses

            results.append(result)

        return results[:max_docs]

    # ==================================================================
    # 索引缓存（可选优化）
    # ==================================================================

    def _build_index(self) -> dict:
        """构建并缓存 TF-IDF 索引。

        Returns:
            {"corpus_df": {...}, "total_docs": int}
        """
        all_cues = self._store.list_all()
        # 过滤 stale_confirmed
        filtered = [c for c in all_cues if c.get("status") != "stale_confirmed"]
        corpus_df = _build_corpus_df(filtered)
        return {
            "corpus_df": corpus_df,
            "total_docs": len(filtered),
        }

    def invalidate_cache(self) -> None:
        """清除内部索引缓存，下次 recall 时将重新构建。"""
        self._index_cache = None


# ======================================================================
# 辅助函数
# ======================================================================

def _compute_tfidf(
    query_tokens: list[str],
    cue_keywords: list[str],
    corpus_dfs: dict[str, int],
    total_docs: int,
) -> float:
    """计算查询与线索关键词的 TF-IDF 余弦相似度。"""
    if not query_tokens or not cue_keywords or total_docs == 0:
        return 0.0

    q_tf = Counter(query_tokens)
    c_tf = Counter(kw.lower() for kw in cue_keywords)
    all_terms = set(q_tf.keys()) | set(c_tf.keys())

    score = 0.0
    q_norm = 0.0
    c_norm = 0.0

    for term in all_terms:
        df = corpus_dfs.get(term, 0)
        idf = math.log((total_docs + 1) / (df + 1)) + 1.0
        q_w = q_tf.get(term, 0) * idf
        c_w = c_tf.get(term, 0) * idf
        score += q_w * c_w
        q_norm += q_w * q_w
        c_norm += c_w * c_w

    if q_norm == 0 or c_norm == 0:
        return 0.0
    return score / (math.sqrt(q_norm) * math.sqrt(c_norm))


def _build_corpus_df(all_cues: list[dict]) -> dict[str, int]:
    """构建所有线索关键词的文档频率。"""
    df: Counter = Counter()
    for cue in all_cues:
        keywords = cue.get("keywords", [])
        if isinstance(keywords, list):
            for kw in set(keywords):
                df[kw.lower()] += 1
    return dict(df)


def _compute_time_decay(created_str: str, days_window: int, now) -> float:
    """计算时间衰减因子。

    规则：
    - created 距 now 在 days_window 天内 → 1.0
    - 超过 days_window 后线性衰减到 0.1（在 year_window 天内）
    """
    if not created_str:
        return 1.0

    try:
        # 支持多种 ISO 格式
        created_str = created_str.replace("T", " ").split(".")[0].split("+")[0]
        created = datetime.strptime(created_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            created = datetime.strptime(created_str[:10], "%Y-%m-%d")
        except ValueError:
            return 1.0

    delta = now - created
    delta_days = delta.days

    if delta_days <= days_window:
        return 1.0

    # 线性衰减到 TIME_DECAY_FLOOR，在 year_window 天内完成
    year_window = TIME_DECAY_YEAR_WINDOW
    decay_range = year_window - days_window
    if delta_days >= year_window:
        return TIME_DECAY_FLOOR

    ratio = (delta_days - days_window) / decay_range
    return max(TIME_DECAY_FLOOR, 1.0 - ratio * 0.9)
