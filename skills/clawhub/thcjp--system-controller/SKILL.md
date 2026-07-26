---
slug: system-controller
name: system-controller
version: "1.0.0"
displayName: 系统控制器
summary: 统一管理系统进程、服务、文件与环境配置，跨平台命令映射，带操作回滚。
license: MIT
description: |-
  系统控制器为 AI Agent 提供操作系统层面的统一控制能力，覆盖进程管理、服务启停、文件事务、环境变量、计划任务与系统信息采集。它把 Linux/macOS/Windows 三套差异巨大的命令抽象为统一语义，让 Agent 用同一套指令跨平台操作。

  核心能力：跨平台进程管理（查/启/停/杀）、系统服务控制、文件事务操作（带原子写入与回滚）、环境变量与持久配置、计划任务管理、系统资源监控、操作审计日志。

  适用场景：自动化运维、环境初始化、服务排障、批量配置、一人公司服务器管理、Agent 长驻守护。

  差异化：相比仅罗列命令的原始方案，本技能新增跨平台命令映射矩阵（同一语义自动翻译为对应平台命令）、文件事务回滚（写前快照，失败自动恢复）、进程安全终止梯度（SIGTERM→等待→SIGKILL）、操作审计日志（所有变更可追溯）、危险操作分级确认。明确聚焦"系统层"控制，不涉及 GUI 鼠标键盘（那是桌面自动驾驶技能的职责）。

  触发关键词：进程, 服务, 文件, 系统, 进程管理, 服务控制, 环境变量, 系统信息, process, service, file, system, control, manage
tags:
- 自动化
- 系统运维
- 跨平台控制
tools:
- read
- exec
---

# 系统控制器

让 AI Agent 用一套语义操控 Linux、macOS、Windows 三大系统。本技能解决五个核心痛点：**命令碎片化**（每平台命令不同）、**操作不可逆**（误删文件/杀错进程无法回滚）、**进程终止粗暴**（直接 SIGKILL 导致数据损坏）、**服务状态不同步**（systemctl 显示 active 但实际挂了）、**变更无审计**（出问题不知道谁改了什么）。

## 职责边界

本技能聚焦**系统层**操作，与桌面自动驾驶技能（GUI 鼠标键盘）明确区分：

| 本技能负责 | 桌面自动驾驶技能负责 |
|:-----------|:---------------------|
| 进程/服务管理 | 鼠标点击与移动 |
| 文件系统操作 | 键盘输入与快捷键 |
| 环境变量/注册表 | 屏幕截图与图像识别 |
| 计划任务（系统级） | 窗口管理（GUI 层） |
| 系统资源监控 | GUI 工作流编排 |

## 快速开始

### 统一命令入口

所有操作通过 `sysctl-cli` 统一入口，自动适配当前平台：

```bash
# 进程管理
sysctl-cli process list --filter "python"
sysctl-cli process kill 12345 --graceful

# 服务管理
sysctl-cli service status nginx
sysctl-cli service restart nginx

# 文件事务
sysctl-cli file write /etc/app.conf --content "..." --atomic

# 系统信息
sysctl-cli system info
sysctl-cli system resources
```

### 跨平台命令映射

Agent 只需表达"做什么"，由本技能翻译为平台命令：

| 语义操作 | Linux | macOS | Windows |
|:---------|:------|:------|:--------|
| 列出进程 | `ps aux` | `ps aux` | `tasklist` / `Get-Process` |
| 终止进程 | `kill` | `kill` | `taskkill` / `Stop-Process` |
| 服务状态 | `systemctl status` | `launchctl list` | `sc query` / `Get-Service` |
| 重启服务 | `systemctl restart` | `launchctl kickstart` | `sc stop; sc start` / `Restart-Service` |
| 环境变量 | `export` / `/etc/profile` | `export` / `~/.zshrc` | `setx` / 注册表 |
| 计划任务 | `crontab` | `crontab` / `launchd` | `schtasks` / Task Scheduler |

## 进程管理

### 列出与查找进程

```bash
sysctl-cli process list [options]
  --filter <pattern>     # 按名称/CMD过滤
  --user <user>          # 按用户过滤
  --show-cpu             # 显示CPU占用
  --sort <field>         # cpu/memory/pid
```

输出统一格式（跨平台一致）：

```
PID    NAME        USER    CPU%   MEM%   STATUS   STARTED
1234   python3     app     12.5   3.2    running  2026-07-18 08:00
1235   nginx       root    0.1    0.5    running  2026-07-18 07:55
```

### 安全终止梯度（防数据损坏）

直接 `kill -9` 是最常见的危险操作。本技能强制使用梯度终止：

```bash
sysctl-cli process kill <pid> [options]
  --graceful             # 默认：梯度终止（推荐）
  --timeout 10           # 梯度等待秒数（默认10）
  --force                # 跳过梯度，直接强杀（危险）
```

梯度终止流程：

1. **SIGTERM**（请求优雅退出）→ 等待 `timeout` 秒
2. 检查进程是否退出
3. 若仍存活 → **SIGINT** → 再等待 `timeout/2` 秒
4. 若仍存活 → 记录警告 → **SIGKILL**（强制）
5. 全程记录到审计日志

```bash
# 推荐：优雅终止
sysctl-cli process kill 12345 --graceful --timeout 15

# 危险：强制（需 --force 显式确认）
sysctl-cli process kill 12345 --force
```

### 批量进程操作

```bash
# 按名称批量终止（带确认）
sysctl-cli process kill-by-name "python*" --graceful --confirm

# 找出占用端口 8080 的进程
sysctl-cli process by-port 8080
```

## 服务管理

### 状态查询与一致性检查

```bash
sysctl-cli service status <name>
sysctl-cli service status <name> --deep   # 深度检查（实际探活）
```

`--deep` 解决"状态不同步"痛点：不仅看服务管理器报告，还实际探测端口/健康端点：

```bash
sysctl-cli service status nginx --deep
```

```
SERVICE: nginx
Reported: active (running) since 2026-07-18 07:55
Deep check:
  Port 80:      OK (HTTP 200)
  Port 443:     OK (HTTP 200)
  PID alive:    YES
Verdict: HEALTHY
```

若 Reported=active 但 Deep check 失败，输出 `Verdict: ZOMBIE`，建议 restart。

### 启停与重启

```bash
sysctl-cli service start <name>
sysctl-cli service stop <name> [--graceful-timeout 30]
sysctl-cli service restart <name>
sysctl-cli service enable <name>    # 开机自启
sysctl-cli service disable <name>
```

### 服务操作前置检查

重启/停止前自动检查：
- 是否有依赖该服务的其他运行中服务
- 是否有活跃连接（可选）
- prod 环境是否在维护窗口内

## 文件事务操作

### 原子写入（防部分写入）

```bash
sysctl-cli file write <path> --content "..." --atomic
sysctl-cli file write <path> --file source.txt --atomic
```

`--atomic` 流程：写入临时文件 → fsync → 原子 rename → 校验。中途断电/出错不会留下半截文件。

### 文件操作回滚（核心差异化）

```bash
sysctl-cli file edit <path> --backup        # 编辑前自动快照
# ... 后续操作 ...
sysctl-cli file rollback <path>             # 恢复到快照
```

回滚机制：
- 每次带 `--backup` 的操作前，复制原文件到 `~/.skill-platform/sysctl/snapshots/`
- 快照命名：`<原路径hash>.<时间戳>.bak`
- 保留最近 10 个快照，超出自动清理最旧的

```bash
# 危险操作示例：修改配置前先备份
sysctl-cli file edit /etc/nginx/nginx.conf --backup --content "..."
# 发现配置错误
sysctl-cli file rollback /etc/nginx/nginx.conf
sysctl-cli service reload nginx
```

### 文件批量操作

```bash
# 批量改权限（带 dry-run）
sysctl-cli file chmod /var/log/app/*.log 644 --dry-run
sysctl-cli file chmod /var/log/app/*.log 644 --confirm

# 批量查找大文件
sysctl-cli file find-large / --threshold 100M --limit 20
```

## 环境变量与持久配置

### 临时与持久环境变量

```bash
# 临时（仅当前会话）
sysctl-cli env set DEBUG=1

# 持久（写入配置文件，跨会话生效）
sysctl-cli env set JAVA_HOME=/usr/lib/jvm/java-17 --persist

# 列出当前环境变量
sysctl-cli env list --filter "JAVA"

# 删除持久变量
sysctl-cli env unset DEBUG --persist
```

`--persist` 自动选择对应平台的配置文件：
- Linux: `~/.bashrc` 或 `~/.profile`
- macOS: `~/.zshrc`
- Windows: 注册表 `HKCU\Environment`

### 系统级配置查询

```bash
# 查看系统信息
sysctl-cli system info
# 输出：OS, 内核版本, CPU, 内存, 磁盘, 运行时间

# 资源占用快照
sysctl-cli system resources
# 输出：CPU%, 内存使用, 磁盘IO, 网络IO, Top 5 进程

# 持续监控（5秒间隔）
sysctl-cli system monitor --interval 5 --duration 60
```

## 计划任务管理（系统级）

与定时调度技能（应用级 cron）不同，这里管理**系统级**计划任务：

```bash
# 列出系统计划任务
sysctl-cli cron list

# 添加（统一格式，自动翻译为平台命令）
sysctl-cli cron add --name "backup" --schedule "0 2 * * *" --command "/opt/backup.sh"

# 删除
sysctl-cli cron remove "backup"

# 查看 cron 日志
sysctl-cli cron logs "backup" --since 24h
```

## 操作审计日志

所有通过本技能执行的操作自动记录到审计日志：

```
日志位置: ~/.skill-platform/sysctl/audit.log
格式: <时间> | <操作类型> | <目标> | <结果> | <详情>
```

```
2026-07-18T09:00:00Z | process.kill | PID 12345 | SUCCESS | graceful, 8s
2026-07-18T09:05:00Z | service.restart | nginx | SUCCESS | 1.2s
2026-07-18T09:10:00Z | file.write | /etc/app.conf | SUCCESS | atomic, backup created
2026-07-18T09:15:00Z | file.rollback | /etc/app.conf | SUCCESS | restored from snapshot
```

查询审计：

```bash
sysctl-cli audit query --since 24h --type process
sysctl-cli audit query --target nginx
```

## 危险操作分级

| 等级 | 操作 | 要求 |
|:-----|:-----|:-----|
| L1 安全 | 查询、列出、监控 | 直接执行 |
| L2 谨慎 | 重启服务、修改配置（带备份） | 记录审计，Agent 自行执行 |
| L3 危险 | 强杀进程、删除文件、改权限 | 需 `--confirm` 显式确认 |
| L4 高危 | 批量删除、格式化、改系统服务 | 需 `--confirm` 且记录快照 |

Agent 应在执行 L3/L4 前向用户说明影响并等待确认。

## 场景化指南

### 场景 A：服务排障

```bash
# 1. 服务状态
sysctl-cli service status mysql --deep
# 发现 ZOMBIE 状态
# 2. 查看进程
sysctl-cli process list --filter mysql
# 3. 查看资源
sysctl-cli system resources
# 4. 优雅重启
sysctl-cli service restart mysql
# 5. 验证
sysctl-cli service status mysql --deep
```

### 场景 B：环境初始化

```bash
# 设置开发环境变量
sysctl-cli env set JAVA_HOME=/usr/lib/jvm/java-17 --persist
sysctl-cli env set MAVEN_HOME=/opt/maven --persist
sysctl-cli env set PATH=$PATH:$JAVA_HOME/bin:$MAVEN_HOME/bin --persist
# 验证
sysctl-cli env list --filter "JAVA\|MAVEN"
```

### 场景 C：配置修改与回滚

```bash
# 修改前备份
sysctl-cli file edit /etc/redis/redis.conf --backup \
  --replace "maxmemory 1gb" "maxmemory 2gb"
# 重启生效
sysctl-cli service restart redis
# 发现问题，回滚
sysctl-cli file rollback /etc/redis/redis.conf
sysctl-cli service restart redis
# 查看审计
sysctl-cli audit query --target redis --since 1h
```

### 场景 D：批量清理僵尸进程

```bash
# 找出僵尸进程
sysctl-cli process list --status zombie
# 优雅清理（按梯度终止父进程）
sysctl-cli process kill-by-name "defunct*" --graceful --confirm
```

## FAQ

**Q：Windows 上 PowerShell 命令和 Linux 差太多怎么办？**
A：本技能的统一入口已做映射。Agent 调用 `sysctl-cli` 语义命令即可，无需关心底层是 `tasklist` 还是 `Get-Process`。若必须用原生命令，参考跨平台映射表。

**Q：rollback 能恢复已删除的文件吗？**
A：不能。rollback 只能恢复"带 --backup 修改过"的文件。删除操作建议用 `file move` 到临时目录代替 `file delete`，保留恢复余地。

**Q：强杀进程为什么默认禁用？**
A：SIGKILL 不给进程清理机会，可能导致数据库损坏、临时文件残留。梯度终止（SIGTERM→等待→SIGKILL）几乎总能达到同样效果且更安全。`--force` 需显式传入。

**Q：审计日志会占满磁盘吗？**
A：日志按大小轮转，默认上限 50MB，保留 3 个历史文件。可通过 `sysctl-cli config audit-max-size` 调整。

**Q：如何限制 Agent 的操作权限？**
A：通过 `~/.skill-platform/sysctl/policy.json` 配置允许/禁止的操作类型。例如禁止 L4 操作：

```json
{"deny_levels": ["L4"], "deny_commands": ["file.delete"]}
```

## 故障排查

| 症状 | 可能原因 | 处置 |
|:-----|:---------|:-----|
| `Permission denied` | 权限不足 | 使用 sudo 或以对应用户运行 |
| 服务 `active` 但实际无响应 | 状态不同步 | 用 `--deep` 检查，restart |
| 进程 kill 后 PID 复用 | 系统正常行为 | 用 PID 时即时操作，不要缓存 PID |
| `file write` 失败但原文件变了 | 非 atomic 模式中断 | 用 `--atomic`；从 snapshot 恢复 |
| Windows 上 `sc query` 找不到服务 | 服务名与显示名不同 | 用 `sysctl-cli service list` 查实际服务名 |
| cron 任务不执行 | 跨平台调度差异 | 检查 `sysctl-cli cron logs`，确认 schedule 语法 |

## 性能优化

1. **批量查询**：`process list` 一次获取全量，避免循环单查。
2. **快照清理**：定期 `sysctl-cli snapshot purge --older 7d` 清理旧快照。
3. **审计异步**：审计日志默认同步写，可配置 `audit-async=true` 改异步提升性能。
4. **缓存系统信息**：`system info` 结果可缓存 60 秒，避免频繁采集。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent
- **操作系统**：Linux / macOS / Windows（需 PowerShell 5+）
- **Shell**：bash 4+（Linux/macOS）/ PowerShell 5+（Windows）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3 | 运行时 | 必需 | 系统自带或 python.org 下载 |
| psutil | Python 包 | 推荐 | `pip install psutil`（增强进程/资源查询） |
| jq | CLI | 可选（日志解析） | 包管理器安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本技能为本地系统操作，无需外部 API Key。
- 执行特权操作需对应的系统权限（sudo / 管理员）。

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令 + 跨平台命令执行）
- **说明**：Agent 通过统一语义指令驱动系统操作，本技能负责命令映射、安全梯度与审计记录。
