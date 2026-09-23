# AI换装 · 提交换装任务

> a7w 插件 `dressing_diffusion` 的接口 `submit` · 官方文档

---

## 提交换装任务

`POST /api/v1/apps/dressing_diffusion/submit`

上传模特图和服装图，AI 自动生成试穿效果。
支持单件上衣、单件下装、上下套装、连衣裙/全身装四种模式。

### 图片要求
- 格式：JPG / JPEG / PNG，建议 JPG
- 模特图：主体清晰、光线均匀
- 服装图：白底或纯色背景、平铺展示

### 请求示例
```json
{
  "model_url": "https://example.com/model.jpg",
  "garment": {
    "data": [
      {"category": "upper", "url": "https://example.com/shirt.jpg"},
      {"category": "bottom", "url": "https://example.com/pants.jpg"}
    ]
  }
}
```

### 返回示例
```json
{"task_id": "7xxxxxxxxxxxxxx", "status": "pending"}
```

提交成功后使用 `query` 接口轮询结果。