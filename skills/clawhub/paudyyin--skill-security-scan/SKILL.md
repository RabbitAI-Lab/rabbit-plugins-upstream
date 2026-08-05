---
name: skill-security-scan
version: 1.0.0
description: "Skill安全扫描工具。L1自动化扫描（scanner.py）+ L2人工审查协议（红旗清单+风险分级）。发现风险时推送信息交给人工复核。"
tags: [security, review, scan, audit, risk]
---

# Skill Security Scan — 技能安全扫描

双层安全机制：**L1 自动化扫描** + **L2 人工审查协议**。发现风险时推送信息交给人工复核。

---

## 双层安全机制

| 层级 | 工具 | 触发场景 | 输出 |
|------|------|----------|------|
| **L1: 自动化扫描** | scanner.py | 技能安装/加载时自动触发 | 退出码（0-3）+ 扫描结果 |
| **L2: 人工审查** | 审查协议 + 红旗清单 | L1 发现风险或用户主动要求时 | 结构化审查报告 |

---

## L1: 自动化扫描

### 触发时机

| 场景 | 扫描时机 |
|------|----------|
| .zip 文件安装 | 安装前扫描，失败则阻止 |
| 目录安装（cp/mv/git clone） | 文件落地后扫描 |
| 远程安装（clawhub/npx skills add） | 安装完成后立即扫描 |
| 未知技能 | 用户提及时扫描 |

### 命令

| 命令 | 用途 |
|------|------|
| `scanner.py scan <path>` | 扫描单个技能（.zip 或目录） |
| `scanner.py scan-all` | 扫描所有已安装技能 |
| `scanner.py first-run` | 首次运行全量扫描 |
| `scanner.py upgrade` | 手动升级 |

### 退出码

| 退出码 | 判定 | 动作 |
|--------|------|------|
| 0 | SAFE | 继续 |
| 1 | LOW / MEDIUM | 警告用户，请求确认 |
| 2 | HIGH / CRITICAL | 阻止，显示详情 |
| 3 | 扫描失败 | 解释原因，提供重试 |

### 首次运行

检查 `scripts/.first_run_done`：
- **不存在** → 告知用户 SkillScan 已安装，询问是否扫描所有现有技能
- **存在** → 跳过，正常运行

### 自动更新

每日自动检查更新，静默执行。手动：`scanner.py upgrade`

---

## L2: 人工审查协议

当 L1 扫描发现风险（退出码 1 或 2）或用户主动要求时，执行 L2 审查。

### Step 1: 来源检查

```
需要回答的问题：
- [ ] 这个技能来自哪里？
- [ ] 作者是否已知/可信？
- [ ] 有多少下载量/星标？
- [ ] 最后更新时间？
- [ ] 是否有其他代理的评审？
```

### Step 2: 代码审查（强制）

阅读技能中的所有文件，检查以下**红旗信号**：

```
🚨 立即拒绝的情况：
─────────────────────────────────────────
✗ curl/wget 到未知 URL
✗ 向外部服务器发送数据
✗ 请求凭证/token/API key
✗ 读取 ~/.ssh, ~/.aws, ~/.config 而无明确理由
✗ 访问 MEMORY.md, USER.md, SOUL.md, IDENTITY.md
✗ 使用 base64 解码
✗ 使用 eval() 或 exec() 处理外部输入
✗ 修改工作区外的系统文件
✗ 安装未列出的包
✗ 网络调用到 IP 而非域名
✗ 混淆代码（压缩、编码、混淆）
✗ 请求提升/sudo 权限
✗ 访问浏览器 cookie/session
✗ 触碰凭证文件
─────────────────────────────────────────
```

### Step 3: 权限范围评估

```
评估：
- [ ] 需要读取哪些文件？
- [ ] 需要写入哪些文件？
- [ ] 运行哪些命令？
- [ ] 是否需要网络访问？访问哪里？
- [ ] 范围是否对其声明目的最小化？
```

### Step 4: 风险分级

| 风险等级 | 示例 | 动作 |
|----------|------|------|
| 🟢 LOW | 笔记、天气、格式化 | 基础审查，可安装 |
| 🟡 MEDIUM | 文件操作、浏览器、API | 完整代码审查后决定 |
| 🔴 HIGH | 凭证、交易、系统 | **推送给用户审批** |
| ⛔ EXTREME | 安全配置、root 访问 | **拒绝安装** |

---

## 风险推送与人工复核

### 推送触发条件

| 条件 | 推送方式 |
|------|----------|
| L1 退出码 = 2（HIGH/CRITICAL） | 立即推送，阻止安装 |
| L1 退出码 = 1（LOW/MEDIUM）且用户未确认 | 推送警告，等待确认 |
| L2 发现红旗信号 | 推送审查报告，等待决策 |
| 风险等级 = 🔴 HIGH | 推送给用户审批 |

### 推送内容格式

```
🔒 Skill 安全扫描报告

技能：[name]
来源：[ClawHub / GitHub / other]
作者：[username]
版本：[version]

扫描结果：
- 退出码：[code]
- 风险等级：[🟢 LOW / 🟡 MEDIUM / 🔴 HIGH / ⛔ EXTREME]

发现的问题：
- [问题1]
- [问题2]

建议动作：[安装 / 谨慎安装 / 拒绝安装]

请确认是否继续安装此技能。
```

### 人工复核流程

```
1. 推送扫描报告给用户
2. 等待用户决策
3. 用户决策：
   ├─ 确认安装 → 记录决策，继续安装
   ├─ 拒绝安装 → 删除技能文件，记录原因
   └─ 需要更多信息 → 执行 L2 深度审查，补充报告
4. 记录审查结果到 memory
```

---

## 信任层级

1. **官方 OpenClaw 技能** → 较低审查（仍需审查）
2. **高星仓库（1000+）** → 中等审查
3. **已知作者** → 中等审查
4. **新/未知来源** → 最大审查
5. **请求凭证的技能** → 始终需要用户审批

---

## 审查报告模板

```
SKILL SECURITY SCAN REPORT
═══════════════════════════════════════
Skill: [name]
Source: [ClawHub / GitHub / other]
Author: [username]
Version: [version]
───────────────────────────────────────
METRICS:
• Downloads/Stars: [count]
• Last Updated: [date]
• Files Reviewed: [count]
───────────────────────────────────────
RED FLAGS: [None / List them]

PERMISSIONS NEEDED:
• Files: [list or "None"]
• Network: [list or "None"]
• Commands: [list or "None"]
───────────────────────────────────────
RISK LEVEL: [🟢 LOW / 🟡 MEDIUM / 🔴 HIGH / ⛔ EXTREME]

VERDICT: [✅ SAFE TO INSTALL / ⚠️ INSTALL WITH CAUTION / ❌ DO NOT INSTALL]

NOTES: [Any observations]
═══════════════════════════════════════
```

---

## Quick Vet 命令（GitHub 仓库）

```bash
# 检查仓库统计
curl -s "https://api.github.com/repos/OWNER/REPO" | jq '{stars: .stargazers_count, forks: .forks_count, updated: .updated_at}'

# 列出技能文件
curl -s "https://api.github.com/repos/OWNER/REPO/contents/skills/SKILL_NAME" | jq '.[].name'

# 获取并审查 SKILL.md
curl -s "https://raw.githubusercontent.com/OWNER/REPO/main/skills/SKILL_NAME/SKILL.md"
```

---

## 错误处理

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 技能文件不存在 | 路径错误或未安装 | 检查技能路径，确认已安装 |
| 无法解析 SKILL.md | 格式错误或编码问题 | 检查文件格式，使用 UTF-8 编码 |
| 依赖检查失败 | 依赖项未安装 | 安装缺失的依赖项 |
| 安全扫描超时 | 文件过大或网络问题 | 增加超时时间或分段扫描 |
| 版本冲突 | 已存在不同版本 | 确认版本兼容性后决定是否覆盖 |

## 降级策略

- 安全扫描失败 → 标记为"未验证"，提示用户手动检查
- 依赖检查失败 → 列出缺失依赖，由用户决定是否继续
- 版本冲突 → 保留原版本，提示用户手动处理

---

## 文件结构

```
skill-security-scan/
├── SKILL.md              # 本文档
└── scripts/
    └── scanner.py        # L1 自动化扫描脚本
```

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0.0 | 2026-07-31 | 合并 skill-vetter + skillscan，双层安全机制 + 风险推送人工复核 |

---

*Paranoia is a feature.* 🔒
