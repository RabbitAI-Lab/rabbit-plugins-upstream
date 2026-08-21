---
name: hcs-obs-metaquery
version: 0.1.0
description: |
  为华为云 OBS 提供语义检索 + 标量检索 + AI 内容感知开通 + 桶/对象管理能力。
  基于 OBS SDK 管理桶/对象，通过华为云 AI 服务 REST API（Image Recognition / VIAS）
  实现以文搜图/视频的语义检索。支持 --mock 模式无凭证验证。
triggers:
  - 查询华为云OBS元数据
  - OBS语义检索
  - OBS标量检索
  - 以文搜图OBS
  - OBS AI内容感知
tags:
  - huawei-cloud
  - obs
  - metaquery
  - ai-search
---

# hcs-obs-metaquery

## Overview / 概述

为华为云 OBS（对象存储服务）提供元数据检索与 AI 内容感知能力的技能，全对标阿里云
`alibabacloud-oss-manage-metaquery`。

| 能力 | 子命令 | 说明 |
|------|--------|------|
| 标量检索 | `scalar-search` | 按文件名/大小/类型/时间过滤桶内对象 |
| 语义检索 | `semantic-search` | 基于华为云 AI 服务（Image Recognition / VIAS）+ OBS 对象列表组合实现以文搜图/视频 |
| AI 内容感知开通 | `enable-ai` | 为 OBS 桶配置 AI 分析能力（图片/视频语义提取） |
| AI 内容感知查询 | `ai-status` | 查询桶的 AI 分析配置状态 |
| AI 内容感知关闭 | `disable-ai` | 关闭桶的 AI 分析配置 |
| 桶管理 | `create-bucket` | 创建 OBS 桶 |
| 桶管理 | `upload-object` | 上传文件到 OBS 桶 |
| 桶统计 | `bucket-stats` | 查询桶的元数据信息（存储类别/区域/冗余等） |
| 桶列表 | `list-buckets` | 列出账号下全部 OBS 桶 |
| 能力清单 | `capability-list` | 列出本 skill 所有能力项 |

## Prerequisites / 前置条件

- Python 3.8+
- 真实调用：`huaweicloudsdkobs` + `huaweicloudsdkcore`（见 `requirements.txt`）
- AI 语义检索：`requests`（REST API 调用华为云 Image Recognition / VIAS 服务）
- mock 模式无需任何第三方依赖

真实调用前需设置环境变量（不硬编码密钥）：

| 变量 | 必填 | 说明 |
|------|------|------|
| `HWCLOUD_AK` | 是 | 华为云 Access Key |
| `HWCLOUD_SK` | 是 | 华为云 Secret Key |
| `HWCLOUD_PROJECT_ID` | 否 | 项目 ID，缺省由 AK/SK 解析默认项目 |

## Workflow / 工作流

### 标量检索

基于 OBS ListObjects API 返回的元数据（key/size/last_modified），本地按文件名/大小/类型/时间过滤。

### 语义检索

华为云 OBS 无桶级向量索引服务（不同于阿里云 MetaQuery），采用组合方案：

- 图片对象：调用华为云 Image Recognition REST API 进行图像标签识别
- 视频对象：调用华为云 VIAS（视频分析服务）REST API 进行视频内容分析
- 将 AI 分析结果与 OBS 对象列表组合，按自然语言查询匹配返回

### AI 内容感知开通/关闭

为桶配置 AI 分析能力，记录桶级 AI 配置状态（启用/关闭），对应阿里云 MetaQuery 的
ImageInsightEnable / VideoInsightEnable。

详见 `references/obs-metaquery-api.md`。

## Core Commands / 核心命令

```bash
# 能力清单
python3 scripts/hcs-obs-metaquery.py capability-list --mock

# 标量检索（按文件名/大小/类型/时间过滤）
python3 scripts/hcs-obs-metaquery.py scalar-search --bucket my-bucket --mock
python3 scripts/hcs-obs-metaquery.py scalar-search --bucket my-bucket --name-filter ".png" --min-size 1024 --mock
python3 scripts/hcs-obs-metaquery.py scalar-search --bucket my-bucket --type image --mock

# 语义检索（以文搜图/视频）
python3 scripts/hcs-obs-metaquery.py semantic-search --bucket my-bucket --query "风景" --mock

# AI 内容感知开通（为桶配置图片/视频语义提取）
python3 scripts/hcs-obs-metaquery.py enable-ai --bucket my-bucket --ai-type image --mock
python3 scripts/hcs-obs-metaquery.py enable-ai --bucket my-bucket --ai-type video --mock

# AI 内容感知查询
python3 scripts/hcs-obs-metaquery.py ai-status --bucket my-bucket --mock

# AI 内容感知关闭
python3 scripts/hcs-obs-metaquery.py disable-ai --bucket my-bucket --mock

# 桶管理
python3 scripts/hcs-obs-metaquery.py create-bucket --bucket new-bucket --region cn-north-4
python3 scripts/hcs-obs-metaquery.py upload-object --bucket my-bucket --file /path/to/file.png
python3 scripts/hcs-obs-metaquery.py bucket-stats --bucket my-bucket --mock

# 桶列表
python3 scripts/hcs-obs-metaquery.py list-buckets --mock

# Markdown 表格输出
python3 scripts/hcs-obs-metaquery.py scalar-search --bucket my-bucket --format md --mock
```

## Parameter Confirmation / 参数确认

| 参数 | 适用命令 | 必填 | 默认值 | 说明 |
|------|---------|------|--------|------|
| `--bucket` | scalar-search, semantic-search, enable-ai, ai-status, disable-ai, create-bucket, upload-object, bucket-stats | 是 | - | OBS 桶名 |
| `--region` | create-bucket, list-buckets | 否 | cn-north-4 | 华为云区域 |
| `--query` | semantic-search | 是 | - | 自然语言搜索词 |
| `--name-filter` | scalar-search | 否 | - | 按文件名过滤（子串匹配） |
| `--min-size` | scalar-search | 否 | - | 最小文件大小（bytes） |
| `--max-size` | scalar-search | 否 | - | 最大文件大小（bytes） |
| `--type` | scalar-search | 否 | - | 文件类型过滤（image/video/document/etc） |
| `--ai-type` | enable-ai | 是 | - | AI 分析类型（image/video） |
| `--file` | upload-object | 是 | - | 上传文件路径 |
| `--format` | scalar-search, bucket-stats | 否 | json | 输出格式（json/md） |
| `--mock` | 全部子命令 | 否 | false | 无凭证 mock 模式 |

## 输出

默认 JSON，字段因能力而异：

### 标量检索

```json
{
  "capability": "scalar-search",
  "bucket": "my-bucket",
  "filters": {"name": ".png", "min_size": 1024, "type": "image"},
  "count": 2,
  "objects": [{"key": "img/photo.png", "size": 4096, "last_modified": "...", "type": "image"}]
}
```

### 语义检索

```json
{
  "capability": "semantic-search",
  "bucket": "my-bucket",
  "query": "风景",
  "count": 3,
  "results": [{"key": "photos/landscape.png", "score": 0.95, "tags": ["mountain", "sky"]}]
}
```

### AI 内容感知

```json
{
  "capability": "enable-ai",
  "bucket": "my-bucket",
  "ai_type": "image",
  "status": "enabled",
  "service": "Image Recognition"
}
```

## 退出码

| 码 | 含义 |
|----|------|
| 0 | 成功 |
| 2 | 参数错误 |
| 3 | 缺少认证（未设置 HWCLOUD_AK/SK） |
| 4 | API 调用失败 |

## 参考文档

- [IAM 权限策略](references/iam-policies.md)
- [API 参考](references/obs-metaquery-api.md)
- [验证方法](references/verification-method.md)
- [验收标准](references/acceptance-criteria.md)
