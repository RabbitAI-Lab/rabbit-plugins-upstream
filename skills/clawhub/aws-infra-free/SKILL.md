---
slug: "aws-infra-free"
name: "aws-infra-free"
version: "1.0.0"
displayName: "AWS Infra LITE"
summary: "通过AWS CLI执行基础只读查询,覆盖EC2/S3/RDS资源清单和实例健康检查两大场景"
license: "MIT"
description: |-
  AWS基础设施基础查询工具(免费版)。通过AWS CLI执行read-only查询,帮助开发者快速了解云资源状态.
  覆盖两大基础场景:EC2/S3/RDS资源清单查询、实例健康检查与CloudWatch告警查看.
  默认只读模式,不执行任何变更操作。适用于日常运维巡检和资源盘点.
  如需安全审计、成本分析、变更追踪等高级功能,请升级至aws-infra付费版.
tags:
  - Cloud
  - DevOps
  - 通用办公
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# AWS Infra LITE

通过AWS CLI执行基础只读查询,覆盖资源清单和健康检查两大场景.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AWS Infra LITE处理的输入数据或指令 |
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

### 1. 资源清单查询 (Inventory)
- **EC2实例清单**: 查询当前区域的EC2实例ID、状态、类型
  `aws ec2 describe-instances --query 'Reservations[].Instances[].[InstanceId,State.Name,InstanceType]' --output table`
- **S3存储桶列表**: 列出账户下所有S3存储桶名称和创建时间
  `aws s3api list-buckets --query 'Buckets[].[Name,CreationDate]' --output table`
- **RDS数据库实例**: 查询RDS实例标识符、引擎类型和运行状态
  `aws rds describe-db-instances --query 'DBInstances[].[DBInstanceIdentifier,Engine,DBInstanceStatus]' --output table`

### 2. 健康检查 (Health)
- **EC2状态检查**: 获取实例系统状态检查和实例状态检查结果
  `aws ec2 describe-instance-status --include-all-instances --query 'InstanceStatuses[].[InstanceId,InstanceStatus.Status,SystemStatus.Status]' --output table`
- **CloudWatch告警**: 列出所有处于ALARM状态的CloudWatch告警
  `aws cloudwatch describe-alarms --state-value ALARM --query 'MetricAlarms[].[AlarmName,StateValue,MetricName]' --output table`

> **升级提示**: 安全审计(IAM/安全组检查)、成本分析(Cost Explorer)、变更追踪(CloudTrail)等高级功能仅在[aws-infra付费版](#)中提供.
### EC2实例清单

针对EC2实例清单,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供EC2实例清单相关的配置参数、输入数据和处理选项.
**输出**: 返回EC2实例清单的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`EC2实例清单`的配置文档进行参数调优
#
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|---:|---:|---:|---:|
| 日常运维巡检 | "检查所有EC2实例状态" | 实例ID、状态、状态检查结果的表格 | 健康检查 |
| 资源盘点 | "列出我们账户下的所有S3存储桶" | 存储桶名称、创建时间列表 | 资源清单 |
| 故障排查 | "查看当前有哪些CloudWatch告警" | 告警名称、状态、指标名称表格 | 健康检查 |

**不适用于**: 需要安全审计、成本分析、变更追踪的场景(请使用付费版),需要创建/修改/删除AWS资源的操作

## 使用流程

### 1. 验证身份与权限
```bash
aws sts get-caller-identity
# 确认当前账户和用户,确保有足够的只读权限
```

### 2. 确定目标区域
```bash
# 查看当前默认区域
aws configure get region
# ...
# 如需切换区域
aws configure set region us-west-2
```

### 3. 执行资源查询
根据运维需求选择对应能力:
1. **盘点资源** → 执行Inventory类命令(如`describe-instances`)
2. **检查健康** → 执行Health类命令(如`describe-instance-status`)

### 4. 格式化输出
```bash
# 表格格式 (适合人类阅读)
--output table
# ...
# JSON格式 (适合程序处理)
--output json
```

#
## 案例展示

### 案例1: 日常运维巡检 (EC2健康检查)
**场景**: 运维人员需要快速检查所有EC2实例的运行状态

```bash
# 查询所有实例的状态检查结果
aws ec2 describe-instance-status --include-all-instances \
  --query 'InstanceStatuses[].[InstanceId,InstanceStatus.Status,SystemStatus.Status,AvailabilityZone]' \
  --output table
```

**预期输出**:
```
------------------------------------------------------------------------------------
|                             DescribeInstanceStatus                               |
+----------------------+-------------------+-----------------+--------------------+
|  i-0abc123def456789  |  ok               |  ok             |  us-east-1a        |
|  i-0def456ghi789123  |  impaired         |  ok             |  us-east-1b        |
|  i-0ghi789jkl123456  |  ok               |  insufficient   |  us-east-1c        |
+----------------------+-------------------+-----------------+--------------------+
```

**分析**: `i-0def456ghi789123`的实例状态为`impaired`,需要进一步检查;`i-0ghi789jkl123456`的系统状态为`insufficient`,可能需要重启或联系AWS支持.
### 案例2: 资源盘点 (S3存储桶列表)
**场景**: 开发者需要确认账户下有哪些S3存储桶

```bash
aws s3api list-buckets --query 'Buckets[].[Name,CreationDate]' --output table
```

**预期输出**:
```
------------------------------------------------------------
|                     ListBuckets                          |
+---------------------------+-----------------------------+
|  my-app-uploads           |  2024-01-15T10:30:00.000Z  |
|  cloudfront-logs          |  2024-02-20T14:15:00.000Z  |
|  backup-data              |  2024-03-10T09:00:00.000Z  |
+---------------------------+-----------------------------+
```

## 异常处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:---:|:---:|:---:|:---:|
| 凭证未配置 | `Unable to locate credentials` | 未运行`aws configure`或环境变量未设置 | 运行`aws configure`配置Access Key和Secret Key |
| 凭证过期 | `The security token included in the request is expired` | 使用了临时凭证(STS)且已过期 | 运行`aws sts get-session-token`获取新凭证 |
| 权限不足 | `User: arn:aws:iam::xxx is not authorized to perform: ec2:DescribeInstances` | IAM用户缺少对应API的调用权限 | 在IAM控制台为用户附加AmazonEC2ReadOnlyAccess策略 |
| 区域错误 | 查询结果为空 | 指定的区域不正确或该区域无资源 | 使用`aws configure set region`切换区域重新查询 |
| 限流(Throttling) | `Rate exceeded` | API调用频率超过限制 | 减少查询频率,添加`--cli-read-timeout 60`参数 |

## 常见问题

### Q1: 如何切换查询的AWS区域?
A: 通过`--region`参数或修改默认区域:
```bash
# 方式1: 单次查询指定区域
aws ec2 describe-instances --region us-west-2
# ...
# 方式2: 修改默认区域
aws configure set region us-west-2
```

### Q2: 如何查询运行中的EC2实例?
A: 使用`--filters`参数过滤:
```bash
aws ec2 describe-instances --filters Name=instance-state-name,Values=running \
  --query 'Reservations[].Instances[].[InstanceId,InstanceType,LaunchTime]' --output table
```

### Q3: 免费版和付费版有什么区别?
A: 免费版(LITE)包含资源清单查询和健康检查两大基础功能。付费版(AWS Infra Inspector)额外提供:
- 安全审计(IAM用户、安全组规则、S3存储桶策略检查)
- 成本分析(Cost Explorer按服务/区域分组成本查询)
- 变更追踪(CloudTrail事件查询、Config配置历史)
- 更多案例展示(3个完整案例 vs 2个基础案例)
- 更详细的异常处理(8种AWS特定错误 vs 5种基础错误)

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **只读模式**: 不执行任何创建/修改/删除操作
- **功能限制**: 仅支持资源清单和健康检查,不支持安全审计、成本分析、变更追踪(需升级付费版)
- **区域限制**: 默认仅查询当前配置的区域,不支持跨区域批量查询(付费版支持)
- **API限流**: AWS API有调用频率限制,大量查询时需要间隔执行
