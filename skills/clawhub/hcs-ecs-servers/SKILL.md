---
name: hcs-ecs-servers
version: 0.1.0
description: 查询华为云 ECS 云服务器实例列表，支持列出账号下（region/project 范围）全部实例，可选按名称/状态过滤，输出实例名称、ID、状态、可用区、实例类型、IP 地址。
triggers:
  - 查询华为云ECS
  - 查询ECS实例
  - 列出云服务器
  - 华为云ECS列表
---

# hcs-ecs-servers

查询华为云 ECS（弹性云服务器）实例的技能，提供以下能力：

- **能力 A**：列出账号下（region/project 范围）全部 ECS 实例，可按 `--name` 模糊过滤、`--status` 状态过滤。
- 输出字段：实例名称、ID、状态、可用区、实例类型（flavor）、IP 地址、创建/更新时间。

## 环境变量（认证）

真实调用前需设置（不硬编码密钥）：

| 变量 | 必填 | 说明 |
|---|---|---|
| `HWCLOUD_AK` | 是 | 华为云 Access Key |
| `HWCLOUD_SK` | 是 | 华为云 Secret Key |
| `HWCLOUD_PROJECT_ID` | 否 | 项目 ID，缺省由 AK/SK 解析默认项目 |

## 使用

```bash
# 列出全部 ECS 实例（默认区域 cn-north-4）
python3 scripts/hcs-ecs-servers.py list --region cn-north-4

# 按名称模糊过滤
python3 scripts/hcs-ecs-servers.py list --name web-server

# 按状态过滤（ACTIVE / SHUTOFF / ERROR 等）
python3 scripts/hcs-ecs-servers.py list --status ACTIVE

# Markdown 表格输出
python3 scripts/hcs-ecs-servers.py list --format md

# 无凭证验证（内置模拟数据）
python3 scripts/hcs-ecs-servers.py list --mock
python3 scripts/hcs-ecs-servers.py list --mock --region cn-north-4 --format json
python3 scripts/hcs-ecs-servers.py list --mock --format md
```

## 输出

默认 JSON，字段：

```json
{
  "capability": "list",
  "region": "cn-north-4",
  "project_id": "xxx",
  "count": 2,
  "servers": [
    {
      "id": "i-0aaa1111bbbb2222cccc",
      "name": "web-server-01",
      "status": "ACTIVE",
      "availability_zone": "cn-north-4a",
      "flavor": {"id": "s6.large.2", "name": "s6.large.2", "vcpus": "2", "ram": "4096", "disk": "0"},
      "addresses": [{"addr": "192.168.1.10", "version": "4", "type": "fixed"}],
      "created": "2024-01-15T08:30:00Z",
      "updated": "2024-06-01T12:00:00Z"
    }
  ]
}
```

`--format md` 输出 Markdown 表格（实例名称/实例ID/状态/可用区/实例类型/IP地址）。

## 退出码

| 码 | 含义 |
|---|---|
| 0 | 成功 |
| 2 | 参数错误 |
| 3 | 缺少认证（未设置 HWCLOUD_AK/HWCLOUD_SK） |
| 4 | API 调用失败 |

## 依赖

- Python 3.8+
- 真实调用：`huaweicloudsdkecs`（见 `requirements.txt`）
- mock 模式无需任何第三方依赖

## 实现说明

使用华为云 ECS Python SDK (`huaweicloudsdkecs`) 的 `ListServersDetailsRequest` 分页拉取全部实例：

- API 端点：`GET /v1/{project_id}/cloudservers/detail`
- 分页参数：`limit`（最大 1000）+ `marker`（上一页最后一条实例 ID）
- 过滤参数：`name`（名称模糊匹配）、`status`（实例状态）

实例详情关键字段映射（SDK 属性 → JSON key）：

| SDK 属性 | JSON key | 说明 |
|---|---|---|
| `name` | `name` | 实例名称 |
| `id` | `id` | 实例 ID |
| `status` | `status` | 实例状态 |
| `os_ext_a_zavailability_zone` | `OS-EXT-AZ:availability_zone` | 可用区 |
| `flavor` | `flavor` | 实例类型（ServerFlavor 对象） |
| `addresses` | `addresses` | 网络地址（dict） |

详见 `references/ecs-servers-api.md`。
