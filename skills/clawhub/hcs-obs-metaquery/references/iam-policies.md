# IAM 权限策略

## 该 Skill 需要的华为云权限

| 操作 | IAM 权限 | 说明 |
|------|---------|------|
| 列出桶 | obs:bucket:ListBucket | 调用 ListBuckets 接口读取桶列表 |
| 列出对象 | obs:object:ListObject | 调用 ListObjects 接口读取桶内对象 |
| 创建桶 | obs:bucket:PutBucket | 创建新 OBS 桶 |
| 上传对象 | obs:object:PutObject | 上传文件到 OBS 桶 |
| 删除桶 | obs:bucket:DeleteBucket | 删除 OBS 桶 |
| 删除对象 | obs:object:DeleteObject | 删除 OBS 桶内对象 |
| 查询桶元数据 | obs:bucket:GetBucketMetadata | 获取桶存储类别/区域/冗余等信息 |
| 图片标签识别 | iam:image:tagging | 调用 Image Recognition REST API |
| 视频内容分析 | iam:vias:analysis | 调用 VIAS 视频分析 REST API |

## 最小权限策略

```json
{
  "Version": "1.1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "obs:bucket:ListBucket",
        "obs:object:ListObject",
        "obs:bucket:GetBucketMetadata"
      ],
      "Resource": ["*"]
    }
  ]
}
```

## 变更类操作权限（按需授予）

```json
{
  "Version": "1.1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "obs:bucket:PutBucket",
        "obs:object:PutObject",
        "obs:bucket:DeleteBucket",
        "obs:object:DeleteObject"
      ],
      "Resource": ["*"]
    }
  ]
}
```

## AI 语义检索权限（按需授予）

```json
{
  "Version": "1.1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:image:tagging",
        "iam:vias:analysis"
      ],
      "Resource": ["*"]
    }
  ]
}
```

## 权限说明

- 只读检索（标量检索/桶统计/桶列表）：只需 ListBucket/ListObject/GetBucketMetadata
- 变更操作（创建桶/上传对象）：需要 PutBucket/PutObject 权限
- 语义检索：需要 Image Recognition / VIAS 服务调用权限
- 不需要管理员权限
