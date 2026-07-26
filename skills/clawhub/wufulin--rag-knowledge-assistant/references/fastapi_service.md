# FastAPI 服务部署指南

## 概述

将 RAG 混合检索封装为 FastAPI 服务，预加载模型，实现毫秒级查询响应。

## 问题：命令行查询慢

**原因**：每次命令行查询都重新加载 BGE-M3 模型（2-3 秒）
**解决**：启动 FastAPI 服务，预加载模型，查询速度从 3-4 秒降至 ~40ms

## 启动服务

```bash
cd scripts
source venv/bin/activate
uvicorn rag_api:app --host 0.0.0.0 --port 8000
```

后台运行：
```bash
nohup uvicorn rag_api:app --host 0.0.0.0 --port 8000 > rag_api.log 2>&1 &
```

## API 端点

### 1. 健康检查
```bash
curl http://localhost:8000/health
```

响应：
```json
{
  "status": "healthy",
  "model_loaded": true,
  "load_time_ms": 13219,
  "uptime_seconds": 17
}
```

### 2. 执行查询
```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "香港专才计划的签证有效期是多久",
    "top_k": 5,
    "score_threshold": 0.6,
    "search_mode": "hybrid"
  }'
```

响应：
```json
{
  "query": "香港专才计划的签证有效期是多久",
  "search_mode": "hybrid",
  "query_time_ms": 40,
  "total_results": 5,
  "results": [
    {
      "rank": 1,
      "doc_id": "faq_immigration_20260618.md#15",
      "content": "专才计划的签证有效期与聘用合同的期限挂钩...",
      "source": "faq_immigration_20260618.md",
      "hybrid_score": 0.0143,
      "bm25_score": 18.2159,
      "vector_score": 0.5314
    }
  ]
}
```

### 3. 统计信息
```bash
curl http://localhost:8000/stats
```

## 请求参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| query | string | 必填 | 查询文本 |
| top_k | int | 5 | 返回结果数量 (1-20) |
| score_threshold | float | 0.6 | 相似度阈值 (0.0-1.0) |
| search_mode | string | "hybrid" | 检索模式: hybrid/bm25/vector |

## 客户端调用

### Python
```python
import requests

response = requests.post(
    "http://localhost:8000/query",
    json={
        "query": "香港专才计划的签证有效期是多久",
        "top_k": 5,
        "search_mode": "hybrid"
    }
)

data = response.json()
print(f"查询耗时: {data['query_time_ms']}ms")
for r in data['results']:
    print(f"{r['rank']}. {r['content'][:100]}...")
```

### JavaScript
```javascript
fetch('http://localhost:8000/query', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        query: '香港专才计划的签证有效期是多久',
        top_k: 5,
        search_mode: 'hybrid'
    })
})
.then(res => res.json())
.then(data => console.log(data));
```

## 速度对比

| 方式 | 首次查询 | 后续查询 |
|------|----------|----------|
| 命令行 rag_query.py | 3-4 秒 | 3-4 秒 |
| FastAPI 服务 | 3-4 秒 | **~40ms** |

## 环境变量

```bash
# 指定向量库目录 (默认 ~/test-vectorstore)
export VECTORSTORE_DIR="~/test-vectorstore"

# 启动服务
uvicorn rag_api:app --host 0.0.0.0 --port 8000
```
