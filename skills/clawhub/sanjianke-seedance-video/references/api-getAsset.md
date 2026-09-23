# Seedance 2.0 · 获取素材详情

> a7w 插件 `seedance` 的接口 `getAsset` · 官方文档

---

## 获取素材详情（GetAsset）

`POST /api/v1/apps/seedance/getAsset`

Content-Type: `multipart/form-data`

`Result.Status`：
- Active：处理完毕，可以使用
- Processing：正在预处理
- Failed：处理失败