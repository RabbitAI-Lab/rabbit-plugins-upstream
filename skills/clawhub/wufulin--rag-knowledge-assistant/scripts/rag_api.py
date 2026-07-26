#!/usr/bin/env python3
"""
RAG 混合检索 API 服务 (FastAPI)
预加载模型，提供毫秒级查询响应

启动方式:
    uvicorn rag_api:app --host 0.0.0.0 --port 8000 --reload

或后台运行:
    nohup uvicorn rag_api:app --host 0.0.0.0 --port 8000 > rag_api.log 2>&1 &

API 端点:
    POST /query       - 执行检索查询
    GET  /health      - 健康检查
    GET  /stats       - 服务统计信息
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

# FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from contextlib import asynccontextmanager

# 设置 UTF-8 编码
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# 添加脚本目录到路径
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

# ============ 全局状态 ============
app_state = {
    "vectorstore": None,
    "embeddings": None,
    "hybrid_retriever": None,
    "hybrid_config": None,
    "model_loaded": False,
    "load_time": 0.0,
    "query_count": 0,
    "total_query_time": 0.0,
}

# ============ Pydantic 模型 ============
class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000, description="查询文本")
    top_k: int = Field(default=5, ge=1, le=20, description="返回结果数量")
    score_threshold: float = Field(default=0.6, ge=0.0, le=1.0, description="相似度阈值")
    search_mode: str = Field(default="hybrid", pattern="^(hybrid|bm25|vector)$", description="检索模式: hybrid/bm25/vector")

class SearchResult(BaseModel):
    rank: int
    doc_id: str
    content: str
    source: str
    hybrid_score: float
    bm25_score: float
    vector_score: float

class QueryResponse(BaseModel):
    query: str
    search_mode: str
    results: List[SearchResult]
    query_time_ms: float
    total_results: int

class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    load_time_ms: float
    uptime_seconds: float

class StatsResponse(BaseModel):
    model_loaded: bool
    load_time_ms: float
    query_count: int
    avg_query_time_ms: float
    vectorstore_dir: str
    total_docs: int
    bm25_enabled: bool
    vector_enabled: bool

# ============ 模型加载 ============
def load_models(vectorstore_dir: str = "~/test-vectorstore"):
    """预加载所有模型和索引"""
    start_time = time.time()
    
    vectorstore_path = Path(vectorstore_dir).expanduser()
    
    if not vectorstore_path.exists():
        raise FileNotFoundError(f"向量数据库不存在: {vectorstore_path}")
    
    print(f"📂 加载向量库: {vectorstore_path}")
    
    # 加载配置
    config_file = vectorstore_path / "index_config.json"
    hybrid_config = None
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        hybrid_config = config.get('hybrid_search', {})
        print(f"✓ 配置加载完成: {config.get('chunk_count', 0)} 个片段")
    
    # 加载 Embedding 模型
    print("🧠 加载 BGE-M3 Embedding 模型...")
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
    print("✓ Embedding 模型加载完成")
    
    # 加载向量库
    print("📊 加载 Chroma 向量库...")
    from langchain_community.vectorstores import Chroma
    vectorstore = Chroma(
        persist_directory=str(vectorstore_path),
        embedding_function=embeddings,
        collection_name="knowledge_base"
    )
    print("✓ 向量库加载完成")
    
    # 加载混合检索器
    hybrid_retriever = None
    try:
        from hybrid_retriever import HybridRetriever
        bm25_path = vectorstore_path / "bm25_index.pkl"
        if bm25_path.exists() and hybrid_config and hybrid_config.get('enabled', False):
            print("🔧 加载混合检索器...")
            retriever = HybridRetriever(
                bm25_weight=hybrid_config.get('bm25_weight', 0.4),
                vector_weight=hybrid_config.get('vector_weight', 0.6),
                rrf_k=hybrid_config.get('rrf_k', 60)
            )
            if retriever.load_index(str(vectorstore_path)):
                hybrid_retriever = retriever
                print("✓ 混合检索器加载完成")
    except Exception as e:
        print(f"⚠️ 混合检索器加载失败: {e}")
    
    load_time = time.time() - start_time
    print(f"\n🚀 模型加载完成！耗时: {load_time:.2f} 秒")
    
    return vectorstore, embeddings, hybrid_retriever, hybrid_config, load_time

# ============ FastAPI 生命周期 ============
@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时加载模型
    print("=" * 60)
    print("🚀 RAG API 服务启动中...")
    print("=" * 60)
    
    try:
        vectorstore_dir = os.environ.get("VECTORSTORE_DIR", "~/test-vectorstore")
        vectorstore, embeddings, hybrid_retriever, hybrid_config, load_time = load_models(vectorstore_dir)
        
        app_state["vectorstore"] = vectorstore
        app_state["embeddings"] = embeddings
        app_state["hybrid_retriever"] = hybrid_retriever
        app_state["hybrid_config"] = hybrid_config
        app_state["model_loaded"] = True
        app_state["load_time"] = load_time
        app_state["start_time"] = time.time()
        
        print(f"\n✅ 模型加载完成！耗时: {load_time:.2f} 秒")
        
        # 预热查询：执行一次模拟查询，消除首次查询延迟
        print("\n🔥 执行预热查询...")
        warmup_start = time.time()
        if hybrid_retriever and vectorstore:
            _ = hybrid_retriever.search("预热查询", vectorstore=vectorstore, top_k=1)
        warmup_time = time.time() - warmup_start
        print(f"✓ 预热完成！耗时: {warmup_time:.3f} 秒")
        
        print(f"\n🚀 服务启动成功！")
        print(f"   访问: http://localhost:8000")
        print(f"   文档: http://localhost:8000/docs")
        print(f"   健康: http://localhost:8000/health")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ 服务启动失败: {e}")
        import traceback
        traceback.print_exc()
        raise
    
    yield
    
    # 关闭时清理
    print("\n🛑 服务关闭中...")

# ============ 创建 FastAPI 应用 ============
app = FastAPI(
    title="RAG 混合检索 API",
    description="基于 BM25 + 向量语义检索的混合检索服务",
    version="2.0.1",
    lifespan=lifespan
)

# ============ API 端点 ============
@app.get("/", tags=["根路径"])
async def root():
    """根路径 - 返回服务信息"""
    return {
        "service": "RAG 混合检索 API",
        "version": "2.0.1",
        "docs": "/docs",
        "health": "/health",
        "query": "POST /query"
    }

@app.get("/health", response_model=HealthResponse, tags=["健康检查"])
async def health():
    """健康检查端点"""
    uptime = time.time() - app_state.get("start_time", time.time())
    return HealthResponse(
        status="healthy" if app_state["model_loaded"] else "unhealthy",
        model_loaded=app_state["model_loaded"],
        load_time_ms=app_state["load_time"] * 1000,
        uptime_seconds=uptime
    )

@app.get("/stats", response_model=StatsResponse, tags=["统计信息"])
async def stats():
    """服务统计信息"""
    query_count = app_state["query_count"]
    total_query_time = app_state["total_query_time"]
    avg_time = (total_query_time / query_count * 1000) if query_count > 0 else 0
    
    hybrid_retriever = app_state.get("hybrid_retriever")
    total_docs = hybrid_retriever.stats.get("total_docs", 0) if hybrid_retriever else 0
    bm25_enabled = hybrid_retriever.stats.get("bm25_enabled", False) if hybrid_retriever else False
    
    return StatsResponse(
        model_loaded=app_state["model_loaded"],
        load_time_ms=app_state["load_time"] * 1000,
        query_count=query_count,
        avg_query_time_ms=avg_time,
        vectorstore_dir=os.environ.get("VECTORSTORE_DIR", "~/test-vectorstore"),
        total_docs=total_docs,
        bm25_enabled=bm25_enabled,
        vector_enabled=True
    )

@app.post("/query", response_model=QueryResponse, tags=["检索查询"])
async def query(request: QueryRequest):
    """
    执行混合检索查询
    
    请求示例:
    ```json
    {
        "query": "香港专才计划的签证有效期是多久",
        "top_k": 5,
        "score_threshold": 0.6,
        "search_mode": "hybrid"
    }
    ```
    """
    if not app_state["model_loaded"]:
        raise HTTPException(status_code=503, detail="模型尚未加载完成")
    
    start_time = time.time()
    
    vectorstore = app_state["vectorstore"]
    hybrid_retriever = app_state["hybrid_retriever"]
    
    try:
        # 根据搜索模式执行查询
        if request.search_mode == "bm25" and hybrid_retriever:
            # 仅 BM25
            bm25_results = hybrid_retriever.bm25_search(request.query, top_k=request.top_k)
            results = []
            for i, (doc_id, score) in enumerate(bm25_results[:request.top_k], 1):
                doc = next((d for d in hybrid_retriever.documents if d.get("id") == doc_id), {})
                results.append(SearchResult(
                    rank=i,
                    doc_id=doc_id,
                    content=doc.get("content", "")[:500],
                    source=doc.get("metadata", {}).get("source", "unknown"),
                    hybrid_score=score,
                    bm25_score=score,
                    vector_score=0.0
                ))
            
        elif request.search_mode == "vector":
            # 仅向量
            from hybrid_retriever import SearchResult as HybridSearchResult
            vector_results = vectorstore.similarity_search_with_score(request.query, k=request.top_k)
            results = []
            for i, (doc, score) in enumerate(vector_results, 1):
                if score < 450:  # BGE-M3 经验阈值
                    results.append(SearchResult(
                        rank=i,
                        doc_id=doc.metadata.get("source", "unknown"),
                        content=doc.page_content[:500],
                        source=doc.metadata.get("source", "unknown"),
                        hybrid_score=0.0,
                        bm25_score=0.0,
                        vector_score=score
                    ))
            
        else:
            # 混合检索（默认）
            if hybrid_retriever:
                hybrid_results = hybrid_retriever.search(
                    request.query,
                    vectorstore=vectorstore,
                    top_k=request.top_k
                )
                
                # 过滤低分结果
                adjusted_threshold = request.score_threshold * 0.5 if hybrid_retriever.stats.get("total_docs", 0) < 10 else request.score_threshold
                filtered = [r for r in hybrid_results if r.hybrid_score >= adjusted_threshold]
                if not filtered and hybrid_results:
                    filtered = hybrid_results[:request.top_k]
                
                results = []
                for i, r in enumerate(filtered[:request.top_k], 1):
                    results.append(SearchResult(
                        rank=i,
                        doc_id=r.doc_id,
                        content=r.content[:500],
                        source=r.metadata.get("source", "unknown"),
                        hybrid_score=r.hybrid_score,
                        bm25_score=r.bm25_score,
                        vector_score=r.vector_score
                    ))
            else:
                #  fallback 到向量检索
                vector_results = vectorstore.similarity_search_with_score(request.query, k=request.top_k)
                results = []
                for i, (doc, score) in enumerate(vector_results, 1):
                    if score < 450:
                        results.append(SearchResult(
                            rank=i,
                            doc_id=doc.metadata.get("source", "unknown"),
                            content=doc.page_content[:500],
                            source=doc.metadata.get("source", "unknown"),
                            hybrid_score=0.0,
                            bm25_score=0.0,
                            vector_score=score
                        ))
        
        query_time = time.time() - start_time
        
        # 更新统计
        app_state["query_count"] += 1
        app_state["total_query_time"] += query_time
        
        return QueryResponse(
            query=request.query,
            search_mode=request.search_mode,
            results=results,
            query_time_ms=query_time * 1000,
            total_results=len(results)
        )
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"查询失败: {str(e)}")

# ============ 主入口 ============
if __name__ == "__main__":
    import uvicorn
    
    # 从环境变量获取配置
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))
    reload = os.environ.get("RELOAD", "false").lower() == "true"
    
    print(f"\n🚀 启动 RAG API 服务...")
    print(f"   地址: {host}:{port}")
    print(f"   热重载: {reload}")
    
    uvicorn.run(
        "rag_api:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )
