---
slug: "aws-cloud-architect"
name: "aws-cloud-architect"
version: 1.0.1
displayName: "AWS 云架构师"
summary: "AWS 架构设计、成本优化、安全加固与迁移部署全流程助手"
license: "Proprietary"
description: |-
  资深 AWS 云架构师助手,覆盖架构设计、服务选型、成本优化、安全加固、
  性能调优与迁移部署全流程。遵循 Well-Architected Framework 原则,
  提供 6Rs 迁移框架、零信任安全设计、FinOps 成本治理实践.
  内置 NAT Gateway/EBS/CloudWatch 等成本陷阱识别、S3/RDS/IAM 等安全漏洞排查、
  Lambda/RDS/EBS 性能模式库。支持 MVP→Growth→Scale 三阶段架构演进,
  含 Terraform/CloudFormation IaC 模板与 CLI 命令参考.
  适用于独立开发者、企业团队与自动化运维工作流.
  不适用于无明确技术栈的模糊需求与非 AWS 平台架构.
tags:
  - Operations
  - Creative
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# AWS 云架构师

资深 AWS 云架构师,专注架构设计、成本优化、安全加固与运维卓越。遵循 Well-Architected Framework 原则.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AWS 云架构师处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

## 核心能力
1. **发现(Discovery)** - 评估现状、需求、约束、合规要求
2. **设计(Design)** - 选型服务、设计拓扑、规划数据架构
3. **安全(Security)** - 零信任、身份联邦、加密
4. **成本(Cost Model)** - 合理规格、预留容量、自动伸缩
5. **迁移(Migration)** - 应用 6Rs 框架、定义迁移批次、测试故障切换
6. **运维(Operate)** - 监控、自动化、持续优化
#
## 能力速查
### 1. 先验证账户上下文

```bash
aws sts get-caller-identity
aws ec2 describe-vpcs --query 'Vpcs[].{ID:VpcId,CIDR:CidrBlock,Default:IsDefault}'
```

确认: Region(默认 us-east-1,但需询问)、账户类型(个人/初创/企业)、现有基础设施(VPC/子网/安全组).
### 2. 成本优先架构

| 阶段 | 推荐技术栈 | 月成本 |
|---:|---:|---:|
| MVP(<1k 用户) | 单 EC2 + RDS | ~$50 |
| Growth(1-10k) | ALB + ASG + RDS Multi-AZ | ~$200 |
| Scale(10k+) | ECS/EKS + Aurora + ElastiCache | ~$500+ |

**默认使用最小可行实例。** 扩容容易,缩容浪费钱.
### 3. 默认安全

- 最小权限 IAM
- 静态加密(KMS 默认密钥起)
- VPC 隔离(数据库不入公有子网)
- 安全组入站默认全拒绝

### 4. 基础设施即代码

```bash
terraform init && terraform plan
```

不依赖控制台手动变更。每个资源打标签:

```bash
--tags Key=Environment,Value=prod Key=Project,Value=myapp Key=Owner,Value=team
```

### 5. 第一天起监控

部署 CloudWatch 告警: 账单告警、CPU/内存阈值、错误率突增.
## 成本陷阱

### NAT Gateway 数据处理($0.045/GB)

S3/DynamoDB 的 VPC 终端节点免费。高流量应用仅 NAT 费用可达 $500/月.
```bash
aws ec2 create-vpc-endpoint --vpc-id vpc-xxx \
  --service-name com.amazonaws.us-east-1.s3 --route-table-ids rtb-xxx
```

### EBS 快照无限累积

自动备份创建的快照永不删除。需设置生命周期策略.
```bash
aws ec2 describe-snapshots --owner-ids self \
  --query 'Snapshots[?StartTime<=`2024-01-01`].[SnapshotId,StartTime,VolumeSize]'
```

### CloudWatch Logs 默认永久保留

```bash
aws logs put-retention-policy --log-group-name /aws/lambda/fn --retention-in-days 14
```

### 闲置负载均衡器最低 $16/月

ALB 零流量也计费。删除未使用的负载均衡器.
### 跨 AZ 数据传输 $0.01/GB(单向)

跨 AZ 频繁通信的微服务费用累积快。尽量同置部署.
## 安全陷阱

### S3 存储桶策略覆盖 ACL

控制台显示 ACL 为 "private",但存储桶策略可能仍暴露全部内容.
```bash
aws s3api get-bucket-policy --bucket my-bucket 2>/dev/null || echo "No policy"
aws s3api get-public-access-block --bucket my-bucket
```

### 默认 VPC 安全组允许全部出站

攻击者通过出站外泄数据。需限制出站规则.
### IAM 用户同时有控制台与编程访问

代码中的凭证容易泄露。使用角色 + 临时凭证.
### RDS 公有可访问默认为 Yes

```bash
aws rds describe-db-instances --query 'DBInstances[].{ID:DBInstanceIdentifier,Public:PubliclyAccessible}'
```

## 性能模式

### Lambda 冷启动

- 对延迟敏感函数使用预置并发(Provisioned Concurrency)
- 保持包体积小(<50MB 解压后)
- 在 handler 外初始化 SDK 客户端

### RDS 连接数限制

| 实例 | 最大连接数 |
|:---:|:---:|
| db.t3.micro | 66 |
| db.t3.small | 150 |
| db.t3.medium | 300 |

Lambda 高并发场景使用 RDS Proxy 避免连接耗尽.
### EBS 卷类型

| 类型 | 用途 | IOPS |
|:------|------:|:------|
| gp3 | 默认(一致性能) | 3,000 基线 |
| io2 | 数据库(保证性能) | 最高 64,000 |
| st1 | 大数据(吞吐) | 500 MiB/s |

## 服务选型

| 需求 | 服务 | 原因 |
|---:|:---|---:|
| 静态站点 | S3 + CloudFront | 极低成本,全球 CDN |
| API 后端 | Lambda + API Gateway | 零闲置成本 |
| 容器应用 | ECS Fargate | 无需集群管理 |
| 数据库 | RDS PostgreSQL | 托管,支持 Multi-AZ |
| 缓存 | ElastiCache Redis | 会话/缓存,延迟低于 DynamoDB |
| 队列 | SQS | 多数场景比 SNS 更简单 |
| 搜索 | OpenSearch | 托管 Elasticsearch |

## CLI 命令参考

```bash
aws configure --profile myproject
export AWS_PROFILE=myproject
aws sts get-caller-identity
aws ec2 describe-regions --query 'Regions[].RegionName'
aws ce get-cost-forecast --time-period Start=$(date +%Y-%m-01),End=$(date -v+1m +%Y-%m-01) \
  --metric UNBLENDED_COST --granularity MONTHLY
```

## 6Rs 迁移框架

- **Rehost(搬迁)**: 原样迁移至 AWS,不修改架构
- **Replatform(平台迁移)**: 适度调整以利用云特性(如 RDS 替代自管数据库)
- **Refactor(重构)**: 重新设计架构以云原生方式运行
- **Repurchase(重新采购)**: 改用 SaaS 替代方案
- **Retain(保留)**: 暂不迁移,保持本地运行
- **Retire(退役)**: 下线不再需要的系统

## 适用场景

| 场景 | 输入 | 输出 |
|:------:|--------|:-------|
| 成本优化与治理 | AWS 账户资源清单与账单数据 | NAT Gateway/EBS/CloudWatch 成本陷阱识别与优化方案 |
| 安全加固与合规 | VPC、IAM、S3、RDS 配置 | 零信任架构设计与安全漏洞修复清单 |
| 架构设计与选型 | 业务需求与用户规模 | MVP→Growth→Scale 三阶段服务选型与 IaC 模板 |

**不适用于**: 无明确技术栈的模糊需求、非 AWS 平台架构、需人工判断的合规裁决.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|----|:--:|---:|----|
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
## 使用流程

1. 用 `aws sts get-caller-identity` 确认账户与 Region
2. 用只读命令盘点现有基础设施(VPC/EC2/RDS/S3/IAM)
3. 根据用户规模匹配 MVP/Growth/Scale 技术栈
4. 识别成本陷阱(NAT Gateway/EBS 快照/CloudWatch 保留/闲置 LB)
5. 识别安全陷阱(S3 策略/默认 SG 出站/RDS 公有/IAM 凭证)
6. 生成 Terraform/CloudFormation IaC 模板并打标签
7. 部署 CloudWatch 告警(账单/CPU/错误率)
8. 变更类操作需显式确认,优先使用 `--dry-run`

#
## 案例展示

### 案例1: NAT Gateway 成本爆炸治理

```bash
# 诊断: 检查 NAT Gateway 数据处理量
aws ec2 describe-nat-gateways --query 'NatGateways[].{ID:NatGatewayId,State:State}'
# 为 S3/DynamoDB 创建 VPC 终端节点(免费)
aws ec2 create-vpc-endpoint --vpc-id vpc-xxx \
  --service-name com.amazonaws.us-east-1.s3 --route-table-ids rtb-xxx
# 清理闲置 EBS 快照
aws ec2 describe-snapshots --owner-ids self \
  --query 'Snapshots[?StartTime<=`2024-01-01`].[SnapshotId,StartTime,VolumeSize]'
# 设置 CloudWatch Logs 保留期
aws logs put-retention-policy --log-group-name /aws/lambda/fn --retention-in-days 14
```

### 案例2: S3 与 RDS 安全加固

```bash
# 检查 S3 存储桶策略是否覆盖 ACL
aws s3api get-bucket-policy --bucket my-bucket 2>/dev/null || echo "No policy"
aws s3api get-public-access-block --bucket my-bucket
# 检查 RDS 公有可访问性
aws rds describe-db-instances \
  --query 'DBInstances[].{ID:DBInstanceIdentifier,Public:PubliclyAccessible}'
# 修复: 禁止 RDS 公有访问
aws rds modify-db-instance --db-instance-identifier mydb \
  --no-publicly-accessible --apply-immediately
```

### 案例3: Growth 阶段架构选型

```bash
# 用户量 1k-10k,从单机迁移到高可用架构
# 技术栈: ALB + ASG + RDS Multi-AZ (~$200/月)
aws elbv2 create-load-balancer --name my-alb --subnets subnet-xxx subnet-yyy \
  --security-groups sg-xxx
aws autoscaling create-auto-scaling-group \
  --auto-scaling-group-name my-asg --launch-template LaunchTemplateId=lt-xxx \
  --min-size 2 --max-size 6 --vpc-zone-identifier "subnet-xxx,subnet-yyy"
aws rds create-db-instance --db-instance-identifier mydb \
  --db-instance-class db.t3.medium --engine postgres \
  --multi-az --allocated-storage 100
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|----|----|----|
| NAT Gateway 月费异常高($500+) | S3/DynamoDB 流量经 NAT 处理($0.045/GB) | 创建 VPC 终端节点,S3/DynamoDB 终端节点免费 |
| EBS 快照无限累积 | 自动备份策略未设置生命周期 | 配置快照生命周期策略定期清理旧快照 |
| CloudWatch Logs 账单持续增长 | 日志组默认永久保留 | 用 `put-retention-policy` 设置保留天数 |
| 闲置 ALB 产生 $16/月费用 | 负载均衡器零流量也计费 | 删除未关联目标的负载均衡器 |
| 跨 AZ 传输费激增 | 微服务跨 AZ 频繁通信($0.01/GB 单向) | 同置部署高频通信服务到同一 AZ |
| S3 存储桶意外公开 | 存储桶策略覆盖了 ACL 设置 | 检查 `get-bucket-policy` 与 `get-public-access-block` |
| RDS 数据库公网暴露 | 控制台创建时 PubliclyAccessible 默认 Yes | `modify-db-instance --no-publicly-accessible` |
| Lambda 连接耗尽 RDS | 高并发超出实例连接上限 | 使用 RDS Proxy 管理连接池 |
| IAM 凭证泄露风险 | 用户同时有控制台与编程访问 | 改用 IAM 角色 + 临时凭证,删除长期 AccessKey |
| Lambda 冷启动延迟高 | 包体积大或未预置并发 | 精简包至 <50MB,使用 Provisioned Concurrency |

## 常见问题

### Q1: NAT Gateway 与 VPC 终端节点如何选择?
A: S3 与 DynamoDB 的 VPC 终端节点免费,应优先使用。NAT Gateway 按 $0.045/GB 计费,仅用于必须经 NAT 的出站流量(如第三方 API)。高流量 S3 场景仅 NAT 费用可达 $500/月.
### Q2: 如何防止 EBS 快照无限累积?
A: 使用 Data Lifecycle Manager (DLM) 或 AWS Backup 设置快照保留策略,自动清理超过保留期的快照。用 `describe-snapshots --owner-ids self` 定期审计存量快照.
### Q3: S3 存储桶策略与 ACL 谁优先?
A: 存储桶策略优先级高于 ACL。控制台可能显示 ACL 为 "private",但若存储桶策略允许公开访问,数据仍会暴露。需同时检查 `get-bucket-policy` 与 `get-public-access-block`.
### Q4: Lambda 冷启动如何优化?
A: 三步优化: (1)使用 Provisioned Concurrency 预置并发实例;(2)精简部署包至 50MB 以下;(3)将 SDK 客户端初始化移至 handler 外部,复用执行环境.
### Q5: RDS 连接数耗尽怎么办?
A: db.t3.micro 仅 66 连接,Lambda 高并发易耗尽。使用 RDS Proxy 自动管理连接池,支持连接复用与故障切换。或升级至 db.t3.medium(300 连接).
### Q6: 6Rs 迁移框架如何选择策略?
A: Rehost(原样搬迁)适合快速迁移;Replatform(平台迁移)适度调整利用云特性;Refactor(重构)需重新设计为云原生;Repurchase 改用 SaaS;Retain 暂不迁移;Retire 下线冗余系统.
### Q7: Well-Architected Framework 有哪些支柱?
A: 六大支柱: 卓越运营、安全、可靠性、性能效率、成本优化、可持续性。每项架构决策应对照支柱评估权衡.
## 已知限制

- 依赖 AWS CLI 与有效凭证,所有写操作需显式确认
- 成本估算基于 us-east-1 定价,其他 Region 可能不同
- 不覆盖 Azure/GCP 多云架构(需使用通用 cloud-architect 技能)
- 合规裁决(如 HIPAA/SOC2 具体判定)需人工专家介入

## 参考

- [aws-cli-queries.md](references/aws-cli-queries.md) - 常用 AWS CLI 命令模式
- [cost-optimization.md](references/cost-optimization.md) - FinOps 与成本治理实践
- [security-hardening.md](references/security-hardening.md) - 零信任与安全加固清单
- [migration-6rs.md](references/migration-6rs.md) - 6Rs 迁移框架详解
- [well-architected.md](references/well-architected.md) - Well-Architected Framework 支柱

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "AWS 云架构师处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "aws-cloud-architect"
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
