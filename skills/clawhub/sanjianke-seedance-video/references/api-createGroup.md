# Seedance 2.0 · 创建素材资产组合

> a7w 插件 `seedance` 的接口 `createGroup` · 官方文档

---

## 创建素材资产组合（Asset Group）

`POST /api/v1/apps/seedance/createGroup`

Content-Type: `multipart/form-data`

同步接口；调用成功后返回上游 `Result.Id`，用于后续上传素材时填入 `GroupId`。