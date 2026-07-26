# RAG 系统架构完整指南

## 系统概览

```
┌─────────────────────────────────────────────────────────────┐
│                     用户交互层                                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  对话界面     │  │  命令行工具   │  │  API 客户端   │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                     FastAPI 服务层                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  rag_api.py                                          │  │
│  │  - 预加载 BGE-M3 模型                                │  │
│  │  - 预加载 Chroma 向量库                              │  │
│  │  - 预加载 BM25 索引                                  │  │
│  │  - 执行 warmup query (消除首次查询延迟)               │  │
│  │  - 提供 /query /health /stats 端点                   │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                     混合检索引擎                             │
│  ┌──────────────────────┐  ┌──────────────────────┐      │
│  │   BM25 关键词检索     │  │   向量语义检索        │      │
│  │  ┌────────────────┐  │  │  ┌────────────────┐  │      │
│  │  │ jieba 中文分词  │  │  │  │ BGE-M3 模型    │  │      │
│  │  │ rank_bm25 算法  │  │  │  │ 1024 维向量     │  │      │
│  │  │ BM25Okapi 索引  │  │  │  │ L2 距离度量     │  │      │
│  │  └────────────────┘  │  │  └────────────────┘  │      │
│  └──────────────────────┘  └──────────────────────┘      │
│                              ↓                              │
│                    ┌─────────────────┐                      │
│                    │  RRF 融合排序    │                      │
│                    │  score = w1/r1  │                      │
│                    │        + w2/r2  │                      │
│                    └─────────────────┘                      │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                     数据存储层                               │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │   Chroma 向量库       │  │   BM25 索引文件      │        │
│  │  chroma.sqlite3      │  │  bm25_index.pkl      │        │
│  │  (1024 维向量)        │  │  (jieba 分词 +       │        │
│  │                      │  │   BM25Okapi)         │        │
│  └──────────────────────┘  └──────────────────────┘        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              原始文档 (md/txt/pdf/docx)              │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## 核心组件详解

### 1. hybrid_retriever.py

混合检索核心模块，实现 BM25 + 向量 + RRF 融合：

```python
class HybridRetriever:
    def __init__(self, bm25_weight=0.4, vector_weight=0.6, rrf_k=60):
        self.bm25_weight = bm25_weight    # BM25 权重
        self.vector_weight = vector_weight  # 向量权重
        self.rrf_k = rrf_k                # RRF 融合参数
    
    def build_bm25_index(self, documents):
        # 使用 jieba 分词构建 BM25 索引
        # 中文: jieba.cut_for_search
        # 英文: 空格分词
    
    def bm25_search(self, query, top_k=20):
        # 返回 [(doc_id, score), ...]
    
    def vector_search(self, query, vectorstore):
        # L2 距离转相似度 (高斯核)
        # 返回 [(doc_id, similarity), ...]
    
    def rrf_fusion(self, bm25_results, vector_results):
        # RRF 公式: score = w_bm25/(k + rank_bm25) + w_vector/(k + rank_vector)
        # 返回融合后的排序结果
    
    def search(self, query, vectorstore=None, top_k=10):
        # 执行完整混合检索流程
```

### 2. index_knowledge.py

索引构建工具，支持多种文档格式：

```python
# 文档加载流程
1. 扫描目录 (支持 md/txt/pdf/docx/xlsx)
2. 按格式加载 (MarkdownLoader, TextLoader, etc.)
3. 文本分块 (chunk_size=500, overlap=50)
4. 生成 Embedding (BGE-M3)
5. 存入 Chroma 向量库
6. 构建 BM25 索引 (jieba 分词)
7. 保存配置和索引文件
```

**关键实现**：doc_id 使用 `source#chunk_index` 格式确保唯一性

```python
source = chunk.metadata.get("source", f"chunk_{i}")
doc_id = f"{source}#{i}"  # 确保 BM25 和向量库 doc_id 一致
```

### 3. rag_api.py

FastAPI 服务，实现模型预加载和预热查询：

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时加载模型
    vectorstore, embeddings, hybrid_retriever = load_models()
    
    # 预热查询 (消除首次查询延迟)
    hybrid_retriever.search("预热查询", vectorstore=vectorstore, top_k=1)
    
    yield
    # 关闭时清理

@app.post("/query")
async def query(request: QueryRequest):
    # 支持三种检索模式: hybrid/bm25/vector
    # 返回结构化结果
```

### 4. rag_query_auto.py

自动查询脚本，用于 Hermes Skill 集成：

```python
def is_rag_query(query: str) -> bool:
    # 检测关键词判断是否适合 RAG 查询
    keywords = ['香港', '身份', '签证', '优才', '专才', ...]
    return any(kw in query.lower() for kw in keywords)

def query_rag_api(query_text: str) -> dict:
    # 调用本地 FastAPI 服务
    # 超时 10 秒

def format_results(response: dict) -> str:
    # 格式化 API 响应为易读文本
```

## 数据流

### 索引构建流程

```
原始文档
    ↓
文档加载器 (按格式选择)
    ↓
文本分块 (chunk_size=500, overlap=50)
    ↓
┌─────────────────┐    ┌─────────────────┐
│ 生成 Embedding   │    │ jieba 分词       │
│ BGE-M3 模型      │    │ 构建 BM25 索引   │
└─────────────────┘    └─────────────────┘
    ↓                         ↓
Chroma 向量库              bm25_index.pkl
    ↓                         ↓
└─────────────────┬─────────────────┘
                  ↓
          index_config.json
          hybrid_config.json
```

### 查询流程

```
用户查询
    ↓
┌─────────────────────────────────────┐
│ FastAPI 服务 (已预加载模型)          │
│ 1. 接收请求                          │
│ 2. 选择检索模式 (hybrid/bm25/vector) │
│ 3. 执行检索                          │
│ 4. 格式化响应                        │
└─────────────────────────────────────┘
    ↓
JSON 响应 (含结果、分数、耗时)
```

## 性能指标

| 指标 | 数值 | 说明 |
|------|------|------|
| 模型加载时间 | ~13 秒 | BGE-M3 (2GB) |
| 预热查询时间 | ~3-4 秒 | 消除首次查询延迟 |
| **查询响应时间** | **~40ms** | 混合检索 |
| 向量维度 | 1024 | BGE-M3 |
| 支持文档格式 | 5 种 | md/txt/pdf/docx/xlsx |
| 分词工具 | jieba | 中文支持 |

## 故障排查

### 问题 1：BM25 索引未找到

```
⚠️  未找到 BM25 索引，将仅使用向量检索
```

**解决**：重新构建索引
```bash
python index_knowledge.py --knowledge-dir ./docs --rebuild
```

### 问题 2：混合检索结果为空

**可能原因**：
- 文档数量太少，RRF 分数低于阈值
- doc_id 未对齐

**解决**：
```bash
# 降低阈值
python rag_query.py "问题" --score-threshold 0.3

# 检查索引配置
cat ./vectorstore/index_config.json
```

### 问题 3：服务启动失败

**检查**：
```bash
# 检查端口占用
lsof -i :8000

# 检查向量库目录
ls -la ~/test-vectorstore/

# 查看日志
cat rag_api.log
```

### 问题 4：中文分词不准确

**解决**：添加自定义词典
```python
import jieba
jieba.load_userdict("custom_dict.txt")
```

## 扩展建议

1. **添加更多文档格式支持**：ppt, html, csv
2. **实现增量索引**：只更新新增/修改的文档
3. **添加文档权限控制**：不同用户访问不同文档
4. **实现多语言支持**：英文、日文等
5. **添加结果高亮**：标记匹配的关键词
6. **实现对话历史**：支持多轮对话上下文
