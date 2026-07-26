"""
Smart Memory v3 — 决策检查点

纯规则引擎，完全无 LLM 依赖。三步决策：
Step 0: 快速短路 → Step 1: 规模评估 → Step 2: 质量评估 → Step 3: 最终裁决
"""

import sqlite3
from typing import Optional

from .cues import CueStore
from .tokenizer import tokenize


class DecideEngine:
    """纯规则决策引擎，判断召回结果的处理策略。"""

    def __init__(self, conn: sqlite3.Connection | None = None, db_path: Optional[str] = None):
        """初始化决策引擎。

        Args:
            conn: 外部 SQLite 连接，None 则使用默认单例连接。
            db_path: SQLite 数据库路径。
        """
        self._db_path = db_path
        self._cue_store = CueStore(conn=conn, db_path=db_path)
        # 初始化时加载所有 active cue 的 keywords+scene 到内存（SPEC §5.2 <5ms）
        self._active_keyword_sets: list[set[str]] = []
        self._refresh_active_index()

    def __repr__(self) -> str:
        return f"DecideEngine(db_path={self._db_path!r})"

    def _refresh_active_index(self):
        """从 SQLite 一次性加载所有 active cue 的 keywords+scene 集合。"""
        active_cues = self._cue_store.list_active()
        self._active_keyword_sets = []
        for cue in active_cues:
            tokens = set()
            keywords = cue.get("keywords", [])
            if isinstance(keywords, list):
                for kw in keywords:
                    if isinstance(kw, str):
                        tokens.add(kw.lower())
            scene = cue.get("scene", "")
            if scene:
                scene_tokens = tokenize(scene)
                tokens.update(t.lower() for t in scene_tokens)
            if tokens:
                self._active_keyword_sets.append(tokens)

    # ==================================================================
    # 公共入口
    # ==================================================================

    def decide(self, query: str, recall_result: dict) -> dict:
        """三步决策主入口。

        Args:
            query: 用户原始查询
            recall_result: recall() 的返回结构

        Returns:
            {
                "action": "skip" | "inject_l1" | "inject_l2" | "full_inject",
                "card_ids": [...],
                "reason": str,
                "stats": {
                    "l1_count": int,
                    "l2_count": int,
                    "avg_relevance": float,
                    "redundancy": float,
                },
            }
        """
        l1_results = recall_result.get("l1_results", [])
        l2_results = recall_result.get("l2_results")
        l2_triggered = recall_result.get("l2_triggered", False)

        # Step 0: 反向语义匹配短路
        step0 = self._step0_shortcut(query)
        if step0 is not None:
            return step0

        # Step 1: 规模评估
        l1_count = len(l1_results)
        step1 = self._step1_scale(l1_count, l2_triggered)

        # Step 2: 质量评估
        step2 = self._step2_quality(l2_results)

        # Step 3: 最终裁决
        return self._step3_verdict(step1, step2, l1_results, l2_results)

    # ==================================================================
    # Step 0 — 快速短路
    # ==================================================================

    def _step0_shortcut(self, query: str) -> Optional[dict]:
        """SPEC §5.1 反向语义匹配短路。

        从 SQLite cues 表批量读取所有 active cue 的 keywords 和 scene，
        做集合反向匹配。若 user_msg 的 token 集与所有 cue keywords/scene
        的交集为空，直接短路返回 skip。

        性能：初始化时已一次性加载到 self._active_keyword_sets（SPEC §5.2），
        不在每次调用时重新查询 SQLite。
        """
        if not query or not query.strip():
            return {
                "action": "skip",
                "card_ids": [],
                "reason": "empty query",
                "stats": {
                    "l1_count": 0,
                    "l2_count": 0,
                    "avg_relevance": 0.0,
                    "redundancy": 0.0,
                },
            }

        query_tokens = set(t.lower() for t in tokenize(query))
        if not query_tokens:
            return {
                "action": "skip",
                "card_ids": [],
                "reason": "no tokens",
                "stats": {
                    "l1_count": 0,
                    "l2_count": 0,
                    "avg_relevance": 0.0,
                    "redundancy": 0.0,
                },
            }

        # 如果没有任何 active cue，直接短路
        if not self._active_keyword_sets:
            return {
                "action": "skip",
                "card_ids": [],
                "reason": "no active cues",
                "stats": {
                    "l1_count": 0,
                    "l2_count": 0,
                    "avg_relevance": 0.0,
                    "redundancy": 0.0,
                },
            }

        # 检查 query tokens 是否与至少一个 cue 的关键词/scene 有交集
        for kw_set in self._active_keyword_sets:
            if query_tokens & kw_set:
                return None  # 有交集，不短路，继续后续步骤

        # 完全无交集 → 短路
        return {
            "action": "skip",
            "card_ids": [],
            "reason": "no semantic match",
            "stats": {
                "l1_count": 0,
                "l2_count": 0,
                "avg_relevance": 0.0,
                "redundancy": 0.0,
            },
        }

    # ==================================================================
    # Step 1 — 规模评估
    # ==================================================================

    def _step1_scale(self, l1_count: int, l2_triggered: bool) -> str:
        """根据 L1 命中数量和 L2 触发状态评估规模。

        Returns:
            'skip' / 'few' / 'many_l1' / 'expanded'
        """
        if l1_count == 0:
            return "skip"
        if l1_count < 3:
            return "few"
        if l1_count >= 5 and l2_triggered:
            return "expanded"
        return "many_l1"

    # ==================================================================
    # Step 2 — 质量评估
    # ==================================================================

    def _step2_quality(self, l2_results: Optional[list[dict]]) -> dict:
        """基于 L2 展开后的内容计算质量指标。

        Returns:
            {"avg_relevance": float, "max_relevance": float, "redundancy": float}
        """
        if not l2_results:
            return {
                "avg_relevance": 0.0,
                "max_relevance": 0.0,
                "redundancy": 0.0,
            }

        # 取所有 content 计算冗余率
        contents = [r.get("content", "") for r in l2_results if r.get("content")]
        redundancy = _compute_global_redundancy(contents)

        # 从 L2 结果中提取 importance × retention 作为质量代理
        scores = []
        for r in l2_results:
            imp = r.get("importance", 0.5)
            ret = r.get("retention", 1.0)
            scores.append(imp * ret)

        if not scores:
            return {
                "avg_relevance": 0.0,
                "max_relevance": 0.0,
                "redundancy": redundancy,
            }

        return {
            "avg_relevance": round(sum(scores) / len(scores), 4),
            "max_relevance": round(max(scores), 4),
            "redundancy": round(redundancy, 4),
        }

    # ==================================================================
    # Step 3 — 最终裁决
    # ==================================================================

    def _step3_verdict(
        self,
        step1: str,
        step2: dict,
        l1_results: list[dict],
        l2_results: Optional[list[dict]],
    ) -> dict:
        """根据规模和质量的组合输出最终决策。

        规则：
        - skip → action='skip'
        - few → 建议直接读取少量卡片 → action='inject_l1'
        - many_l1 → 多匹配但无需展开 → action='inject_l1'
        - expanded → 已展开全文 → action='inject_l2'
        """
        l1_count = len(l1_results)

        # 提取 card_ids
        if step1 == "expanded" and l2_results:
            card_ids = [r.get("card_id") for r in l2_results]
        else:
            card_ids = [r.get("card_id") for r in l1_results]

        action_map = {
            "skip": "skip",
            "few": "inject_l1",
            "many_l1": "inject_l1",
            "expanded": "inject_l2",
        }

        reason_map = {
            "skip": "no match",
            "few": f"few matches ({l1_count}), suggest direct read",
            "many_l1": f"multiple matches ({l1_count}) without L2 expansion",
            "expanded": f"L2 expanded with {len(l2_results) if l2_results else 0} full-text cards",
        }

        l2_count = len(l2_results) if l2_results else 0

        stats = {
            "l1_count": l1_count,
            "l2_count": l2_count,
            "avg_relevance": step2.get("avg_relevance", 0.0),
            "redundancy": step2.get("redundancy", 0.0),
        }

        return {
            "action": action_map.get(step1, "skip"),
            "card_ids": card_ids,
            "reason": reason_map.get(step1, "unknown"),
            "stats": stats,
        }


# ======================================================================
# 辅助函数
# ======================================================================

def _compute_global_redundancy(contents: list[str]) -> float:
    """计算多段文本间的全局冗余率。

    使用平均成对 Jaccard 相似度（两两比较取均值）。
    """
    if len(contents) < 2:
        return 0.0

    token_sets = [set(tokenize(c)) for c in contents if c]
    token_sets = [ts for ts in token_sets if ts]

    if len(token_sets) < 2:
        return 0.0

    total_sim = 0.0
    pair_count = 0
    n = len(token_sets)
    for i in range(n):
        for j in range(i + 1, n):
            intersect = token_sets[i] & token_sets[j]
            union = token_sets[i] | token_sets[j]
            if union:
                total_sim += len(intersect) / len(union)
            pair_count += 1

    if pair_count == 0:
        return 0.0
    return total_sim / pair_count
