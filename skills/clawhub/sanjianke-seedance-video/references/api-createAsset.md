# Seedance 2.0 · 上传素材

> a7w 插件 `seedance` 的接口 `createAsset` · 官方文档

---

## 上传素材（CreateAsset）

`POST /api/v1/apps/seedance/createAsset`

Content-Type: `multipart/form-data`

上游会异步处理素材，调用 `getAsset` 查询 `Status` 为 `Active` 后即可在创建任务中以 `asset://<ASSET_ID>` 引用。