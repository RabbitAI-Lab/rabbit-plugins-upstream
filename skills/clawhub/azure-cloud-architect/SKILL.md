---
slug: "azure-cloud-architect"
name: "azure-cloud-architect"
version: 1.0.1
displayName: "Azure云架构师"
summary: "基于Azure CLI的多订阅导航、RBAC角色审计、成本分析、合规检查、跨订阅批量操作。"
license: "Proprietary"
description: |-
  基于 Azure CLI 的智能云基础设施管理助手。提供多订阅导航、RBAC 角色审计与最小权限、
  成本分析工作流、合规检查清单、跨订阅批量操作五大核心能力。适用于 Azure 资源盘点、健康监控、
  安全审计、Cost Management 分析、多订阅多租户管理场景.
  默认只读查询，写操作与破坏性操作需确认。分层权限模型 L0-L4 保障生产环境安全.
tags:
  - 智能代理
  - 云计算
  - Azure
  - 基础设施
  - 安全合规
  - 通用办公
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# Azure 云架构师

使用本地 Azure CLI 回答关于 Azure 资源的问题。默认只读查询，仅在用户明确要求变更并确认后执行写/破坏性操作.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Azure云架构师处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| Azure云架构师成本分析 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

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

### 1. 多订阅导航器
自动列出所有可访问订阅，智能检测默认订阅，支持按名称或 ID 切换，避免在错误订阅执行操作.
**输入**: 用户提供多订阅导航器所需的指令和必要参数.
**输出**: 返回多订阅导航器的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`多订阅导航器`的配置文档进行参数调优
### 2. 分层权限模型
L0 只读直接执行、L1 预演展示计划、L2 确认写、L3 破坏性详细影响分析、L4 敏感操作双重确认，保障生产环境安全.
**输入**: 用户提供分层权限模型所需的指令和必要参数.
**输出**: 返回分层权限模型的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`分层权限模型`的配置文档进行参数调优
### 3. 安全审计剧本
RBAC 角色审计（检测 Owner 过度授权）、存储安全检查（公共访问/HTTPS/TLS）、NSG 规则检查（0.0.0.0/0 入站）、Key Vault 访问审计.
**输入**: 用户提供安全审计剧本所需的指令和必要参数.
**输出**: 返回安全审计剧本的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`安全审计剧本`的配置文档进行参数调优
### 4. 成本分析工作流
按资源组/服务维度查询 Cost Management，识别空闲资源（停止的 VM/未挂载磁盘/未使用公网 IP）以优化成本.
**输入**: 用户提供成本分析工作流所需的指令和必要参数.
**处理**: 解析成本分析工作流的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回成本分析工作流的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`成本分析工作流`的配置文档进行参数调优
### 5. 跨订阅批量操作
提供跨订阅遍历模板，统一执行 VM 列举、NSG 检查等操作，避免遗漏订阅.
**输出**: 返回跨订阅批量的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`跨订阅批量操作`的配置文档进行参数调优
#
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|:---:|:---:|:---:|:---:|
| 资源盘点 | "列出当前订阅的虚拟机" | VM 名称、资源组、状态表格 | 多订阅导航 |
| 安全审计 | "审计谁有 Owner 角色" | RBAC 角色分配列表+建议 | 安全审计 |
| 成本分析 | "查询本月各资源组成本" | Cost Management 分组数据 | 成本分析 |
| 合规检查 | "检查 NSG 是否开放 0.0.0.0/0" | 入站规则风险报告 | 安全审计 |
| 多订阅管理 | "遍历所有订阅列出 VM" | 跨订阅 VM 汇总表 | 跨订阅批量 |

**不适用于**: Azure Portal GUI 操作指导（本 skill 基于 CLI），非 Azure 云平台（AWS/GCP/阿里云），需要 Azure SDK 编程开发场景.
## 使用流程

### Step 1: 确认登录身份
```bash
az account show
```
如未登录，运行 `az login --use-device-code`（SSH 环境适用），终端会显示码和 URL，在浏览器中完成登录.
### Step 2: 选择订阅（多订阅时）
```bash
# 列出所有可访问的订阅
az account list --output table
# ...
# 设置活跃订阅（按名称或ID）
az account set --subscription "Production"
```
**订阅选择规则**: 用户明确指定 → 使用指定；未指定但有默认 → 使用默认；无默认且多个 → 询问用户；仅一个 → 直接使用.
### Step 3: 执行只读查询
根据需求执行 `list`/`show`/`get` 类命令，结果以表格形式展示便于阅读.
### Step 4: 写操作预演（如需变更）
- 优先使用 `--dry-run` 或 `--what-if` 预演
- 展示影响范围与计划
- 等待用户显式确认

### Step 5: 执行变更并验证
确认后执行写/破坏性操作，执行后用只读命令验证结果.
#
## 案例展示

### 案例1: 虚拟机清单与健康状态检查
**场景**: 运维人员需要快速检查当前订阅里有哪些虚拟机及运行状态

```bash
az vm list --query '[].{Name:name,ResourceGroup:resourceGroup,State:powerState}' -d --output table
```

**预期输出**:
```
Name           ResourceGroup    State
-------------  ---------------  --------
prod-web-01    prod-rg          VM running
prod-web-02    prod-rg          VM running
dev-test-01    dev-rg           VM stopped
```

**分析**: `dev-test-01` 处于 `VM stopped` 状态，如非计划停机可能造成资源浪费。`-d` 参数用于显示实例视图状态，便于确认电源状态.
### 案例2: RBAC 角色审计（最小权限检查）
**场景**: 安全团队需要审计当前订阅里谁有 Owner 角色，检查是否有过度授权

```bash
az role assignment list --role "Owner" \
  --query '[].{Assignee:principalName,Scope:scope}' --output table
```

**预期输出**:
```
Assignee               Scope
---------------------  ------------------------------------
admin@company.com      /subscriptions/xxx-xxx-xxx
deploy-spn@company.com /subscriptions/xxx-xxx-xxx/resourceGroups/prod-rg
```

**审计结论**: 发现 2 个 Owner 分配。`deploy-spn@company.com` 为部署服务主体，其作用域限定在 `prod-rg`，但 Owner 权限过高。建议降级为 Contributor，遵循最小权限原则。生产订阅的 Owner 角色应仅授予少数管理员.
### 案例3: 跨订阅成本分析（按资源组分组）
**场景**: 财务团队需要了解本月各资源组的成本分布以优化支出

```bash
az costmanagement query --type ActualCost \
  --timeframe MonthToDate \
  --dataset-grouping name=ResourceGroupName type=Dimension \
  --dataset-aggregation totalCost=name=Cost function=Sum
```

**预期输出**:
```
ResourceGroupName    Cost    Currency
-------------------  ------  --------
prod-rg              4523.67 USD
dev-rg               892.15  USD
shared-rg            2156.43 USD
```

**分析**: `prod-rg` 成本占比最高，建议进一步检查是否有空闲资源。可结合 `az vm list -d` 查找 `VM stopped` 的实例、`az disk list --query '[?diskState==`Attached`]'` 查找未挂载磁盘，识别可释放的空闲资源以降低成本.
## 异常处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------|------:|:------|:------|
| 未登录 | `Please run az login` | 会话过期或未登录 | 运行 `az login --use-device-code` 重新登录 |
| 订阅未找到 | `Subscription not found` | 订阅 ID 错误或无权限 | 用 `az account list` 确认可访问的订阅列表 |
| 权限不足 | `Access denied` / 403 | RBAC 角色权限不足 | 检查 `az account show` 确认身份，只读至少需 Reader 角色 |
| 未选择订阅 | `No subscription selected` | 未设置活跃订阅 | 运行 `az account set --subscription <名称或ID>` |
| 命令未找到 | `command not found` | Azure CLI 版本过旧 | 运行 `az version`，升级到最新版 `az upgrade` |
| 操作超时 | `Operation timeout` | 网络或服务问题 | ，确认 Azure 服务状态 |
| 密钥泄露风险 | 输出含密钥/令牌 | 命令输出意外包含敏感信息 | 立即停止，绝不在聊天/日志中输出密钥值，必要时轮换密钥 |
| 多订阅遗漏 | 部分订阅未检查 | 未遍历所有订阅 | 使用跨订阅批量操作模板遍历所有订阅 |
| 成本查询为空 | Cost Management 返回空 | 未配置或订阅类型不支持 | 确认 CSP 等订阅类型是否支持 Cost Management |

## 安全审计剧本

### RBAC 角色审计
```bash
# 检查 Owner 角色分配（高风险）
az role assignment list --role "Owner" --query '[].{Assignee:principalName,Scope:scope}' --output table
# ...
# 检查 Contributor 角色分配（中风险，作用域过大时需关注）
az role assignment list --role "Contributor" --query '[].{Assignee:principalName,Scope:scope}' --output table
```
建议将非管理员的 Owner 角色降级为 Contributor，部署服务主体限定作用域。Owner 角色应仅授予少数管理员，生产订阅控制在 2-3 人以内.
### NSG 规则检查
```bash
# 列出所有 NSG
az network nsg list --query '[].{Name:name,ResourceGroup:resourceGroup}' --output table
# ...
# 检查特定 NSG 的入站规则
az network nsg rule list --nsg-name NSG_NAME --resource-group RG_NAME \
  --query "[?sourceAddressPrefix=='*' && direction=='Inbound'].{Name:name,Port:destinationPortRange,Priority:priority}" --output table
```
重点排查 22（SSH）、3389（RDP）、3306（MySQL）、1433（SQL Server）等敏感端口对公网开放的情况。建议使用 Just-In-Time 访问或堡垒机替代直接开放管理端口.
### 存储安全检查
```bash
# 检查存储账户公共访问设置
az storage account list --query '[].{Name:name,AllowBlobPublicAccess:allowBlobPublicAccess,HttpsOnly:enableHttpsTrafficOnly}' --output table
```
`AllowBlobPublicAccess` 为 true 的存储账户存在数据泄露风险，建议关闭公共访问。`HttpsOnly` 为 false 的账户应立即启用 HTTPS 强制传输.
### Key Vault 访问审计
```bash
# 检查 Key Vault 访问策略
az keyvault list --query '[].{Name:name,ResourceGroup:resourceGroup}' --output table
```
审计 Key Vault 的访问策略，确认是否使用 RBAC 权限模型替代传统访问策略，限制机密读取范围.
## 成本优化策略

- 使用 `az vm list -d` 识别 `VM stopped` 状态的实例，评估是否可释放
- 查找未挂载磁盘：`az disk list --query '[?diskState==`Unattached`]'`
- 查找未使用公网 IP：`az network public-ip list --query '[?ipConfiguration==null]'`
- 设置预算告警：在 Azure Portal 配置 Cost Management 预算阈值
- 考虑预留实例或 Savings Plans 降低长期 VM 成本

## 常见问题

### Q1: 如何切换订阅？
A: 使用 `az account set --subscription "订阅名"` 或 `az account set --subscription "订阅ID"`。结果为订阅范围时明确说明使用的订阅，避免在错误订阅执行操作.
### Q2: 设备码登录怎么用？
A: 运行 `az login --use-device-code`，终端会显示一个码和 URL。在浏览器中打开 URL，输入码完成登录。适合无法打开浏览器的 SSH 环境.
### Q3: 命令执行失败提示权限不足？
A: 检查当前身份 `az account show`，确认关联的 RBAC 角色是否包含所需权限。只读操作至少需要 Reader 角色，写操作需要 Contributor，角色管理需要 User Access Administrator.
### Q4: 如何安全地执行破坏性操作？
A: 1) 先用 `--what-if` 或 `--dry-run` 预演；2) 列出精确影响范围；3) 等待用户显式确认；4) 执行后验证结果。绝不在未确认时执行破坏性操作，L3/L4 级操作需双重确认.
### Q5: 多租户如何管理？
A: 使用 `az login --tenant <tenant-id>` 登录特定租户。使用 `az account list --query '[].tenantId'` 查看可访问的租户。跨租户操作时需重新登录目标租户.
### Q6: Cost Management 返回空结果怎么办？
A: 确认订阅类型。CSP（云解决方案提供商）等部分订阅类型可能不支持 Cost Management API，返回空结果。检查是否已在 Azure Portal 启用 Cost Management 数据，数据通常有 8-12 小时延迟.
### Q7: 如何识别空闲资源以降低成本？
A: 结合多条命令识别：用 `az vm list -d` 查找 `VM stopped` 实例，用 `az disk list --query '[?diskState==`Unattached`]'` 查找未挂载磁盘，用 `az network public-ip list --query '[?ipConfiguration==null]'` 查找未关联的公网 IP。释放这些空闲资源可显著降低月度成本.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

1. **仅支持 Azure CLI 命令**: 不提供 Azure Portal GUI 操作指导，不覆盖 Azure SDK 编程开发场景
2. **依赖本地 Azure CLI 环境**: 需提前安装并配置 Azure CLI，未安装时无法使用
3. **成本查询依赖订阅类型**: CSP 等部分订阅类型可能不支持 Cost Management，返回空结果
4. **跨订阅操作性能受限**: 遍历多订阅时为串行执行，订阅数量多时耗时较长
5. **不修改 Azure 资源默认行为**: 所有写操作需用户显式确认，自动化流水线场景需额外集成确认机制
6. **Cost Management 数据延迟**: 成本数据通常有 8-12 小时延迟，当天数据可能不可用
7. **CloudShell 限制**: 在 Azure CloudShell 中部分交互式命令行为与本地 CLI 不同，建议使用本地环境
