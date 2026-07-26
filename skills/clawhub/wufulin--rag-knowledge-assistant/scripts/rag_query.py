#!/usr/bin/env python3
"""
RAG 向量检索脚本
使用向量相似度搜索知识库中的相关内容

使用方法:
    python rag_query.py "你的问题" [--vectorstore ./vectorstore] [--top-k 5]
"""

import os
import sys
import argparse
import json
from pathlib import Path

# Windows 控制台 UTF-8 支持
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# 检查依赖
try:
    from langchain_community.vectorstores import Chroma
    from langchain_community.embeddings import HuggingFaceEmbeddings
    print("✓ LangChain 依赖已加载")
except ImportError as e:
    print(f"✗ 缺少依赖：{e}")
    print("\n请安装必要的包:")
    print("  pip install langchain langchain-community chromadb")
    sys.exit(1)

# 混合检索模块
try:
    from hybrid_retriever import HybridRetriever, SearchResult
    HYBRID_AVAILABLE = True
except ImportError:
    HYBRID_AVAILABLE = False
    print("⚠️  混合检索模块未加载，将仅使用向量检索")
    print("   如需混合检索，请确保 hybrid_retriever.py 在同目录")


def load_vectorstore(vectorstore_dir: str):
    """加载已有的向量数据库"""
    vectorstore_path = Path(vectorstore_dir)
    
    if not vectorstore_path.exists():
        raise FileNotFoundError(
            f"向量数据库不存在：{vectorstore_dir}\n"
            "请先运行 index_knowledge.py 创建索引"
        )
    
    # 检查配置文件
    config_file = vectorstore_path / "index_config.json"
    hybrid_config = None
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print(f"✓ 加载配置：{config_file}")
        print(f"  - 知识库：{config.get('knowledge_dir', '未知')}")
        print(f"  - 文档数：{config.get('document_count', 0)}")
        print(f"  - 片段数：{config.get('chunk_count', 0)}")
        
        # 检查是否支持混合检索
        hybrid_config = config.get('hybrid_search', {})
        if hybrid_config.get('enabled', False):
            print(f"  - 混合检索：已启用")
            print(f"    BM25权重: {hybrid_config.get('bm25_weight', 0.4)}")
            print(f"    向量权重: {hybrid_config.get('vector_weight', 0.6)}")
    
    print(f"\n正在加载向量数据库：{vectorstore_path.absolute()}...")
    
    # 加载 BGE-M3 Embedding 模型
    print("加载 Embedding 模型 (BAAI/bge-m3)...")
    from transformers import AutoTokenizer, AutoModel
    import torch
    
    tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-m3")
    model = AutoModel.from_pretrained("BAAI/bge-m3")
    model.eval()
    
    class BGEM3Embeddings:
        def __init__(self, model, tokenizer):
            self.model = model
            self.tokenizer = tokenizer
        
        def embed_documents(self, texts):
            embeddings = []
            with torch.no_grad():
                for text in texts:
                    inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
                    outputs = self.model(**inputs)
                    attention_mask = inputs['attention_mask']
                    last_hidden = outputs.last_hidden_state
                    mask_expanded = attention_mask.unsqueeze(-1).expand(last_hidden.size()).float()
                    sum_embeddings = torch.sum(last_hidden * mask_expanded, 1)
                    sum_mask = torch.clamp(mask_expanded.sum(1), min=1e-9)
                    embedding = (sum_embeddings / sum_mask).squeeze().numpy()
                    embeddings.append(embedding)
            return embeddings
        
        def embed_query(self, text):
            return self.embed_documents([text])[0]
    
    embeddings = BGEM3Embeddings(model, tokenizer)
    
    # 加载向量库
    vectorstore = Chroma(
        persist_directory=str(vectorstore_path),
        embedding_function=embeddings,
        collection_name="knowledge_base"
    )
    
    print("✓ 向量数据库加载成功")
    return vectorstore, embeddings, hybrid_config


def load_hybrid_retriever(vectorstore_dir: str, hybrid_config: dict = None):
    """
    加载混合检索器
    
    Args:
        vectorstore_dir: 向量库目录
        hybrid_config: 混合检索配置
        
    Returns:
        HybridRetriever 实例或 None
    """
    if not HYBRID_AVAILABLE:
        return None
    
    # 检查 BM25 索引是否存在
    bm25_path = Path(vectorstore_dir) / "bm25_index.pkl"
    if not bm25_path.exists():
        print("⚠️  未找到 BM25 索引，将仅使用向量检索")
        print(f"   如需混合检索，请重新运行 index_knowledge.py --hybrid")
        return None
    
    print("\n🔧 加载混合检索器...")
    
    # 从配置获取权重
    bm25_weight = hybrid_config.get('bm25_weight', 0.4) if hybrid_config else 0.4
    vector_weight = hybrid_config.get('vector_weight', 0.6) if hybrid_config else 0.6
    rrf_k = hybrid_config.get('rrf_k', 60) if hybrid_config else 60
    
    retriever = HybridRetriever(
        bm25_weight=bm25_weight,
        vector_weight=vector_weight,
        rrf_k=rrf_k
    )
    
    if retriever.load_index(vectorstore_dir):
        print("✓ 混合检索器加载成功")
        return retriever
    else:
        print("⚠️  混合检索器加载失败")
        return None


def hybrid_search(
    query: str,
    vectorstore,
    hybrid_retriever: HybridRetriever = None,
    top_k: int = 5,
    score_threshold: float = 0.6,
    bm25_only: bool = False,
    vector_only: bool = False
):
    """
    执行混合检索（BM25 + 向量）
    
    Args:
        query: 查询文本
        vectorstore: Chroma 向量库
        hybrid_retriever: 混合检索器（可选）
        top_k: 返回结果数量
        score_threshold: 相似度阈值
        bm25_only: 仅使用 BM25
        vector_only: 仅使用向量
        
    Returns:
        List[SearchResult] 或 List[(doc, score)]
    """
    
    if bm25_only and hybrid_retriever and HYBRID_AVAILABLE:
        # 仅 BM25 模式
        print(f"\n🔍 BM25 关键词检索: '{query}'")
        bm25_results = hybrid_retriever.bm25_search(query, top_k=top_k)
        
        # 转换为 SearchResult
        results = []
        for doc_id, score in bm25_results:
            doc = next((d for d in hybrid_retriever.documents if d.get("id") == doc_id), {})
            results.append(SearchResult(
                doc_id=doc_id,
                content=doc.get("content", ""),
                metadata=doc.get("metadata", {}),
                bm25_score=score,
                hybrid_score=score
            ))
        
        print(f"\n✓ BM25 检索完成：{len(results)} 个相关片段")
        return results, True
        
    elif vector_only or not hybrid_retriever or not HYBRID_AVAILABLE:
        # 纯向量检索模式
        print(f"\n🔍 向量检索: '{query}'")
        print(f"   返回数量：top_k={top_k}")
        
        results = vectorstore.similarity_search_with_score(query, k=top_k)
        
        # 过滤低相似度结果
        filtered = []
        for doc, score in results:
            if score < 450:  # BGE-M3 经验阈值
                filtered.append((doc, score))
        
        print(f"\n✓ 找到 {len(filtered)} 个相关片段")
        return filtered, False  # False 表示是纯向量检索结果
    
    else:
        # 混合检索模式
        results = hybrid_retriever.search(query, vectorstore=vectorstore, top_k=top_k)
        
        # 过滤低分结果 - 对于小文档集降低阈值
        # 当文档数量少时，RRF 分数会偏低，需要更宽松的阈值
        adjusted_threshold = score_threshold * 0.5 if hybrid_retriever.stats.get("total_docs", 0) < 10 else score_threshold
        filtered = [r for r in results if r.hybrid_score >= adjusted_threshold]
        
        # 如果过滤后为空，返回原始结果（避免小文档集无结果）
        if not filtered and results:
            filtered = results[:top_k]
        
        print(f"\n✓ 混合检索完成：{len(filtered)} 个相关片段")
        print(f"   (BM25: {len([r for r in results if r.bm25_score > 0])}, "
              f"向量: {len([r for r in results if r.vector_score > 0])})")
        
        return filtered, True  # True 表示是混合检索结果


def format_hybrid_results(results: list, is_hybrid: bool = True):
    """格式化混合检索结果"""
    output = []
    
    if is_hybrid:
        # 混合检索结果
        for i, result in enumerate(results, 1):
            output.append(f"\n{'='*60}")
            output.append(f"📄 结果 #{i} (融合分数: {result.hybrid_score:.4f})")
            output.append(f"{'='*60}")
            
            # 显示各检索方式分数
            scores = []
            if result.bm25_score > 0:
                scores.append(f"BM25: {result.bm25_score:.4f}")
            if result.vector_score > 0:
                scores.append(f"向量: {result.vector_score:.4f}")
            if scores:
                output.append(f"分数详情: {', '.join(scores)}")
            
            # 显示来源
            source = result.metadata.get('source', '未知来源')
            output.append(f"来源：{source}")
            if 'page' in result.metadata:
                output.append(f"页码：{result.metadata['page']}")
            
            output.append(f"\n{result.content}")
    else:
        # 纯向量检索结果
        for i, (doc, score) in enumerate(results, 1):
            output.append(f"\n{'='*60}")
            output.append(f"📄 结果 #{i} (L2距离：{score:.2f}，越小越相关)")
            output.append(f"{'='*60}")
            
            source = doc.metadata.get('source', '未知来源')
            output.append(f"来源：{source}")
            if 'page' in doc.metadata:
                output.append(f"页码：{doc.metadata['page']}")
            
            output.append(f"\n{doc.page_content}")
    
    return "\n".join(output)


def format_results(results, include_metadata: bool = True):
    """格式化搜索结果（兼容旧版）"""
    output = []
    
    for i, (doc, score) in enumerate(results, 1):
        # L2 距离，越小越相似
        output.append(f"\n{'='*60}")
        output.append(f"📄 结果 #{i} (L2距离：{score:.2f}，越小越相关)")
        output.append(f"{'='*60}")
        
        if include_metadata:
            source = doc.metadata.get('source', '未知来源')
            output.append(f"来源：{source}")
            if 'page' in doc.metadata:
                output.append(f"页码：{doc.metadata['page']}")
        
        output.append(f"\n{doc.page_content}")
    
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="RAG 混合检索工具 (BM25 + 向量)")
    parser.add_argument(
        "query",
        nargs="?",
        help="检索问题"
    )
    parser.add_argument(
        "--vectorstore", "-v",
        default="./vectorstore",
        help="向量数据库目录 (默认：./vectorstore)"
    )
    parser.add_argument(
        "--top-k", "-k",
        type=int,
        default=5,
        help="返回结果数量 (默认：5)"
    )
    parser.add_argument(
        "--score-threshold", "-t",
        type=float,
        default=0.6,
        help="相似度阈值 (默认：0.6)"
    )
    parser.add_argument(
        "--hybrid",
        action="store_true",
        default=True,
        help="启用混合检索 (默认：True)"
    )
    parser.add_argument(
        "--bm25-only",
        action="store_true",
        help="仅使用 BM25 关键词检索"
    )
    parser.add_argument(
        "--vector-only",
        action="store_true",
        help="仅使用向量语义检索"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="以 JSON 格式输出结果"
    )
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="交互模式 (连续问答)"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🤖 OpenClaw RAG 智能检索 (混合检索版)")
    print("=" * 60)
    
    # 确定检索模式
    search_mode = "混合检索"
    if args.bm25_only:
        search_mode = "BM25 关键词检索"
        args.hybrid = False
    elif args.vector_only:
        search_mode = "向量语义检索"
        args.hybrid = False
    elif args.hybrid and HYBRID_AVAILABLE:
        search_mode = "混合检索 (BM25 + 向量)"
    
    print(f"\n🔍 检索模式: {search_mode}")
    
    try:
        # 加载向量库
        vectorstore, embeddings, hybrid_config = load_vectorstore(args.vectorstore)
        
        # 加载混合检索器
        hybrid_retriever = None
        if not args.vector_only and HYBRID_AVAILABLE:
            hybrid_retriever = load_hybrid_retriever(args.vectorstore, hybrid_config)
        
        # 交互模式
        if args.interactive or not args.query:
            print("\n💬 进入交互模式 (输入 'quit' 退出)")
            print("-" * 60)
            
            while True:
                try:
                    query = input("\n你的问题：").strip()
                    if query.lower() in ['quit', 'exit', 'q']:
                        print("再见！")
                        break
                    if not query:
                        continue
                    
                    results, is_hybrid = hybrid_search(
                        vectorstore=vectorstore,
                        query=query,
                        hybrid_retriever=hybrid_retriever,
                        top_k=args.top_k,
                        score_threshold=args.score_threshold,
                        bm25_only=args.bm25_only,
                        vector_only=args.vector_only
                    )
                    
                    if results:
                        print(format_hybrid_results(results, is_hybrid))
                    else:
                        print("\n⚠️  未找到足够相关的信息")
                        print("   建议：尝试更具体的关键词或降低阈值")
                
                except KeyboardInterrupt:
                    print("\n\n再见！")
                    break
            return
        
        # 单次查询模式
        if args.query:
            results, is_hybrid = hybrid_search(
                vectorstore=vectorstore,
                query=args.query,
                hybrid_retriever=hybrid_retriever,
                top_k=args.top_k,
                score_threshold=args.score_threshold,
                bm25_only=args.bm25_only,
                vector_only=args.vector_only
            )
            
            if args.json:
                # JSON 输出
                if is_hybrid:
                    output = {
                        "query": args.query,
                        "search_mode": "hybrid",
                        "results": [
                            {
                                "rank": i,
                                "hybrid_score": float(r.hybrid_score),
                                "bm25_score": float(r.bm25_score),
                                "vector_score": float(r.vector_score),
                                "source": r.metadata.get('source', 'unknown'),
                                "content": r.content
                            }
                            for i, r in enumerate(results, 1)
                        ]
                    }
                else:
                    output = {
                        "query": args.query,
                        "search_mode": "vector",
                        "results": [
                            {
                                "rank": i,
                                "l2_distance": float(score),
                                "source": doc.metadata.get('source', 'unknown'),
                                "content": doc.page_content
                            }
                            for i, (doc, score) in enumerate(results, 1)
                        ]
                    }
                print(json.dumps(output, ensure_ascii=False, indent=2))
            else:
                # 文本输出
                print(format_hybrid_results(results, is_hybrid))
            
            if not results:
                print("\n⚠️  未找到足够相关的信息")
                print("   建议：尝试更具体的关键词或降低阈值")
        
    except FileNotFoundError as e:
        print(f"\n✗ 错误：{e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ 检索失败：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
