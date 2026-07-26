---
slug: "azure-cli-toolkit"
name: "azure-cli-toolkit"
version: 1.0.1
displayName: "Azure命令行工具专业版"
summary: "企业级Azure云管理,支持批量操作、自动化脚本、多订阅管理与成本优化分析"
license: "Proprietary"
edition: "pro"
description: |-
  面向企业团队的高级 Azure 云平台管理工具,在免费版基础上扩展自动化、批量操作与成本治理能力。核心能力:
  - 服务主体与托管身份认证(自动化场景)
  - 批量资源操作与脚本化部署
  - 多订阅跨租户统一管理
  - 成本分析与资源优化建议
  - 策略合规审计与安全基线检查

  适用场景:
  - 企业级基础设施自动化部署
  - 多环境(开发/测试/生产)统一管理
  - 云成本治理与资源清理

  差异化:
  - 兼容免费版全部命令,无缝升级
  - 支持自动化脚本与 CI/CD 集成
  - 提供成本优化与合规审计能力
  -...
tags:
  - 云平台
  - Azure
  - 命令行工具
  - 自动化
  - 企业级
  - 成本治理
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# Azure命令行工具专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Azure命令行工具专业版业级Azure云管理 | 不支持 | 支持 |
| Azure命令行工具专业版多订阅管理 | 不支持 | 支持 |
| Azure命令行工具专业版与成本优化分析 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |

## 核心能力

### 1. 自动化认证方式
| 认证方式 | 适用场景 | 命令 |
|:-----|:-----|:-----|
| 服务主体 | CI/CD、自动化脚本 | `az login --service-principal` |
| 托管身份 | Azure 资源内部调用 | `az login --identity` |
| 令牌认证 | 无状态流水线 | `az login --service-principal --password-stdin` |

```bash
# 服务主体认证(自动化场景)
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID
# ...
# 托管身份认证(虚拟机内部)
az login --identity
# ...
# 令牌认证(CI/CD)
echo "$AZURE_ACCESS_TOKEN" | az login --service-principal \
  -u $AZURE_CLIENT_ID --password-stdin --tenant $AZURE_TENANT_ID
```

**输出**: 返回自动化认证方式的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 批量资源操作
```bash
# 批量删除资源组下所有虚拟机
az vm list -g myRG -d --query "[].id" -o tsv | xargs az vm delete --ids --yes
# ...
# 批量停止所有运行中的虚拟机
az vm list -d --query "[?powerState=='VM running'].id" -o tsv | xargs az vm stop --ids
# ...
# 按标签批量筛选资源
az resource list --tag env=production --query "[].id" -o tsv
```

**输入**: 用户提供批量资源操作所需的指令和必要参数.
**输出**: 返回批量资源的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `批量资源操作` 选项

### 3. 自动化部署脚本
```bash
#!/bin/bash
set -e  # 出错即退出
# ...
# 创建资源组
az group create -g prod-rg -l eastus
# ...
# 创建虚拟机并获取 ID
VM_ID=$(az vm create \
  -g prod-rg \
  -n prod-vm \
  --image UbuntuLTS \
  --query id \
  --output tsv)
# ...
echo "Created VM: $VM_ID"
# ...
# 验证状态
az vm show --ids "$VM_ID" --query provisioningState
# ...
# 配置网络安全组
az network nsg create -g prod-rg -n prod-nsg
az network nsg rule create -g prod-rg --nsg-name prod-nsg \
  -n allow-ssh --priority 1000 \
  --source-address-prefixes '*' \
  --destination-port-ranges 22 \
  --access Allow --protocol Tcp
```

**输入**: 用户提供自动化部署脚本所需的指令和必要参数.
**处理**: 解析自动化部署脚本的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `自动化部署脚本` 选项

### 4. 多订阅管理
```bash
# 列出所有订阅
az account list --query "[].{name:name, id:id, state:state}" -o table
# ...
# 跨订阅操作
for sub in $(az account list --query "[].id" -o tsv); do
  az account set --subscription $sub
  echo "=== 订阅: $(az account show --query name -o tsv) ==="
  az vm list -o table
done
```

**输入**: 用户提供多订阅管理所需的指令和必要参数.
**处理**: 解析多订阅管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回多订阅管理的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `多订阅管理` 选项

### 5. 成本分析与优化
```bash
# 查看订阅费用(本月)
az consumption usage list \
  --top 10 \
  --query "[].{service:instanceName, cost:pretaxCost}" \
  -o table
# ...
# 识别未使用的资源
az resource list --query "[?tags.env=='dev']" -o table
# ...
# 查看虚拟机实际使用率
az monitor metrics list \
  --resource $(az vm show -g myRG -n myVM --query id -o tsv) \
  --metric "Percentage CPU" \
  --interval PT1H -o table
```

**输入**: 用户提供成本分析与优化所需的指令和必要参数.
**处理**: 解析成本分析与优化的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回成本分析与优化的处理结果,包含执行状态码、结果数据和执行日志.
### 6. 策略合规审计
```bash
# 查看策略分配
az policy assignment list -o table
# ...
# 合规状态检查
az policy state list --query "[?complianceState=='NonCompliant']" -o table
# ...
# 安全基线扫描
az security assessment list -o table
```

**输入**: 用户提供策略合规审计所需的指令和必要参数.
**输出**: 返回策略合规审计的处理结果,包含执行状态码、结果数据和执行日志.
#
## 适用场景

### 场景一: 企业级基础设施自动化部署

通过脚本化方式部署完整的生产环境.
```bash
#!/bin/bash
set -e
# ...
ENV=${1:-dev}
RG="app-${ENV}-rg"
LOCATION="eastus"
# ...
# 1. 创建资源组
az group create -g $RG -l $LOCATION
# ...
# 2. 部署应用服务
az deployment group create \
  -g $RG \
  --template-file infra/main.bicep \
  --parameters env=$ENV location=$LOCATION
# ...
# 3. 配置监控
az monitor log-analytics workspace create \
  -g $RG -n "logs-${ENV}" -l $LOCATION
# ...
# 4. 输出部署结果
echo "部署完成: $ENV 环境"
az resource list -g $RG --query "[].{name:name, type:type}" -o table
```

### 场景二: 多环境统一管理

统一管理开发、测试、生产三个环境的资源状态.
```bash
# 批量查询所有环境资源
for env in dev test prod; do
  echo "=== 环境: $env ==="
  az resource list -g "app-${env}-rg" \
    --query "[].{name:name, type:type, location:location}" \
    -o table
done
# ...
# 批量启停(夜间自动关停开发环境)
az vm list -g app-dev-rg --query "[].id" -o tsv | \
  xargs az vm deallocate --ids
```

### 场景三: 成本治理与资源清理

识别闲置资源并清理,优化云成本.
```bash
# 查找未附加的磁盘
az disk list --query "[?diskState=='Unattached']" -o table
# ...
# 查找停止超过 7 天的虚拟机
az vm list -d --query "[?powerState!='VM running']" -o table
# ...
# 批量删除未使用的存储容器
az storage container list \
  --account-name mystorage \
  --query "[?properties.leaseStatus=='unlocked'].name" -o tsv | \
  xargs -I {} az storage container delete \
    --account-name mystorage -n {}
```

## 使用流程

### 优秀步: 配置服务主体

```bash
# 创建服务主体
az ad sp create-for-rbac --name my-automation-sp
# ...
# 示例
# {
#   "appId": "详情见说明xx-详情见说明x-详情见说明x",
#   "password": "详情见说明xx-详情见说明x-详情见说明x",
#   "tenant": "详情见说明xx-详情见说明x-详情见说明x"
# }
# ...
# 配置环境变量
export AZURE_CLIENT_ID="<appId>"
export AZURE_CLIENT_SECRET="<password>"
export AZURE_TENANT_ID="<租户ID>"
```

### 第二步: 初始化项目配置

```bash
mkdir -p .azure-toolkit/{scripts,templates,reports}
# ...
cat > .azure-toolkit/config.json << 'EOF'
{
  "edition": "pro",
  "default_location": "eastus",
  "environments": ["dev", "test", "prod"],
  "auto_shutdown": {
    "dev": "22:00",
    "test": "20:00"
  },
  "cost_alert_threshold": 1000
}
EOF
```

### 第三步: 运行自动化部署

```bash
# 执行部署脚本
./.azure-toolkit/（请参考skill目录中的脚本文件） prod
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | azure-cli-toolkit处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 数据源读取失败 | 文件损坏或数据库连接中断 | 校验文件完整性,检查数据库连接参数,尝试备份数据源 |
| 数据处理内存溢出 | 数据集过大超出内存限制 | 启用流式处理模式,分批加载数据,或增加可用内存 |
| 查询结果为空 | 过滤条件过严或数据源无匹配记录 | 放宽查询条件,检查数据源时间范围,提示用户调整参数 |

## 依赖说明

### 运行环境

- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Azure CLI**: v2.50 或更高版本
- **Bash**: 4.0+(自动化脚本执行)

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Azure CLI | CLI 工具 | 必需 | brew / apt / choco 安装 |
| Azure 订阅 | 云服务 | 必需 | azure.com 注册 |
| 服务主体 | 认证 | 自动化必需 | `az ad sp create-for-rbac` |
| jq | CLI 工具 | 推荐 | 系统包管理器 |
| xargs | CLI 工具 | 批量操作必需 | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

自动化场景需配置服务主体凭据:

```bash
export AZURE_CLIENT_ID="your-client-id"
export AZURE_CLIENT_SECRET="your-client-secret"
export AZURE_TENANT_ID="your-tenant-id"
export AZURE_SUBSCRIPTION_ID="your-subscription-id"
```

建议使用 Azure KeyVault 管理敏感凭据:

```bash
# 从 KeyVault 获取密钥(推荐)
az keyvault secret show --vault-name myVault -n azure-client-secret \
  --query value -o tsv
```

### 可用性分类

- **分类**: MD+EXEC+SCRIPT(Markdown 指令 + 命令行执行 + 自动化脚本)
- **说明**: 通过自然语言指令驱动 Agent 执行 `az` 命令,支持脚本化批量操作与 CI/CD 集成
- **离线可用**: 否,所有操作需要连接 Azure 云平台

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100
# ...
检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100
# ...
检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100
# ...
检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过
# ...
改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1: 专业版是否兼容免费版的命令?

完全兼容。专业版使用相同的 `az` 命令语法,免费版的所有命令在专业版中可直接使用.
### Q2: 服务主体的密码过期了怎么办?

```bash
# 重置服务主体密码
az ad sp credential reset --name <appId> --password <new-password>
```

### Q3: 如何在 CI/CD 中安全存储凭据?

使用 CI/CD 平台的密钥管理功能(如 Azure KeyVault、GitHub Secrets),不要在代码中硬编码凭据.
### Q4: 批量操作误删了资源怎么办?

专业版支持软删除恢复:

```bash
# 恢复已删除的资源
az resource recover --ids <deleted-resource-id>
```

### Q5: 成本分析数据延迟多久?

成本数据通常有 8-24 小时延迟,建议结合监控指标做实时预估.
### Q6: 策略合规扫描多久执行一次?

建议每周执行一次全量扫描,新资源部署后立即扫描:

```bash
az policy state trigger-scan
```

## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖云服务，需要网络连接
- 需要有效的云服务凭证和配置好的CLI环境
- 产生的云资源可能产生费用，使用前请确认计费方式
- 不同区域的服务可用性和功能支持可能存在差异
