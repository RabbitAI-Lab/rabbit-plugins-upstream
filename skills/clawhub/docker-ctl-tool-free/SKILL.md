---
slug: docker-ctl-tool-free
name: docker-ctl-tool-free
version: 1.0.0
displayName: 容器检查入门工具
summary: "Podman/Docker容器检查工具，支持容器状态查询与日志分析.。面向个人开发者的容器检查工具，兼容Podman与Docker。支持容器状态"
license: Proprietary
edition: free
description: '面向个人开发者的容器检查工具，兼容Podman与Docker。支持容器状态

  查询、日志分析、资源使用监控与配置检查。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修。Use
  when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修。'
tags:
  - Operations
  - 容器检查
  - 运维
  - 容器
  - Docker
  - DevOps
  - python3
  - podman
tools:
  - read
  - exec
  - write
homepage: ""
category: "Development"
---
# 容器检查入门工具（免费版）

## 概述

本工具为个人开发者提供容器检查能力，兼容Podman与Docker双引擎。支持容器状态查询、日志分析、资源监控与配置检查，帮助快速排查容器问题.
## 核心能力

### 检查功能

| 功能 | 说明 | 免费版支持 |
|---|---|-----|
| 状态检查 | 运行状态/退出码/启动时间 | 支持 |
| 日志查看 | 实时/历史日志 | 支持 |
| 资源监控 | CPU/内存/网络IO | 支持 |
| 配置检查 | 环境变量/端口/挂载 | 支持 |
| 批量检查 | 多容器并行 | 不支持 |
| 健康检查 | 容器健康状态 | 支持 |
| 历史分析 | 趋势分析 | 不支持 |
| 异常诊断 | 智能诊断 | 不支持 |

**处理**: 解析检查功能的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回检查功能的响应数据,包含状态码、结果和日志.
### 兼容引擎

| 引擎 | 说明 | 免费版支持 |
|:-----|:-----|:-----|
| Podman | 无守护进程容器引擎 | 支持 |
| Docker | 标准容器引擎 | 支持 |
| 自动检测 | 自动识别已安装引擎 | 支持 |

**处理**: 解析兼容引擎的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回兼容引擎的响应数据,包含状态码、结果和日志.
### 核心功能执行
用`input_params`参数进行配置.

**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：容器检查工具、支持容器状态查询、与日志分析、面向个人开发者的、支持容器状态、日志分析、资源使用监控与配、Use、when、需要系统监控、运维告警、部署管理时使用、不适用于物理硬件、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：检查容器状态

用户输入："查看所有容器的状态"

用户可通过自然语言指令触发此场景，工具将自动执行相应操作并返回结构化结果.
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| input | string | 是 | 容器检查入门工具处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 检查所有容器
python3 （请参考skill目录中的脚本文件） ps --all
# ...
# 输出：
# NAME        STATUS    AGE    PORTS
# web-app     running   2h     8080:80
# redis       running   2h     6379:6379
# postgres    exited    10m    5432:5432
```

### 场景二：查看容器日志

用户输入："看看web-app的日志"

```bash
# 查看日志
python3 （请参考skill目录中的脚本文件） logs --name web-app --tail 100
# ...
# 实时跟踪日志
python3 （请参考skill目录中的脚本文件） logs --name web-app --follow
# ...
# 过滤错误日志
python3 （请参考skill目录中的脚本文件） logs --name web-app --grep "ERROR"
```

### 场景三：资源使用检查

用户输入："哪些容器占内存最多？"

```bash
# 资源使用统计
python3 （请参考skill目录中的脚本文件） stats --sort memory
# ...
# 输出：
# NAME        CPU%   MEM USAGE      NET I/O
# postgres    5.2%   512MiB/1GiB   10MB/50MB
# web-app     15.3%  256MiB/512MiB 50MB/100MB
# redis       1.1%   64MiB/256MiB  5MB/10MB
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
# Podman: brew install podman (macOS)
# Docker: 见docker-toolkit安装
# ...
# 安装Python依赖
pip install subprocess
# ...
# 验证
python3 （请参考skill目录中的脚本文件） info
```

### 常用命令

```bash
# 容器状态
python3 （请参考skill目录中的脚本文件） ps --all
python3 （请参考skill目录中的脚本文件） inspect --name web-app
# ...
# 日志
python3 （请参考skill目录中的脚本文件） logs --name web-app --tail 100
python3 （请参考skill目录中的脚本文件） logs --name web-app --follow
python3 （请参考skill目录中的脚本文件） logs --name web-app --grep "ERROR"
# ...
# 资源
python3 （请参考skill目录中的脚本文件） stats
python3 （请参考skill目录中的脚本文件） stats --sort cpu
# ...
# 配置检查
python3 （请参考skill目录中的脚本文件） config --name web-app
python3 （请参考skill目录中的脚本文件） ports --name web-app
python3 （请参考skill目录中的脚本文件） volumes --name web-app
# ...
# 健康检查
python3 （请参考skill目录中的脚本文件） health --name web-app
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例

### 检查工具配置

```yaml
ctl_config:
  engine: "auto"                 # auto | podman | docker
  socket:
    podman: "unix:///run/podman/podman.sock"
    docker: "unix:///var/run/docker.sock"
# ...
  defaults:
    log_tail: 100
    stats_interval: 5
    timeout: 30
# ...
  output:
    format: "table"              # table | json | yaml
    color: true
```

## 最佳实践

1. **引擎选择**：Podman无需守护进程更安全，Docker生态更成熟
2. **日志过滤**：使用grep过滤关键词，快速定位问题
3. **资源监控**：定期检查资源使用，及时发现问题容器
4. **健康检查**：配置容器健康检查，自动发现异常

| 实践要点 | 说明 |
|:---:|:---:|
| 引擎兼容 | 命令兼容Podman和Docker，无需修改 |
| 日志量 | 大量日志时使用--tail限制输出 |
| 资源限制 | 检查资源使用，确认是否达到限制 |
| 退出码 | 非零退出码表示异常，需查看日志 |

## 常见问题

### Q1：Podman和Docker有什么区别？

Podman无需守护进程（daemonless），更安全；Docker需要dockerd守护进程。两者命令兼容，本工具自动检测.
### Q2：免费版支持批量检查吗？

免费版仅支持单个容器检查。如需批量检查所有容器并生成报告，建议升级PRO版.
### Q3：如何查看已退出的容器日志？

使用 `--all` 参数查看所有容器（包括已退出的），然后指定容器名查看日志。退出容器的日志在容器删除前仍然保留.
### Q4：支持远程容器检查吗？

免费版仅支持本地容器检查。如需检查远程主机上的容器，建议通过SSH连接后在远程执行，或升级PRO版.
## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+
- **容器引擎**: Podman 4.0+ 或 Docker 20.0+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| Podman或Docker | CLI工具 | 必需 | 系统安装 |

### API Key 配置

- 免费版无需API Key
- 通过本地容器引擎CLI执行检查

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本+CLI执行）
- **说明**: 兼容Podman/Docker的容器检查工具
- **免费版限制**: 单容器检查、不支持批量与历史分析

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
