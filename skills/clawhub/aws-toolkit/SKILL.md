---
slug: "aws-toolkit"
name: "aws-toolkit"
version: 1.0.1
displayName: "AWS部署专业版"
summary: "企业级AWS全服务管理平台，支持多区域、IaC、合规审计与成本优化。"
license: "Proprietary"
edition: "pro"
description: |-
  面向企业运维团队的AWS全服务管理平台。支持EC2/S3/VPC/RDS/Lambda/
  CloudWatch等全量AWS服务，提供基础设施即代码（IaC）、多区域批量
  部署、合规审计、成本优化与安全扫描功能。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标.
tags:
  - Operations
  - AWS
  - 企业级
  - 基础设施
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# AWS部署专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| AWS部署专业版业级AWS全服务管理 | 不支持 | 支持 |
| 多租户管理与权限分配 | 不支持 | 支持 |
| 操作审计与合规日志 | 不支持 | 支持 |
| 自定义仪表盘与报表 | 不支持 | 支持 |
| API开放与第三方集成 | 不支持 | 支持 |

## 核心能力

### PRO版功能增强对比
| 功能 | 免费版 | PRO版 |
|:-----|:-----|:-----|
| 服务覆盖 | 5项基础服务 | 30+全量服务 |
| 部署方式 | 命令行 | +IaC(Terraform/CFN) |
| 区域支持 | 单区域 | 多区域批量 |
| 合规审计 | 不支持 | 支持 |
| 成本优化 | 不支持 | 分析+建议 |
| 安全扫描 | 不支持 | 自动扫描 |
| 监控告警 | 不支持 | CloudWatch |
| 灾备管理 | 不支持 | 跨区域灾备 |

**输入**: 用户提供PRO版功能增强对比所需的指令和必要参数.
**输出**: 返回PRO版功能增强对比的处理结果,包含执行状态码、结果数据和执行日志。### 支持的AWS服务

| 类别 | 服务 | PRO版支持 |
|---:|---:|---:|
| 计算 | EC2/Lambda/ECS/EKS/Batch | 支持 |
| 存储 | S3/EBS/EFS/FSx/Glacier | 支持 |
| 网络 | VPC/Route53/CloudFront/ELB | 支持 |
| 数据库 | RDS/DynamoDB/ElastiCache/Redshift | 支持 |
| 安全 | IAM/KMS/WAF/GuardDuty | 支持 |
| 监控 | CloudWatch/CloudTrail/X-Ray | 支持 |
| AI/ML | SageMaker/Rekognition/Lex | 支持 |
| 分析 | Athena/EMR/Kinesis/Glue | 支持 |
### 服务覆盖

针对服务覆盖,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供服务覆盖相关的配置参数、输入数据和处理选项.
**输出**: 返回服务覆盖的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`服务覆盖`的配置文档进行参数调优
### 部署方式

针对部署方式,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供部署方式相关的配置参数、输入数据和处理选项.
**输出**: 返回部署方式的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`部署方式`的配置文档进行参数调优
#
## 适用场景

### 场景一：IaC基础设施部署

用户输入："用Terraform部署一套Web应用架构"

```bash
# 生成Terraform配置
python3 （请参考skill目录中的脚本文件） generate \
  --template "web_app_ha" \
  --regions "us-east-1,us-west-2" \
  --output ./terraform/
# ...
# 部署基础设施
python3 （请参考skill目录中的脚本文件） apply \
  --config ./terraform/ \
  --auto-approve
# ...
# 输出：
# VPC: 10.0.0.0/16 (2区域)
# EC2: 4台 (2区域x2可用区)
# RDS: 主从 (跨区域灾备)
# ELB: 负载均衡 (2区域)
# Route53: 健康检查+故障转移
```

### 场景二：合规审计

用户输入："检查AWS环境的合规性"

```bash
# 合规审计
python3 （请参考skill目录中的脚本文件） run \
  --standards "CIS,PCI-DSS,HIPAA" \
  --output audit_report.pdf
# ...
# 输出包含：
# - 合规检查项清单
# - 不合规项详情
# - 修复建议
# - 风险等级评估
```

### 场景三：成本优化

用户输入："分析AWS成本并给出优化建议"

```bash
# 成本分析
python3 （请参考skill目录中的脚本文件） analyze \
  --period "3m" \
  --output cost_report.xlsx
# ...
# 优化建议
python3 （请参考skill目录中的脚本文件） optimize \
  --apply-recommendations \
  --dry-run
# ...
# 输出：
# - 月度成本趋势
# - 各服务成本占比
# - 闲置资源识别
# - 预留实例建议
# - 预估节省金额
```

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt
# ...
# 安装Terraform
# macOS: brew install terraform
# Linux: 下载官方安装包
# ...
# 配置多区域凭证
cp config_pro_template.yaml config_pro.yaml
```

### 常用命令

```bash
# IaC部署
python3 （请参考skill目录中的脚本文件） generate --template "web_app_ha" --regions "us-east-1,us-west-2"
python3 （请参考skill目录中的脚本文件） apply --config ./terraform/
# ...
# 合规审计
python3 （请参考skill目录中的脚本文件） run --standards "CIS,PCI-DSS"
# ...
# 成本优化
python3 （请参考skill目录中的脚本文件） analyze --period "3m"
python3 （请参考skill目录中的脚本文件） optimize --dry-run
# ...
# 安全扫描
python3 （请参考skill目录中的脚本文件） scan --output security_report.pdf
# ...
# 多区域管理
python3 （请参考skill目录中的脚本文件） deploy --template web_app --regions "us-east-1,eu-west-1,ap-southeast-1"
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数"
  },
  "error": null
}
```

## 异常处理

- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+
- **Terraform**: 1.0+（IaC部署需要）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| boto3 | Python库 | 必需 | `pip install boto3` |
| awscli | CLI工具 | 必需 | `pip install awscli` |
| terraform | CLI工具 | 可选 | 官网下载（IaC部署） |
| botocore | Python库 | 必需 | 随boto3安装 |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:------:|--------|:-------|:------:|
| AWS Access Key | `AWS_ACCESS_KEY_ID` | 必需 | API认证 |
| AWS Secret | `AWS_SECRET_ACCESS_KEY` | 必需 | API认证 |
| AWS Region | `AWS_DEFAULT_REGION` | 必需 | 默认区域 |
| 多区域凭证 | 配置文件profile | 推荐 | 多区域操作 |

- 建议使用IAM角色而非Access Key（EC2上）
- 凭证通过 `aws configure --profile` 管理多账户

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本+IaC执行）
- **说明**: 企业级AWS全服务管理平台，支持IaC与合规审计
- **PRO版特性**: 全量服务、IaC部署、多区域、合规审计、成本优化、安全扫描
- **兼容性**: 完全兼容免费版命令与配置

## 案例展示

### PRO企业级配置

```yaml
pro_config:
  regions:
    primary: "us-east-1"
    secondary: ["us-west-2", "eu-west-1", "ap-southeast-1"]
# ...
  infrastructure:
    iac: "terraform"               # terraform | cloudformation
    state_backend: "s3"
    state_bucket: "my-tf-state"
    state_lock: "dynamodb"
# ...
  services:
    compute: ["ec2", "lambda", "ecs", "eks"]
    database: ["rds", "dynamodb", "elasticache"]
    storage: ["s3", "ebs", "efs"]
    networking: ["vpc", "route53", "cloudfront"]
    security: ["iam", "kms", "waf", "guardduty"]
    monitoring: ["cloudwatch", "cloudtrail", "x-ray"]
# ...
  audit:
    standards: ["CIS", "PCI-DSS", "HIPAA", "SOC2"]
    schedule: "weekly"
    auto_remediation: false        # 自动修复（谨慎开启）
# ...
  cost:
    analysis_period: "3m"
    recommendations: true
    budget_alerts:
      monthly: 10000
      alert_threshold: 0.8
# ...
  security:
    scan_frequency: "daily"
    vulnerability_scan: true
    config_compliance: true
# ...
  disaster_recovery:
    enabled: true
    rpo: 15                        # 恢复点目标（分钟）
    rto: 30                        # 恢复时间目标（分钟）
    cross_region: true
```

## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖云服务，需要网络连接
- 需要有效的云服务凭证和配置好的CLI环境
- 产生的云资源可能产生费用，使用前请确认计费方式
- 不同区域的服务可用性和功能支持可能存在差异

## 常见问题

**Q: 如何处理异常输入?**
A: 系统会自动检测并返回错误提示, 同时提供修复建议.
**Q: 支持哪些输入格式?**
A: 支持标准文本、JSON、CSV等常见格式.