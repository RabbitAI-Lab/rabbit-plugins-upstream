# 混合检索 (Hybrid Search) 实现细节

## 概述

混合检索结合 **BM25 关键词检索** 和 **向量语义检索**，通过 RRF (Reciprocal Rank Fusion) 融合两种检索结果的排名，兼顾精确匹配和语义理解能力。

## 架构

```
查询文本
    ↓
┌─────────────────┐    ┌─────────────────┐
│   jieba 分词     │    │   BGE-M3        │
│   BM25Okapi     │    │   Chroma        │
│   关键词检索     │    │   向量检索       │
└─────────────────┘    └─────────────────┘
    ↓                         ↓
  [(doc_id, score)]      [(doc_id, similarity)]
    ↓                         ↓
    └────────────┬────────────┘
                 ↓
           RRF 融合排序
    score = w_bm25/(k + rank_bm25) + w_vector/(k + rank_vector)
                 ↓
           返回 Top-K 结果
```

## 核心组件

### 1. hybrid_retriever.py

混合检索核心模块，提供 `HybridRetriever` 类：

```python
from hybrid_retriever import HybridRetriever

retriever = HybridRetriever(
    bm25_weight=0.4,      # BM25 权重
    vector_weight=0.6,   # 向量权重
    rrf_k=60,            # RRF 融合参数
    top_k=10,            # 返回结果数
    use_jieba=True       # 使用 jieba 中文分词
)

# 构建 BM25 索引
retriever.build_bm25_index(documents)

# 执行混合检索
results = retriever.search(query, vectorstore=vectorstore)
```

### 2. BM25 关键词检索

- **分词**：中文使用 `jieba.cut_for_search`，英文按空格分词
- **算法**：`rank_bm25.BM25Okapi`
- **特点**：精确匹配关键词，适合产品型号、代码片段、术语查询

### 3. 向量语义检索

- **模型**：`BAAI/bge-m3` (1024 维)
- **数据库**：Chroma
- **距离度量**：L2 距离转相似度 (高斯核)
- **特点**：理解语义关系，支持同义词、概念查询

### 4. RRF 融合

```python
# RRF 公式
hybrid_score = bm25_weight * (1 / (rrf_k + rank_bm25)) + \
               vector_weight * (1 / (rrf_k + rank_vector))
```

- `rrf_k=60`：默认参数，越小越强调头部排名
- 权重默认 `bm25:vector = 0.4:0.6`

## 三种检索模式

| 模式 | 参数 | 适用场景 |
|------|------|----------|
| 混合检索 | `--hybrid` (默认) | 通用场景，兼顾精确和语义 |
| BM25 仅 | `--bm25-only` | 精确术语、产品型号、代码 |
| 向量仅 | `--vector-only` | 概念查询、同义词、自然语言 |

## 实现注意事项

### doc_id 对齐

BM25 索引和向量库必须使用相同的 `doc_id`，否则融合时无法匹配。由于文档分块后多个 chunk 可能来自同一文件，使用 `source#chunk_index` 格式确保唯一性：

```python
# index_knowledge.py 中
source = chunk.metadata.get("source", f"chunk_{i}")
doc_id = f"{source}#{i}"
```

**注意**：向量检索时也需要使用相同的 doc_id 格式：

```python
# hybrid_retriever.py 中
source = doc.metadata.get("source", "unknown")
chunk_index = doc.metadata.get("chunk_index", i)
doc_id = f"{source}#{chunk_index}"
```

### 分数归一化

- **BM25**：原始分数，范围不固定
- **向量**：L2 距离通过高斯核转换为 [0,1] 相似度
- **融合**：RRF 分数范围 [0, 1/(k+1)]，需根据文档数量调整阈值

### 小文档集处理

当文档数量 < 10 时，RRF 分数会偏低，系统会自动降低阈值避免无结果：

```python
adjusted_threshold = score_threshold * 0.5 if total_docs < 10 else score_threshold
```

## 依赖

```
rank-bm25>=0.2.2    # BM25 算法
jieba>=0.42.1       # 中文分词
```

## 性能

- **索引构建**：BM25 索引在向量索引之后构建，增加 ~10% 时间
- **检索延迟**：混合检索增加 ~20ms (BM25 检索时间)
- **内存占用**：BM25 索引约为原始文本的 2-3 倍

## 故障排查

### 问题：BM25 索引未找到

```
⚠️  未找到 BM25 索引，将仅使用向量检索
```

**解决**：重新运行索引构建，确保 `--hybrid` 参数启用（默认已启用）：
```bash
python index_knowledge.py --knowledge-dir ./docs --rebuild
```

### 问题：混合检索结果为空

**可能原因**：
1. 文档数量太少，RRF 分数低于阈值
2. doc_id 未对齐（BM25 和向量库不匹配）

**解决**：
```bash
# 降低阈值
python rag_query.py "问题" --score-threshold 0.3

# 检查索引配置
cat ./vectorstore/index_config.json
```

### 问题：中文分词不准确

**解决**：确保 jieba 已安装并加载词典：
```python
import jieba
jieba.load_userdict("custom_dict.txt")  # 添加自定义词典
```
