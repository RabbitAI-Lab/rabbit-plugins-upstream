---
name: knowledge-base-manager
description: 管理AI Agent工作台的知识库，支持文件上传、向量存储和语义检索。Agent可根据用户提问自动搜索知识库获取参考来源。
read_when:
  - 用户需要上传私人文档到知识库
  - 用户提问涉及知识库内容
  - 需要基于文档回答问题
  - 语义搜索相关功能
metadata: {"clawdbot":{"emoji":"📚","requires":{"ports":[3000],"python":["fastapi","pymilvus","pypdf","python-docx"]}}}
allowed-tools: Bash(curl:*), Bash(python3:*)
---

# 知识库管理技能 (Knowledge Base Manager)

管理 AI Agent 工作台的知识库功能，支持文件上传、向量化存储和语义检索。

## 概述

本技能为 AI Agent 工作台提供完整的知识库管理能力，包含：

- 📚 **知识库管理** - 创建、删除知识库
- 📤 **文件上传** - 支持 PDF、Word、TXT、Markdown
- 🔍 **语义搜索** - 基于向量相似度的智能检索
- ⚙️ **分块配置** - 可调整块大小和重叠量
- 🤖 **Embedding** - 使用 SiliconFlow BAAI/bge-m3 模型

## 技术架构

```
用户上传文件 → FastAPI 解析 → 文本分块 → SiliconFlow Embedding → Milvus 向量存储
                                                              ↓
用户搜索查询 ───────────→ 向量转换 ──────────────→ Milvus 相似度检索 → 返回结果
```

**技术栈：**
- 后端：FastAPI (Python)
- 向量数据库：Milvus (SQLite 存储)
- Embedding：SiliconFlow API (BAAI/bge-m3, 1024维)
- 文档解析：pypdf、python-docx

## 启动服务

```bash
# 方式1：直接运行
cd /root/ai-agent-kb-service
python3 kb_service.py

# 方式2：PM2 管理
pm2 start kb_service.py --name ai-agent-kb
```

**服务地址：**
- 本地：http://localhost:3000
- 生产：http://crawdxiaowu.com:3000

## 功能详解

### 1. 知识库管理

#### 列出所有知识库
```bash
curl http://crawdxiaowu.com:3000/api/knowledge-bases
```

#### 创建知识库
```bash
curl -X POST http://crawdxiaowu.com:3000/api/knowledge-bases \
  -d "kb_id=my-kb&name=我的知识库"
```

#### 获取知识库详情
```bash
curl http://crawdxiaowu.com:3000/api/knowledge-bases/{kb_id}
```

#### 删除知识库
```bash
curl -X DELETE http://crawdxiaowu.com:3000/api/knowledge-bases/{kb_id}
```

### 2. 文件上传

上传文件到知识库（支持 PDF、Word、TXT、Markdown）：

```bash
curl -X POST http://crawdxiaowu.com:3000/api/knowledge-bases/{kb_id}/files \
  -F "file=@/path/to/document.pdf" \
  -F "chunk_size=500" \
  -F "chunk_overlap=50"
```

**参数说明：**
| 参数 | 说明 | 默认值 |
|------|------|--------|
| file | 要上传的文件 | 必填 |
| chunk_size | 分块大小(字符) | 500 |
| chunk_overlap | 块重叠量 | 50 |

### 3. 语义搜索

这是 **Agent 最重要的能力** - 当用户提问涉及知识库内容时，自动调用搜索：

```bash
# 基本搜索
curl -X POST http://crawdxiaowu.com:3000/api/knowledge-bases/{kb_id}/search \
  -d "query=搜索关键词&top_k=5"
```

**返回格式：**
```json
{
  "success": true,
  "data": [
    {
      "content": "文档内容片段...",
      "source": "文件名.pdf",
      "score": 0.9234
    }
  ]
}
```

#### Agent 搜索脚本

提供了便捷的搜索脚本，Agent 可直接调用：

```bash
# 完整参数
python3 /root/.openclaw/workspace/skills/kb-manager/search.py \
  --query "用户问题" \
  --kb-id "知识库ID" \
  --top-k 5

# 快速搜索
python3 /root/.openclaw/workspace/skills/kb-manager/search.py "搜索内容" [知识库ID]
```

### 4. 文件管理

#### 删除文件
```bash
curl -X DELETE http://crawdxiaowu.com:3000/api/knowledge-bases/{kb_id}/files/{filename}
```

#### 解析预览
```bash
curl -X POST http://crawdxiaowu.com:3000/api/knowledge-bases/{kb_id}/files/{filename}/parse \
  -d "chunk_size=500&chunk_overlap=50"
```

## 现有知识库

| ID | 名称 | 文件 | 块数 |
|----|------|------|------|
| test-kb | 测试知识库 | 个人简历20240529.pdf, 厦门旅游攻略.docx | 81 |
| Test | 123 | 厦门旅游攻略.docx | 79 |

查看所有知识库：
```bash
curl http://crawdxiaowu.com:3000/api/knowledge-bases
```

## Agent 集成指南

### 自动搜索触发

当用户提问符合以下情况时，Agent 应自动调用搜索：

1. **明确引用文档** - "我之前上传的PDF里说什么？"
2. **知识库相关内容** - "我的简历里..."
3. **需要外部参考** - "根据知识库..."

### 搜索示例

**用户：** 我的简历里写了我之前的工作经历吗？

**Agent 调用：**
```bash
python3 /root/.openclaw/workspace/skills/kb-manager/search.py --query "工作经历" --kb-id test-kb
```

**返回结果：**
```
📚 知识库搜索结果:

**结果 1** (相关性: 92.34%)
来源: 个人简历20240529.pdf
内容: 工作经历：2020-2024 某互联网公司...
```

**Agent 回答：** 根据您上传的简历，您的工作经历包括...

### 结果处理

Agent 收到搜索结果后：
1. 提取高相关性结果 (score > 0.6)
2. 将内容融入回答
3. 注明来源："根据知识库中的xxx文件..."

## 依赖安装

```bash
pip install fastapi uvicorn pypdf python-docx pymilvus requests tiktoken pydantic python-multipart
```

## 故障排除

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 上传失败 | 文件格式不支持 | 检查是否为 PDF/DOCX/TXT/MD |
| 搜索无结果 | 关键词不匹配 | 使用更通用的关键词 |
| 服务无响应 | 端口3000被占用 | `lsof -i:3000` 检查 |
| 无知识库 | 未创建知识库 | 先调用创建API |

## 文件结构

```
kb-manager/
├── SKILL.md          # 本技能说明
├── search.py         # 搜索脚本（完整版）
└── search_kb.py     # 搜索脚本（快速版）
```
