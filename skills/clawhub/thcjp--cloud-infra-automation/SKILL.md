---
slug: cloud-infra-automation
name: cloud-infra-automation
version: "1.0.0"
displayName: Cloud Infra Automation
summary: Automate provisioning and management of AWS, GCP, and Azure infrastructure
  using Terraform, Ansib...
license: MIT
description: |-
  Automate provisioning and management of AWS, GCP, and Azure infrastructure
  using Terraform, Ansib...

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: cloud, azure, automation, infra, infrastructure, management, provisioning,
  automate
tags:
- Automation
tools:
- read
- exec
---

# Cloud Infra Automation

Automate cloud infrastructure with IaC.

## Features

### Multi-Cloud Support

* AWS
* Google Cloud Platform
* Azure

### Infrastructure as Code

* Terraform templates
* Ansible playbooks
* CloudFormation

### Automation

* Server provisioning
* Configuration management
* Deployment pipelines

## Quick Start

```bash
./cloud.sh init aws

./cloud.sh apply prod

./cloud.sh destroy prod
```

## Templates

* Web application
* Database setup
* Kubernetes cluster
* Serverless functions

## Requirements

* Terraform
* Ansible
* AWS/GCP/Azure CLI

## Author

Sunshine-del-ux

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
