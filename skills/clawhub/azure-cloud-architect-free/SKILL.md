---
slug: "azure-cloud-architect-free"
name: "azure-cloud-architect-free"
version: "1.0.0"
displayName: "Azure云架构师LITE"
summary: "基于Azure CLI的多订阅导航与资源清单查询,提供只读查询与VM健康检查。"
license: "MIT"
description: |-
  基于 Azure CLI 的基础云资源查询工具（免费版）。提供多订阅导航与资源清单查询两大基础能力.
  支持虚拟机列表、运行状态检查、订阅切换等只读操作。默认只读模式，不执行任何变更操作.
  适用于日常资源盘点和健康巡检场景。如需 RBAC 角色审计、成本分析、合规检查、跨订阅批量操作等
  高级功能，请升级至 azure-cloud-architect 付费版.
tags:
  - 云计算
  - Azure
  - 基础设施
  - 通用办公
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# Azure 云架构师 LITE

使用本地 Azure CLI 回答关于 Azure 资源的基础问题。默认只读查询，不执行任何变更操作.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Azure云架构师LITE处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
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
### 2. 资源清单查询
查询虚拟机列表、运行状态、资源组等只读信息，结果以表格形式展示便于阅读.
> **升级提示**: RBAC 角色审计（Owner 过度授权检测）、成本分析工作流（Cost Management）、合规检查（NSG/存储安全）、跨订阅批量操作、分层权限模型（L0-L4）等高级功能仅在 [azure-cloud-architect 付费版] 中提供。- 验证返回数据的完整性和格式正确性
- 参考`资源清单查询`的配置文档进行参数调优
#
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|---:|---:|---:|---:|
| 资源盘点 | "列出当前订阅的虚拟机" | VM 名称、资源组、状态表格 | 资源清单查询 |
| 订阅切换 | "切换到生产订阅" | 活跃订阅变更确认 | 多订阅导航 |
| 健康巡检 | "查看虚拟机运行状态" | VM 电源状态表格 | 资源清单查询 |

**不适用于**: 需要 RBAC 角色审计的场景（需付费版），需要成本分析的场景（需付费版），需要合规检查的场景（需付费版），Azure Portal GUI 操作指导，非 Azure 云平台.
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
根据需求执行 `list`/`show` 类命令，结果以表格形式展示便于阅读.
### Step 4: 格式化输出
```bash
# 表格格式（适合人类阅读）
--output table
# ...
# JSON 格式（适合程序处理）
--output json
```

### Step 5: 验证查询范围
执行查询后确认结果来源的订阅范围。多订阅环境下，明确说明当前使用的订阅名称或 ID，避免在错误订阅上下文中误读数据。如需跨订阅统一查询，请升级至付费版使用跨订阅批量操作模板.
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

**分析**: `dev-test-01` 处于 `VM stopped` 状态，如非计划停机可能造成资源浪费。`-d` 参数用于显示实例视图状态（instance view），便于确认电源状态。不加 `-d` 时 `powerState` 字段为空，无法判断 VM 是否运行.
如需进一步审计 RBAC 权限或分析成本，请升级至付费版。付费版可检测 Owner 过度授权、按资源组分组查询 Cost Management、识别空闲磁盘和未使用公网 IP 等资源.
### 案例2: 订阅列表与切换
**场景**: 开发者需要确认可访问的订阅并切换到目标订阅

```bash
# 列出所有可访问的订阅
az account list --output table
```

**预期输出**:
```
Name              CloudName    State    IsDefault
----------------  -----------  -------  -----------
Production        AzureCloud   Enabled  True
Development       AzureCloud   Enabled  False
Staging           AzureCloud   Enabled  False
```

**切换订阅**:
```bash
az account set --subscription "Development"
```

**分析**: `IsDefault` 为 True 的订阅是当前活跃订阅。切换后所有后续命令将在新订阅上下文中执行，需注意确认订阅范围避免误操作。切换后可运行 `az account show` 验证当前订阅是否已更新.
## 异常处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:---:|:---:|:---:|:---:|
| 未登录 | `Please run az login` | 会话过期或未登录 | 运行 `az login --use-device-code` 重新登录 |
| 订阅未找到 | `Subscription not found` | 订阅 ID 错误或无权限 | 用 `az account list` 确认可访问的订阅列表 |
| 权限不足 | `Access denied` / 403 | RBAC 角色权限不足 | 检查 `az account show` 确认身份，只读至少需 Reader 角色 |
| 未选择订阅 | `No subscription selected` | 未设置活跃订阅 | 运行 `az account set --subscription <名称或ID>` |
| 命令未找到 | `command not found` | Azure CLI 版本过旧 | 运行 `az version`，升级到最新版 `az upgrade` |

## 常见问题

### Q1: 如何切换订阅？
A: 使用 `az account set --subscription "订阅名"` 或 `az account set --subscription "订阅ID"`。结果为订阅范围时明确说明使用的订阅，避免在错误订阅执行操作.
切换后建议运行 `az account show` 验证当前活跃订阅。多租户环境下，如需访问其他租户的订阅，需先运行 `az login --tenant <tenant-id>` 登录目标租户.
### Q2: 设备码登录怎么用？
A: 运行 `az login --use-device-code`，终端会显示一个码和 URL。在浏览器中打开 URL，输入码完成登录。适合无法打开浏览器的 SSH 环境.
设备码有效期为 15 分钟，如过期需重新运行命令获取新码。登录成功后会话通常保持 90 天，过期后需重新登录.
如本地环境支持浏览器，直接运行 `az login` 会自动打开浏览器完成 OAuth 认证，体验更佳.
### Q3: 命令执行失败提示权限不足？
A: 检查当前身份 `az account show`，确认关联的 RBAC 角色是否包含所需权限。只读操作至少需要 Reader 角色，写操作需要 Contributor。如需查询具体角色分配，请升级至付费版使用 RBAC 角色审计功能.
如提示 `az login` 则表示会话已过期，运行 `az login --use-device-code` 重新登录。SSH 环境下推荐使用设备码登录方式.
### Q4: 免费版和付费版有什么区别？
A: 免费版（LITE）包含多订阅导航和资源清单查询两大基础功能。付费版（Azure 云架构师）额外提供：
- RBAC 角色审计（检测 Owner 过度授权，最小权限建议）
- 成本分析工作流（Cost Management 按资源组/服务分组，空闲资源识别）
- 合规检查（NSG 0.0.0.0/0 检查、存储公共访问、Key Vault 审计）
- 跨订阅批量操作（遍历所有订阅统一执行）
- 分层权限模型 L0-L4（L0 只读到 L4 敏感操作双重确认）
- 安全审计剧本（RBAC、NSG、存储、Key Vault 四类审计命令）
- 更多案例展示（3 个完整案例 vs 2 个基础案例）
- 更详细的异常处理（9 种 Azure 特定错误 vs 5 种基础错误）

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **功能限制**: 仅支持多订阅导航和资源清单查询，不支持 RBAC 审计、成本分析、合规检查、跨订阅批量操作（需升级付费版）
- **仅支持 Azure CLI 命令**: 不提供 Azure Portal GUI 操作指导，不覆盖 Azure SDK 编程开发场景
- **依赖本地 Azure CLI 环境**: 需提前安装并配置 Azure CLI，未安装时无法使用
- **只读模式**: 不执行任何创建/修改/删除操作，变更操作需升级付费版并使用分层权限模型确认
- **不支持跨订阅批量查询**: 遍历多订阅需逐个手动切换，无法自动汇总结果（付费版提供跨订阅批量操作模板）
- **不含安全审计**: 无法检测 Owner 过度授权、NSG 开放端口、存储公共访问等安全风险（需付费版安全审计剧本）
- **不含成本分析**: 无法查询 Cost Management 数据，无法识别空闲资源以优化成本（需付费版成本分析工作流）
- **不含分层权限模型**: 不提供 L0-L4 分层确认机制，所有操作均为只读（需付费版）
- **不含安全审计剧本**: 不提供 NSG 规则检查、存储公共访问检查、Key Vault 访问审计等命令模板（需付费版）
