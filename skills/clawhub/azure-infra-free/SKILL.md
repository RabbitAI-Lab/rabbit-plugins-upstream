---
slug: "azure-infra-free"
name: "azure-infra-free"
version: "2.0.0"
displayName: "Azure Infra Free"
summary: "通过本地 Azure CLI 只读查询 Azure 资源，基础盘点与健康检查。"
license: "MIT"
description: |-
  Azure Infra Free 是 Azure Infra 技能的免费精简版，通过本地 Azure CLI（az 命令）
  提供 Azure 资源的只读查询能力。支持基础的资源清单查询与简单的健康检查，
  不包含写操作、安全审计、成本分析等高级功能.
  核心能力：
  - 资源清单查询：资源组、虚拟机、存储账户、虚拟网络等基础资源的列举
  - 简单健康检查：查看虚拟机电源状态、查询失败的活动日志
  - 只读优先：所有操作默认只读，不执行任何写操作或破坏性变更

  适用场景：
  - 快速盘点订阅内的虚拟机与存储资源
  - 查看虚拟机运行状态
  - 初步了解 Azure 资源分布

  限制：不支持写操作（启停 VM、删除资源）、安全审计、RBAC 检查、Cost Management、
  跨订阅批量查询。如需完整能力，请升级至付费版 azure-infra 技能.
tags:
  - Agents
  - Cloud
  - Azure
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# Azure Infra Free

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Azure Infra Free处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 概述

通过本地 Azure CLI（`az` 命令）对 Azure 资源进行只读查询。本免费版仅支持基础盘点与健康检查，不执行任何写操作.
## 快速开始

1. 检查 CLI 是否安装：`az --version`。若未安装，提示用户安装 Azure CLI.
2. 检查登录状态：`az account show`。若未登录，引导用户执行 `az login --use-device-code`.
3. 使用默认订阅或询问用户选择目标订阅.
4. 使用只读命令（`list/show/get`）回答用户问题.
**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 安全规则

- 所有操作均为**只读**，本免费版不执行任何写操作或破坏性变更.
- 若用户请求变更（删除、启停、修改），提示该功能需升级至付费版.
- 禁止输出或记录任何密钥（access key、client secret、token、password）.
## 基础查询命令

| 资源类型 | 只读命令 |
|:-----|:-----|
| 资源组 | `az group list --query "[].{name:name,location:location}" -o table` |
| 虚拟机 | `az vm list --show-details --query "[].{name:name,rg:resourceGroup,state:powerState}" -o table` |
| 存储账户 | `az storage account list --query "[].{name:name,rg:resourceGroup}" -o table` |
| 虚拟网络 | `az network vnet list -o table` |
| 公网 IP | `az network public-ip list -o table` |
| 网络安全组 | `az network nsg list --query "[].{name:name,rg:resourceGroup}" -o table` |

**订阅切换**：`az account list -o table` 查看所有订阅，`az account set --subscription <id>` 切换目标订阅。查询结果涉及订阅范围时明确标注所用订阅名称.
## 简单健康检查

- **VM 电源状态**：`az vm list --show-details --query "[].{name:name,state:powerState}" -o table`
- **VM 实例视图**：`az vm get-instance-view --name <vm> -g <rg> --query "instanceView.statuses" -o table`
- **失败活动日志**：`az monitor activity-log list --status Failed --offset 1h -o table`
- **CPU 指标**：`az monitor metrics list --resource <resource-id> --metric "Percentage CPU" --interval PT1H -o table`

## 工作流程

1. **前置检查**：CLI 安装、登录状态、订阅上下文.
2. **只读执行**：执行 `list/show` 命令查询资源.
3. **结果呈现**：结构化输出结果，标注所用订阅.
4. **写操作拦截**：用户请求变更时，提示升级付费版.
## 案例展示

### 案例 1：盘点订阅内虚拟机运行状态

**用户请求**：帮我看看这个订阅里有哪些虚拟机，分别是什么状态.
**执行流程**：

```bash
# 1. 确认当前订阅
az account show --query "{name:name,id:id}" -o table
# ...
# 2. 列出所有虚拟机及电源状态（只读）
az vm list --show-details --query "[].{name:name,rg:resourceGroup,state:powerState,sku:hardwareProfile.vmSize}" -o table
```

**输出说明**：以表格列出虚拟机名称、资源组、电源状态、规格。用户可据此识别停止的实例。若用户希望启停或删除实例，提示该操作需升级付费版.
### 案例 2：查看最近失败的活动日志

**用户请求**：最近一小时有没有什么操作失败了？

**执行流程**：

```bash
az monitor activity-log list --status Failed --offset 1h --query "[].{time:eventTimestamp,resource:resourceId,op:operationName.value}" -o table
```

**输出说明**：列出最近 1 小时状态为 Failed 的活动事件，包含时间、资源 ID、操作名。用于初步定位异常操作.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| `az: command not found` | 本地未安装 Azure CLI | 提示用户安装 Azure CLI（`winget install Microsoft.AzureCLI`） |
| `Please run 'az login'` | 未登录或会话过期 | 引导用户执行 `az login --use-device-code` |
| `SubscriptionNotFound` | 订阅 ID 错误或无权访问 | `az account list` 确认可用订阅后用 `az account set` 切换 |
| `AuthorizationFailed` | 账号缺少 Reader 权限 | 建议联系订阅 Owner 分配 Reader 角色 |
| `ResourceNotFound` | 资源名称或资源组拼写错误 | 用 `az resource list` 模糊搜索确认正确名称 |
| `429 Too Many Requests` | ARM 请求触发限流 | 降低查询频率，添加 `--query` 过滤减少返回量 |
| 请求写操作被拦截 | 本免费版不支持写操作 | 提示用户升级至付费版 azure-infra 技能 |

## 常见问题

### Q1：如何切换到另一个订阅查询？
A：`az account list -o table` 查看所有订阅，`az account set --subscription <id>` 切换，然后执行查询命令.
### Q2：查询返回数据太多看不清怎么办？
A：使用 `--query` 参数过滤字段，例如 `--query "[].{name:name,rg:resourceGroup}"`，并用 `-o table` 输出表格格式.
### Q3：我能用这个免费版启停虚拟机或删除资源吗？
A：不能。本免费版仅支持只读查询。启停虚拟机、删除资源、修改配置等写操作需升级至付费版 azure-infra 技能，付费版提供完整的确认机制与 dry-run 支持.
### Q4：Key Vault 机密值能查出来吗？
A：本免费版不查询 Key Vault 机密值，也不展示任何密钥、令牌等敏感凭据，确保安全.
## 已知限制

- 仅支持只读查询，不支持任何写操作或破坏性变更.
- 不包含安全审计（NSG 暴露面、RBAC 检查、存储公开访问检查）.
- 不包含 Cost Management 成本分析.
- 不支持跨订阅批量查询，需手动切换订阅.
- 依赖本地 Azure CLI 与网络连接到 Azure ARM 端点.
## 升级提示

> 本免费版仅提供基础只读查询能力。如需完整功能（写操作确认、安全审计、成本分析、跨订阅查询、故障诊断、Key Vault 管理），请升级至付费版 **azure-infra** 技能.
## 触发条件

- 用户明确提到 Azure、az cli、Azure 资源查询等关键词且仅需只读查询时激活.
- 用户请求写操作、安全审计、成本分析时，提示需升级付费版.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 安全规则(补充)

### 基础查询命令(补充)

| 资源类型(续)| 只读命令 |
|:---------|---------:|
| 资源组 | `az group list --query "[].{name:name,location:location}" -o table` |
| 虚拟机 | `az vm list --show-details --query "[].{name:name,rg:resourceGroup,state:pow

**输入**: 用户提供基础查询命令相关的配置参数、输入数据和处理选项.
**处理**: 解析基础查询命令的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回基础查询命令的处理结果,包含执行状态码、结果数据和执行日志.
### 简单健康检查(补充)

- **VM 电源状态**：`az vm list --show-details --query "[].{name:name,state:powerState}" -o table`
- **VM 实例视图**：`az vm get-instance-view --name <vm> -g <rg> --query "instanceView.statuses" -o table`
- **失败

**输入**: 用户提供简单健康检查相关的配置参数、输入数据和处理选项.
**处理**: 解析简单健康检查的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回简单健康检查的处理结果,包含执行状态码、结果数据和执行日志.
### 工作流程(补充)

### 触发条件(补充)

**处理**: 解析触发条件的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回触发条件的处理结果,包含执行状态码、结果数据和执行日志.
#

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Azure Infra Free处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "azure-infra"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
