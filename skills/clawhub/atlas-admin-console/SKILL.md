---
slug: "atlas-admin-console"
name: "atlas-admin-console"
version: 1.0.1
displayName: "Atlas管理台专业版"
summary: "MongoDB Atlas全功能管理控制台，含批量API调用、结果导出、历史回放、多API编排与监控告警自动化。"
license: "Proprietary"
edition: "pro"
description: |-
  面向MongoDB Atlas运维团队的企业级全功能管理控制台。在免费版基础上新增批量API调用与并发执行、调用结果导出（CSV/JSON）、调用历史记录与回放、多API编排（工作流）、监控告警自动化、Terraform集成、多项目统一管理等高级能力，配套面向DBA、SRE、平台工程的多角色场景指南
tags:
  - 集成工具
  - MongoDB
  - 云数据库
  - 企业级
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# Atlas管理台专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Atlas管理台专业版Atlas全功能管理 | 不支持 | 支持 |
| Atlas管理台专业版结果导出 | 不支持 | 支持 |
| Atlas管理台专业版多API编排与监控 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |

## 核心能力

| 能力分类 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| API调用 | 单次串行 | 批量并发（多线程） |
| 结果导出 | 无 | CSV/JSON/Excel导出 |
| 历史记录 | 无 | 调用历史+回放 |
| 工作流编排 | 无 | 多API串联+条件分支 |
| 监控告警 | 手动查询 | 自动响应+自愈 |
| Terraform | 无 | 官方Provider集成 |
| 多项目管理 | 单项目 | 跨组织/项目统一视图 |
| 审计日志 | 无 | 完整操作审计 |
| 优先支持 | 社区 | 工单优先响应 |
### 能力分类

针对能力分类,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力分类相关的配置参数、输入数据和处理选项.
**输出**: 返回能力分类的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力分类`的配置文档进行参数调优
### API调用

针对API调用,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供API调用相关的配置参数、输入数据和处理选项.
**输出**: 返回API调用的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`API调用`的配置文档进行参数调优
### 结果导出

针对结果,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供结果导出相关的配置参数、输入数据和处理选项.
**输出**: 返回结果导出的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`结果导出`的配置文档进行参数调优
#
## 适用场景

### 场景一：批量集群巡检（DBA视角）

每日对全部集群执行健康检查，输出CSV报告.
```bash
# 批量查询所有集群状态并导出CSV
atlas-pro batch \
  --operation listClusters \
  --groups "group1,group2,group3" \
  --output cluster-health-$(date +%Y%m%d).csv \
  --format csv \
  --parallel 5
# ...
# 批量检查备份状态
atlas-pro batch \
  --operation listSnapshots \
  --groups "group1,group2,group3" \
  --output backup-status.csv \
  --filter "createdAt > now-24h"
```

### 场景二：监控告警自动响应（SRE视角）

CPU使用率超80%自动扩容节点规格.
```yaml
# alert-rules.yml
rules:
  - name: auto-scale-on-high-cpu
    condition:
      metric: cpu_usage
      threshold: 80
      duration: 5m
    action:
      workflow: scale-up-cluster
      params:
        new_size: M30
    cooldown: 30m  # 防止频繁触发
```

### 场景三：Terraform基础设施管理（平台工程视角）

通过Terraform管理Atlas集群，所有变更走代码评审流程.
```hcl
# main.tf
terraform {
  required_providers {
    mongodbatlas = {
      source = "mongodb/mongodbatlas"
      version = "~> 1.0"
    }
  }
}
# ...
provider "mongodbatlas" {
  public_key  = var.atlas_public_key
  private_key = var.atlas_private_key
}
# ...
resource "mongodbatlas_cluster" "main" {
  project_id   = var.project_id
  name         = "production-cluster"
  cluster_type = "REPLICASET"
# ...
  replication_factor = 3
  provider_name      = "AWS"
  region_name        = "us-east-1"
  provider_instance_size_name = "M30"
# ...
  backup_enabled = true
  auto_scaling_disk_gb_enabled = true
}
```

### 场景四：多API编排工作流（自动化视角）

将多个API调用串联为工作流，支持条件分支与循环.
```yaml
# workflow: provision-new-cluster.yml
steps:
  - name: create-cluster
    operation: createCluster
    params:
      name: ""console_result""
      providerSettings:
        providerName: "AWS"
        instanceSizeName: "M10"
# ...
  - name: wait-for-ready
    operation: getCluster
    until: "status == 'IDLE'"
    timeout: 600s
    interval: 30s
# ...
  - name: create-db-user
    operation: createDatabaseUser
    depends_on: wait-for-ready
    params:
      username: ""console_metadata""
      password: ""console_status""
      roles: [{roleName: "readWrite", databaseName: "admin"}]
# ...
  - name: add-ip-to-whitelist
    operation: createProjectIpAddress
    params:
      cidrBlock: ""console_summary"/32"
```

## 使用流程

### 优秀步：配置多项目凭证

```bash
# 配置多个项目的API Key
cat > ~/.atlas-pro/credentials.yml <<EOF
profiles:
  production:
    client_id: "\${ATLAS_PROD_CLIENT_ID}"
    client_secret: "\${ATLAS_PROD_CLIENT_SECRET}"
    groups: ["prod-group-1", "prod-group-2"]
  staging:
    client_id: "\${ATLAS_STAGING_CLIENT_ID}"
    client_secret: "\${ATLAS_STAGING_CLIENT_SECRET}"
    groups: ["staging-group-1"]
EOF
```

### 第二步：执行首次批量巡检

```bash
atlas-pro batch \
  --operation listClusters \
  --profile all \
  --output daily-report.csv \
  --format csv
```

### 第三步：启用监控告警自动化

```bash
atlas-pro alert start --config alert-rules.yml
```

完整上手时间约180秒（含多项目配置）.
#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | atlas-admin-console处理的内容输入 |, 默认: 全部维度 |
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
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+
- **Terraform**: 1.0+（基础设施即代码管理需要）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Node.js | 运行时 | 必需 | nodejs.org 官方下载 |
| atlas-pro.mjs | 脚本 | 必需 | 随本Skill分发 |
| Terraform | IaC工具 | 可选 | terraform.io 官方下载 |
| mongodbatlas Terraform Provider | 插件 | 可选 | Terraform Registry自动获取 |
| AWS CLI | 命令行 | 可选 | aws.amazon.com（S3 state存储） |
| Prometheus | 监控 | 可选 | prometheus.io 官方下载 |

### API Key 配置
- **ATLAS_PROD_CLIENT_ID/SECRET**: 生产环境Atlas API凭证，通过环境变量注入
- **ATLAS_STAGING_CLIENT_ID/SECRET**: 测试环境Atlas API凭证，通过环境变量注入
- **ATLAS_PUBLIC_KEY/PRIVATE_KEY**: Terraform Provider使用的凭证，通过环境变量注入
- **ALERT_WEBHOOK_URL**: 告警Webhook地址，通过环境变量配置
- **DINGTALK_TOKEN**: 钉钉告警机器人Token，通过环境变量配置
- **AWS_ACCESS_KEY_ID/SECRET_ACCESS_KEY**: S3 state存储凭证，通过环境变量配置
- 所有凭证禁止硬编码在脚本或配置文件中，必须通过环境变量注入

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，

## 案例展示

### 批量调用配置

```yaml
# ~/.atlas-pro/batch.yml
batch:
  parallel: 5                    # 并发数
  retry: 3                       # 失败重试次数
  retry_interval: 5s             # 重试间隔
  rate_limit: 100                # 每分钟最大调用数
  timeout: 30s                   # 单次调用超时
  output:
    format: csv                  # csv/json/xlsx
    include_metadata: true       # 包含调用元数据
    split_by_group: false        # 是否按项目分文件
```

### 工作流编排

```yaml
# workflows/backup-and-restore-test.yml
name: backup-restore-test
description: 创建备份并验证可恢复性
steps:
  - id: create_snapshot
    operation: createSnapshot
    params:
      clusterName: ""console_details""
      description: "automated-test-"console_count""
# ...
  - id: wait_snapshot_complete
    operation: getSnapshot
    depends_on: create_snapshot
    until: "status == 'completed'"
    timeout: 1800s
# ...
  - id: restore_to_test_cluster
    operation: createRestoreJob
    depends_on: wait_snapshot_complete
    params:
      snapshotId: "按流程执行"
      targetClusterName: "test-cluster"
# ...
  - id: verify_restore
    operation: getCluster
    depends_on: restore_to_test_cluster
    until: "status == 'IDLE'"
    on_failure:
      alert: true
      message: "备份恢复测试失败"
```

### Terraform状态管理

```bash
# 初始化Terraform
terraform init
# ...
# 查看变更计划
terraform plan -out=tfplan
# ...
# 应用变更
terraform apply tfplan
# ...
# 销毁资源（谨慎）
terraform destroy -target=mongodbatlas_cluster.main
```

### 监控告警自动化

```yaml
# alert-rules.yml
rules:
  - name: high-cpu-auto-scale
    condition:
      metric: system.cpu.usage
      threshold: 80
      operator: ">"
      duration: 5m
    action:
      workflow: scale-up-cluster
    cooldown: 30m
    notify:
      - type: webhook
        url: "${ALERT_WEBHOOK_URL}"
      - type: dingtalk
        token: "${DINGTALK_TOKEN}"
# ...
  - name: disk-space-low
    condition:
      metric: disk.used_percent
      threshold: 90
      operator: ">"
      duration: 1m
    action:
      operation: modifyCluster
      params:
        diskSizeGB: "current * 1.5"
    cooldown: 1h
# ...
  - name: connection-pool-exhausted
    condition:
      metric: connections.current
      threshold: "max * 0.9"
      operator: ">"
      duration: 2m
    action:
      workflow: add-connection-pool
    cooldown: 15m
```

## 常见问题

### Q1：批量调用部分失败如何处理？

A：专业版默认重试3次，仍失败的记录在错误报告中。可通过`--resume`参数从断点继续，避免重复执行已成功的部分.
### Q2：工作流执行中断如何恢复？

A：专业版持久化工作流执行状态，使用`atlas-pro workflow resume <execution-id>`从断点恢复。若步骤已副作用（如集群已创建），恢复时会跳过该步骤.
### Q3：Terraform state冲突怎么办？

A：(1) 使用远程state存储（S3/OSS）配合state锁（DynamoDB）；(2) 团队协作时先`terraform state pull`再操作；(3) 冲突时通过`terraform state push`强制覆盖（谨慎使用）.
### Q4：告警自愈动作误触发怎么办？

A：(1) 设置合理的`cooldown`冷却期；(2) 增加`duration`持续时间要求，避免瞬时波动触发；(3) 关键动作（如销毁集群）配置`require_approval: true`人工确认；(4) 监控告警动作日志，发现异常立即停用规则.
### Q5：如何跨组织批量管理？

A：在`credentials.yml`中配置多个profile，使用`--profile all`遍历所有配置的组织与项目。专业版支持跨组织统一视图，便于集团级管理.
### 错误恢复步骤
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

A：(1) 降低`parallel`并发数；(2) 降低`rate_limit`每分钟调用数；(3) 启用指数退避重试；(4) 大批量操作分批执行，间隔5-10分钟.
### Q7：Terraform变更如何回滚？

A：(1) 使用`terraform apply`前先`plan`并保存计划；(2) 变更出问题时`terraform apply`之前的state文件回滚；(3) 关键资源变更前备份state：`terraform state pull > backup.tfstate`.
### Q8：如何与现有CMDB集成？

A：(1) 批量导出集群信息为JSON，定时同步到CMDB；(2) 通过Webhook接收Atlas事件变更，实时更新CMDB；(3) 专业版提供REST API供CMDB主动查询.
## 错误处理

| 错误场景(续)(续)| 原因 | 处理方式 |
|:------------:|--------------|:-------------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 监控精度受限于系统采样频率
- 免费版不支持远程监控与多设备管理
