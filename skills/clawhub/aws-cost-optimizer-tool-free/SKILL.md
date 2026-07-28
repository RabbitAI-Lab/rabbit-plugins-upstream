---
slug: aws-cost-optimizer-tool-free
name: aws-cost-optimizer-tool-free
version: 1.0.0
displayName: AWS成本优化入门
summary: "AWS成本分析工具，支持支出概览与基础优化建议.。面向个人开发者与初创团队的AWS成本分析工具。支持月度支出概览、"
license: Proprietary
edition: free
description: '面向个人开发者与初创团队的AWS成本分析工具。支持月度支出概览、

  按服务/区域分解成本、识别闲置资源与基础优化建议。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。Use
  when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。'
tags:
  - Operations
  - AWS
  - 成本优化
  - 云财务
  - 云计算
  - DevOps
  - aws
  - python3
tools:
  - read
  - exec
  - write
homepage: ""
category: "Operations"
---
# AWS成本优化入门（免费版）

## 概述

本工具为个人开发者和初创团队提供AWS成本分析能力。支持月度支出概览、按服务和区域分解成本、识别闲置资源并提供基础优化建议，帮助用户控制AWS支出.
## 核心能力

### 分析功能

| 功能 | 说明 | 免费版支持 |
|---|---|-----|
| 成本概览 | 月度支出总览 | 支持 |
| 成本分解 | 按服务/区域 | 支持 |
| 趋势分析 | 月度趋势 | 支持 |
| 闲置资源 | 识别未使用资源 | 支持 |
| 优化建议 | 节省成本建议 | 基础建议 |
| 预算告警 | 超预算告警 | 不支持 |
| RI建议 | 预留实例建议 | 不支持 |
| 自动优化 | 自动执行优化 | 不支持 |

**处理**: 解析分析功能的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回分析功能的响应数据,包含状态码、结果和日志.
### 核心功能执行
用`input_params`参数进行配置.

**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.

**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：AWS、成本分析工具、支持支出概览与基、础优化建议、面向个人开发者与、初创团队的、支持月度支出概览、区域分解成本、识别闲置资源与基、Use、when、需要数据分析、报表生成、统计洞察、数据可视化时使用、不适用于实时流数、据处理、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：查看成本概览

用户输入："这个月AWS花了多少钱？"

```bash
# 月度成本概览
python3 （请参考skill目录中的脚本文件） summary --month 2026-07
# ...
# 输出：
# === AWS成本概览 2026年7月 ===
# 总支出: $1,250.50
# 环比上月: +$120.30 (+10.6%)
#
# 按服务分解:
# EC2:        $580.20 (46.4%)
# S3:         $220.50 (17.6%)
# RDS:        $180.00 (14.4%)
# CloudWatch: $95.30  (7.6%)
# 其他:       $174.50 (14.0%)
```

### 场景二：识别闲置资源

用户输入："有没有在浪费钱的资源？"

```bash
# 闲置资源检测
python3 （请参考skill目录中的脚本文件） idle-resources --scan
# ...
# 输出：
# === 闲置资源 ===
# 1. EC2实例 i-xxx (停止状态) - $0/月
# 2. EBS卷 vol-xxx (未挂载) - $40/月
# 3. EIP 1.2.3.4 (未关联) - $7.2/月
# 4. S3存储桶 old-backup (90天未访问) - $120/月
# 预计可节省: $167.2/月
```

### 场景三：优化建议

用户输入："怎么节省AWS成本？"

```bash
# 优化建议
python3 （请参考skill目录中的脚本文件） recommendations
# ...
# 输出：
# === 优化建议 ===
# 1. [高] 删除闲置EBS卷 - 节省$40/月
# 2. [高] 释放未关联EIP - 节省$7.2/月
# 3. [中] S3旧数据转Glacier - 节省$80/月
# 4. [中] EC2实例降配 - 节省$100/月
# 5. [低] 启用S3生命周期 - 节省$30/月
# 预计总节省: $257.2/月
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 环境准备

```bash
# 依赖说明
pip install boto3
# ...
# 配置AWS凭证
aws configure
# ...
# 分析成本
python3 （请参考skill目录中的脚本文件） summary --month 2026-07
```

### 常用命令

```bash
# 成本概览
python3 （请参考skill目录中的脚本文件） summary --month 2026-07
python3 （请参考skill目录中的脚本文件） trend --months 6
# ...
# 成本分解
python3 （请参考skill目录中的脚本文件） breakdown --by service
python3 （请参考skill目录中的脚本文件） breakdown --by region
# ...
# 闲置资源
python3 （请参考skill目录中的脚本文件） idle-resources --scan
# ...
# 优化建议
python3 （请参考skill目录中的脚本文件） recommendations
# ...
# 导出报告
python3 （请参考skill目录中的脚本文件） export --month 2026-07 --format csv --output cost_report.csv
```

## 示例

### 成本分析配置

```yaml
cost_config:
  aws:
    region: "us-east-1"
    profile: "default"
# ...
  analysis:
    currency: "USD"
    timezone: "Asia/Shanghai"
# ...
  idle_resources:
    ec2_stopped_days: 7         # 停止超过7天视为闲置
    ebs_unattached: true        # 未挂载EBS
    eip_unassociated: true      # 未关联EIP
    s3_inactive_days: 90        # 90天未访问
# ...
  recommendations:
    levels: ["high", "medium", "low"]
    min_savings: 5              # 最小节省金额（美元/月）
# ...
  export:
    formats: ["csv", "json"]
    output_dir: "./reports"
```

## 最佳实践

1. **定期检查**：每月初查看上月成本，及时发现问题
2. **闲置清理**：定期清理闲置资源，避免持续计费
3. **标签管理**：为资源打标签，便于成本归因
4. **预算控制**：设置心理预算线，超过时重点排查

| 实践要点 | 说明 |
|:-----|:-----|
| 停止vs删除 | 停止EC2仍收EBS费用，删除才完全免费 |
| S3生命周期 | 冷数据转Glacier/Deep Archive节省70%+ |
| EIP费用 | 未关联的EIP每小时收费，及时释放 |
| 免费层 | 关注免费层用量，超出后收费 |

## 常见问题

### Q1：免费版支持预算告警吗？

免费版不包含预算告警功能。如需超预算自动通知，建议升级PRO版或使用AWS Budgets.
### Q2：数据准确吗？

成本数据来自AWS Cost Explorer API，与AWS账单一致。可能有数小时延迟，月初数据可能不完整.
### Q3：支持多账户吗？

免费版仅支持单账户分析。如需分析多账户（组织）成本，建议升级PRO版.
### Q4：优化建议可以直接执行吗？

免费版仅提供建议，需手动在AWS控制台执行。如需一键执行优化，建议升级PRO版.
## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+
- **AWS CLI**: 已配置凭证

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| boto3 | Python库 | 必需 | `pip install boto3` |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:---:|:---:|:---:|:---:|
| AWS | `AWS_ACCESS_KEY_ID` | 必需 | API认证 |
| AWS | `AWS_SECRET_ACCESS_KEY` | 必需 | API认证 |
| AWS | `AWS_DEFAULT_REGION` | 必需 | 默认区域 |

- 需要开启AWS Cost Explorer服务（默认可能未启用）
- 建议使用只读权限的IAM用户

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 通过AWS Cost Explorer API分析成本
- **免费版限制**: 单账户、基础建议、不支持预算告警与自动优化

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 依赖云服务，需要网络连接
- 需要有效的云服务凭证和配置好的CLI环境
- 产生的云资源可能产生费用，使用前请确认计费方式
- 不同区域的服务可用性和功能支持可能存在差异
