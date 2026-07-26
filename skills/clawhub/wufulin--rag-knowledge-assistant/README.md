# RAG 混合检索知识库助手

`rag-knowledge-assistant` 是一个本地 RAG 知识库 skill，面向 OpenClaw/Hermes 使用场景。它可以把 PDF、Word、Excel、Markdown、TXT 等本地文档构建为 Chroma 向量库，并通过 BM25 + 向量语义检索的混合排序返回带来源的答案片段。

## 发布信息

| 项目 | 内容 |
|------|------|
| Skill 版本 | `2.0.1` |
| ClawHub 发布者 | `wufulin` |
| ClawHub 页面 | `https://clawhub.ai/wufulin/skills/rag-knowledge-assistant` |
| GitHub 来源 | `https://github.com/wufulinit/rag-knowledge-assistant` |
| GitHub 邮箱 | `wufulinit@gmail.com` |
| 许可证 | MIT-0 |

## 核心能力

| 能力 | 说明 |
|------|------|
| 混合检索 | 使用 BM25 关键词检索 + BGE-M3/Chroma 向量检索，并通过 RRF 融合排序 |
| 多格式文档 | 支持 `.pdf`、`.docx`、`.xlsx`、`.md`、`.txt` |
| 中文友好 | 使用 `jieba` 中文分词，适合中文制度、政策、FAQ、技术文档 |
| FastAPI 服务 | 预加载模型和索引，避免每次命令行查询重复加载模型 |
| 查询模式切换 | 支持 `hybrid`、`bm25`、`vector` 三种检索模式 |
| 来源追踪 | 返回文档来源、chunk id、BM25 分数、向量分数和融合分数 |

## 快速开始

### 1. 安装依赖

```bash
cd scripts
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

如果使用 Ollama embedding，请先启动 Ollama 并拉取模型：

```bash
ollama serve
ollama pull nomic-embed-text-v2-moe
```

### 2. 准备知识库

把待检索文档放入一个知识库目录，例如：

```text
knowledge/
├── company-policies/
│   ├── 员工手册.pdf
│   ├── 考勤制度.docx
│   └── 报销流程.xlsx
├── product-docs/
│   ├── API 文档.md
│   └── 产品说明.pdf
└── notes/
    └── research.txt
```

### 3. 构建索引

使用本地 BGE-M3 模型，并启用混合检索：

```bash
python index_knowledge.py \
  --knowledge-dir ./knowledge \
  --output-dir ./vectorstore \
  --rebuild \
  --hybrid
```

使用 Ollama embedding：

```bash
python index_knowledge_ollama.py \
  --knowledge-dir ./knowledge \
  --output-dir ./vectorstore \
  --rebuild \
  --model nomic-embed-text-v2-moe
```

### 4. 命令行查询

```bash
# 混合检索，默认模式
python rag_query.py "公司年假是怎么规定的？" --vectorstore ./vectorstore

# 仅 BM25，适合精确术语、编号、产品型号
python rag_query.py "ABC-123 审批规则" --vectorstore ./vectorstore --bm25-only

# 仅向量检索，适合概念和自然语言问题
python rag_query.py "如何处理员工出差报销？" --vectorstore ./vectorstore --vector-only

# 交互模式
python rag_query.py --interactive --vectorstore ./vectorstore
```

### 5. 启动 FastAPI 服务

FastAPI 服务会在启动时加载模型、向量库和 BM25 索引，适合高频查询。

```bash
cd scripts
source venv/bin/activate
export VECTORSTORE_DIR="./vectorstore"
uvicorn rag_api:app --host 0.0.0.0 --port 8000
```

查询 API：

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "香港专才计划的签证有效期是多久？",
    "top_k": 5,
    "score_threshold": 0.6,
    "search_mode": "hybrid"
  }'
```

## 目录结构

```text
rag-knowledge-assistant/
├── SKILL.md                         # OpenClaw/Hermes skill 定义
├── README.md                        # 使用说明
├── PUSH_GUIDE.md                    # GitHub 与 ClawHub 发布说明
├── rag-config.yaml                  # 配置模板
├── scripts/
│   ├── index_knowledge.py           # BGE-M3 索引构建，支持混合检索
│   ├── index_knowledge_ollama.py    # Ollama embedding 索引构建
│   ├── rag_query.py                 # 混合检索命令行查询
│   ├── rag_query_ollama.py          # Ollama 向量检索查询
│   ├── rag_api.py                   # FastAPI 查询服务
│   ├── rag_query_auto.py            # 对话自动查询集成
│   ├── hybrid_retriever.py          # BM25 + 向量 + RRF 核心模块
│   └── requirements.txt             # Python 依赖
└── references/
    ├── system_architecture.md       # 系统架构
    ├── hybrid_search.md             # 混合检索实现说明
    ├── hybrid_search_testing.md     # 混合检索测试说明
    ├── fastapi_service.md           # API 服务部署说明
    ├── pdf_reading.md               # PDF 读取说明
    ├── excel_reading.md             # Excel 读取说明
    └── excel_analysis.md            # Excel 分析说明
```

## 配置示例

`rag-config.yaml` 可作为配置模板：

```yaml
rag:
  vectorstore:
    type: chroma
    persist_directory: ./vectorstore

  embedding:
    type: huggingface
    model: BAAI/bge-m3

  retrieval:
    top_k: 5
    score_threshold: 0.6
    search_mode: hybrid

  chunking:
    chunk_size: 500
    chunk_overlap: 50

  hybrid_search:
    enabled: true
    bm25_weight: 0.4
    vector_weight: 0.6
    rrf_k: 60
```

## OpenClaw / ClawHub 安装

ClawHub 发布页：

```bash
open https://clawhub.ai/wufulin/skills/rag-knowledge-assistant
```

注意：ClawHub 上仍保留旧 owner `@aixbinge` 的同名 skill，因此部分 CLI 命令使用裸 slug `rag-knowledge-assistant` 时可能提示 `AMBIGUOUS_SKILL_SLUG`。请确认选择 `@wufulin/rag-knowledge-assistant`；如果旧包后续被隐藏、迁移或重命名，再使用裸 slug 安装即可。

从 GitHub 安装到本地 skills 目录：

```bash
git clone https://github.com/wufulinit/rag-knowledge-assistant.git \
  ~/.openclaw/skills/rag-knowledge-assistant
```

在对话中可以直接触发：

```text
从知识库查一下公司年假规定
检索文档：车辆管理制度
香港专才计划的签证有效期是多久？
```

## 2.0.1 更新内容

- 新增 BM25 + 向量语义的混合检索模式。
- 新增 `hybrid_retriever.py`，通过 RRF 融合关键词和向量结果。
- 新增 `rag_api.py` FastAPI 服务，支持 `/query`、`/health`、`/stats`。
- 新增 `rag_query_auto.py`，便于在 Hermes/OpenClaw 对话中自动调用本地 RAG API。
- 更新文档和发布元数据，迁移到 `wufulin` / `wufulinit` 发布身份。
- 增加 owner-qualified ClawHub 页面说明，避免旧同名包导致 CLI 裸 slug 歧义。
- 发布包排除本地虚拟环境、缓存和日志文件，避免上传机器本地状态。

## 故障排查

### 检索结果为空

```bash
# 检查向量库是否存在
ls -la ./vectorstore

# 降低阈值
python rag_query.py "问题" --vectorstore ./vectorstore --score-threshold 0.3

# 重新构建索引
python index_knowledge.py --knowledge-dir ./knowledge --output-dir ./vectorstore --rebuild --hybrid
```

### BM25 索引未找到

```bash
python index_knowledge.py --knowledge-dir ./knowledge --output-dir ./vectorstore --rebuild --hybrid
```

构建完成后，确认 `./vectorstore/bm25_index.pkl` 存在。

### FastAPI 服务启动失败

```bash
# 检查端口占用
lsof -i :8000

# 指定向量库目录
export VECTORSTORE_DIR="./vectorstore"

# 启动服务
uvicorn rag_api:app --host 0.0.0.0 --port 8000
```

### Ollama 连接失败

```bash
ollama serve
ollama list
ollama pull nomic-embed-text-v2-moe
```

## 参考文档

- [系统架构](references/system_architecture.md)
- [混合检索实现](references/hybrid_search.md)
- [混合检索测试](references/hybrid_search_testing.md)
- [FastAPI 服务部署](references/fastapi_service.md)
- [PDF 读取指南](references/pdf_reading.md)
- [Excel 读取指南](references/excel_reading.md)
- [Excel 分析指南](references/excel_analysis.md)
