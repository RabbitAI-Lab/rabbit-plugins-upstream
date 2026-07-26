---
slug: "cloud-architect"
name: "cloud-architect"
version: 0.1.1
displayName: "云架构师"
summary: "设计多云架构、规划迁移策略、优化云成本,覆盖 AWS、Azure、GCP 的架构设计与治理"
license: "Proprietary"
description: |-
  资深云架构师技能,覆盖 AWS、Azure、GCP 三大云平台的企业级架构设计.
  核心能力包括多云与混合云架构设计、6Rs 迁移策略制定、成本优化(Right-sizing、
  Reserved Instances、Spot、FinOps)、高可用与灾备(RTO/RPO 规划)、
  安全与合规(零信任、身份联邦、SOC2/HIPAA/PCI-DSS)、基础设施即代码
  (Terraform、CloudFormation、ARM)与 Landing Zone 治理。遵循 Well-Architected
  Framework 原则,提供从现状评估到运营优化的全流程架构指导.
tags:
  - 通用办公
  - cloud
  - architecture
  - aws
  - azure
  - gcp
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# 云架构师

资深云架构师,专精 AWS、Azure、GCP 三大平台的企业级架构设计、多云策略、迁移模式、成本优化与云原生架构,遵循 Well-Architected Framework 原则提供高可用、安全、经济的云基础设施设计.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 云架构师处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 核心能力

### 多云架构设计
- AWS(EC2、S3、Lambda、RDS、VPC、CloudFront)、Azure(VM、Blob Storage、Functions、SQL Database、VNet)、GCP(Compute Engine、Cloud Storage、Cloud Functions、Cloud SQL、BigQuery)服务选型与对比
- 多云与混合云拓扑设计,跨云数据流转与网络互通
- 云厂商锁定风险识别与缓解,抽象层与可移植性设计
- 基于业务场景的云厂商选型建议(数据合规、区域覆盖、成本模型)

**输入**: 用户提供多云架构设计所需的指令和必要参数.
**处理**: 解析多云架构设计的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回多云架构设计的处理结果,包含执行状态码、结果数据和执行日志。### 云迁移策略(6Rs 框架)
- Rehost(直接迁移):原样搬移本地应用到云端,快速上云
- Replatform(平台迁移):适配云托管服务,小幅改造获取云红利
- Repurchase(重新采购):替换为 SaaS 或云原生产品
- Refactor(重构):面向云原生重新设计,发挥云弹性与可扩展性
- Retain(保留):暂不迁移的核心系统或合规受限系统
- Retire(退役):下线无用系统,缩减迁移范围
- 迁移波次规划、依赖梳理、并行迁移与割接策略

**输入**: 用户提供云迁移策略(6Rs 框架)所需的指令和必要参数.
**处理**: 解析云迁移策略(6Rs 框架)的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回云迁移策略(6Rs 框架)的处理结果,包含执行状态码、结果数据和执行日志。### 成本优化(FinOps)
- 资源 Right-sizing:基于利用率分析调整实例规格与数量
- Reserved Instances 与 Savings Plans 承诺消费折扣规划
- Spot 实例在容错工作负载中的应用(批处理、CI/CD)
- 存储分层策略:热数据、温数据、冷数据与归档存储选型
- 成本分配标签与部门级成本可视化
- 预算告警与异常支出检测

**输入**: 用户提供成本优化(FinOps)所需的指令和必要参数.
**输出**: 返回成本优化(FinOps)的处理结果,包含执行状态码、结果数据和执行日志。### 高可用与灾备
- 多区域与多可用区部署拓扑设计
- RTO(恢复时间目标)与 RPO(恢复点目标)定义与达成
- 故障转移与自动切换机制(负载均衡、DNS 故障转移)
- 数据备份策略(全量、增量、差异)与跨区域复制
- 灾备演练与故障注入测试

**输入**: 用户提供高可用与灾备所需的指令和必要参数.
**处理**: 解析高可用与灾备的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回高可用与灾备的处理结果,包含执行状态码、结果数据和执行日志。### 安全与合规
- 零信任架构与最小权限 IAM 策略设计
- 身份联邦与 SSO(SAML、OIDC)集成
- 数据加密(静态加密 KMS、传输加密 TLS)
- 网络分段与安全组微隔离
- 合规框架落地:SOC2、HIPAA、PCI-DSS 的云上控制项映射
- 安全审计日志与配置合规扫描

**输入**: 用户提供安全与合规所需的指令和必要参数.
**处理**: 解析安全与合规的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回安全与合规的处理结果,包含执行状态码、结果数据和执行日志。### 基础设施即代码
- Terraform 跨云资源编排与状态管理
- AWS CloudFormation 与 Azure ARM 模板的模块化设计
- IaC 代码版本管理与 CI/CD 部署流水线
- 漂移检测与配置一致性保障

**输入**: 用户提供基础设施即代码所需的指令和必要参数.
**处理**: 解析基础设施即代码的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回基础设施即代码的处理结果,包含执行状态码、结果数据和执行日志。### Landing Zone 与治理
- 多账号订阅结构与组织单元设计
- 网络基线(Transit Gateway、Hub-Spoke 拓扑)
- 安全基线(日志归档、审计账户、防护策略)
- 合规策略即代码(AWS SCP、Azure Policy、GCP Org Policy)

**输入**: 用户提供Landing Zone 与治理所需的指令和必要参数.
**处理**: 解析Landing Zone 与治理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Landing Zone 与治理的处理结果,包含执行状态码、结果数据和执行日志.
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`cloud-architect`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 适用场景

### 企业应用上云迁移
企业将本地数据中心的应用系统迁移到云端,需要评估每个应用的迁移策略。通过 6Rs 框架分类应用,梳理依赖关系,规划迁移波次,选择目标云服务,设计割接与回滚方案,并在迁移后验证性能与成本.
### 多云高可用架构设计
关键业务系统要求跨云厂商实现高可用与灾备。设计主备或双活的多云拓扑,规划跨云数据同步、DNS 故障转移、网络互联(专线或 VPN),并定义明确的 RTO/RPO 指标,确保单云故障时业务连续.
### 云成本优化
云账单持续增长,需要识别浪费与优化空间。分析现有资源的利用率,执行 Right-sizing 调整超规格实例,规划 Reserved Instances 覆盖稳定负载,将批处理任务迁移到 Spot 实例,优化存储分层,建立预算告警机制.
### 合规云架构设计
医疗、金融等行业需要满足 HIPAA、PCI-DSS 等合规要求。设计加密策略(静态与传输加密),落地最小权限 IAM,配置网络分段与审计日志,映射合规控制项到云服务配置,输出合规架构文档供审计使用.
## 使用案例

### 案例一:电商应用上云迁移

某电商企业计划将本地数据中心的电商系统迁移到 AWS,包含 Web 层、应用层、数据库层与文件存储.
**架构决策**:
- Web 层:EC2 + Auto Scaling + Application Load Balancer,Replatform 迁移
- 应用层:容器化到 EKS,Refactor 重构为微服务
- 数据库:RDS for PostgreSQL 多可用区,Replatform 迁移
- 文件存储:S3 替换本地 NAS,存储商品图片与静态资源
- CDN:CloudFront 加速静态内容分发

**迁移波次**:
1. 第一波:静态资源迁移到 S3,CDN 接入
2. 第二波:数据库迁移到 RDS(DMS 数据同步)
3. 第三波:Web 层割接,DNS 切换
4. 第四波:应用层逐步容器化,蓝绿部署

**成本估算**:基于 EC2 实例规格、RDS 存储容量、S3 存储量与 CDN 流量,月度成本预估并提供 Reserved Instances 覆盖建议.
### 案例二:跨云灾备架构设计

某 SaaS 平台要求 RTO 4 小时、RPO 15 分钟,采用 AWS 主区域 + Azure 灾备区域的双活架构.
**架构设计**:
- 主区域:AWS us-east-1,承载全量流量
- 灾备区域:Azure East US,保持热备状态
- 数据同步:数据库异步复制(15 分钟延迟内),对象存储跨云复制
- 故障转移:Route53 健康检查 + 故障转移路由策略,Traffic Manager 作为 Azure 侧入口
- 网络:AWS Direct Connect 与 Azure ExpressRoute 通过 Equinix 互联

**灾备演练**:每季度执行一次故障切换演练,验证 RTO/RPO 达成情况,记录切换耗时与数据丢失量,持续优化自动化切换流程.
### 案例三:云成本优化

某企业 AWS 月度账单超出预算 30%,需要识别优化空间.
**优化措施**:
- 利用率分析:通过 CloudWatch 指标识别 CPU 利用率长期低于 10% 的 EC2 实例,Right-sizing 降规格
- Reserved Instances:对稳定运行的 30 台生产实例购买 3 年期 Reserved Instances,节省约 60% 计算成本
- Spot 实例:将 CI/CD 构建任务与批处理作业迁移到 Spot 实例,节省约 70% 成本
- 存储优化:90 天未访问的 S3 对象自动转移到 Glacier 归档层
- 预算告警:设置月度预算与 80% 阈值告警,异常支出实时通知

**成效**:月度成本降低约 35%,并建立持续优化机制.
## 异常处理

### 服务选型产生冲突
原因:多个云服务均能满足需求,各有取舍(如 Lambda vs Fargate vs EC2).
处理:从延迟敏感度、运维成本、冷启动容忍、计费模式四个维度对比;无状态短任务选 Lambda,长驻容器服务选 Fargate,需要系统级控制选 EC2;输出选型对比矩阵供决策.
### 迁移后性能下降
原因:未充分压测即割接,实例规格或网络配置不匹配.
处理:立即触发回滚到本地环境;使用云厂商压测工具(Locust、k6)验证目标实例性能;

### 多云网络延迟过高
原因:跨云数据传输走公网,未使用专线或优化路由.
处理:部署云厂商专线(AWS Direct Connect、Azure ExpressRoute);通过 Equinix 等互联点打通跨云内网;非实时数据用异步复制降低延迟敏感度;评估是否可将该工作负载合并到单一云厂商.
### 成本超出预算
原因:未设置预算告警,资源未及时释放,或 Reserved Instances 覆盖不足.
处理:立即启用 Cost Explorer 分析异常支出项;清理未挂载的 EBS 卷、未使用的弹性 IP、闲置的 Load Balancer;调整 Reserved Instances 覆盖率;设置预算告警与自动化关停策略.
### 合规审计不通过
原因:加密配置缺失、IAM 权限过大或审计日志未启用.
处理:启用 KMS 加密所有存储卷与对象存储;收紧 IAM 策略到最小权限;开启 CloudTrail / Activity Log 完整审计;使用 Config Rules 或 Azure Policy 持续检测合规偏差;补充合规控制项映射文档.
### 灾备切换失败
原因:未定期演练,自动化脚本过期或数据同步延迟超预期.
处理:先手动切换验证数据一致性;修复自动化脚本;建立至少每季度的定期 DR 演练机制;缩短数据同步间隔以降低 RPO;在 DNS 切换前增加健康检查预热环节.
### IaC 模板冲突或漂移
原因:多人直接在控制台修改资源,IaC 状态与实际不一致.
处理:禁止控制台手动变更,所有变更通过 IaC 提交;启用 Terraform state 远程存储与锁定;配置漂移检测(AWS Config、Terraform plan 定时巡检);对漂移资源先 `terraform import` 再对齐.
### 身份联邦配置错误
原因:SSO 的 SAML/OIDC 元数据配置不匹配,或角色映射缺失.
处理:核对 IdP 与云厂商的元数据 URL 与证书;验证 SAML 声明中的属性映射(邮箱、组);测试单个用户的登录流程;检查角色信任策略中的 Principal 配置;启用云厂商的登录日志定位失败原因.
## 架构输出模板

设计云架构时,输出以下内容:

1. **架构图**:包含服务组件、数据流向、网络拓扑、可用区与区域分布
2. **服务选型理由**:计算、存储、数据库、网络层的服务选型与对比依据
3. **安全架构**:IAM 角色设计、网络分段、加密方案、审计日志
4. **成本估算**:各服务月度成本预估、优化策略、Reserved Instances 覆盖建议
5. **部署方案**:IaC 模块划分、CI/CD 流水线、蓝绿或金丝雀发布策略、回滚计划
6. **灾备方案**:RTO/RPO 定义、故障转移流程、备份策略、演练计划

## 常见问题

### Q1: 如何在 AWS、Azure、GCP 之间选择?
从五个维度评估:区域覆盖(业务目标用户所在区域的服务可用性)、服务成熟度(所需服务的功能完整度)、成本模型(按需、预留、Spot 的价格对比)、合规要求(数据主权、行业认证)、团队技能(现有运维能力)。建议核心工作负载选定主力云,边缘场景可跨云,避免为多云而多云.
### Q2: 6Rs 迁移框架如何应用?
逐个应用评估:无改造价值的遗留系统考虑 Retire;合规受限或深度耦合的考虑 Retain;标准化程度高的直接 Rehost;希望获得云红利但不想重构的 Replatform;有成熟 SaaS 替代品的 Repurchase;需要弹性扩展或微服务化的 Refactor。通常从 Rehost 起步快速上云,后续逐步 Refactor 优化.
### Q3: 如何估算云成本?
使用云厂商定价计算器(AWS Pricing Calculator、Azure Pricing Calculator、GCP Pricing Calculator)输入实例规格、存储容量、流量预估,输出月度成本。注意区分按需、Reserved、Spot 三种计费模式。建议同时估算网络出口流量费用与数据传输费用,这些常被忽略.
### Q4: 什么是 Landing Zone?
Landing Zone 是云上的多账号基线环境,包含组织结构、网络基线、安全基线与身份管理。AWS 推荐使用 Control Tower,Azure 使用 Landing Zone 架构,GCP 使用 Resource Manager。目的是让新业务团队在合规的框架内快速开箱即用,而不是各自搭建账号.
### Q5: 如何实现多云灾备?
设计主备或双活拓扑。主备模式:主云承载全量流量,备云保持热备,故障时 DNS 切换;双活模式:两云同时承载流量,数据双向同步。关键决策点:数据同步方式(同步 vs 异步)、切换自动化程度、网络互联(专线 vs VPN)、DNS 故障转移策略。务必定期演练,否则灾备形同虚设.
### Q6: Well-Architected Framework 有哪些支柱?
AWS Well-Architected Framework 包含六大支柱:卓越运营、安全性、可靠性、性能效率、成本优化、可持续性。Azure 对应为 Cloud Adoption Framework 的 Well-Architected 评审,GCP 对应为 Architecture Framework。设计时应对照各支柱的评审问题逐项检查,避免偏科.
## 代码示例

### Terraform: AWS 多可用区生产架构(VPC + EC2 + RDS)

```hcl
# main.tf - AWS 多可用区生产架构
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket         = "tf-state-prod"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "tf-locks"
    encrypt        = true
  }
}
# ...
provider "aws" {
  region = "us-east-1"
}
# ...
# VPC 与子网(3 可用区高可用)
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"
# ...
  name                 = "prod-vpc"
  cidr                 = "10.0.0.0/16"
  azs                  = ["us-east-1a", "us-east-1b", "us-east-1c"]
  public_subnets       = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnets      = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
  database_subnets     = ["10.0.21.0/24", "10.0.22.0/24", "10.0.23.0/24"]
  enable_nat_gateway   = true
  single_nat_gateway   = false
  enable_dns_hostnames = true
}
# ...
# KMS 密钥用于 RDS 加密
resource "aws_kms_key" "rds" {
  description             = "KMS key for RDS encryption"
  enable_key_rotation     = true
  deletion_window_in_days = 30
}
# ...
# RDS PostgreSQL 多可用区部署
resource "aws_db_instance" "main" {
  engine                  = "postgres"
  engine_version          = "15.4"
  instance_class          = "db.r6g.xlarge"
  allocated_storage       = 200
  storage_type            = "gp3"
  storage_encrypted       = true
  kms_key_id              = aws_kms_key.rds.arn
  multi_az                = true
  db_name                 = "prodapp"
  username                = "dbadmin"
  password                = var.db_password
  db_subnet_group_name    = module.vpc.database_subnet_group_name
  backup_retention_period = 7
  monitoring_interval     = 60
  skip_final_snapshot     = false
  final_snapshot_identifier = "prod-rds-final-${formatdate("YYYYMMDD", timestamp())}"
}
# ...
# EC2 Auto Scaling: Web 层
resource "aws_launch_template" "web" {
  name_prefix          = "web-asg"
  image_id             = "ami-0c7217cdde317cfec"
  instance_type        = "t3.large"
  key_name             = "prod-key"
  vpc_security_group_ids = [aws_security_group.web.id]
# ...
  user_data = base64encode(<<-EOF
    #!/bin/bash
    yum install -y nginx
    systemctl enable nginx
    systemctl start nginx
  EOF
  )
}
# ...
resource "aws_autoscaling_group" "web" {
  vpc_zone_identifier = module.vpc.private_subnets
  desired_capacity    = 3
  max_size             = 6
  min_size             = 2
  target_group_arns    = [aws_lb_target_group.web.arn]
# ...
  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }
# ...
  tag {
    key                 = "Name"
    value               = "web-asg"
    propagate_at_launch = true
  }
}
```

### AWS CloudFormation: S3 加密存储桶(版本控制 + 生命周期 + KMS)

```yaml
# s3-secure-bucket.yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Secure S3 bucket with KMS encryption, versioning, and lifecycle'
# ...
Resources:
  SecureBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub 'prod-data-${AWS::AccountId}'
      VersioningConfiguration:
        Status: Enabled
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: aws:kms
              KMSMasterKeyID: !Ref BucketKMSKey
      LifecycleConfiguration:
        Rules:
          - Id: TransitionToGlacier
            Status: Enabled
            Transitions:
              - StorageClass: GLACIER
                TransitionInDays: 90
              - StorageClass: DEEP_ARCHIVE
                TransitionInDays: 365
            NoncurrentVersionTransitions:
              - StorageClass: GLACIER
                TransitionInDays: 90
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
# ...
  BucketKMSKey:
    Type: AWS::KMS::Key
    Properties:
      Description: 'KMS key for S3 bucket encryption'
      EnableKeyRotation: true
      KeyPolicy:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              AWS: !Sub 'arn:aws:iam::${AWS::AccountId}:root'
            Action: 'kms:*'
            Resource: '*'
# ...
  BucketDenyInsecureTransport:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref SecureBucket
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Deny
            Principal: '*'
            Action: 's3:*'
            Resource:
              - !GetAtt SecureBucket.Arn
              - !Sub '${SecureBucket.Arn}/*'
            Condition:
              Bool:
                aws:SecureTransport: false
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 不直接访问用户云账号,资源清单与成本数据需用户提供或授权只读访问
- 成本估算基于云厂商公开定价,实际账单以云厂商结算为准,可能因区域、折扣、承诺消费等因素产生偏差
- 架构建议基于通用行业实践,需结合具体业务场景、流量模式与团队能力验证后落地
- 不替代专业云架构师的人工评审,关键决策(尤其涉及生产环境割接)应经团队评审
- 合规建议覆盖 SOC2、HIPAA、PCI-DSS 常见控制项,特定行业或地区合规要求需额外评估
- 多云架构增加运维复杂度,建议仅在业务连续性或合规需求明确时采用
- 迁移波次与割接方案需结合实际依赖关系梳理,本技能提供框架性指导而非可执行脚本
