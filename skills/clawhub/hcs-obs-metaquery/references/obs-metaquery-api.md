# OBS MetaQuery API 参考

> 依据华为云 OBS SDK 及 AI 服务官方文档整理。

## 1. 桶列表（ListBuckets）

```
SDK: client.list_buckets(ListBucketsRequest())
返回: resp.buckets.bucket -> [{name, location, creation_date}]
```

- `ListBucketsRequest()` — 无需参数，返回账号下全部桶
- 每个桶对象含：`name`（桶名）、`location`（区域）、`creation_date`（创建时间）

## 2. 对象列表（ListObjects）

```
SDK: client.list_objects(ListObjectsRequest(
    bucket_name=<bucket>, prefix=<prefix>, max_keys=<n>, marker=<marker>))
返回: resp.contents.object -> [{key, size, last_modified}]
```

- `bucket_name` — 桶名（必填）
- `prefix` — 对象名前缀过滤
- `max_keys` — 单次返回最大数量（默认 1000）
- `marker` — 分页标记（上次返回最后一个对象的 key）
- 返回对象含：`key`（对象名）、`size`（字节数）、`last_modified`（最后修改时间）

## 3. 创建桶（CreateBucket）

```
SDK: client.create_bucket(CreateBucketRequest(
    bucket_name=<name>, body=CreateBucketRequestBody(location=<region>),
    x_obs_storage_class=<STANDARD|WARM|COLD>))
```

- `bucket_name` — 桶名（必填，全局唯一）
- `body.location` — 桶所在区域
- `x_obs_storage_class` — 存储类别

## 4. 上传对象（PutObject）

```
SDK: client.put_object(PutObjectRequest(
    bucket_name=<bucket>, object_key=<key>, stream=<file_stream>))
```

- `bucket_name` — 桶名
- `object_key` — 对象名
- `stream` — 文件流（Python file object）

## 5. 删除桶（DeleteBucket）

```
SDK: client.delete_bucket(DeleteBucketRequest(bucket_name=<name>))
```

## 6. 删除对象（DeleteObject）

```
SDK: client.delete_object(DeleteObjectRequest(
    bucket_name=<bucket>, object_key=<key>))
```

## 7. 桶元数据（GetBucketMetadata）

```
SDK: client.get_bucket_metadata(GetBucketMetadataRequest(bucket_name=<name>))
返回: resp.x_obs_storage_class, resp.x_obs_bucket_location, resp.x_obs_az_redundancy
```

## 8. 语义检索——AI 服务 REST API

### 8.1 Image Recognition（图片标签识别）

```
POST https://{region}.api.{region}.myhuaweicloud.com/v2/{project_id}/image/tagging
Body: {"url": "<obs_object_url>", "language": "zh"}
返回: {"result": {"tags": [{"tag": "sunset", "confidence": 0.95}]}}
```

- 参考: https://support.huaweicloud.com/api-image/image_01_0007.html
- 认证: AK/SK 签名（huaweicloudsdkcore Signer）
- 输入: OBS 对象的公开或授权 URL
- 输出: 图片标签列表 + 置信度

### 8.2 VIAS 视频分析服务

```
POST https://{region}.api.{region}.myhuaweicloud.com/v2/{project_id}/video-analysis
Body: {"obs_url": "<obs_object_url>", "analysis_type": "tagging"}
返回: {"result": {"tags": [{"tag": "presentation", "confidence": 0.88}]}}
```

- 参考: https://support.huaweicloud.com/api-vias/vias_01_0001.html
- 认证: AK/SK 签名
- 输入: OBS 对象 URL
- 输出: 视频内容标签 + 置信度

## 9. 认证

### OBS SDK 认证
- 使用 `ObsCredentials(ak, sk)` 构建（注意：OBS SDK 不使用 BasicCredentials）
- AK/SK 从环境变量动态扫描获取

### AI 服务 REST API 认证
- 使用 `huaweicloudsdkcore.signer.signer.Signer` 进行 AK/SK 签名
- 需要 project_id（从环境变量获取）

## 10. 区域域名

- OBS: `https://obs.{region}.myhuaweicloud.com`
- Image Recognition: `https://{region}.api.{region}.myhuaweicloud.com`
- VIAS: `https://{region}.api.{region}.myhuaweicloud.com`

## 依赖

- Python 3.8+
- `huaweicloudsdkobs` — OBS SDK（桶/对象管理）
- `huaweicloudsdkcore` — 核心库（签名器）
- `requests` — REST API 调用（AI 服务）
- mock 模式无需任何第三方依赖
