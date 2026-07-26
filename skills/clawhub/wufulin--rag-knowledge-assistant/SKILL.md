---
name: rag-knowledge-assistant
description: 基于混合检索(BM25+向量语义)的本地RAG知识库系统，支持FastAPI服务、自动查询集成
version: 2.0.1
category: openclaw-imports
---

# RAG 混合检索知识库助手

## 触发条件

当用户需要以下功能时触发：

1. **构建/管理本地知识库**
   - "搭建知识库"、"创建 RAG 系统"、"索引文档"
   - "添加文档到知识库"、"更新知识库"

2. **查询知识库**
   - 包含关键词：香港身份、香港签证、优才、专才、高才通、续签、永居、受养人
   - 包含关键词：公司制度、考勤、请假、报销、福利
   - 包含关键词：Python、机器学习、算法、编程
   - 通用：任何已索引文档的查询

3. **优化检索性能**
   - "查询太慢"、"加速检索"、"优化 RAG"
   - "启动 API 服务"、"FastAPI 服务"

## 核心能力

### 1. 混合检索 (BM25 + 向量语义)

结合关键词精确匹配和语义理解，通过 RRF 融合排序：

```
查询文本
    ↓
┌─────────────────┐    ┌─────────────────┐
│   jieba 分词     │    │   BGE-M3        │
│   BM25Okapi     │    │   Chroma        │
│   关键词检索     │    │   向量检索       │
└─────────────────┘    └─────────────────┘
    ↓                         ↓
    └────────────┬────────────┘
                 ↓
           RRF 融合排序
                 ↓
           返回 Top-K 结果
```

**三种检索模式：**
| 模式 | 参数 | 适用场景 |
|------|------|----------|
| 混合检索 | `--hybrid` (默认) | 通用场景，兼顾精确和语义 |
| BM25 仅 | `--bm25-only` | 精确术语、产品型号、代码 |
| 向量仅 | `--vector-only` | 概念查询、同义词、自然语言 |

### 2. FastAPI 服务 (毫秒级查询)

预加载模型，实现 ~40ms 查询响应：

```bash
# 启动服务
cd scripts && source venv/bin/activate
uvicorn rag_api:app --host 0.0.0.0 --port 8000

# 查询
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "问题", "top_k": 5}'
```

### 3. 自动查询集成

在 Hermes 对话中直接提问，自动调用 RAG API：

```python
# scripts/rag_query_auto.py
if is_rag_query(user_question):
    response = query_rag_api(user_question)
    return format_results(response)
```

## 工作流程

### 阶段 1：构建知识库

```bash
# 1. 准备文档 (支持 md/txt/pdf/docx/xlsx)
mkdir ~/test-knowledge
cp your_docs/*.md ~/test-knowledge/

# 2. 构建索引 (含混合检索)
cd scripts && source venv/bin/activate
python index_knowledge.py \
  --knowledge-dir ~/test-knowledge \
  --output-dir ~/test-vectorstore \
  --rebuild --hybrid
```

### 阶段 2：启动服务

```bash
# 启动 FastAPI 服务 (预加载模型)
uvicorn rag_api:app --host 0.0.0.0 --port 8000

# 或后台运行
nohup uvicorn rag_api:app --host 0.0.0.0 --port 8000 > rag_api.log 2>&1 &
```

### 阶段 3：查询使用

**方式 A：命令行**
```bash
python rag_query.py "问题" --vectorstore ~/test-vectorstore --top-k 5
```

**方式 B：API 调用**
```bash
curl -X POST http://localhost:8000/query \
  -d '{"query": "问题", "top_k": 5, "search_mode": "hybrid"}'
```

**方式 C：对话中直接提问**
```
用户: 香港专才计划的签证有效期是多久？
助手: [自动查询知识库] 根据知识库信息...
```

## 关键文件

| 文件 | 说明 |
|------|------|
| `scripts/index_knowledge.py` | 构建索引 (支持混合检索) |
| `scripts/rag_query.py` | 命令行查询工具 |
| `scripts/rag_api.py` | FastAPI 服务 |
| `scripts/rag_query_auto.py` | 自动查询脚本 |
| `scripts/hybrid_retriever.py` | 混合检索核心模块 |
| `references/hybrid_search.md` | 混合检索实现细节 |
| `references/fastapi_service.md` | FastAPI 服务部署指南 |

## 依赖安装

```bash
cd scripts && source venv/bin/activate
pip install rank-bm25 jieba fastapi uvicorn
```

## 故障处理

- **服务未启动**：运行 `uvicorn rag_api:app --host 0.0.0.0 --port 8000`
- **查询超时**：检查服务状态或简化查询
- **无结果**：知识库中暂无相关信息，建议更新知识库
- **首次查询慢**：服务已包含预热查询，启动时即完成初始化

## 性能优化

| 优化前 | 优化后 | 方法 |
|--------|--------|------|
| 3-4 秒/查询 | ~40ms/查询 | FastAPI + 模型预加载 |
| 首次查询慢 | 启动即预热 | lifespan 中执行 warmup query |
| 仅关键词匹配 | 语义理解 | BGE-M3 + jieba 分词 |

## 与 LLM Wiki 的协作

RAG 和 LLM Wiki 是互补的知识管理方式：

| | **RAG** | **LLM Wiki** |
|---|---|---|
| **用途** | 快速检索原始文档 | 持久化整理知识 |
| **查询速度** | ~40ms | 直接读取 |
| **交叉引用** | 无 | `[[wikilinks]]` |
| **矛盾处理** | 无法发现 | 显式标记 |
| **适合场景** | 日常问答、快速查找 | 深度整理、长期积累 |

**推荐工作流：**
1. **日常查询** → 使用 RAG 快速获取答案
2. **有价值的信息** → 归档到 LLM Wiki（`llm-wiki` 技能）
3. **定期整理** → 将 RAG 高频查询结果整理为 Wiki 页面

**示例：**
```
用户问：优才和专才的区别？
→ RAG 查询 → 获得答案
→ 如果答案有价值 → 更新到 Wiki 的 [[香港移民FAQ]] 页面
→ 添加交叉引用 [[香港优才计划]]、[[香港专才计划]]
```

## 注意事项

1. **服务依赖**：需要确保本地 RAG API 服务已启动（端口 8000）
2. **查询超时**：API 调用超时时间为 10 秒
3. **结果限制**：最多返回 5 个相关片段，避免信息过载
4. **内容截断**：如果内容过长，只返回前 500 字符
5. **与 Wiki 互补**：RAG 适合快速查询，Wiki 适合深度整理，两者结合效果更佳
