---
name: "self-upgrade-openclaw"
description: "零停机升级 OpenClaw：查 release notes → 主公确认 → 旁路备份 → npm install → 重启 + 回滚兜底"
---

# openclaw-self-update-zero-downtime

## 用途

**零停机升级 OpenClaw**。适用于以下指令：
- "升级 OpenClaw"
- "更新 openclaw" / "帮我更新"
- "检查更新" / "检查升级"
- "升级到最新版"
- "帮我升级一下 OpenClaw"
- 任何涉及 OpenClaw 自身升级的对话

## 核心策略

```
查 release notes → 主公确认无 breaking change → 
旁路备份（安全锚点）→ npm install -g（不用本地 build）→ 
修正 systemd Node 路径 → 更新 systemd 版本号 → 重启 + 健康检查 →
失败则从备份回滚 / 成功则自动清理
```

**特点**：
- ✅ 零停机：仅重启瞬间闪断（~10s），systemd `Restart=always` 自动恢复
- ✅ 永不 offline：旁路备份 + 回滚机制确保任何情况可恢复
- ✅ 用户确认：先展示 release notes，确认无 breaking change 后再执行
- ✅ 全日志：所有输出落文件，不依赖终端
- ✅ Node 版本自动检测：自动检查新版 openclaw 的 Node.js 要求，修正 systemd ExecStart

## 触发条件

- 主公明确要求升级/更新 OpenClaw
- 会话上下文表明需要进行 OpenClaw 自身升级

## 环境要求

| 项目 | 说明 |
|------|------|
| 操作系统 | Linux（WSL2 亦可） |
| Node.js | 至少一个版本满足新版 openclaw 的 engines.node 要求 |
| npm | 任意（但需要能访问 npm registry） |
| service 管理 | systemd user 模式 |
| 磁盘空间 | 至少 2G 可用 |
| 网络 | 能访问 `registry.npmjs.org` 和 `api.github.com` |

## 前提假设

- OpenClaw 是通过 `npm install -g` 全局安装的
- 服务通过 systemd user 管理（`openclaw-gateway.service`）
- npm global 目录在 `$HOME/.npm-global/`
- 有 `systemctl --user` 权限

## 流程

### 阶段 0: 获取当前状态

1. 读取 systemd 单元文件和 npm 全局目录，获取当前版本
2. 查询 npm registry 获取最新稳定版版本号
3. 如果最新版 ≤ 当前版，告知主公已是最新版，结束

### 阶段 1: 获取 release notes，主公确认

1. 从 GitHub API 获取目标版本的 release notes
2. 展示给主公：
   - 当前版本 → 目标版本
   - release notes 核心摘要（前 20-30 行）
   - 是否包含 breaking changes / 需要手动操作的事项（如重新输密码、配置变更等）
3. 询问主公：

   > 新版本 vX.Y.Z 的 release notes 如上。
   > 是否有 breaking changes 需要你手动操作？（密码重认证等）
   > 现在升级还是等你有空？

4. 如果主公说"现在升"且无大问题 → 执行阶段 2
5. 如果主公说"稍后"/"晚上升" → 设置 cron 任务定时执行（isolated agentTurn）
6. 如果有 breaking change 需要主公先处理 → 中止，告知需要处理的内容

### 阶段 2: 执行升级

运行升级脚本（全自主、无交互）。

升级脚本内容（`scripts/upgrade-openclaw.sh`）：

> ⚠️ 脚本较长，建议直接查看文件：`~/.openclaw/workspace/scripts/upgrade-openclaw.sh`

核心步骤：

1. **Node 版本兼容性预检**：先下载新包、读取 `engines.node`，检查 systemd 当前使用的 Node 是否满足要求
2. **自动寻找兼容 Node**：如果不满足，遍历 `which -a node` 及各常见安装路径寻找可用版本
3. **旁路备份**：`cp -r openclaw → openclaw-fallback`
4. **npm install -g openclaw@latest**：失败则自动回滚
5. **修正 systemd ExecStart**：用检测到的兼容 Node 路径替换 unit 中写死的路径
6. **更新 systemd 版本号**：兼容 `Description=OpenClaw Gateway (vX.Y.Z)` 和 `OPENCLAW_SERVICE_VERSION=` 两种格式
7. **重启 + 健康检查**：60s 超时等待
8. **失败回滚 / 成功清理**

### 阶段 3: 汇报结果

读取日志最后几行，向主公汇报：
- ✅ 升级成功：旧版本 → 新版本，闪断耗时
- ❌ 升级失败（已自动回滚）：原因 + 日志路径
- ⚠️ 需要手动操作：如果有 breaking change 提示，告知主公

## 安全机制

| 机制 | 说明 |
|------|------|
| Node 兼容性预检 | `npm pack` 下载包 → 解析 `engines.node` → 检查 `which -a node` 中各版本 → 无兼容版本则中止 |
| systemd Node 路径自动修正 | 检测 unit 中 `ExecStart` 的 node 路径，不满足要求时自动切换到兼容版本 |
| 旁路备份 | `cp -r openclaw → openclaw-fallback`，完整安全锚点 |
| 自动回滚 | 健康检查失败后从 fallback 恢复 + 恢复旧 Node 路径 + 重启旧版 |
| systemd 兜底 | `Restart=always` + `StartLimitBurst=5` |
| 日志落盘 | 所有输出写日志文件，不依赖终端 |
| 人工确认 | 必须先展示 release notes，主公确认后再执行 |
| 定时执行 | 通过 cron 支持指定时间自动升级 |

## 故障排除

### Node 版本不兼容

脚本会自动检测并提示：

```
❌ 系统中找不到满足 >=22.22.3 <23 || >=24.15.0 <25 || >=25.9.0 的 Node.js 版本！
❌ 当前 node 版本: v22.22.1
❌ 请先升级 Node.js 后再尝试升级
```

升级 Node 后重试即可。

### systemd ExecStart 路径不对

旧脚本写死 `/usr/bin/node`，v2 开始会自动检测 unit 中的路径并修正。如果系统中有多个版本的 Node（如 `/usr/bin/node` v22.22.1 和 `/usr/local/bin/node` v25.9.0），脚本会优先选择满足引擎要求的版本。

### 升级后需要重新输密码

部分版本可能改动了认证机制。如果升级后 WebChat 提示密码错误：
- 检查 `~/.openclaw/openclaw.json` 中的 gateway password 配置
- 在 WebChat Control UI 设置中重新输入密码

### 服务启动失败

```bash
systemctl --user status openclaw-gateway
journalctl --user -u openclaw-gateway -n 50
```

### 手动回滚

```bash
rm -rf ~/.npm-global/lib/node_modules/openclaw
cp -r ~/.npm-global/lib/node_modules/openclaw-fallback ~/.npm-global/lib/node_modules/openclaw
systemctl --user restart openclaw-gateway
```

## 安装

1. 安装本 skill
2. 脚本自动写入 `~/.openclaw/workspace/scripts/upgrade-openclaw.sh`
3. 确认环境满足要求即可使用

## 变更日志

### v2.0.0 (2026-07-19)
- **新增** Node 版本兼容性预检：`npm pack` → 读取 `engines.node` → 检查 `which -a node` 各版本
- **新增** 自动修正 systemd ExecStart 路径：当 systemd 当前使用的 Node 不满足新版要求时，自动寻找兼容版本并更新 unit
- **新增** systemd 单元支持两种版本号格式：`Description=OpenClaw Gateway (vX.Y.Z)` 和 `OPENCLAW_SERVICE_VERSION=`
- **修复** release notes 查询硬编码版本号的 bug，改为动态获取目标版本
- **优化** 回滚时同步恢复 Node 路径和版本号

### v1.0.0
- 初始版本，零停机升级方案
- release notes 检查 + 用户确认
- 旁路备份 + 自动回滚
- 全日志，无控制台输出
