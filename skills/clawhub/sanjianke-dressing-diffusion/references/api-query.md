# AI换装 · 查询换装结果

> a7w 插件 `dressing_diffusion` 的接口 `query` · 官方文档

---

## 查询换装结果

`POST /api/v1/apps/dressing_diffusion/query`

根据 `submit` 返回的 `task_id` 查询换装任务状态和结果图片。
任务处理通常需要 10~30 秒，建议每 3~5 秒轮询一次。

### 返回示例（处理中）
```json
{"task_id": "7xxxxxxxxxxxxxx", "status": "processing"}
```

### 返回示例（完成）
```json
{
  "task_id": "7xxxxxxxxxxxxxx",
  "status": "done",
  "images": ["https://cdn.example.com/result_1.jpg"]
}
```