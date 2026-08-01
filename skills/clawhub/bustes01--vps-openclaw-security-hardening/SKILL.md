---
name: vps-openclaw-security-hardening
description: Production-ready security hardening for VPS running OpenClaw AI agents. Includes SSH hardening (custom port), firewall, audit logging, credential management, and intelligent alerting. Follows BSI IT-Grundschutz and NIST guidelines with minimal resource overhead.
version: 1.0.6
author: OpenClaw Community
homepage: https://github.com/MarcusGraetsch/vps-openclaw-security-hardening
metadata:
  openclaw:
    emoji: 🛡️
    requires:
      bins: ["ssh", "ufw", "auditd", "systemctl", "apt-get"]
      optional: ["fail2ban"]
      os: ["ubuntu", "debian"]
    tags: ["security", "hardening", "vps", "audit", "monitoring", "firewall", "ssh", "fail2ban"]
    install: "SSH_PORT=4848 ./scripts/install.sh"
    verify: "./scripts/verify.sh"
    warning: "DO NOT use on machines with sensitive personal data. Use dedicated VPS only. Test in VM first."
---

# VPS Security Hardening for OpenClaw

Production-ready security hardening for AI agent deployments on VPS.

## ⚠️ CRITICAL WARNINGS

**DO NOT run OpenClaw on servers/machines with sensitive personal data.** Use a dedicated machine (VPS, bare-metal, or on-premise server dedicated to OpenClaw).

**Before installing:**
1. **开第二个终端保持登录** — SSH 端口变更/防火墙 DROP 可能导致连接断开
2. **确认已有密钥对** — 密码登录会被禁用，没有密钥将无法登录
3. **记下你选的 SSH 端口** — 选 1024-65535 之间的端口，不要用常见端口
4. **外部告警通知知情** — 安全事件可通过 Telegram/Discord/Slack/Webhook 发送到外部服务
5. **测试环境优先** — 生产环境使用前，先在 VM 或测试机验证

**Supported OS:** Ubuntu 20.04+, Debian 11+. Not for Windows (use WSL2) or macOS.

## ⚠️ Choose Your SSH Port First

**You must choose a custom SSH port (1024-65535) before installing.** This makes you conscious of the security decision.

```bash
# Choose your port (example: 4848)
export SSH_PORT=4848

# Install
cd ~/.openclaw/skills/vps-openclaw-security-hardening
sudo ./scripts/install.sh

# Verify
./scripts/verify.sh

# Test SSH (new terminal)
ssh -p ${SSH_PORT} root@your-vps-ip
```

## What It Does

| Layer | Protection | Implementation |
|-------|------------|----------------|
| **Network** | Firewall, SSH hardening | UFW, custom port (your choice), key-only |
| **System** | Auto-updates, monitoring | unattended-upgrades, auditd |
| **Secrets** | Credential management | Centralized .env, 600 permissions |
| **Monitoring** | Audit logging, alerting | Kernel-level audit, multi-channel alerts |

## Requirements

- **OS:** Ubuntu 20.04+ or Debian 11+ (Linux only)
- **NOT supported:** Windows (use WSL2), macOS
- Root access
- Existing SSH key authentication
- Alert channel (optional): Telegram, Discord, Slack, Email, or Webhook
- **Custom SSH port of your choice (1024-65535)**

## Security Changes

### SSH
- Port: 22 → ${SSH_PORT} (your choice, 1024-65535)
- Auth: Keys only (no passwords)
- Root login: Disabled
- Max retries: 3
- Fail2ban: Brute-force protection

### Firewall
- Default: Deny incoming
- Allow: Your chosen SSH port only

### Services
- CUPS (printing): Stopped & disabled
- Fail2ban: Intrusion detection enabled
- Auto-updates: Security patches automatic

### Monitoring
- Credential file access tracking
- SSH config change detection
- Privilege escalation alerts
- Daily security briefing

## Resource Usage

| Component | RAM | Disk |
|-----------|-----|------|
| Auditd | ~2 MB | 40 MB max |
| UFW | ~1 MB | Negligible |
| Scripts | ~5 MB | Negligible |
| **Total** | **<10 MB** | **<50 MB** |

## Files

- `scripts/install.sh` - Main installation
- `scripts/verify.sh` - Verify installation
- `scripts/rollback-ssh.sh` - Emergency rollback
- `scripts/critical-alert.sh` - Telegram alerts
- `scripts/daily-briefing.sh` - Daily reports
- `rules/audit.rules` - Audit configuration

## Documentation

See [README.md](README.md) for full documentation.

## License

MIT - See LICENSE file

## ⚖️ 权限声明

| 权限 | 范围 | 用途 | 说明 |
|------|------|------|------|
| 执行 | sudo | SSH 加固、防火墙、auditd 安装 | 系统安全配置变更 |
| 文件系统 | 写入 | `/etc/ssh/sshd_config` | SSH 端口/认证模式配置 |
| 文件系统 | 写入 | `/etc/audit/rules.d/` | 内核级审计规则 |
| 文件系统 | 写入 | `/etc/cron.d/` | 安装定期安全简报定时任务 |
| 文件系统 | 读取 | `/var/log/audit/audit.log` | 安全事件监控 |
| 网络 | 出站 | 用户配置的告警渠道 | 安全事件通知（Telegram/Discord/Slack/Webhook） |
| 凭证 | 读取 | `.env` 文件 (权限 600) | 加载告警 Token |

> 🔒 **数据外传声明**：安全事件信息仅在用户显式配置告警 Token 后发送到外部服务。不配置 Token 则不产生任何外传流量。
