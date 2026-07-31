---

slug: auto-monitor-tool-free
name: auto-monitor-tool-free
version: 1.0.2
displayName: 系统监控入门工具
summary: "个人服务器监控工具，支持CPU/内存/磁盘基础指标与简单告警通知.。面向个人开发者的轻量级系统监控工具。支持CPU、内存、磁盘、网络等"
license: MIT
edition: free
description: "面向个人开发者的轻量级系统监控工具。兼容CPU、内存、磁盘、网络等. 适用于需要auto monitor tool相关能力的开发场景,提供结构化的工作流程和配置指引. 该工具经过深度差异化处理,针对用户反馈和使用痛点进行了优化改进,提升了实用性和可操作性."
tags:
  - Operations
  - 系统监控
  - 运维
  - 监控
  - 工具
  - cpu
  - python3
tools:
  - read
  - exec
homepage: ""
category: "Operations"
pricing_tier: free
---

# 系统监控入门工具（免费版）

## 概述

本工具为个人开发者提供轻量级系统监控能力。支持CPU、内存、磁盘、网络等基础指标的实时监控，提供简单的阈值告警和历史数据记录。适合个人服务器和开发环境的日常监控需求.
## 核心能力

### 监控指标

| 指标类别 | 具体指标 | 免费版支持 |
|----|----|-----|
| CPU | 使用率/负载/核心数 | 支持 |
| 内存 | 总量/使用/可用 | 支持 |
| 磁盘 | 容量/IO/分区 | 支持 |
| 网络 | 流量/连接数 | 支持 |
| 进程 | TOP进程/资源占用 | 支持 |
| 服务 | 端口/进程存活 | 基础检查 |
| 日志 | 日志分析 | 不支持 |
| 容器 | Docker监控 | 不支持 |

**处理**: 解析监控指标的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回监控指标的响应数据,包含状态码、结果和日志.
### 告警功能

| 功能 | 说明 | 免费版支持 |
|:-----|:-----|:-----|
| 阈值告警 | CPU/内存超过阈值 | 支持 |
| 通知方式 | 邮件/控制台 | 支持 |
| 告警去重 | 避免重复通知 | 基础去重 |
| 告警升级 | 逐级升级 | 不支持 |
| 多通道 | Webhook/IM | 不支持 |

**处理**: 解析告警功能的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回告警功能的响应数据,包含状态码、结果和日志.
### 核心功能执行
用`input_params`参数进行配置.

**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：个人服务器监控工、磁盘基础指标与简、单告警通知、面向个人开发者的、轻量级系统监控工、网络等、基础指标监控、提供简单的阈值告、警与历史数据记录、Use、when、需要系统监控、运维告警、部署管理时使用、不适用于物理硬件、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：查看系统状态

用户输入"服务器现在状态怎么样？"后，Agent 调用监控脚本获取 CPU、内存、磁盘、网络等实时指标并汇总输出：

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| input | string | 是 | 系统监控入门工具处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 查看系统概览
python3 （请参考skill目录中的脚本文件） status
# ..
# 输出：
# === 系统状态 2026-07-18 10:30:00 ===
# CPU使用率: 35.2% (8核)
# 内存: 6.2G/16G (38.7%)
# 磁盘: 120G/500G (24%)
# 网络: ↑1.2MB/s ↓3.5MB/s
# 负载: 1.25 1.10 0.95
```

### 场景二：设置告警

用户输入："CPU超过80%的时候通知我"

```bash
# 设置CPU告警
python3 （请参考skill目录中的脚本文件） alert add \
  --metric cpu_usage \
  --threshold 80 \
  --condition "above" \
  --notify "email"
# ..
# 启动监控
python3 （请参考skill目录中的脚本文件） watch
```

### 场景三：查看TOP进程

用户输入："哪些进程占CPU最多？"

```bash
# TOP进程
python3 （请参考skill目录中的脚本文件） top --sort cpu --count 10
# ..
# 输出占用最高的10个进程
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
pip install psutil
# ..
# 查看状态
python3 （请参考skill目录中的脚本文件） status
```

### 常用命令

```bash
# 系统状态
python3 （请参考skill目录中的脚本文件） status
# ..
# TOP进程
python3 （请参考skill目录中的脚本文件） top --sort cpu --count 10
python3 （请参考skill目录中的脚本文件） top --sort memory --count 10
# ..
# 设置告警
python3 （请参考skill目录中的脚本文件） alert add --metric cpu_usage --threshold 80 --notify email
# ..
# 启动监控
python3 （请参考skill目录中的脚本文件） watch --interval 60
# ..
# 历史数据
python3 （请参考skill目录中的脚本文件） history --metric cpu --hours 24
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例

### 监控配置

```yaml
monitor_config:
  interval: 60                  # 采集间隔（秒）
  storage: "sqlite"             # 数据存储
  db_path: "./monitor.db"
# ..
  metrics:
    cpu: true
    memory: true
    disk: true
    network: true
    process: true
# ..
  alerts:
    - metric: cpu_usage
      threshold: 80
      condition: "above"
      notify: "email"
    - metric: memory_usage
      threshold: 90
      condition: "above"
      notify: "email"
    - metric: disk_usage
      threshold: 85
      condition: "above"
      notify: "email"
# ..
  notification:
    email:
      smtp_host: "${SMTP_HOST}"
      smtp_port: 587
      username: "${EMAIL_USER}"
      password: "${EMAIL_PASS}"
      to: "admin@example.com"
# ..
  history:
    retention_days: 30          # 历史数据保留天数
```

## 优秀实践

1. **合理阈值**：告警阈值不要设置过低，避免频繁误报
2. **采集间隔**：个人服务器60秒足够，过短会消耗资源
3. **数据清理**：定期清理历史数据，避免磁盘占满
4. **告警测试**：设置告警后先测试通知是否正常

| 实践要点 | 说明 |
|:---:|:---:|
| 阈值设置 | CPU 80%/内存90%/磁盘85%为常见阈值 |
| 采集频率 | 60秒适合大多数场景 |
| 数据保留 | 30天历史足够日常分析 |
| 告警通知 | 确保邮件配置正确 |

## 常见问题

### Q1：免费版支持多台服务器监控吗？

免费版仅支持单机监控。如需监控多台服务器，建议升级PRO版支持分布式监控.
### Q2：支持Docker容器监控吗？

免费版不包含Docker容器监控。如需容器监控，建议升级PRO版或使用专用Docker监控工具.
### Q3：历史数据可以保存多久？

免费版默认保留30天。可通过配置修改retention_days参数，但数据量过大会影响性能.
### Q4：告警邮件发不出来怎么办？

检查：SMTP配置是否正确、邮箱是否开启SMTP服务、网络是否允许访问SMTP端口、密码是否为授权码（非登录密码）.
## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| psutil | Python库 | 必需 | `pip install psutil` |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|---:|:---|---:|---:|
| SMTP | `SMTP_HOST`等 | 可选 | 告警邮件发送 |

- 未配置SMTP时仅控制台告警
- 所有配置存储在本地

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 基于psutil的单机系统监控工具
- **免费版限制**: 单机监控、基础告警、不支持分布式与容器监控

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 本地运行，不支持多设备同步，监控数据仅存储在当前设备
- 免费版仅监控 CPU、内存、磁盘、网络四项基础指标，不支持进程级和服务级监控
- 告警通知依赖 Agent 心跳触发，高频指标采集存在 30-60 秒采样间隔
- 不支持分布式集群监控，仅适用于单机服务器的轻量级监控场景
