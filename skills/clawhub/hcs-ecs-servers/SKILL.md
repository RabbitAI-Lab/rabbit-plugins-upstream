---
name: hcs-ecs-servers
version: 0.1.0
description: |
  查询华为云 ECS（弹性云服务器）实例列表。CLI 工具支持 list-servers 子命令，
  返回实例名称/ID/状态/IP/规格，支持 --region 和 --status 筛选。
  AK/SK 签名认证，通过环境变量或 .project-info/ JSON 配置解析凭据。
triggers:
  - 查询华为云ECS
  - 列出云服务器
  - ECS实例查询
  - 华为云服务器列表
tags:
  - huawei-cloud
  - ecs
  - query
  - cli
tools:
  - curl
  - python3
---

# hcs-ecs-servers

## Overview / 概述

查询华为云 ECS（弹性云服务器）实例列表的 CLI 工具。通过华为云 ECS API（`GET /v1/{project_id}/cloudservers/detail`）查询实例信息，AK/SK 签名认证，返回实例名称、ID、状态、IP 地址、规格等关键字段。

## 安全硬约束（必须遵守）

**通用约束（所有 skill 必含）**：

1. 严禁读取 data/、configs/、sessions.db、user_accounts 等 Grape 内部数据。
2. API 返回 403/无权限时：立即停止该操作并回复用户，严禁尝试其他 token 或绕行手段。
3. 所有 curl / API 调用设 30s 超时——超时判定失败，不 hang。
4. 严禁 mock 模式/假数据：所有 API 调用必须真实访问目标系统。
5. AK/SK 不写入任何文件/日志/评论，仅从环境变量/项目知识读取。

**动态约束**：

- 本 skill 为只读查询类，仅调用 ListServersDetails API，不涉及创建/删除/变更操作。
- 凭据（AK/SK）通过环境变量或 `.project-info/` JSON 配置解析，不硬编码。

## 评论规范

- 所有 Issue/PR 评论 body 必须以 `[Coding Agent]` 开头
- 引用用户原文：`> {用户评论}\n\n[Coding Agent] {回复}`

## Configuration

华为云 AK/SK 凭据必须在使用前配置。凭据解析优先级：

1. **项目知识** — 递归扫描 `.project-info/` 下所有 JSON 文件（`secrets.HUAWEI_AK` / `secrets.HUAWEI_SK`）
2. **环境变量** — 动态扫描 `HUAWEI`/`HW`/`HWC` 开头 + 含 `ACCESS_KEY`/`_AK`/`SECRET_KEY`/`_SK` 的环境变量

### 配置指导

**方式一：环境变量（临时，推荐快速测试）**

```bash
export HUAWEI_AK="your-access-key"
export HUAWEI_SK="your-secret-key"
```

或使用任意 `HUAWEI`/`HW`/`HWC` 前缀 + `AK`/`SK` 后缀的变量名：

```bash
export HUAWEICLOUD_SDK_AK="your-access-key"
export HUAWEICLOUD_SDK_SK="your-secret-key"
```

**方式二：项目知识 JSON 文件（持久化，推荐生产使用）**

在项目根目录下创建 `.project-info/` 目录，放入任意名称的 `.json` 文件：

```json
{
  "secrets": {
    "HUAWEI_AK": "your-access-key",
    "HUAWEI_SK": "your-secret-key"
  }
}
```

> ⚠️ `.project-info/` 含敏感配置，不提交到 git 仓库（加入 .gitignore）。

### 区域配置

- 默认区域：`cn-north-4`（可通过 `--region` 参数覆盖）
- project_id 自动通过 IAM API `GET /v3/projects?name={region}` 获取

## 场景 / When to Use

- 用户要求查询华为云 ECS 实例列表
- 用户需要查看云服务器状态（运行中/关机/异常等）
- 用户需要查看 ECS 实例的 IP 地址、规格信息
- 日常巡检/故障排查时需要快速查看 ECS 资源概览

Don't use for: 非 ECS 服务的查询（VPC/OBS/RDS 等已有或将有独立 skill）；ECS 实例的创建/删除/启停等变更操作；hcloud CLI 封装。

## 知识 / Knowledge

### API 端点

```
GET https://ecs.{region}.myhuaweicloud.com/v1/{project_id}/cloudservers/detail
```

认证方式：AK/SK 签名（SDK-HMAC-SHA256）

### 返回字段

| 字段 | 类型 | 说明 |
|------|------|------|
| name | string | 实例名称 |
| id | string | 实例 ID |
| status | string | 实例状态（ACTIVE/SHUTOFF/ERROR 等） |
| addresses | object | 网络地址（含私有/公网 IP） |
| flavor | object | 规格信息（id/vcpus/ram） |
| created | string | 创建时间 |
| availability_zone | string | 可用区 |

### Common Pitfalls

1. **AK/SK 权限需匹配区域。** AK/SK 绑定特定区域项目，跨区域调用会返回 401（`Common.0013`）。
2. **project_id 必须正确。** 不同区域有不同的 project_id，脚本自动从 IAM API 获取。
3. **空列表是正常的。** 如果该区域无 ECS 实例，API 返回 `count: 0, servers: []`，退出码仍为 0。
4. **status 筛选是 API 层筛选。** `--status` 参数直接传给 API 的 `status` query 参数，支持的值：`ACTIVE`/`SHUTOFF`/`BUILD`/`ERROR`/`REBOOT`/`HARD_REBOOT`/`MIGRATING`。

## 步骤 / Steps

### 1. 检查凭据配置

```bash
python3 scripts/hcs-ecs-servers.py capability-list
```
Expected: 输出 skill 能力清单

### 2. 查询 ECS 实例列表

```bash
python3 scripts/hcs-ecs-servers.py list-servers
```
Expected: 返回 ECS 实例列表（名称/ID/状态/IP/规格）

### 3. 按区域/状态筛选

```bash
python3 scripts/hcs-ecs-servers.py list-servers --region cn-north-4 --status ACTIVE
```

### 4. JSON 格式输出

```bash
python3 scripts/hcs-ecs-servers.py list-servers --json
```

### 5. 分页查询

```bash
python3 scripts/hcs-ecs-servers.py list-servers --limit 10 --offset 1
```

## Core Commands / 核心命令

### list-servers

查询华为云 ECS 实例列表。

```bash
python3 scripts/hcs-ecs-servers.py list-servers [--region REGION] [--status STATUS] [--limit N] [--offset N] [--json]
```

参数说明：

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| --region | string | cn-north-4 | 华为云区域 |
| --status | string | - | 实例状态筛选（ACTIVE/SHUTOFF/ERROR 等） |
| --limit | int | - | 每页最大返回数（API 默认 25，最大 1000） |
| --offset | int | - | 页码偏移（从 1 开始） |
| --json | flag | false | 输出 JSON 格式（默认表格格式） |

### capability-list

列出本 skill 所有能力项。

```bash
python3 scripts/hcs-ecs-servers.py capability-list
```

## Parameter Confirmation / 参数确认

| 参数 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| AK | 是 | - | 华为云 Access Key（环境变量/项目知识） |
| SK | 是 | - | 华为云 Secret Key（环境变量/项目知识） |
| region | 否 | cn-north-4 | 华为云区域 |
| status | 否 | - | 实例状态筛选 |
| limit | 否 | - | 每页返回数 |
| offset | 否 | - | 页码偏移 |

## KooCLI Command Format Standard

本 skill 不使用 hcloud CLI，使用 Python+requests 直接调用华为云 ECS API。API 端点通过 SDK `_http_info` 确认：

- Service: ECS
- Operation: ListServersDetails
- Method: GET
- Resource Path: `/v1/{project_id}/cloudservers/detail`

## 前置条件 / Prerequisites

- Python 3.8+
- `requests` 库（`pip install requests`）
- `huaweicloudsdkcore` 库（签名用，`pip install huaweicloudsdkcore`）
- 华为云 AK/SK 凭据（ECS 只读权限）
- IAM 权限：`ECS:cloudServers:list`

## Workflow / 工作流

1. **读取凭据** — 从环境变量/项目知识获取 AK/SK
2. **获取 project_id** — 调用 IAM API `GET /v3/projects?name={region}`
3. **签名请求** — 使用 huaweicloudsdkcore Signer 生成 SDK-HMAC-SHA256 签名
4. **调用 ECS API** — `GET /v1/{project_id}/cloudservers/detail`
5. **格式化输出** — 表格格式（默认）或 JSON 格式（--json）

## 判断标准 / Verification

- [ ] `python3 scripts/hcs-ecs-servers.py list-servers` 可查询 ECS 实例列表
- [ ] 返回实例名称、ID、状态、IP、规格等关键字段
- [ ] 支持 `--region` 区域参数指定
- [ ] 支持 `--status` 状态筛选
- [ ] AK/SK 凭据通过环境变量或 `.project-info/` JSON 配置解析
- [ ] `--help` 无语法错误，退出码规范（0=成功/2=参数错误/3=缺少配置/4=API失败）
- [ ] `--json` 选项输出 JSON 格式结果

## 输出规范 / Output Format

### 表格格式（默认）

```
实例名称          实例ID              状态     规格            私有IP          公网IP
test-ecs-01       1234abcd...         ACTIVE   s6.large.2      192.168.1.10    1.2.3.4
```

### JSON 格式（--json）

```json
{
  "count": 1,
  "servers": [
    {
      "name": "test-ecs-01",
      "id": "1234abcd-...",
      "status": "ACTIVE",
      "flavor": "s6.large.2",
      "private_ip": "192.168.1.10",
      "public_ip": "1.2.3.4"
    }
  ]
}
```

## 参考文档 / References

- [API 端点文档](references/api-reference.md)
- [IAM 权限策略](references/iam-policies.md)
- [验证方法](references/verification-method.md)
- [数据流图](references/dataflow-diagram.md)
- [测试用例](templates/test-vars.json)

## 分析结论示例

```
分析结论：
- 场景：查询华为云 ECS 实例列表
- Skill：hcs-ecs-servers v0.1.0
- 操作：list-servers --region cn-north-4
- 结果：✅ 成功（返回 N 个实例）
- 必须执行：Issue 评论汇总结果 → 任务结束
```
