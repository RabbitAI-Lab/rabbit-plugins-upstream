---
slug: "cloud-architect-free"
name: "cloud-architect-free"
version: "1.0.0"
displayName: "云架构师免费版"
summary: "基础云架构设计,覆盖 AWS、Azure、GCP 服务选型与迁移策略框架"
license: "MIT"
description: |-
  面向云架构入门场景的基础技能,覆盖 AWS、Azure、GCP 三大云平台的
  服务选型、迁移策略框架与基础架构设计原则。适合单云架构设计、
  成本入门优化与基础安全合规咨询。多云灾备、FinOps 深度优化、
  Landing Zone 治理等进阶能力请使用付费版本.
tags:
  - 通用办公
  - cloud
  - architecture
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# 云架构师免费版

基础云架构设计技能,覆盖 AWS、Azure、GCP 三大云平台的服务选型、迁移策略框架与基础架构设计原则,适合单云架构设计入门与常见云架构咨询.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 云架构师免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 核心能力

### 单云架构设计
- AWS(EC2、S3、Lambda、RDS、VPC)、Azure(VM、Blob Storage、Functions、SQL Database、VNet)、GCP(Compute Engine、Cloud Storage、Cloud Functions、Cloud SQL)核心服务选型
- 计算、存储、数据库、网络层的基础架构设计
- 基于业务场景的云厂商选型建议

**输入**: 用户提供单云架构设计所需的指令和必要参数.
**处理**: 解析单云架构设计的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回单云架构设计的处理结果,包含执行状态码、结果数据和执行日志。### 迁移策略框架(6Rs)
- Rehost(直接迁移):原样搬移应用到云端
- Replatform(平台迁移):适配云托管服务小幅改造
- Repurchase(重新采购):替换为 SaaS 或云原生产品
- Refactor(重构):面向云原生重新设计
- Retain(保留):暂不迁移的系统
- Retire(退役):下线无用系统

**输入**: 用户提供迁移策略框架(6Rs)所需的指令和必要参数.
**处理**: 解析迁移策略框架(6Rs)的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回迁移策略框架(6Rs)的处理结果,包含执行状态码、结果数据和执行日志。### 基础成本优化
- 资源 Right-sizing:基于利用率调整实例规格
- Reserved Instances 承诺消费折扣入门
- 存储分层:热数据与冷数据的存储选型

**输入**: 用户提供基础成本优化所需的指令和必要参数.
**处理**: 解析基础成本优化的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回基础成本优化的处理结果,包含执行状态码、结果数据和执行日志。### 基础安全与合规
- 数据加密(静态加密与传输加密)
- IAM 最小权限策略入门
- 网络分段与安全组基础配置

**输入**: 用户提供基础安全与合规所需的指令和必要参数.
**处理**: 解析基础安全与合规的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回基础安全与合规的处理结果,包含执行状态码、结果数据和执行日志。### 基础设施即代码
- Terraform 跨云资源编排入门
- IaC 代码版本管理基础

**输入**: 用户提供基础设施即代码所需的指令和必要参数.
**处理**: 解析基础设施即代码的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回基础设施即代码的处理结果,包含执行状态码、结果数据和执行日志.
### 输出格式

完成响应以Markdown格式返回,包含任务状态(成功/失败)、解析摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。- 验证返回数据的完整性和格式正确性
- 参考`输出格式`的配置文档进行参数调优
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`cloud-architect-free`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 适用场景

### 单云应用架构设计
为应用系统设计单云架构,选择合适的计算、存储、数据库与网络服务,输出基础架构方案与服务选型理由。适合首次上云或新业务系统的架构规划.
### 应用上云迁移评估
评估本地应用的迁移策略,使用 6Rs 框架分类应用,选择目标云服务,规划迁移步骤。适合迁移前的初步评估与方案制定.
## 使用案例

### 案例一:Web 应用上云架构设计

某企业 Web 应用计划部署到 AWS,需要设计基础架构.
**架构决策**:
- 计算层:EC2 + Auto Scaling + Application Load Balancer,应对流量波动
- 数据库:RDS for PostgreSQL 多可用区部署,保障数据持久性
- 存储:S3 存放静态资源与用户上传文件
- 网络:VPC 公有子网与私有子网分层,数据库置于私有子网
- CDN:CloudFront 加速静态内容分发

**输出**:架构图、服务选型理由、基础成本估算、安全配置建议.
### 案例二:本地应用迁移策略评估

某企业评估本地数据中心 5 个应用的迁移方式.
**评估结果**:
- 应用 A(标准化 Web 应用):Rehost 直接迁移到 EC2
- 应用 B(需要弹性扩展):Replatform 到容器服务
- 应用 C(有成熟 SaaS 替代):Repurchase 替换为 SaaS
- 应用 D(深度耦合本地系统):Retain 暂保留
- 应用 E(已无人使用):Retire 下线

**输出**:迁移优先级排序、目标云服务选型、基础迁移步骤.
## 异常处理

### 服务选型产生冲突
原因:多个云服务均能满足需求,难以抉择.
处理:从延迟敏感度、运维成本、计费模式三个维度对比;无状态短任务选 Lambda,长驻服务选 EC2 或容器服务;输出简要选型对比.
### 迁移后性能下降
原因:实例规格不匹配或未充分压测.
处理:使用压测工具验证目标实例性能;检查实例规格是否过小;确认数据库索引与连接池配置;必要时回滚后重新评估.
### 成本超出预期
原因:未及时释放资源或未使用预留折扣.
处理:清理未挂载的存储卷与闲置资源;评估 Reserved Instances 覆盖稳定负载;检查网络连接和配置后重试;设置预算告警.
### IAM 权限配置不当
原因:权限过大或角色信任策略配置错误.
处理:收紧到最小权限;按职能划分角色;启用审计日志;定期审查权限分配.
### IaC 状态漂移
原因:控制台手动修改了 IaC 管理的资源.
处理:禁止控制台手动变更;对漂移资源先 import 再对齐;启用定期 plan 巡检.
## 常见问题

### Q1: 如何在 AWS、Azure、GCP 之间选择?
从区域覆盖、服务成熟度、成本模型、团队技能四个维度评估。建议核心工作负载选定主力云,避免初期就引入多云复杂度。先选定一个云平台深耕,后续按需扩展.
### Q2: 6Rs 迁移框架怎么用?
逐个应用评估:标准化程度高的直接 Rehost 快速上云;希望获得云红利但不想重构的 Replatform;有 SaaS 替代品的 Repurchase;需要弹性的 Refactor;深度耦合的 Retain;无用的 Retire.
### Q3: 如何估算云成本?
使用云厂商定价计算器输入实例规格、存储容量与流量预估,输出月度成本。注意区分按需与 Reserved 计费模式,并估算网络出口流量费用.
### Q4: 什么是基础设施即代码?
使用 Terraform、CloudFormation 等工具以代码形式定义云资源,实现可重复部署、版本管理与团队协作。避免控制台手动创建资源导致的不可追溯与漂移问题.
## 代码示例

### Terraform: AWS 基础架构(VPC + EC2 + RDS)

```hcl
# main.tf - AWS 单云基础架构
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
# ...
provider "aws" {
  region = "ap-northeast-1"
}
# ...
# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "main-vpc"
  }
}
# ...
# 公有子网
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "ap-northeast-1a"
  map_public_ip_on_launch = true
  tags = { Name = "public-subnet-1a" }
}
# ...
# 私有子网(数据库层)
resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.11.0/24"
  availability_zone = "ap-northeast-1a"
  tags = { Name = "private-subnet-1a" }
}
# ...
# 互联网网关
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
}
# ...
# EC2 Web 服务器
resource "aws_instance" "web" {
  ami                    = "ami-0c7217cdde317cfec"
  instance_type          = "t3.small"
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.web.id]
  key_name               = "prod-key"
# ...
  user_data = <<-EOF
    #!/bin/bash
    yum install -y httpd
    systemctl enable httpd
    systemctl start httpd
  EOF
# ...
  tags = { Name = "web-server" }
}
# ...
# 安全组: 仅允许 HTTP/SSH
resource "aws_security_group" "web" {
  name        = "web-sg"
  vpc_id      = aws_vpc.main.id
# ...
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
# ...
# RDS PostgreSQL
resource "aws_db_instance" "db" {
  engine               = "postgres"
  engine_version       = "15.4"
  instance_class       = "db.t3.micro"
  allocated_storage    = 20
  storage_encrypted    = true
  db_name              = "appdb"
  username             = "dbadmin"
  password             = var.db_password
  publicly_accessible  = false
  skip_final_snapshot  = true
}
```

### AWS CLI: 成本查询与资源 Right-sizing

```bash
# 查询过去 30 天 EC2 按需实例成本
aws ce get-cost-and-usage \
  --time-period Start=2026-06-22,End=2026-07-22 \
  --granularity MONTHLY \
  --metrics "UnblendedCost" \
  --group-by Type=DIMENSION,Key=SERVICE Type=DIMENSION,Key=INSTANCE_TYPE
# ...
# 列出所有运行中的 EC2 实例及其实例类型
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,Tags[?Key==`Name`].Value | [0]]' \
  --output table
# ...
# 查找 CPU 利用率低于 10% 的实例(Right-sizing 候选)
for instance_id in $(aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query 'Reservations[*].Instances[*].InstanceId' \
  --output text); do
  avg_cpu=$(aws cloudwatch get-metric-statistics \
    --namespace AWS/EC2 \
    --metric-name CPUUtilization \
    --dimensions Name=InstanceId,Value=$instance_id \
    --start-time $(date -u -v-7d +%Y-%m-%dT%H:%M:%S 2>/dev/null || date -u -d '7 days ago' +%Y-%m-%dT%H:%M:%S) \
    --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
    --period 86400 \
    --statistics Average \
    --query 'Datapoints[*].Average' \
    --output text | awk '{s+=$1} END {print s/NR}')
  echo "Instance: $instance_id | Avg CPU(7d): ${avg_cpu}%"
done
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 不直接访问用户云账号,资源清单与成本数据需用户提供
- 成本估算基于公开定价,实际账单以云厂商结算为准
- 架构建议需结合具体业务场景验证后落地
- 不替代专业云架构师的人工评审
- 仅覆盖基础架构设计,不包含多云灾备与深度 FinOps

## 升级提示

当前为免费版本,提供单云架构设计、6Rs 迁移框架与基础成本优化等核心功能。升级至付费版本可解锁以下能力:

- 多云与混合云架构设计,跨云拓扑与网络互通
- 迁移波次规划、依赖梳理与割接方案
- 深度成本优化(FinOps、Spot 实例、成本分配标签、预算告警)
- 高可用与灾备设计(RTO/RPO 规划、故障转移、灾备演练)
- 安全与合规落地(零信任、身份联邦、SOC2/HIPAA/PCI-DSS 映射)
- Landing Zone 与多账号治理
- 完整架构输出模板与详细异常处理

如需多云灾备、深度成本优化、合规架构设计等进阶能力,请使用 `cloud-architect` 付费版本.