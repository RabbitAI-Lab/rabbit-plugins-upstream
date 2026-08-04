---
name: server-health
description: Comprehensive server health monitoring showing system stats, top processes, OpenClaw gateway status, and running services. Perfect for quick health checks via Telegram or CLI.
---

# Server Health Skill

Quick server monitoring with system stats, processes, OpenClaw gateway info, and services.

## Usage

**Standard view:**
```bash
./server-health.sh
```

**Verbose (includes temp, network, swap, I/O):**
```bash
./server-health.sh --verbose
```

**JSON output (for automation):**
```bash
./server-health.sh --json
```

**Alerts only (warnings/errors):**
```bash
./server-health.sh --alerts
```

## What It Shows

### 🔴 Always
- System stats (CPU, RAM, Disk, Uptime)
- Top 3-5 processes by CPU/RAM
- OpenClaw Gateway status & config
- Running services (Docker, PostgreSQL, etc.)

### 🟡 Conditional
- Alerts (disk >90%, RAM >80%, CPU >90%)
- Swap usage (if in use)

### 🟢 Verbose only
- Temperature (if sensors available)
- Network traffic
- Disk I/O
- Detailed service info

## Example Output

```
🖥️ SERVER HEALTH
━━━━━━━━━━━━━━━━━━━━

💻 SYSTEM
CPU: ████░░░░░░ 42% (Load: 1.2, 0.8, 0.5)
RAM: ██████░░░░ 1.4GB/8GB (18%)
DISK: ████░░░░░░ 45GB/100GB (45%)
UP: ⏱️ 5d 3h

🔄 TOP PROCESSES
node         35%    450MB
postgres     12%    280MB
openclaw      8%    180MB

⚡ OPENCLAW GATEWAY
Status: ✅ Running (PID: 1639125)
Uptime: 2d 5h | Port: 18789 | v2026.2.6-3

🤖 MODEL CONFIG
Primary: claude-sonnet-4-5
Context: 43k/128k (33%) | 574↓ 182↑ tokens
Fallbacks: glm-4.7 → copilot-sonnet → opus-4-5

📊 SESSIONS
Active: 3 | Heartbeat: 30m | Last: 1m ago

🐳 SERVICES
Docker: ✅ 3 containers
PostgreSQL: ✅ Running
```

## ⚖️ 权限声明

| 权限 | 范围 | 用途 | 说明 |
|------|------|------|------|
| 文件系统 | 只读 | 读取系统指标 (`/proc`, `/sys`) | 仅读取公开的系统统计信息 |
| 文件系统 | 只读 | 读取 OpenClaw 配置 (`/root/.openclaw/`) | 仅获取端口号和模型配置 |
| 文件系统 | 只读 | 读取会话文件 (`/root/.openclaw/agents/main/sessions/*.json`) | 仅计数，不读取内容 |
| 进程 | 只读 | `/proc` 进程列表 | 基于 `ps` 获取进程信息 |
| 网络 | 出站 | 无 | 不主动发起任何网络请求 |
| 执行 | 无 | N/A | 只读监控，不执行任何修改操作 |
