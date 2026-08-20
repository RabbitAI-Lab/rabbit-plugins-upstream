# 华为云 OBS 桶相关 API 摘录（用于 hcs-obs-buckets 技能）

> 依据华为云 OBS 官方文档整理。真实调用使用华为云官方 Python SDK `huaweicloudsdkobs`（v3 `ObsClient`），对应的 REST 接口如下。

## 1. 列举全部桶 / 过滤（能力 A / B）

```
GET /?type=OBS   # 实际需经鉴权（如 AK/SK 签名）
```

华为云 OBS 的桶列举走「HeadBucket / ListAllMyBuckets」风格，实际 SDK 封装为：

- `ListBucketsRequest` → `client.list_buckets()`（支持 `marker` + `max_keys` 分页）
- 返回 `Buckets`，每项含：
  - `name`：桶名
  - `creation_time`：创建时间
  - `storage_class`：存储类别（STANDARD / STANDARD_IA / GLACIER 等）
- 可选服务端过滤：按 `prefix` 前缀匹配

## 2. 查询关联桶（能力 C）

真实环境中「资源 → 桶」无直接列表接口。通过 IAM/OBS 策略与项目级授权建立关联。查询路径：

```
资源（VPC/云服务器） → IAM/策略检索 → 解析允许访问的桶名 → 去重聚合
```

参考：`IAMPolicy`（列出用户/角色的策略）→ `ListBuckets`（账号下可见范围）。组合后得到「资源关联桶集合」。

## 3. 列举桶内对象（能力 D）

```
GET /{bucket}?list-type=2&prefix={prefix}&max-keys={n}
```

SDK：`ListObjectsRequest` / `client.list_objects`，支持：

- `prefix` 前缀过滤
- `max_keys` 限制数量
- 返回 `Contents`（对象名 / Size 大小 / LastModified 最后修改时间）

## 区域域名

- 北京四（cn-north-4，默认）：`https://obs.{region}.myhuaweicloud.com`
- 其余区域：`https://obs.{region}.myhuaweicloud.com`

## 认证

- AK/SK（环境变量 `HWCLOUD_AK` / `HWCLOUD_SK`），经 `huaweicloudsdkcore.auth.credentials.BasicCredentials` 构造。
- 项目 ID：`BasicCredentials.with_project_id()` 显式指定；缺省由 AK/SK 解析出默认项目。

## 依赖

- Python 3.8+
- 真实调用：`huaweicloudsdkobs`（见 `requirements.txt`）
- mock 模式无需任何第三方依赖

---

> 本文件是 `references/obs-bucket-api.md` 的摘要摘录，供技能实现时对照。