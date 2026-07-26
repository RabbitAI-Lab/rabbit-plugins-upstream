---
slug: "aws-infra"
name: "aws-infra"
version: 1.0.1
displayName: "AWS Infra Inspector"
summary: "通过AWS CLI执行只读基础设施查询,覆盖实例清单、健康检查、安全审计、成本分析、变更追踪五大场景"
license: "Proprietary"
description: |-
  AWS基础设施只读检查工具。通过AWS CLI执行read-only查询,帮助开发者和管理员快速了解云资源状态.
  覆盖五大场景:EC2/S3/RDS资源清单、实例健康检查与CloudWatch告警、IAM用户与安全组审计、
  Cost Explorer成本分析、CloudTrail变更追踪。默认只读模式,所有变更操作需显式确认并使用--dry-run.
  适用于日常运维、安全审计、成本优化和故障排查场景.
tags:
  - Cloud
  - DevOps
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
# AWS Infra Inspector

通过AWS CLI执行只读基础设施查询,覆盖五大运维场景.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AWS Infra Inspector处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| AWS Infra Inspector执行只读基础设施查询 | 不支持 | 支持 |
| AWS Infra Inspector成本分析 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |

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

### 1. 资源清单查询 (Inventory)
- **EC2实例清单**: 查询所有区域的EC2实例ID、状态、类型
  `aws ec2 describe-instances --query 'Reservations[].Instances[].[InstanceId,State.Name,InstanceType]' --output table`
- **S3存储桶列表**: 列出账户下所有S3存储桶名称和创建时间
  `aws s3api list-buckets --query 'Buckets[].[Name,CreationDate]' --output table`
- **RDS数据库实例**: 查询RDS实例标识符、引擎类型、实例规格和运行状态
  `aws rds describe-db-instances --query 'DBInstances[].[DBInstanceIdentifier,Engine,DBInstanceClass,DBInstanceStatus]' --output table`
- **Lambda函数列表**: 列出所有Lambda函数名称、运行时和最后修改时间
  `aws lambda list-functions --query 'Functions[].[FunctionName,Runtime,LastModified]' --output table`

### 2. 健康检查 (Health)
- **EC2状态检查**: 获取实例系统状态检查和实例状态检查结果
  `aws ec2 describe-instance-status --include-all-instances --query 'InstanceStatuses[].[InstanceId,InstanceStatus.Status,SystemStatus.Status]' --output table`
- **RDS事件查询**: 查询最近60分钟内的RDS事件
  `aws rds describe-events --source-type db-instance --duration 60`
- **CloudWatch告警**: 列出所有处于ALARM状态的CloudWatch告警
  `aws cloudwatch describe-alarms --state-value ALARM --query 'MetricAlarms[].[AlarmName,StateValue,MetricName]' --output table`
- **ELB目标健康**: 检查负载均衡器目标组的健康状态
  `aws elbv2 describe-target-health --target-group-arn arn:aws:elasticloadbalancing:REGION:ACCOUNT:targetgroup/TG_NAME/TG_ID`

**输入**: 用户提供健康检查 (Health)所需的指令和必要参数.
### 3. 安全审计 (Security)
- **IAM用户列表**: 查询所有IAM用户及其最后登录时间
  `aws iam list-users --query 'Users[].[UserName,CreateDate,PasswordLastUsed]' --output table`
- **安全组规则**: 检查安全组的入站和出站规则
  `aws ec2 describe-security-groups --query 'SecurityGroups[].[GroupName,IpPermissions[].IpRanges[].CidrIp]' --output table`
- **S3存储桶策略**: 检查存储桶是否有公共访问权限
  `aws s3api get-bucket-policy-status --bucket BUCKET_NAME`
- **IAM访问密钥年龄**: 检查Access Key的创建时间,识别过期密钥
  `aws iam list-access-keys --user-name USERNAME --query 'AccessKeyMetadata[].[AccessKeyId,CreateDate,Status]' --output table`

### 4. 成本分析 (Costs)
- **月度总成本**: 查询指定月份的总成本
  `aws ce get-cost-and-usage --time-period Start=2024-01-01,End=2024-02-01 --granularity MONTHLY --metrics BlendedCost`
- **按服务分组成本**: 查询各AWS服务的成本占比
  `aws ce get-cost-and-usage --time-period Start=2024-01-01,End=2024-02-01 --granularity MONTHLY --metrics BlendedCost --group-by Type=DIMENSION Key=SERVICE`
- **按区域分组成本**: 查询各区域的成本分布
  `aws ce get-cost-and-usage --time-period Start=2024-01-01,End=2024-02-01 --granularity MONTHLY --metrics BlendedCost --group-by Type=DIMENSION Key=REGION`
- **成本预测**: 获取本月剩余时间的成本预测
  `aws ce get-cost-forecast --time-period Start=2024-01-15,End=2024-02-15 --granularity MONTHLY --metric BLENDED_COST`

**输入**: 用户提供成本分析 (Costs)所需的指令和必要参数.
**处理**: 解析成本分析 (Costs)的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回成本分析 (Costs)的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 变更追踪 (Changes)
- **CloudTrail事件查询**: 查询特定的API调用事件(如谁启动了实例)
  `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=RunInstances --max-results 20`
- **Config配置历史**: 查询资源的配置变更历史
  `aws configservice get-resource-config-history --resource-type AWS::EC2::Instance --resource-id i-1234567890abcdef0 --limit 10`
- **CloudFormation变更集**: 查看CloudFormation堆栈的待执行变更
  `aws cloudformation describe-change-set --change-set-name CHANGESET_NAME --stack-name STACK_NAME`

#
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|:---:|:---:|:---:|:---:|
| 日常运维巡检 | "检查所有EC2实例状态" | 实例ID、状态、状态检查结果的表格 | 健康检查 |
| 资源盘点 | "列出我们账户下的所有S3存储桶" | 存储桶名称、创建时间、区域列表 | 资源清单 |
| 安全合规审计 | "检查是否有安全组开放了0.0.0.0/0" | 安全组名称、规则、风险等级报告 | 安全审计 |
| 月度成本复盘 | "查询上个月各服务的AWS成本" | 按服务分组的成本表格和占比图表 | 成本分析 |
| 故障排查 | "查找最近谁修改了RDS配置" | CloudTrail事件列表(时间、用户、操作) | 变更追踪 |
| 跨区域资源统计 | "统计所有区域的EC2实例数量" | 各区域实例数量汇总表 | 资源清单+跨区域 |

**不适用于**: 需要创建/修改/删除AWS资源的操作(本Skill默认只读),需要实时监控指标(应使用CloudWatch Dashboard)

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
# 查询所有可用区域
aws ec2 describe-regions --query 'Regions[].RegionName' --output text
# ...
# 如需切换区域
aws configure set region us-west-2
```

### 3. 执行资源查询
根据运维需求选择对应能力:
- **盘点资源** → 执行Inventory类命令(如`describe-instances`)
- **检查健康** → 执行Health类命令(如`describe-instance-status`)
- **审计安全** → 执行Security类命令(如`describe-security-groups`)
- **分析成本** → 执行Costs类命令(如`get-cost-and-usage`)
- **追踪变更** → 执行Changes类命令(如`lookup-events`)

### 4. 格式化输出
```bash
# 表格格式 (适合人类阅读)
--output table
# ...
# JSON格式 (适合程序处理)
--output json
# ...
# 文本格式 (适合脚本提取)
--output text
```

### 5. 安全确认 (仅变更操作)
本Skill默认只读。如用户请求变更操作:
1. 明确显示将要执行的完整命令
2. 列出可能影响的资源
3. 建议使用 `--dry-run` 参数预检
4. 等待用户显式确认后才执行

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
### 案例2: 安全合规审计 (检查开放的安全组)
**场景**: 安全团队需要检查是否有安全组对互联网开放了敏感端口

```bash
# 查询所有安全组中开放0.0.0.0/0的规则
aws ec2 describe-security-groups \
  --filters Name=ip-permission.cidr,Values=0.0.0.0/0 \
  --query 'SecurityGroups[].[GroupName,GroupId,IpPermissions[].[FromPort,ToPort,IpProtocol,IpRanges[].CidrIp]]' \
  --output table
```

**预期输出**:
```
------------------------------------------------------------------------------
|                          DescribeSecurityGroups                            |
+------------+-----------------+----------+--------+-------------+------------+
|  web-sg    |  sg-0abc123    |  80      |  80    |  tcp        |  0.0.0.0/0 |
|  web-sg    |  sg-0abc123    |  443     |  443   |  tcp        |  0.0.0.0/0 |
|  db-sg     |  sg-0def456    |  3306    |  3306  |  tcp        |  0.0.0.0/0 |
+------------+-----------------+----------+--------+-------------+------------+
```

**分析**: `db-sg`安全组对0.0.0.0/0开放了3306端口(MySQL),这是**高风险**配置,数据库不应直接暴露在公网。建议立即修改安全组规则,仅允许应用服务器的内网IP访问.
### 案例3: 月度成本分析 (按服务分组)
**场景**: 财务团队需要了解上个月各AWS服务的成本分布

```bash
aws ce get-cost-and-usage \
  --time-period Start=2024-06-01,End=2024-07-01 \
  --granularity MONTHLY \
  --metrics BlendedCost \
  --group-by Type=DIMENSION Key=SERVICE \
  --query 'ResultsByGroups[].[Keys[0],Metrics.BlendedCost.Amount]' \
  --output table
```

**预期输出**:
```
------------------------------------------------------
|                GetCostAndUsage                     |
+------------------------+----------------------------+
|  Amazon Elastic Compute Cloud |  4523.67           |
|  Amazon Simple Storage Service|  892.15            |
|  Amazon RDS Service           |  2156.43           |
|  Amazon CloudFront            |  234.89            |
|  AWS Lambda                   |  67.22             |
+------------------------+----------------------------+
```

**分析**: EC2成本占比最高(57%),建议检查是否有闲置实例可优化;RDS成本较高(27%),可考虑预留实例或Savings Plans降低成本.
## 异常处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------|------:|:------|:------|
| 凭证未配置 | `Unable to locate credentials` | 未运行`aws configure`或环境变量未设置 | 运行`aws configure`配置Access Key和Secret Key |
| 凭证过期 | `The security token included in the request is expired` | 使用了临时凭证(STS)且已过期 | 运行`aws sts get-session-token`获取新凭证,或使用长期凭证 |
| 权限不足 | `User: arn:aws:iam::xxx is not authorized to perform: ec2:DescribeInstances` | IAM用户缺少对应API的调用权限 | 在IAM控制台为用户附加对应服务的ReadOnlyAccess策略 |
| 区域错误 | `Invalid Availability Zone` 或查询结果为空 | 指定的区域不正确或该区域无资源 | 使用`aws ec2 describe-regions`确认区域名称,切换区域重新查询 |
| 限流(Throttling) | `Rate exceeded` | API调用频率超过限制(默认每秒20次) | 添加`--cli-read-timeout 60 --cli-connect-timeout 60`参数,或减少并发查询 |
| Cost Explorer未启用 | `Policy doesn't allow Cost Explorer access` | 账户未启用Cost Explorer或无权限 | 在AWS控制台Billing页面启用Cost Explorer,等待24小时后数据可用 |
| CloudTrail查询超时 | `LookupEvents operation: Rate exceeded` | CloudTrail API限流 | 缩小时间范围,使用`--start-time`和`--end-time`参数分段查询 |
| S3存储桶不存在 | `NoSuchBucket` | 存储桶名称拼写错误或属于其他账户 | 使用`aws s3api list-buckets`确认存储桶名称,检查是否跨账户访问 |

## 常见问题

### Q1: 如何查询多个区域的资源?
A: AWS CLI默认只查询当前配置的区域。跨区域查询有两种方式:
```bash
# 方式1: 逐个区域查询
for region in us-east-1 us-west-2 eu-west-1 ap-northeast-1; do
  echo "=== $region ==="
  aws ec2 describe-instances --region $region --query 'Reservations[].Instances[].InstanceId' --output text
done
# ...
# 方式2: 使用AWS Config聚合查询 (需要预先配置)
aws configservice select-aggregate-resource-config \
  --expression "SELECT resourceId WHERE resourceType = 'AWS::EC2::Instance'" \
  --configuration-aggregator-name my-aggregator
```

### Q2: 如何使用不同的AWS账户(Profile)?
A: 通过`--profile`参数或`AWS_PROFILE`环境变量切换:
```bash
# 方式1: 命令行指定
aws ec2 describe-instances --profile production
# ...
# 方式2: 环境变量
export AWS_PROFILE=production
aws ec2 describe-instances
# ...
# 配置多个Profile (在~/.aws/credentials中)
# [production]
# aws_access_key_id = AKIAXXXXXXXX
# aws_secret_access_key = YOUR_API_KEY
# [staging]
# aws_access_key_id = AKIAYYYYYYYY
# aws_secret_access_key = yyyyyyyyyyyy
```

### Q3: 如何处理MFA(多因素认证)保护的账户?
A: 需要先获取临时凭证:
```bash
# 获取MFA临时凭证 (有效期12小时)
aws sts get-session-token --serial-number arn:aws:iam::123456789012:mfa/user --token-code 123456
# ...
# 将返回的临时凭证配置到Profile
aws configure set aws_access_key_id ASIAXXXXXXXX --profile mfa
aws configure set aws_secret_access_key xxxxxxxxxx --profile mfa
aws configure set aws_session_token xxxxxxxxxx --profile mfa
# ...
# 使用MFA Profile执行查询
aws ec2 describe-instances --profile mfa
```

### Q4: 查询结果太多如何过滤?
A: 使用JMESPath查询语言通过`--query`参数过滤:
```bash
# 只查询运行中的实例
aws ec2 describe-instances --filters Name=instance-state-name,Values=running \
  --query 'Reservations[].Instances[].[InstanceId,InstanceType,LaunchTime]'
# ...
# 按标签过滤
aws ec2 describe-instances --filters "Name=tag:Environment,Values=production" \
  --query 'Reservations[].Instances[].InstanceId'
# ...
# 使用JMESPath高级过滤
aws ec2 describe-instances \
  --query 'Reservations[].Instances[?State.Name==`running` && InstanceType==`t3.medium`].[InstanceId,Tags[?Key==`Name`].Value | [0]]'
```

### Q5: 如何导出查询结果到文件?
A: 使用`--output`参数配合重定向:
```bash
# 导出为JSON
aws ec2 describe-instances --output json > instances.json
# ...
# 导出为CSV (使用jq转换)
aws ec2 describe-instances --output json | jq -r '.Reservations[].Instances[] | [.InstanceId,.InstanceType,.State.Name] | @csv' > instances.csv
# ...
# 导出为表格文本
aws ec2 describe-instances --output table > instances.txt
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **只读模式**: 默认不执行任何创建/修改/删除操作,变更操作需用户显式确认
- **成本数据延迟**: Cost Explorer的数据通常有12-24小时延迟,当天数据可能不可用
- **CloudTrail事件限制**: `lookup-events`仅支持查询最近90天的事件,更早的事件需使用Athena查询S3日志
- **跨账户查询**: 无法直接查询其他AWS账户的资源,需通过AWS Config聚合器或RAM共享
- **区域限制**: 某些服务(如CloudFront、IAM)是全球服务,不支持`--region`参数
- **API限流**: AWS API有调用频率限制,大量查询时需要添加重试和退避逻辑
