---
slug: "azure-infra"
name: "azure-infra"
version: 1.0.1
displayName: "Azure Infra"
summary: "通过本地 Azure CLI 查询与管理 Azure 资源，默认只读，写操作需确认。"
license: "Proprietary"
description: |-
  Azure Infra 技能通过本地 Azure CLI（az 命令）帮助用户查询、诊断和管理 Azure 云资源.
  默认所有操作为只读查询，任何写操作或破坏性变更（删除、缩放、修改 IAM、计费配置等）
  必须先展示完整命令与影响范围，经用户显式确认后方可执行.
  核心能力：
  - 资源清单查询：虚拟机、存储账户、虚拟网络、资源组、AKS、App Service 等资源的列举与详情
  - 健康与诊断：Azure Monitor 指标、活动日志、启动诊断、资源健康状态
  - 安全审计：RBAC 角色分配、NSG 暴露面、存储账户公开访问、Key Vault 访问策略
  - 成本分析：Cost Management 只读查询，按订阅/资源组/服务维度统计
  - 变更操作：在用户确认后执行启停虚拟机、修改配置、删除资源等写操作

  适用场景：
  - 云资源盘点与成本优化（找出停止的虚拟机、未使用的公网 IP、空存储账户）
  - 安全合规检查（排查 NSG 暴露的 RDP/SSH 端口、公开的 Blob 容器、过宽的 RBAC 权限）
  - 故障排查（通过活动日志与启动诊断定位虚拟机无法启动的原因）
  - 多订阅环境下的资源统一查询

  差异化：严格遵循只读优先原则，内置确认机制与 dry-run 偏好，避免误操作；
  支持多订阅/多租户上下文切换；禁止输出任何密钥、令牌等敏感凭据.
tags:
  - 通用办公
  - Cloud
  - Azure
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Azure Infra

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Azure Infra处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| Azure Infra查询与管理 | 不支持 | 支持 |
| 多租户管理与权限分配 | 不支持 | 支持 |
| 操作审计与合规日志 | 不支持 | 支持 |
| 自定义仪表盘与报表 | 不支持 | 支持 |
| API开放与第三方集成 | 不支持 | 支持 |

## 概述

通过本地 Azure CLI（`az` 命令）查询与管理 Azure 资源。默认所有操作为只读查询；仅当用户明确请求变更并确认后，才执行写操作或破坏性操作.
## 快速开始

1. 检查 CLI 是否安装：`az --version`。若未安装，提示用户安装 Azure CLI.
2. 检查登录状态：`az account show`。若未登录，引导用户执行 `az login --use-device-code`.
3. 确认订阅上下文：若存在多个订阅，询问用户选择目标订阅；否则使用默认订阅.
4. 使用只读命令回答用户问题.
5. 若用户请求变更，列出完整命令与影响范围，等待用户确认后执行.
#
## 安全规则（必须遵守）

- 默认所有操作为**只读**，除非用户明确请求变更**并**确认.
- 任何潜在破坏性变更（delete / terminate / destroy / modify / scale / billing / IAM 凭据）必须经过确认步骤.
- 优先使用 `--dry-run` 或 `what-if` 参数，先展示执行计划再运行.
- 禁止输出或记录任何密钥（access key、client secret、token、password）。查询 Key Vault 机密时只展示机密名称与元数据，不展示值.
- 写操作执行前，向用户展示完整命令、目标资源 ID、预期影响.
## 订阅与租户处理

- 用户指定订阅/租户时，使用 `az account set --subscription <id>` 切换并说明.
- 未指定时，使用 `az account show` 返回的默认订阅.
- 查询结果涉及订阅范围时，明确标注所用订阅名称与 ID.
- 跨订阅查询时，先 `az account list --query "[].{name:name,id:id}" -o table` 列出可用订阅，逐个查询或使用 `--query` 过滤.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
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

### 资源清单查询
| 资源类型 | 只读命令示例 |
|:---:|:---:|
| 资源组 | `az group list --query "[].{name:name,location:location}" -o table` |
| 虚拟机 | `az vm list --show-details --query "[].{name:name,rg:resourceGroup,powerState:powerState}" -o table` |
| 存储账户 | `az storage account list --query "[].{name:name,rg:resourceGroup,sku:sku.name}" -o table` |
| 虚拟网络 | `az network vnet list --query "[].{name:name,rg:resourceGroup,location:location}" -o table` |
| 网络安全组 | `az network nsg list -o table` |
| 公网 IP | `az network public-ip list --query "[].{name:name,ip:ipAddress,rg:resourceGroup}" -o table` |
| AKS 集群 | `az aks list --query "[].{name:name,rg:resourceGroup,state:provisioningState}" -o table` |
| App Service | `az webapp list --query "[].{name:name,rg:resourceGroup,state:state}" -o table` |
| Key Vault | `az keyvault list --query "[].{name:name,rg:resourceGroup}" -o table` |

**输入**: 用户提供资源清单查询所需的指令和必要参数.
**处理**: 解析资源清单查询的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回资源清单查询的处理结果,包含执行状态码、结果数据和执行日志。### 健康与诊断
- **活动日志**：`az monitor activity-log list --resource-group <rg> --status Failed -o table`
- **指标查询**：`az monitor metrics list --resource <resource-id> --metric "Percentage CPU" --interval PT1H -o table`
- **资源健康**：`az resource health --resource <resource-id>`
- **VM 启动诊断**：`az vm boot-diagnostics get-boot-log --name <vm> --resource-group <rg>`

**输入**: 用户提供健康与诊断所需的指令和必要参数.
**处理**: 解析健康与诊断的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回健康与诊断的处理结果,包含执行状态码、结果数据和执行日志。### 安全审计
- **RBAC 角色**：`az role assignment list --resource-group <rg> --query "[].{user:principalName,role:roleDefinitionName}" -o table`
- **NSG 规则**：`az network nsg rule list --nsg-name <nsg> -g <rg> --query "[].{name:name,access:access,destPort:destinationPortRange}" -o table`
- **存储公开访问**：`az storage container list --account-name <acct> --query "[].{name:name,perm:publicAccess}" -o table`
- **Key Vault 策略**：`az keyvault show --name <vault> --query "properties.accessPolicies"`

**处理**: 解析安全审计的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回安全审计的处理结果,包含执行状态码、结果数据和执行日志。### 成本分析
- **按订阅查询**：`az costmanagement query --type ActualCost --timeframe MonthToDate --scope "subscriptions/<sub-id>"`
- **按资源组**：追加 `--query "items[*].properties"` 过滤分组维度

**输入**: 用户提供成本分析所需的指令和必要参数.
**输出**: 返回成本分析的解析响应,包含完成状态码、响应数据和完成日志。### 变更任务（需确认）
| 操作 | 命令 | 确认要求 |
|:------|------:|:------|
| 启动 VM | `az vm start --name <vm> -g <rg>` | 列出 VM 名称与资源组 |
| 停止 VM | `az vm deallocate --name <vm> -g <rg>` | 提示停止后将释放计费资源 |
| 删除资源组 | `az group delete --name <rg>` | 高风险，列出组内资源数量后等待确认 |
| 修改 NSG 规则 | `az network nsg rule update ...` | 展示变更前后差异 |

**输入**: 用户提供变更操作（需确认）所需的指令和必要参数.
**解析**: 解析变更任务（需确认）的输入参数,完成核心解析逻辑,返回结构化响应和完成状态.
**输出**: 返回变更任务（需确认）的解析响应,包含完成状态码、响应数据和完成日志.
### 资源类型

针对资源类型,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供资源类型相关的配置参数、输入数据和处理选项.
**输出**: 返回资源类型的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`资源类型`的配置文档进行参数调优
### 资源组

针对资源组,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供资源组相关的配置参数、输入数据和处理选项.
**输出**: 返回资源组的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`资源组`的配置文档进行参数调优
#
## 工作流程

1. **意图识别**：判断用户请求是查询（只读）还是变更（写操作）.
2. **前置检查**：CLI 安装、登录状态、订阅上下文.
3. **只读执行**：查询类请求直接执行 `list/show/get` 命令.
4. **写操作确认**：变更类请求展示完整命令 + 目标资源 + 影响 → 等待用户确认 → 执行.
5. **结果呈现**：结构化输出结果，标注所用订阅，隐藏敏感字段.
## 案例展示

### 案例 1：盘点虚拟机并识别可回收的停止实例

**用户请求**：帮我看一下这个订阅里有哪些虚拟机是停止状态，可以省钱.
**执行流程**：

```bash
# 1. 确认当前订阅
az account show --query "{name:name,id:id}" -o table
# ...
# 2. 列出所有虚拟机及其电源状态（只读）
az vm list --show-details --query "[].{name:name,rg:resourceGroup,state:powerState,sku:hardwareProfile.vmSize}" -o table
# ...
# 3. 过滤出已停止/已释放的实例
az vm list --show-details --query "[?powerState=='VM deallocated'].{name:name,rg:resourceGroup,sku:hardwareProfile.vmSize}" -o table
```

**输出说明**：列出所有 `VM deallocated` 状态的实例，标注资源组与规格。若用户决定释放或删除，展示 `az vm deallocate` / `az vm delete` 命令并等待确认.
### 案例 2：安全审计 NSG 暴露面与公开存储

**用户请求**：检查我的网络有没有把 RDP 或 SSH 端口暴露给公网，再看下存储账户有没有公开的容器.
**执行流程**：

```bash
# 1. 列出所有 NSG 规则中允许公网访问 3389/22 的条目
az network nsg list --query "[].{name:name,rg:resourceGroup}" -o table
az network nsg rule list --nsg-name <nsg> -g <rg> --query "[?destinationPortRange=='3389' || destinationPortRange=='22' || destinationPortRange=='*'].{name:name,access:access,source:sourceAddressPrefix,port:destinationPortRange}" -o table
# ...
# 2. 检查存储账户容器的公开访问配置
az storage account list --query "[].name" -o tsv
az storage container list --account-name <acct> --query "[?publicAccess!='None'].{name:name,perm:publicAccess}" -o table
```

**输出说明**：汇总暴露 RDP/SSH 给 `0.0.0.0/0` 的 NSG 规则、公开访问非 None 的存储容器。给出修复建议（如收窄源地址范围、关闭容器公开访问），若用户确认修改再执行 `az network nsg rule update`.
### 案例 3：排查虚拟机无法启动故障

**用户请求**：prod-vm-01 重启后一直起不来，帮我查下原因.
**执行流程**：

```bash
# 1. 查看 VM 实例视图状态
az vm get-instance-view --name prod-vm-01 -g prod-rg --query "instanceView.statuses" -o table
# ...
# 2. 获取启动诊断日志
az vm boot-diagnostics get-boot-log --name prod-vm-01 -g prod-rg
# ...
# 3. 查询最近 1 小时的失败活动日志
az monitor activity-log list --resource prod-vm-01 --resource-group prod-rg --status Failed --offset 1h -o table
```

**输出说明**：结合实例视图状态码、启动日志内容（如磁盘满、内核 panic、OSProfile 错误）、活动日志中的失败事件，定位根因并给出修复方向.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| `az: command not found` | 本地未安装 Azure CLI | 提示用户安装 Azure CLI（`winget install Microsoft.AzureCLI` 或参考官方安装文档） |
| `Please run 'az login'` | 未登录或会话过期 | 引导用户执行 `az login --use-device-code` 完成登录 |
| `SubscriptionNotFound` | 订阅 ID 错误或当前账号无权访问 | 先 `az account list` 确认可用订阅，再 `az account set` 切换 |
| `AuthorizationFailed` | 当前服务主体/账号缺少 RBAC 权限 | 列出所需角色（如 Reader），建议联系订阅 Owner 分配权限 |
| `ResourceNotFound` | 资源名称或资源组拼写错误 | 用 `az resource list` 模糊搜索确认资源存在性与正确名称 |
| `429 Too Many Requests` | ARM 请求触发限流 | 降低查询频率，添加 `--query` 过滤减少返回量，分批查询 |
| `Cloud shell write operation blocked` | 用户未确认写操作 | 重新展示命令与影响范围，等待显式确认（`y`）后再执行 |
| `InvalidResourceID` | 资源 ID 格式错误 | 校验 ID 是否符合 `/subscriptions/<sub>/resourceGroups/<rg>/providers/...` 格式 |
| `LocationNotAvailableForResourceType` | 所选区域不支持该资源类型 | `az provider list --query "[?namespace=='Microsoft.Compute'].resourceTypes"` 查询可用区域 |
| `az cli 版本过旧` | 某些命令或参数在新版本才支持 | 提示 `az upgrade` 升级 Azure CLI 后 |
| 网络不可达 ARM 端点 | 本地网络限制或代理拦截 | 检查 `HTTPS_PROXY` 环境变量与 `management.azure.com` 连通性 |

## 常见问题

### Q1：如何在多个订阅之间切换查询？
A：先用 `az account list --query "[].{name:name,id:id,isDefault:isDefault}" -o table` 查看所有订阅，再用 `az account set --subscription <id>` 切换。每次切换后说明当前订阅。跨订阅统计时可逐个切换查询后汇总.
### Q2：查询资源时如何避免返回过多数据？
A：使用 `--query` 参数配合 JMESPath 语法过滤字段，例如 `--query "[].{name:name,rg:resourceGroup}"`。也可用 `-o table` 替代 JSON 输出提升可读性。按资源组或区域加 `--resource-group` / `--location` 参数缩小范围.
### Q3：删除资源组前能预览会删除哪些资源吗？
A：`az group delete` 不支持 dry-run，但可先 `az resource list --resource-group <rg> -o table` 列出组内全部资源，统计数量后向用户展示，等待确认再执行删除.
### Q4：如何查看某个用户在订阅里有哪些权限？
A：`az role assignment list --assignee <user-email> --all --query "[].{role:roleDefinitionName,scope:scope}" -o table`，列出该用户所有角色分配及作用范围.
### Q5：Key Vault 里的机密值能直接查出来吗？
A：不展示机密值。只查询机密元数据：`az keyvault secret list --vault <vault> --query "[].{name:name,updated:attributes.updated}" -o table`。如需查看值，提示用户这属于敏感操作，由用户自行在 Azure Portal 或通过 `az keyvault secret show` 谨慎操作.
### Q6：Cost Management 查询报权限不足怎么办？
A：Cost Management 需要 `Cost Management Reader` 或更高角色。若权限不足，改用 `az consumption usage list`（需 `Billing Reader`）查询用量，或建议用户在 Portal 的 Cost Management 页面查看.
### Q7：写操作确认后如何确保不会误删？
A：执行前展示完整命令、目标资源 ID、影响范围；对删除类操作额外要求用户输入资源组名或资源名确认；优先使用 `--dry-run` 或 `what-if`（如 ARM 模板部署）预览变更.
## 已知限制

- 依赖本地 Azure CLI 与网络连接到 Azure ARM 端点，离线不可用.
- 大规模查询（如列出上万资源）可能触发 ARM 限流，需分页或分批.
- 跨租户查询需要用户预先配置并登录对应租户.
- Azure CLI 版本差异可能导致部分命令或参数不可用.
- 中国区 Azure（Azure China 21Vianet）需先 `az cloud set --name AzureChinaCloud` 切换云环境.
## 触发条件

- 用户明确提到 Azure、az cli、Azure 资源查询、虚拟机/存储/网络/RBAC/成本等关键词时激活.
- 用户请求涉及其他云平台（AWS、GCP、阿里云）时不触发.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Azure Infra处理结果",
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
