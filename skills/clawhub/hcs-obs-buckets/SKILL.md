---
name: hcs-obs-buckets
version: 0.1.0
description: 查询华为云账号下关联 OBS 桶集合，支持列出账号下（region/project 范围）全部 OBS 桶、按桶名/前缀过滤、按资源（如 VPC/云服务器）关联查询，并支持列出桶内对象。
triggers:
  - 查询华为云OBS
  - 查询OBS桶
  - 列出账号下OBS桶
  - 按资源关联查询OBS
---

# hcs-obs-buckets

查询华为云 OBS（对象存储服务）桶的技能，提供三种能力：

- **能力 A**：列出账号下（region/project 范围）全部 OBS 桶，可按 `vpc_id` 过滤。
- **能力 B**：按桶名/前缀过滤。
- **能力 C**：查询某个资源（如 VPC/云服务器）关联的桶。
- **能力 D**：列出指定桶内对象列表。

## 环境变量（认证）

真实调用前需设置（不硬编码密钥）：

| 变量 | 必填 | 说明 |
|---|---|---|
| `HWCLOUD_AK` | 是 | 华为云 Access Key |
| `HWCLOUD_SK` | 是 | 华为云 Secret Key |
| `HWCLOUD_PROJECT_ID` | 否 | 项目 ID，缺省由 AK/SK 解析默认项目 |

## 使用

```bash
# 能力 A：列出全部桶（默认区域 cn-north-4）
python3 scripts/hcs-obs-buckets.py list --region cn-north-4

# 能力 B：按桶名/前缀过滤
python3 scripts/hcs-obs-buckets.py list --prefix prod

# 能力 C：查询某个资源（如 VPC / 云服务器）关联的 OBS 桶
python3 scripts/hcs-obs-buckets.py associated <resource_id 或名称>

# 能力 D：列出桶内对象
python3 scripts/hcs-obs-buckets.py objects --bucket <bucket_name_or_id>

# Markdown 表格输出
python3 scripts/hcs-obs-buckets.py list --format md

# 无凭证验证（内置模拟数据）
python3 scripts/hcs-obs-buckets.py list --mock
python3 scripts/hcs-obs-buckets.py associated vpc-prod --mock
python3 scripts/hcs-obs-buckets.py objects --bucket prod-data --mock
```

## 输出

默认 JSON，字段：

```json
{
  "capability": "list",
  "region": "cn-north-4",
  "project_id": "xxx",
  "count": 2,
  "buckets": [
    {"name": "prod-data", "region": "cn-north-4", "creation_time": "2024-01-01T00:00:00Z",
     "storage_class": "STANDARD"}
  ]
}
```

- 能力 C 额外含 `resource: {id, name}` 与 `associated_buckets`。
- `--format md` 输出 Markdown 表格（桶名/区域/创建时间/存储类别）。
- 能力 D 输出 `objects`: [{key, size, last_modified}]。

## 退出码

| 码 | 含义 |
|---|---|
| 0 | 成功 |
| 2 | 参数错误 |
| 3 | 缺少认证（未设置 HWCLOUD_AK/HWCLOUD_SK） |
| 4 | API 调用失败 |

## 依赖

- Python 3.8+
- 真实调用：`huaweicloudsdko`（见 `requirements.txt`）
- mock 模式无需任何第三方依赖

## 实现说明

OBS 服务本身不提供「资源 → 桶」的直接关联接口。桶通过 **桶策略/桶 ACL/账号级授权** 与资源关联，因此：

- 能力 A/B：`ListBuckets` 支持分页（`MaxKeys` + `Marker`）。
- 能力 C：通过 IAM/OBS 3.0 的接口按前缀/ResourceName 解析桶，再聚合。
- 能力 D：`ListObjects`（`prefix`、`max-keys`）。

详见 `references/obs-bucket-api.md`。