---
name: huawei-cloud-ecs-list
description: |
  查询华为云 ECS（弹性云服务器）实例列表与详情。支持基础列表查询、
  按条件过滤（区域/状态/名称关键字/规格/IP）以及按实例 ID 查询详情。
  只读操作，JSON 输出全部字段，AK/SK 环境变量认证。
version: 1.0.0
triggers:
  - 查询华为云ECS
  - 列出ECS实例
  - ECS实例查询
  - 华为云服务器列表
  - 查看ECS详情
tags:
  - huawei-cloud
  - ecs
  - query
  - list
  - show
tools:
  - hcloud
---

# Huawei Cloud ECS 查询 Skill

## 安全硬约束

1. **AK/SK 不写日志/不硬编码**：凭据通过动态扫描环境变量获取（`HUAWEI_AK`/`HUAWEI_SK` 等任意 `HUAWEI*`/`HW*`/`HWC*` 前缀变量），不写死任何固定变量名，不输出到日志/评论。
2. **超时控制**：所有 hcloud CLI 调用设 30s 超时（`HCLOUD_TIMEOUT=30`），超时判定失败不 hang。
3. **403/401 处理**：鉴权失败时返回明确错误提示（exit 3），不尝试其他 token 或绕行手段。
4. **只读操作**：仅支持 List / Show（GET），无创建/删除/变更操作，无不可逆风险。
5. **参数校验**：状态过滤使用枚举校验，实例 ID / 区域参数经校验后透传 hcloud，防注入。

## Overview / 概述

本 skill 用于查询华为云 ECS（弹性云服务器）实例信息，提供两个核心功能：

- **列表查询（list）**：查询当前账号下的 ECS 实例列表，支持按区域、状态、名称关键字、规格、IP 过滤。
- **详情查询（show）**：按实例 ID 查询单个 ECS 实例的完整详情。

**架构**：用户 → Python 脚本 → hcloud CLI → 华为云 ECS API（ListServersDetails / ShowServer）→ 返回 JSON。

**适用场景**：日常巡检、资源盘点、故障排查、实例信息核查。

**技术模式**：CLI（hcloud KooCLI 优先）。SDK 未安装时自动使用 CLI 模式；hcloud 已配置 AKSK 认证或通过 `--cli-access-key`/`--cli-secret-key` 运行时注入。

## Prerequisites / 前置条件

1. **hcloud CLI**：已安装 KooCLI（版本 ≥ 4.0），安装方法见 `references/cli-installation-guide.md`。
2. **认证配置**：AK/SK 通过环境变量注入（如 `HUAWEI_AK` / `HUAWEI_SK`），脚本动态扫描 `HUAWEI*`/`HW*`/`HWC*` 前缀的变量。
3. **IAM 权限**：`ECS:ecs:servers:list`（只读），详见 `references/iam-policies.md`。
4. **Python 3.8+**：运行入口脚本。

## Workflow / 工作流

1. 脚本启动，动态扫描环境变量获取 AK/SK。
2. 校验 AK/SK 非空（缺失 → exit 3，输出 JSON 错误到 stderr）。
3. 解析子命令与参数（list / show / capability-list）。
4. 组装 hcloud CLI 命令，注入 `--cli-access-key`/`--cli-secret-key`。
5. 执行 hcloud 调用（30s 超时）。
6. 解析 JSON 响应，输出到 stdout（全部字段保留）。
7. 错误处理：空列表返回 `{"count":0,"servers":[]}`；无效 ID 返回明确错误；API 失败返回 JSON 错误。

## Core Commands / 核心命令

### 列表查询

```bash
# 列出所有 ECS 实例（默认区域 cn-north-4）
python3 scripts/huawei-cloud-ecs-list.py list

# 指定区域
python3 scripts/huawei-cloud-ecs-list.py list --region cn-east-3

# 按状态过滤
python3 scripts/huawei-cloud-ecs-list.py list --status ACTIVE

# 按名称关键字过滤（模糊匹配）
python3 scripts/huawei-cloud-ecs-list.py list --name web

# 按规格过滤
python3 scripts/huawei-cloud-ecs-list.py list --flavor s6.small.1

# 按 IP 过滤（模糊匹配）
python3 scripts/huawei-cloud-ecs-list.py list --ip 192.168

# 组合过滤 + 分页
python3 scripts/huawei-cloud-ecs-list.py list --region cn-north-4 --status ACTIVE --name web --limit 100
```

### 详情查询

```bash
# 按实例 ID 查询详情
python3 scripts/huawei-cloud-ecs-list.py show --server-id i-xxxxxxx

# 指定区域查询详情
python3 scripts/huawei-cloud-ecs-list.py show --server-id i-xxxxxxx --region cn-east-3
```

### 能力列表

```bash
# 查看支持的操作
python3 scripts/huawei-cloud-ecs-list.py capability-list
```

### 帮助

```bash
python3 scripts/huawei-cloud-ecs-list.py --help
python3 scripts/huawei-cloud-ecs-list.py list --help
```

## Parameter Confirmation / 参数确认

| 参数 | 子命令 | 必填 | 默认值 | 说明 |
|------|--------|------|--------|------|
| `--region` | list / show | 否 | cn-north-4 | 区域 ID（如 cn-north-4、cn-east-3） |
| `--status` | list | 否 | - | 实例状态：ACTIVE/SHUTOFF/ERROR/BUILD/REBOOT 等 |
| `--name` | list | 否 | - | 实例名称关键字（API 模糊匹配） |
| `--flavor` | list | 否 | - | 规格 ID（如 s6.small.1） |
| `--ip` | list | 否 | - | IPv4 地址（模糊匹配） |
| `--limit` | list | 否 | 25 | 每页最大返回数（max 1000） |
| `--offset` | list | 否 | 1 | 页码 |
| `--server-id` | show | 是 | - | ECS 实例 ID（UUID 格式） |

## KooCLI Command Format Standard

本 skill 通过 hcloud CLI 调用华为云 ECS API，命令格式遵循 KooCLI 规范：

```
hcloud ECS <Operation> --cli-region=<region> [--params] --cli-access-key=<AK> --cli-secret-key=<SK>
```

| 操作 | hcloud 命令 | HTTP 方法 | API 端点 |
|------|------------|-----------|----------|
| 列表 | `hcloud ECS ListServersDetails` | GET | `/v1/{project_id}/cloudservers/detail` |
| 详情 | `hcloud ECS ShowServer` | GET | `/v1/{project_id}/cloudservers/{server_id}` |

**参数规范**：
- Service 名：`ECS`（首字母大写）
- Operation 名：PascalCase（`ListServersDetails` / `ShowServer`）
- `--cli-region`：必填，指定区域
- `--cli-access-key` / `--cli-secret-key`：运行时注入 AK/SK（不依赖固定 profile）
- `--project_id`：hcloud 自动从认证信息解析，无需手动指定

## Reference Documents / 参考文档

- [IAM 权限策略](references/iam-policies.md)
- [hcloud CLI 安装指南](references/cli-installation-guide.md)
- [验证方法](references/verification-method.md)
- [数据流图](references/dataflow-diagram.md)
- [验收标准](references/acceptance-criteria.md)

## 输出格式

所有输出为 JSON：

- **list**：`{"count": N, "servers": [...]}`（空列表时 `count=0, servers=[]`）
- **show**：`{"server": {...}}`（包含实例全部字段）
- **错误**：`{"error": "消息", "details": "..."}`（输出到 stderr）

**实例字段**（API 返回全部字段，包括但不限于）：实例 ID、名称、状态、公网 IP、私网 IP、规格（vCPU/内存）、区域、可用区、创建时间、镜像、VPC、子网、安全组、磁盘等。

## 退出码

| 退出码 | 含义 |
|--------|------|
| 0 | 成功 |
| 2 | 输入无效（参数错误/实例 ID 无效） |
| 3 | AK/SK 缺失或无效 |
| 4 | API 调用失败（超时/网络/服务端错误） |
