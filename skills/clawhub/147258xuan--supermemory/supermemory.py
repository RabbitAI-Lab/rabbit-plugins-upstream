#!/usr/bin/env python3
"""
SuperMemory V1.4 — 参考实现
MIT License | 小虾总

改进 (v1.3 → v1.4):
  - 🔍 字段加权 BM25：keywords 权重 2.0，digest 权重 1.0
  - 🎯 精确匹配加权：搜索词完整命中时额外 +2.0 × 字段权重

改进 (v1.2 → v1.3):
  - 🔍 BM25 评分：替代纯关键词匹配，考虑词频×逆文档频率×文档长度
  - 💾 内存缓存：索引和节点常驻内存，避免每次查询读磁盘
  - 📦 导出/导入/合并：export_all() / import_from() / merge_from() / export_all_json() / import_json()
  - 📅 时间搜索：search_by_time("2026") 按日期前缀匹配
  - ⚖️ 权重搜索：search_by_weight_range(min_w=70) 按权重区间
  - 📉 降级策略：无 BM25 命中时返回权重最高的记忆

改进 (v1.1 → v1.2):
  - 🆕 Pinned 锁定：pin()/unpin() 永久保护关键记忆
  - 📖 窄门复活参数透明化（REVIVE_THRESHOLD/REVIVE_WINDOW/REVIVE_WEIGHT）
  - 🛡️ 衰减引擎自动跳过 pinned 节点
  - 📊 stats() 新增 pinned_count

改进 (v1.0 → v1.1):
  - jieba 中文分词 (+n-gram 回退)
  - 完整三级索引 (keywords + time + weight)
  - 自动赋权规则
  - 按权重区间分档衰减
  - JSON 导出
"""

import json
import os
import math
import time
import random
import re
from datetime import datetime

# ─── 可选中文分词 ───
try:
    import jieba
    HAS_JIEBA = True
except ImportError:
    HAS_JIEBA = False


def tokenize(text: str, min_len: int = 1) -> list[str]:
    """
    中文友好分词。
    优先 jieba，回退时走 n-gram(2-4) + 空格分割混用。
    """
    if not text:
        return []
    if HAS_JIEBA:
        tokens = list(jieba.cut(text))
    else:
        parts = re.split(r'[\s,，。.!！?？;；:：、\n]+', text)
        tokens = []
        for part in parts:
            if not part:
                continue
            for n in range(2, min(5, len(part) + 1)):
                for i in range(len(part) - n + 1):
                    tokens.append(part[i : i + n])
    return [t.strip() for t in tokens if len(t.strip()) >= min_len]


# ─── BM25 参数 ───
BM25_K1 = 1.5
BM25_B = 0.75


def bm25_score(query_tokens, doc_tokens, doc_len, avg_doc_len, df, N):
    """
    BM25 相似度评分。
    比纯关键词匹配更准确：考虑词频、文档长度、逆文档频率。
    """
    score = 0.0
    doc_tf = {}
    for t in doc_tokens:
        doc_tf[t] = doc_tf.get(t, 0) + 1
    for qt in query_tokens:
        if qt not in df:
            continue
        tf = doc_tf.get(qt, 0)
        idf = math.log((N - df[qt] + 0.5) / (df[qt] + 0.5) + 1)
        tf_norm = (tf * (BM25_K1 + 1)) / (tf + BM25_K1 * (1 - BM25_B + BM25_B * doc_len / max(avg_doc_len, 1)))
        score += idf * tf_norm
    return score


class SuperMemory:
    """V1.2 — 锁定版记忆引擎"""

    def __init__(self, path: str = "./memory"):
        self.path = path
        self.nodes_dir = os.path.join(path, "nodes")
        self.index_dir = os.path.join(path, "index")
        os.makedirs(self.nodes_dir, exist_ok=True)
        os.makedirs(self.index_dir, exist_ok=True)

        # ─── 内存缓存（避免每次查询读磁盘）───
        self._cache = {
            "nodes": {},       # nid -> node dict
            "keywords": None,  # keyword index
            "time": None,      # time index
            "weight": None,    # weight index
        }

        # ─── 分档衰减常数 ───
        self.DECAY_TAU_MAP = {
            "permanent": 365 * 86400,   # W≥95 几乎不衰减
            "high": 30 * 86400,         # 70-94
            "mid": 14 * 86400,          # 40-69
            "low": 7 * 86400,           # 10-39
            "ephemeral": 3 * 86400,     # <10
        }
        self.FORGET_THRESHOLD = 10

        # ─── 窄门复活参数（V1.2 透明化）───
        self.REVIVE_THRESHOLD = 8      # 复活最低门槛：权重≥8才进窄门
        self.REVIVE_WINDOW = 7 * 86400 # 复活窗口：7天内被访问才触发复活
        self.REVIVE_WEIGHT = 30        # 复活后恢复到 W=30

        # ─── Pinned 锁定（V1.2 新增）───
        self.PINNED_WEIGHT = 101       # 锁定记忆的显示权重

        # ─── 字段加权（V1.4 新增）───
        self.FIELD_WEIGHTS = {
            "keywords": 2.0,   # 关键词命中权重更高
            "digest": 1.0,     # 摘要命中权重
        }
        self.EXACT_MATCH_BONUS = 2.0  # 精确匹配额外加分

    # ═══ 公开 API ═══

    def remember(self, content: str, weight: int | None = None,
                 keywords: list[str] | None = None,
                 pinned: bool = False) -> str:
        """
        写入一条新记忆。

        Args:
            content: 记忆内容（≤200字符）
            weight: 权重 0-101，None 时自动赋权
            keywords: 关键词列表，None 时自动提取
            pinned: 是否永久锁定（V1.2 新增）。锁定的记忆永不衰减，不受权重影响。

        Returns:
            节点 ID
        """
        node = {
            "id": self._make_id(),
            "digest": content[:200],
            "keywords": keywords or self._extract_kw(content),
            "weight": weight if weight is not None else self._auto_weight(content),
            "pinned": pinned,  # V1.2 新增
            "created_at": datetime.now().isoformat(),
            "last_access": datetime.now().isoformat(),
            "times_accessed": 1,
            "_auto_weighted": weight is None,
        }
        self._save_node(node)
        self._update_index(node, "add")
        return node["id"]

    def recall(self, query: str, top_k: int = 5) -> list[dict]:
        """
        按查询词检索记忆（BM25 评分）。
        更新 last_access 以触发窄门复活。Pinned 记忆优先排列。
        """
        kws = self._extract_kw(query)
        if not kws:
            return []

        # BM25: 收集文档频率
        kw_idx = self._load_index("keywords")
        candidates: set = set()
        df: dict = {}  # 词 -> 出现在多少文档中
        for kw in kws:
            doc_ids = kw_idx.get(kw, [])
            candidates.update(doc_ids)
            df[kw] = len(doc_ids)

        if not candidates:
            # 降级：无关键词命中时，返回权重最高的记忆
            all_nodes = [self._load_node(nid) for nid in self._all_node_ids()]
            all_nodes = [n for n in all_nodes if n]
            all_nodes.sort(key=lambda n: (not n.get("pinned", False), -n.get("weight", 0)))
            return all_nodes[:top_k]

        nodes = []
        doc_lens = []
        for nid in candidates:
            node = self._load_node(nid)
            if node:
                nodes.append(node)
                doc_lens.append(len(node.get("keywords", [])))

        if not nodes:
            return []

        avg_doc_len = sum(doc_lens) / len(doc_lens) if doc_lens else 1
        N = len(nodes)

        # BM25 评分（字段加权 + 精确匹配加权）
        scored = []
        for i, node in enumerate(nodes):
            is_pinned = node.get("pinned", False)
            kw_tokens = node.get("keywords", [])
            digest_tokens = tokenize(node.get("digest", ""), min_len=2)
            
            # 字段加权 BM25
            kw_bm = bm25_score(kws, kw_tokens, len(kw_tokens), avg_doc_len, df, N) * self.FIELD_WEIGHTS["keywords"]
            dg_bm = bm25_score(kws, digest_tokens, len(digest_tokens), avg_doc_len, df, N) * self.FIELD_WEIGHTS["digest"]
            bm = kw_bm + dg_bm
            
            # 精确匹配加权：搜索词完整出现在关键词中
            kw_text = " ".join(kw_tokens).lower()
            dg_text = node.get("digest", "").lower()
            for qk in kws:
                if qk in kw_text:
                    bm += self.EXACT_MATCH_BONUS * self.FIELD_WEIGHTS["keywords"]
                if qk in dg_text:
                    bm += self.EXACT_MATCH_BONUS * self.FIELD_WEIGHTS["digest"]
            
            if is_pinned:
                bm += 1000  # Pinned 节点加权保证排最前
            scored.append((bm, node))

        scored.sort(key=lambda x: -x[0])
        result = [n for _, n in scored[:top_k]]

        # 窄门复活：更新访问时间 + 权重（pinned 节点只更新 access，不调权重）
        now = datetime.now()
        for node in result:
            node["times_accessed"] += 1
            node["last_access"] = now.isoformat()
            if node.get("pinned"):
                pass  # 锁定节点不参与复活波动
            elif self.REVIVE_THRESHOLD <= node["weight"] <= 10:
                node["weight"] = self.REVIVE_WEIGHT
            self._save_node(node)
            self._update_index(node, "add")

        return result

    def decay(self) -> list[dict]:
        """执行一轮衰减检查。Pinned 节点自动跳过，永不衰减。返回被遗忘的节点列表。"""
        now = time.time()
        forgotten = []

        for nid in self._all_node_ids():
            node = self._load_node(nid)
            if not node:
                continue

            # 🆕 V1.2: Pinned 节点永不衰减
            if node.get("pinned"):
                # 仍然更新 last_access（保持活跃统计）
                continue

            w = node.get("weight", 50)
            age = now - datetime.fromisoformat(node["created_at"]).timestamp()
            tau = self._tau_for_weight(w)
            new_w = w * math.exp(-age / tau)

            if new_w < self.FORGET_THRESHOLD:
                p_delete = ((self.FORGET_THRESHOLD - new_w) / self.FORGET_THRESHOLD) ** 2

                if w >= self.REVIVE_THRESHOLD:
                    # 窄门复活：降至临界区但不删
                    node["weight"] = max(new_w, self.REVIVE_THRESHOLD)
                elif random.random() < p_delete:
                    self._forget(node)
                    forgotten.append({
                        "id": node["id"],
                        "digest": node["digest"],
                        "weight_before": w,
                        "weight_final": round(new_w, 1),
                        "reason": "weight_decay",
                    })
                    continue

            node["weight"] = round(max(new_w, 0), 1)
            self._save_node(node)
            self._update_index(node, "add")

        return forgotten

    # ═══ Pinned 锁定 API（V1.2 新增）═══

    def pin(self, node_id: str) -> bool:
        """
        锁定一条记忆，使其永不衰减。

        适用于：用户红线、API Key、核心身份、铁律等不能遗忘的信息。
        锁定后 weight 设为 PINNED_WEIGHT(101)，decay() 永远跳过。

        Args:
            node_id: 节点 ID

        Returns:
            是否成功
        """
        node = self._load_node(node_id)
        if not node:
            return False
        node["pinned"] = True
        node["weight_before_pin"] = node.get("weight")  # 保留原始权重
        node["weight"] = self.PINNED_WEIGHT
        node["pinned_at"] = datetime.now().isoformat()
        self._save_node(node)
        self._update_index(node, "add")
        return True

    def unpin(self, node_id: str) -> bool:
        """
        解锁一条记忆，恢复其原始权重，重新参与衰减。

        Args:
            node_id: 节点 ID

        Returns:
            是否成功
        """
        node = self._load_node(node_id)
        if not node or not node.get("pinned"):
            return False
        node["pinned"] = False
        node["weight"] = node.get("weight_before_pin", 50)  # 恢复原始权重
        node["unpinned_at"] = datetime.now().isoformat()
        self._save_node(node)
        self._update_index(node, "add")
        return True

    def list_pinned(self) -> list[dict]:
        """列出所有已锁定的记忆。"""
        nodes = [self._load_node(nid) for nid in self._all_node_ids()]
        return [n for n in nodes if n and n.get("pinned")]

    # ═══ V1.1 已有 API ═══

    def export_json(self, out_path: str, min_weight: int = 0) -> int:
        """导出所有记忆为 JSON 文件。Pinned 节点标记 `pinned: true`。"""
        nodes = []
        for nid in self._all_node_ids():
            node = self._load_node(nid)
            if node and node.get("weight", 0) >= min_weight:
                nodes.append(node)

        nodes.sort(key=lambda n: (not n.get("pinned", False), n.get("weight", 0)), reverse=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(
                {"exported_at": datetime.now().isoformat(), "count": len(nodes), "nodes": nodes},
                f, ensure_ascii=False, indent=2,
            )
        return len(nodes)

    def stats(self) -> dict:
        """获取记忆系统统计信息"""
        nodes = [self._load_node(nid) for nid in self._all_node_ids()]
        nodes = [n for n in nodes if n]
        weights = [n.get("weight", 0) for n in nodes]
        pinned_count = sum(1 for n in nodes if n.get("pinned"))
        return {
            "total_nodes": len(nodes),
            "pinned": pinned_count,
            "permanent": sum(1 for w in weights if w >= 95),
            "high_value": sum(1 for w in weights if 70 <= w < 95),
            "mid_value": sum(1 for w in weights if 40 <= w < 70),
            "low_value": sum(1 for w in weights if 10 <= w < 40),
            "forgetting_zone": sum(1 for w in weights if w < 10),
            "avg_weight": round(sum(weights) / len(weights), 1) if weights else 0,
            "oldest": min((n["created_at"] for n in nodes), default="N/A"),
            "newest": max((n["created_at"] for n in nodes), default="N/A"),
        }

    # ═══ 内部方法 ═══

    def _make_id(self) -> str:
        return datetime.now().strftime("%Y%m%d-") + f"{random.randint(100, 999)}"

    def _extract_kw(self, text: str) -> list[str]:
        """关键词提取：jieba 中文 + 去重去噪"""
        tokens = tokenize(text, min_len=2)
        seen = set()
        result = []
        for t in tokens:
            if t not in seen and not re.match(r'^[\d\W_]+$', t):
                seen.add(t)
                result.append(t)
        return result[:8]

    def _auto_weight(self, content: str) -> int:
        """
        自动赋权规则。

        基于内容特征：
          - 含「永久/铁律/身份」等 → 95+
          - 含「项目/计划/目标」等 → 70-85
          - 含「偏好/习惯/喜欢/讨厌」 → 60-75
          - 含「日常/午饭/晚饭/今天」 → 30-45
          - 默认 → 50
        """
        text = content.lower()
        rules = [
            (["永久", "铁律", "身份", "诞生", "架构", "核心", "api key", "密钥", "密码", "红线"], 95),
            (["项目", "计划", "战略", "目标", "决定"], 75),
            (["偏好", "习惯", "喜欢", "讨厌", "爱吃", "不吃"], 65),
            (["学习", "笔记", "观点", "想法", "教训"], 55),
            (["日常", "午饭", "晚饭", "今天", "昨天", "吃了"], 35),
        ]
        for keywords, base_weight in rules:
            if any(kw in text for kw in keywords):
                return base_weight
        return 50

    def _tau_for_weight(self, weight: float) -> int:
        """根据权重返回衰减常数 τ"""
        if weight >= 95:
            return self.DECAY_TAU_MAP["permanent"]
        elif weight >= 70:
            return self.DECAY_TAU_MAP["high"]
        elif weight >= 40:
            return self.DECAY_TAU_MAP["mid"]
        elif weight >= 10:
            return self.DECAY_TAU_MAP["low"]
        else:
            return self.DECAY_TAU_MAP["ephemeral"]

    def _node_path(self, nid: str) -> str:
        return os.path.join(self.nodes_dir, f"{nid}.json")

    def _save_node(self, node: dict):
        with open(self._node_path(node["id"]), "w", encoding="utf-8") as f:
            json.dump(node, f, ensure_ascii=False)

    def _load_node(self, nid: str) -> dict | None:
        p = self._node_path(nid)
        if not os.path.exists(p):
            return None
        with open(p, encoding="utf-8") as f:
            return json.load(f)

    def _all_node_ids(self) -> list[str]:
        return [f.replace(".json", "") for f in os.listdir(self.nodes_dir) if f.endswith(".json")]

    # ─── 三级索引 ───

    def _load_index(self, name: str) -> dict:
        """加载索引，优先读缓存"""
        if self._cache[name] is not None:
            return self._cache[name]
        p = os.path.join(self.index_dir, f"{name}.json")
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {}
        self._cache[name] = data
        return data

    def _save_index(self, name: str, data: dict):
        """保存索引：更新缓存 + 写盘"""
        self._cache[name] = data
        with open(os.path.join(self.index_dir, f"{name}.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    def _load_node(self, nid: str) -> dict | None:
        """加载节点，优先读缓存"""
        if nid in self._cache["nodes"]:
            return self._cache["nodes"][nid]
        p = self._node_path(nid)
        if not os.path.exists(p):
            return None
        with open(p, encoding="utf-8") as f:
            node = json.load(f)
        self._cache["nodes"][nid] = node
        return node

    def _save_node(self, node: dict):
        """保存节点：更新缓存 + 写盘"""
        self._cache["nodes"][node["id"]] = node
        with open(self._node_path(node["id"]), "w", encoding="utf-8") as f:
            json.dump(node, f, ensure_ascii=False)

    def _update_index(self, node: dict, action: str):
        nid = node["id"]

        # 1) keywords
        kw_idx = self._load_index("keywords")
        for kw in node.get("keywords", []):
            if action == "add":
                arr = kw_idx.setdefault(kw, [])
                if nid not in arr:
                    arr.append(nid)
            elif action == "remove":
                if kw in kw_idx and nid in kw_idx[kw]:
                    kw_idx[kw].remove(nid)
                    if not kw_idx[kw]:
                        del kw_idx[kw]
        self._save_index("keywords", kw_idx)

        # 2) time
        time_idx = self._load_index("time")
        date_key = node.get("created_at", "")[:10]
        if action == "add":
            arr = time_idx.setdefault(date_key, [])
            if nid not in arr:
                arr.append(nid)
        elif action == "remove":
            if date_key in time_idx and nid in time_idx[date_key]:
                time_idx[date_key].remove(nid)
                if not time_idx[date_key]:
                    del time_idx[date_key]
        self._save_index("time", time_idx)

        # 3) weight
        weight_idx = self._load_index("weight")
        w = node.get("weight", 50)
        bucket = self._weight_bucket(w)
        if action == "add":
            arr = weight_idx.setdefault(bucket, [])
            if nid not in arr:
                arr.append(nid)
        elif action == "remove":
            if bucket in weight_idx and nid in weight_idx[bucket]:
                weight_idx[bucket].remove(nid)
                if not weight_idx[bucket]:
                    del weight_idx[bucket]
        self._save_index("weight", weight_idx)

    @staticmethod
    def _weight_bucket(w: float) -> str:
        if w >= 95:
            return "permanent"
        elif w >= 70:
            return "high"
        elif w >= 40:
            return "mid"
        elif w >= 10:
            return "low"
        return "forgetting"

    def _forget(self, node: dict):
        """遗忘节点：生成碎片 → 从索引移除 → 删除节点文件"""
        frag = {
            "id": node["id"],
            "digest": node["digest"],
            "keywords": node.get("keywords", []),
            "weight_before": node.get("weight"),
            "forgotten_at": datetime.now().isoformat(),
        }
        frag_dir = os.path.join(self.path, "fragments")
        os.makedirs(frag_dir, exist_ok=True)
        frag_path = os.path.join(frag_dir, f"{node['id']}.frag")
        with open(frag_path, "w", encoding="utf-8") as f:
            json.dump(frag, f, ensure_ascii=False)
        self._update_index(node, "remove")
        os.remove(self._node_path(node["id"]))


# ═══ 命令行 ═══

# ─── 导出/导入/合并 (V1.3 新增) ───

    def export_all(self) -> dict:
        """
        导出所有记忆为可序列化字典。
        可用于备份、迁移、跨实例同步。
        """
        all_nodes = []
        for nid in self._all_node_ids():
            node = self._load_node(nid)
            if node:
                all_nodes.append(node)
        return {
            "version": "1.3",
            "exported_at": datetime.now().isoformat(),
            "count": len(all_nodes),
            "nodes": all_nodes,
        }

    def import_from(self, data: dict, skip_duplicates: bool = True) -> int:
        """
        从导出数据导入记忆。
        返回实际导入的条数。跳过已存在的节点。
        """
        nodes = data.get("nodes", [])
        imported = 0
        for node in nodes:
            nid = node.get("id", "")
            if not nid:
                continue
            if skip_duplicates and self._load_node(nid):
                continue
            self._save_node(node)
            self._update_index(node, "add")
            imported += 1
        return imported

    def merge_from(self, other_path: str) -> dict:
        """
        合并另一个 SuperMemory 实例的记忆。
        返回 {"imported": N, "skipped": N}。
        """
        other = SuperMemory(path=other_path)
        other_data = other.export_all()
        imported = self.import_from(other_data, skip_duplicates=True)
        return {
            "imported": imported,
            "skipped": other_data["count"] - imported,
            "total": self.stats()["total_nodes"],
        }

    def export_json(self, filepath: str):
        """导出为 JSON 文件"""
        data = self.export_all()
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def import_json(self, filepath: str) -> int:
        """从 JSON 文件导入"""
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
        return self.import_from(data)

    def search_by_time(self, date_str: str) -> list:
        """按日期搜索记忆 (YYYY-MM-DD 或前缀匹配)"""
        time_idx = self._load_index("time")
        results = []
        for date_key, nids in time_idx.items():
            if date_key.startswith(date_str):
                for nid in nids:
                    node = self._load_node(nid)
                    if node:
                        results.append(node)
        results.sort(key=lambda n: n.get("created_at", ""), reverse=True)
        return results

    def search_by_weight_range(self, min_w: int = 0, max_w: int = 100) -> list:
        """按权重范围搜索"""
        results = []
        for nid in self._all_node_ids():
            node = self._load_node(nid)
            if node and min_w <= node.get("weight", 0) <= max_w:
                results.append(node)
        results.sort(key=lambda n: -n.get("weight", 0))
        return results


if __name__ == "__main__":
    import sys

    m = SuperMemory()

    if "export" in sys.argv:
        path = sys.argv[2] if len(sys.argv) > 2 else "supermemory_export.json"
        n = m.export_json(path)
        print(f"✅ 导出 {n} 条记忆 → {path}")

    elif "stats" in sys.argv:
        s = m.stats()
        for k, v in s.items():
            print(f"  {k}: {v}")

    elif "pinned" in sys.argv:
        pinned = m.list_pinned()
        if pinned:
            print(f"🔒 已锁定 {len(pinned)} 条:")
            for p in pinned:
                print(f"  [{p['id']}] {p['digest'][:60]}")
        else:
            print("未锁定任何记忆")

    else:
        # 演示
        print("=== SuperMemory V1.2 演示 ===\n")

        m.remember("宇宸总爱吃香菜，不吃辣", weight=80, keywords=["宇宸总", "香菜", "辣", "饮食"])
        m.remember("小虾总诞生于2026年5月18日", weight=101, keywords=["小虾总", "诞生", "2026", "5月18日"])
        m.remember("今天的午饭是宫保鸡丁外卖", keywords=["午饭", "外卖", "宫保鸡丁"])
        m.remember("用户红线：永不授权给大厂，禁止商业化", weight=95,
                   keywords=["红线", "授权", "大厂", "商业化"], pinned=True)
        m.remember("宸总偏好：不喜欢吃辣椒，做菜不放辣", weight=85, keywords=["宸总", "辣椒", "饮食", "偏好"])

        print("写入 5 条记忆（1 条已锁定 🔒）\n")

        print("查询: '宸总吃什么'")
        for r in m.recall("宸总吃什么"):
            pin_tag = "🔒" if r.get("pinned") else ""
            w = r["weight"]
            tag = "★" if w >= 95 else ("◆" if w >= 70 else "○")
            print(f"  {pin_tag}[{tag} W{w}] {r['digest']}")

        print(f"\n统计: {json.dumps(m.stats(), ensure_ascii=False, indent=2)}")

        print("\n衰减检查...")
        forgotten = m.decay()
        print(f"  遗忘: {len(forgotten)} 条")
        for fg in forgotten:
            print(f"    ❌ {fg['digest'][:40]}... (W{fg['weight_before']}→{fg['weight_final']})")

        print("\n锁定节点检查:")
        pinned = m.list_pinned()
        if pinned:
            print(f"  ✅ {len(pinned)} 条锁定记忆未被衰减影响")
        else:
            print("  ⚠️ 无锁定记忆（如果之前有锁定则该 bug）")

