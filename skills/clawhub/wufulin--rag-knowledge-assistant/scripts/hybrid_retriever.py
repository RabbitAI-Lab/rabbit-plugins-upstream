#!/usr/bin/env python3
"""
混合检索核心模块 (Hybrid Search)
结合 BM25 关键词检索 + 向量语义检索，使用 RRF 融合排序

支持中文分词 (jieba)，适用于中英文混合文档
"""

import os
import json
import pickle
import numpy as np
from pathlib import Path
from typing import List, Tuple, Dict, Any, Optional
from dataclasses import dataclass

# 中文分词
try:
    import jieba
    JIEBA_AVAILABLE = True
except ImportError:
    JIEBA_AVAILABLE = False

# BM25
try:
    from rank_bm25 import BM25Okapi
    BM25_AVAILABLE = True
except ImportError:
    BM25_AVAILABLE = False


@dataclass
class SearchResult:
    """检索结果"""
    doc_id: str
    content: str
    metadata: Dict[str, Any]
    bm25_score: float = 0.0
    vector_score: float = 0.0
    hybrid_score: float = 0.0
    rank_bm25: int = 0
    rank_vector: int = 0


class HybridRetriever:
    """
    混合检索器：BM25 + 向量语义检索 + RRF 融合
    
    参数:
        bm25_weight: BM25 检索权重 (0-1)，默认 0.4
        vector_weight: 向量检索权重 (0-1)，默认 0.6
        rrf_k: RRF 融合参数，默认 60
        top_k: 返回结果数量，默认 10
    """
    
    def __init__(
        self,
        bm25_weight: float = 0.4,
        vector_weight: float = 0.6,
        rrf_k: int = 60,
        top_k: int = 10,
        use_jieba: bool = True
    ):
        self.bm25_weight = bm25_weight
        self.vector_weight = vector_weight
        self.rrf_k = rrf_k
        self.top_k = top_k
        self.use_jieba = use_jieba and JIEBA_AVAILABLE
        
        # 索引数据
        self.documents: List[Dict[str, Any]] = []  # 原始文档列表
        self.doc_ids: List[str] = []  # 文档 ID 列表
        self.bm25_index: Optional[BM25Okapi] = None
        self.vectorstore = None  # Chroma 向量库
        
        # 统计信息
        self.stats = {
            "total_docs": 0,
            "indexed_at": None,
            "bm25_enabled": False,
            "vector_enabled": False
        }
    
    def _tokenize(self, text: str) -> List[str]:
        """
        文本分词：中文使用 jieba，英文按空格分词
        """
        if not text:
            return []
        
        # 清理文本
        text = text.strip().lower()
        
        if self.use_jieba and JIEBA_AVAILABLE:
            # jieba 分词，支持中英文混合
            tokens = list(jieba.cut_for_search(text))
            # 过滤空字符串和单字符（保留英文单词）
            tokens = [t for t in tokens if t.strip() and (len(t) > 1 or t.isalpha())]
        else:
            # 简单空格分词（英文）
            tokens = text.split()
        
        return tokens
    
    def build_bm25_index(self, documents: List[Dict[str, Any]]):
        """
        构建 BM25 关键词索引
        
        Args:
            documents: 文档列表，每个文档包含 id, content, metadata
        """
        if not BM25_AVAILABLE:
            print("⚠️  rank-bm25 未安装，跳过 BM25 索引构建")
            print("   安装命令: pip install rank-bm25")
            return False
        
        print(f"\n📚 构建 BM25 关键词索引...")
        print(f"   文档数量: {len(documents)}")
        print(f"   分词工具: {'jieba (中文)' if self.use_jieba else '空格分词'}")
        
        self.documents = documents
        self.doc_ids = [doc.get("id", f"doc_{i}") for i, doc in enumerate(documents)]
        
        # 对每篇文档进行分词
        tokenized_docs = []
        for doc in documents:
            content = doc.get("content", "")
            tokens = self._tokenize(content)
            tokenized_docs.append(tokens)
        
        # 构建 BM25 索引
        self.bm25_index = BM25Okapi(tokenized_docs)
        self.stats["bm25_enabled"] = True
        self.stats["total_docs"] = len(documents)
        
        print(f"✓ BM25 索引构建完成")
        return True
    
    def bm25_search(self, query: str, top_k: Optional[int] = None) -> List[Tuple[str, float]]:
        """
        BM25 关键词检索
        
        Returns:
            List[(doc_id, score)] 按分数降序排列
        """
        if not self.bm25_index or not BM25_AVAILABLE:
            return []
        
        k = top_k or self.top_k * 2  # 多取一些用于融合
        
        # 查询分词
        query_tokens = self._tokenize(query)
        if not query_tokens:
            return []
        
        # BM25 检索
        scores = self.bm25_index.get_scores(query_tokens)
        
        # 获取 top-k 结果
        top_indices = np.argsort(scores)[::-1][:k]
        results = []
        for idx in top_indices:
            if scores[idx] > 0:
                results.append((self.doc_ids[idx], float(scores[idx])))
        
        return results
    
    def vector_search(self, query: str, vectorstore, top_k: Optional[int] = None) -> List[Tuple[str, float]]:
        """
        向量语义检索
        
        Args:
            query: 查询文本
            vectorstore: Chroma 向量库实例
            top_k: 返回数量
            
        Returns:
            List[(doc_id, score)] 按相似度降序排列（分数已归一化）
        """
        if not vectorstore:
            return []
        
        k = top_k or self.top_k * 2
        
        # 执行相似度搜索（Chroma 返回 L2 距离）
        results = vectorstore.similarity_search_with_score(query, k=k)
        
        # 转换 L2 距离为相似度分数 (0-1)
        # L2 距离越小越相似，使用指数衰减转换
        vector_results = []
        for i, (doc, l2_distance) in enumerate(results):
            # 使用与 BM25 索引相同的 doc_id 格式：source#chunk_index
            source = doc.metadata.get("source", "unknown")
            chunk_index = doc.metadata.get("chunk_index", i)
            doc_id = f"{source}#{chunk_index}"
            
            # L2 距离转相似度：使用高斯核
            # BGE-M3 的 L2 距离通常在 0-1000 范围
            max_dist = 1000.0
            normalized_dist = min(l2_distance / max_dist, 1.0)
            similarity = np.exp(-normalized_dist * 2)  # 指数衰减
            
            vector_results.append((doc_id, similarity))
        
        return vector_results
    
    def rrf_fusion(
        self,
        bm25_results: List[Tuple[str, float]],
        vector_results: List[Tuple[str, float]]
    ) -> List[SearchResult]:
        """
        RRF (Reciprocal Rank Fusion) 融合排序
        
        公式: score = Σ 1 / (k + rank)
        
        Args:
            bm25_results: [(doc_id, score), ...] 按 BM25 分数降序
            vector_results: [(doc_id, score), ...] 按向量相似度降序
            
        Returns:
            List[SearchResult] 按融合分数降序
        """
        # 构建 doc_id -> rank 映射
        bm25_ranks = {doc_id: rank + 1 for rank, (doc_id, _) in enumerate(bm25_results)}
        vector_ranks = {doc_id: rank + 1 for rank, (doc_id, _) in enumerate(vector_results)}
        
        # 获取所有唯一文档 ID
        all_doc_ids = set(bm25_ranks.keys()) | set(vector_ranks.keys())
        
        # 构建 doc_id -> 文档内容映射
        doc_map = {doc.get("id", f"doc_{i}"): doc for i, doc in enumerate(self.documents)}
        
        # 计算 RRF 分数
        fused_results = []
        for doc_id in all_doc_ids:
            # RRF 公式
            bm25_rank = bm25_ranks.get(doc_id, float('inf'))
            vector_rank = vector_ranks.get(doc_id, float('inf'))
            
            bm25_rrf = 1.0 / (self.rrf_k + bm25_rank) if bm25_rank != float('inf') else 0
            vector_rrf = 1.0 / (self.rrf_k + vector_rank) if vector_rank != float('inf') else 0
            
            # 加权融合
            hybrid_score = (
                self.bm25_weight * bm25_rrf +
                self.vector_weight * vector_rrf
            )
            
            # 获取原始分数
            bm25_score = next((s for d, s in bm25_results if d == doc_id), 0.0)
            vector_score = next((s for d, s in vector_results if d == doc_id), 0.0)
            
            # 获取文档内容
            doc = doc_map.get(doc_id, {})
            
            result = SearchResult(
                doc_id=doc_id,
                content=doc.get("content", ""),
                metadata=doc.get("metadata", {}),
                bm25_score=bm25_score,
                vector_score=vector_score,
                hybrid_score=hybrid_score,
                rank_bm25=bm25_ranks.get(doc_id, 9999),
                rank_vector=vector_ranks.get(doc_id, 9999)
            )
            fused_results.append(result)
        
        # 按融合分数降序排序
        fused_results.sort(key=lambda x: x.hybrid_score, reverse=True)
        
        return fused_results
    
    def search(
        self,
        query: str,
        vectorstore=None,
        top_k: Optional[int] = None
    ) -> List[SearchResult]:
        """
        执行混合检索
        
        Args:
            query: 查询文本
            vectorstore: Chroma 向量库实例（可选）
            top_k: 返回结果数量
            
        Returns:
            List[SearchResult] 按融合分数降序
        """
        k = top_k or self.top_k
        
        print(f"\n🔍 混合检索: '{query}'")
        print(f"   BM25 权重: {self.bm25_weight}, 向量权重: {self.vector_weight}")
        
        # 1. BM25 关键词检索
        bm25_results = self.bm25_search(query)
        print(f"   BM25 检索: {len(bm25_results)} 个结果")
        
        # 2. 向量语义检索
        vector_results = []
        if vectorstore:
            vector_results = self.vector_search(query, vectorstore)
            print(f"   向量检索: {len(vector_results)} 个结果")
        
        # 3. RRF 融合
        if bm25_results and vector_results:
            # 两者都有，进行融合
            fused_results = self.rrf_fusion(bm25_results, vector_results)
            print(f"   RRF 融合: {len(fused_results)} 个结果")
        elif vector_results:
            # 只有向量结果
            fused_results = [
                SearchResult(
                    doc_id=doc_id,
                    content=next((d.get("content", "") for d in self.documents 
                                if d.get("id") == doc_id), ""),
                    metadata=next((d.get("metadata", {}) for d in self.documents 
                               if d.get("id") == doc_id), {}),
                    vector_score=score,
                    hybrid_score=score
                )
                for doc_id, score in vector_results
            ]
        elif bm25_results:
            # 只有 BM25 结果
            fused_results = [
                SearchResult(
                    doc_id=doc_id,
                    content=next((d.get("content", "") for d in self.documents 
                                if d.get("id") == doc_id), ""),
                    metadata=next((d.get("metadata", {}) for d in self.documents 
                               if d.get("id") == doc_id), {}),
                    bm25_score=score,
                    hybrid_score=score
                )
                for doc_id, score in bm25_results
            ]
        else:
            fused_results = []
        
        # 返回 top-k
        return fused_results[:k]
    
    def save_index(self, output_dir: str):
        """保存索引到磁盘"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # 保存 BM25 索引
        if self.bm25_index:
            bm25_path = output_path / "bm25_index.pkl"
            with open(bm25_path, 'wb') as f:
                pickle.dump({
                    'bm25_index': self.bm25_index,
                    'documents': self.documents,
                    'doc_ids': self.doc_ids,
                    'stats': self.stats
                }, f)
            print(f"✓ BM25 索引已保存: {bm25_path}")
        
        # 保存配置
        config = {
            'bm25_weight': self.bm25_weight,
            'vector_weight': self.vector_weight,
            'rrf_k': self.rrf_k,
            'top_k': self.top_k,
            'use_jieba': self.use_jieba,
            'stats': self.stats
        }
        config_path = output_path / "hybrid_config.json"
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        print(f"✓ 混合检索配置已保存: {config_path}")
    
    def load_index(self, index_dir: str) -> bool:
        """从磁盘加载索引"""
        index_path = Path(index_dir)
        
        # 加载 BM25 索引
        bm25_path = index_path / "bm25_index.pkl"
        if bm25_path.exists():
            with open(bm25_path, 'rb') as f:
                data = pickle.load(f)
                self.bm25_index = data['bm25_index']
                self.documents = data['documents']
                self.doc_ids = data['doc_ids']
                self.stats = data['stats']
            print(f"✓ BM25 索引已加载: {len(self.documents)} 个文档")
        
        # 加载配置
        config_path = index_path / "hybrid_config.json"
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                self.bm25_weight = config.get('bm25_weight', 0.4)
                self.vector_weight = config.get('vector_weight', 0.6)
                self.rrf_k = config.get('rrf_k', 60)
                self.top_k = config.get('top_k', 10)
                self.use_jieba = config.get('use_jieba', True)
        
        return self.bm25_index is not None


# 便捷函数
def create_hybrid_retriever(
    documents: List[Dict[str, Any]],
    bm25_weight: float = 0.4,
    vector_weight: float = 0.6,
    **kwargs
) -> HybridRetriever:
    """
    快速创建混合检索器并构建索引
    
    Args:
        documents: 文档列表 [{"id": str, "content": str, "metadata": dict}, ...]
        bm25_weight: BM25 权重
        vector_weight: 向量权重
        
    Returns:
        HybridRetriever 实例
    """
    retriever = HybridRetriever(
        bm25_weight=bm25_weight,
        vector_weight=vector_weight,
        **kwargs
    )
    retriever.build_bm25_index(documents)
    return retriever


if __name__ == "__main__":
    # 测试代码
    print("=" * 60)
    print("🧪 混合检索模块测试")
    print("=" * 60)
    
    # 测试文档
    test_docs = [
        {
            "id": "doc_1",
            "content": "Python 是一种高级编程语言，支持多种编程范式。",
            "metadata": {"source": "python_intro.md", "category": "编程"}
        },
        {
            "id": "doc_2",
            "content": "Java 是面向对象的编程语言，广泛用于企业级开发。",
            "metadata": {"source": "java_guide.md", "category": "编程"}
        },
        {
            "id": "doc_3",
            "content": "机器学习是人工智能的一个分支，使用统计方法让计算机从数据中学习。",
            "metadata": {"source": "ml_basics.md", "category": "AI"}
        },
        {
            "id": "doc_4",
            "content": "深度学习是机器学习的一种，使用神经网络进行特征提取。",
            "metadata": {"source": "deep_learning.md", "category": "AI"}
        },
        {
            "id": "doc_5",
            "content": "Python 在数据科学和机器学习领域非常流行。",
            "metadata": {"source": "python_ds.md", "category": "数据科学"}
        }
    ]
    
    # 创建检索器
    retriever = create_hybrid_retriever(test_docs, bm25_weight=0.4, vector_weight=0.6)
    
    # 测试查询
    queries = [
        "Python 编程语言",
        "机器学习算法",
        "深度学习神经网络"
    ]
    
    for query in queries:
        print(f"\n{'='*60}")
        print(f"查询: {query}")
        print(f"{'='*60}")
        
        # 单独测试 BM25
        bm25_results = retriever.bm25_search(query)
        print(f"\n📊 BM25 结果:")
        for doc_id, score in bm25_results[:3]:
            print(f"   {doc_id}: {score:.4f}")
        
        # 混合检索（无向量库）
        results = retriever.search(query)
        print(f"\n🔀 混合检索结果:")
        for r in results[:3]:
            print(f"   {r.doc_id}: hybrid={r.hybrid_score:.4f}, "
                  f"bm25={r.bm25_score:.4f}, vector={r.vector_score:.4f}")
            print(f"   内容: {r.content[:50]}...")
    
    print("\n✅ 测试完成!")
