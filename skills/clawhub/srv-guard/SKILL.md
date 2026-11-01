---
name: srv-guard
description: |-
  服务器安全防护一体化能力：扫描漏洞、修复漏洞、感知攻击、防御攻击，并生成安全报告。
  当需要对 Linux 服务器进行安全加固、漏洞巡检、入侵检测或应急防御时加载此 Skill。
  触发词：服务器安全、漏洞扫描、漏洞修复、攻击感知、入侵检测、安全加固、封禁 IP。
  English triggers: server security hardening, vulnerability scan, patch/audit Linux config,
  intrusion detection, brute-force log analysis, block malicious IP, security report.
allowed-tools: Bash(python:*) Bash(ssh:*) Bash(sudo:*) read write edit glob grep
---

# server-security-guard — 服务器安全防护

> 防御性安全加固 Skill。在已获授权的服务器上执行漏洞巡检、自动修复、攻击感知与应急防御，输出可审计的安全报告。

## 核心原则

1. **仅防御用途** — 只对已获书面授权的服务器执行安全加固。禁止用于未授权系统、禁止植入后门、禁止开发攻击载荷。
2. **默认安全（dry-run）** — 修复与防御脚本默认 `--dry-run`，仅打印将执行的操作；需显式 `--apply` 才真正改动系统。
3. **最小副作用** — 改动范围最小化，写前检查目标状态，高风险操作可回滚，所有变更写入审计日志。
4. **能力边界诚实** — 扫描覆盖常见配置类漏洞，不声称替代专业 CVE 数据库或商业 IDS；修复只自动处理可安全自动化的项。
5. **Agent 判断 + 脚本执行** — Agent 负责理解上下文、权衡风险、决定修复策略；脚本负责确定性扫描、执行与校验。

## 工作流

### Phase 1: 漏洞扫描（只读）

```text
输入: 目标服务器（本地或 SSH）、扫描范围
执行: python scripts/vuln_scan.py --target <local|ssh://user@host> [--scope all|config|service|port|patch|ssh]
输出: scan-result.json（漏洞清单 + 严重度 + 证据）
```

扫描项见 `references/scan-checklist.md`。脚本检测目标系统工具可用性并优雅降级。

### Phase 2: 漏洞修复（默认 dry-run）

```text
输入: scan-result.json 或指定修复项
执行: python scripts/vuln_fix.py --target <local|ssh://user@host> --input scan-result.json [--apply] [--items item1,item2]
输出: fix-result.json（每项修复: 成功/失败/回滚信息）
```

修复手册见 `references/fix-playbook.md`。默认 dry-run（不传 `--apply` 即只打印不执行）。破坏性操作先备份。

输出状态：`fixed`（已改）/ `would_fix`（dry-run 下将要执行，尚未改）/ `skipped`（不可自动修复）/ `failed`。dry-run 绝不报告 `fixed`。

### Phase 3: 攻击感知（日志分析）

```text
输入: 目标服务器、时间窗口、检测规则集
执行: python scripts/attack_monitor.py --target <...> --window 24h [--rules brute-force,scan,anomaly]
输出: monitor-result.json（告警事件 + 来源 IP + 证据日志行）
```

攻击特征与检测规则见 `references/attack-signatures.md`。只读取日志，不修改系统。

### Phase 4: 攻击防御（默认 dry-run）

```text
输入: monitor-result.json 或指定恶意 IP/事件
执行: python scripts/attack_defend.py --target <local|ssh://user@host> --input monitor-result.json [--apply] [--action block|harden|alert] [--block-threshold high|medium] [--ips ip1,ip2]
输出: defend-result.json（封禁/加固操作记录 + 回滚命令）
```

防御策略见 `references/defense-strategies.md`。默认 dry-run（不传 `--apply` 即只打印不执行）。封禁操作生成回滚命令，便于误封后恢复。

- `--action block`：按严重度阈值封禁来源 IP；白名单支持任意前缀长度 CIDR（`/24`、`/32`、`::/0` 等），非法条目跳过。
- `--action harden`：改 sshd_config（禁用空口令 / root 密码登录）与 4 项内核参数；改配置前先备份，备份失败即中止该项，全部操作带回滚命令。

### Phase 5: 安全报告

```text
执行: python scripts/security_report.py --scan scan-result.json [--fix fix-result.json] [--monitor monitor-result.json] [--defend defend-result.json] --output report.html
输出: report.html（基于 assets/report-template.html 生成）
```

## 决策规则

| 任务类型 | 执行方式 |
|----------|----------|
| 仅了解安全状况 | Phase 1 + Phase 5（只读扫描 + 报告） |
| 扫描并修复 | Phase 1 → 2 → 5，修复前人工确认 dry-run 输出 |
| 持续监控攻击 | Phase 3 定时执行 + Phase 5，可结合 cron |
| 应急响应攻击 | Phase 3 → 4 → 5，防御前人工确认封禁列表 |
| 全面安全加固 | Phase 1 → 2 → 3 → 4 → 5，逐阶段确认 |

## 脚本

| 脚本 | 用途 | 默认模式 |
|------|------|----------|
| `scripts/vuln_scan.py` | 漏洞扫描 | 只读 |
| `scripts/vuln_fix.py` | 漏洞修复 | dry-run |
| `scripts/attack_monitor.py` | 攻击感知 | 只读 |
| `scripts/attack_defend.py` | 攻击防御 | dry-run |
| `scripts/security_report.py` | 生成 HTML 报告 | 只读 |
| `scripts/web_ui.py` | 本机网页端扫描、dry-run 预览、确认后修复 | 默认只预览；用户二次确认后才执行 |

所有脚本：基于自身文件位置解析 Skill 内资源（不依赖 cwd）、UTF-8 编码、JSON 输出到 stdout、进度/错误到 stderr、非零退出码表示失败、支持 `--help`。

### 网页端一键修复（仅本机）

```bash
python scripts/web_ui.py                 # 默认 http://127.0.0.1:8765
python scripts/web_ui.py --port 9000     # 自定义本机端口
```

打开启动时打印的本机 URL。界面流程：扫描 → 选择支持自动修复的项目 → 查看 dry-run 命令 → 点击确认并输入 `APPLY` → 执行。只绑定 loopback（`127.0.0.1`/`localhost`/`::1`），启动参数拒绝非 loopback 地址；不要通过反向代理/端口转发暴露到网络。页面 token 每次启动随机生成，放在 URL fragment（不发送给服务端、无访问日志泄露），API 使用 bearer token；跨站请求还要满足本机 Host/Origin 校验。扫描会话 30 分钟过期，apply 前服务端会重新生成预览并校验所选项仍来自该扫描且为 auto-fixable。这个「一键」是**确认后执行**，不会绕过 dry-run 或人工确认。

UI 调用原有 `vuln_fix.py`，不新增修复能力；当前仅支持自动修复列表中的项目，其余仍需人工处理。仅对有授权的主机使用。

## 资源导航

| 资源 | 路径 | 用途 |
|------|------|------|
| 扫描清单 | `references/scan-checklist.md` | 扫描项、判断标准、严重度分级 |
| 修复手册 | `references/fix-playbook.md` | 每类漏洞的修复步骤、风险评估、回滚方法 |
| 攻击特征 | `references/attack-signatures.md` | 检测规则、日志来源、阈值 |
| 防御策略 | `references/defense-strategies.md` | 封禁/加固策略、防火墙操作、回滚 |
| 报告模板 | `assets/report-template.html` | HTML 报告模板 |

### 已知覆盖边界（勿超范围承诺）

`references/scan-checklist.md` 与 `references/fix-playbook.md` 描述的是完整检查/修复清单，脚本尚未全部实现自动化。当前情况：

- **扫描已实现**：CFG-01~09、SVC-01/02/04/05/06、PRT-01、PCH-01/02
- **扫描未实现**（清单有、脚本无，需人工核查）：CFG-10、SVC-03、PRT-02、PRT-03、PCH-03、SSH-06、SSH-07
- **自动修复已实现**：CFG-01、CFG-02、CFG-03、CFG-06、CFG-07、SVC-01
- **仅能人工修复**（脚本会记为 `skipped` 并说明）：CFG-04/09、SVC-04/06、PCH-01/03 等

向用户汇报时必须区分"已扫描/未扫描"与"已修复/需人工"，不得把清单条目当作已覆盖能力。

## 安全约束

以下操作**禁止**：
- 对未获书面授权的服务器执行任何操作
- 植入后门、rootkit、持久化恶意载荷
- 开发攻击工具、生成漏洞利用代码
- 在脚本中硬编码凭证、密钥、目标 IP
- 跳过 dry-run 直接对生产服务器 `--apply` 而无人工确认
- 删除与安全加固无关的文件

以下操作**优先**：
- 修复/防御前先 dry-run 并由人工确认
- 破坏性操作前备份原配置
- 所有变更写入审计日志（`/var/log/security-guard-audit.log`）
- 封禁操作同时生成回滚命令
- 扫描结果包含证据（具体配置项/日志行），便于人工复核

## 权限说明

- 扫描与监控：普通用户可读取的日志/配置即可；部分项需 root（脚本会标注并跳过）
- 修复与防御：需 root/sudo。脚本检测权限不足时明确提示，不静默跳过
- SSH 远程：通过 `ssh` 执行，需已配置免密或使用 ssh-agent，不在脚本中存储密码
