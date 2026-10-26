# 防御策略

> `attack_defend.py` 的封禁/加固策略、防火墙操作与回滚。默认 dry-run。

## 防御动作（--action）

### block — 封禁恶意 IP

**输入**: monitor-result.json 中的事件，或 `--ips` 显式指定。

**封禁策略**:

| 后端 | 检测顺序 | 封禁命令 | 回滚命令 |
|------|----------|----------|----------|
| firewalld | `systemctl is-active firewalld` | `firewall-cmd --add-source=<ip> --zone=drop --permanent` | `firewall-cmd --remove-source=<ip> --zone=drop --permanent` |
| ufw | `which ufw` | `ufw deny from <ip>` | `ufw delete deny from <ip>` |
| iptables | `which iptables` | `iptables -I INPUT -s <ip> -j DROP` | `iptables -D INPUT -s <ip> -j DROP` |
| nftables | `which nft` | `nft add rule inet filter input ip saddr <ip> drop` | `nft delete rule ...` |

按顺序检测第一个可用的后端。无可用后端 → 报错，不伪造成功。

**封禁阈值**: 默认仅封禁 `severity >= HIGH` 事件的来源 IP；`--block-threshold medium` 可放宽。

**白名单保护**: `--whitelist` 指定的 IP/网段永不封禁（防止误封管理员/内网）。默认白名单: `127.0.0.0/8`, `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`（可覆盖）。

**输出**:
```json
{
  "action": "block",
  "backend": "iptables",
  "blocked_ips": [{"ip": "203.0.113.5", "reason": "brute_force", "event_id": "evt-001"}],
  "skipped_ips": [{"ip": "10.0.0.5", "reason": "in_whitelist"}],
  "rollback_commands": ["iptables -D INPUT -s 203.0.113.5 -j DROP"],
  "dry_run": true
}
```

### harden — 加固配置

对当前会话发现的漏洞执行加固（调用 `vuln_fix.py` 的安全子集）。与 block 区别: harden 改配置，block 改防火墙。

可执行的加固（均为低风险、可回滚）:
- SSH: 禁用空口令、禁用 root 登录（前提: 有密钥/sudo 普通用户）
- 锁定空口令账户
- 修复私钥文件权限

**不自动执行**: 软件升级、服务禁用（需人工确认业务影响）。

### alert — 仅告警不处置

生成告警记录到 `/var/log/security-guard-audit.log`，不封禁不加固。用于需要人工研判的场景。

## 审计日志

所有防御操作（无论 dry-run 或 apply）写入审计日志:

```
[2026-01-01T12:00:00Z] ACTION=block IP=203.0.113.5 REASON=brute_force DRY_RUN=true BY=server-security-guard
[2026-01-01T12:01:00Z] ACTION=block IP=203.0.113.5 REASON=brute_force DRY_RUN=false APPLIED=true BY=server-security-guard
```

日志路径: `/var/log/security-guard-audit.log`（需 root 创建；无权限则降级到脚本运行目录的 `security-guard-audit.log` 并标注）。

## 回滚

每个 apply 操作在 defend-result.json 中记录 `rollback_commands`。脚本支持:

```bash
python scripts/attack_defend.py --rollback defend-result.json --apply
```

按记录的回滚命令逆序执行，恢复封禁/加固。回滚本身也写审计日志。

## 安全约束

- **永不封禁白名单 IP**，即使显式 `--ips` 指定也拒绝并告警
- **封禁前再次确认**: apply 模式下打印将封禁的 IP 列表，要求人工确认（脚本通过 `--yes` 跳过，但 SKILL.md 工作流要求 Agent 先展示 dry-run）
- **不永久封禁**: 默认封禁规则为持久化到防火墙，但 defend-result.json 始终保留回滚命令；如需限时封禁，用 `--expire <duration>`（依赖 fail2ban 或 cron 自动解封，脚本本身不实现定时解封）
- **不封禁整个网段**除非显式 `--cidr` 且经人工确认（防止误伤）

## 与 fail2ban 的关系

若目标已运行 fail2ban，`attack_monitor.py` 会读取 fail2ban 日志作为补充证据；`attack_defend.py` 的封禁与 fail2ban 并行（不冲突，iptables 规则独立）。建议: 持续防护优先用 fail2ban，本 Skill 用于一次性应急响应和加固。
