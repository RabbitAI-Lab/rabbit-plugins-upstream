# Context Optimizer Skill

## 概述

自动优化 OpenClaw 会话上下文，减少基础内容膨胀，提升对话效率。

## 触发条件

- **定时**：每天 23:00（Asia/Shanghai）
- **手动**：用户发送 `/optimize-context`
- **阈值**：当检测到上下文 token 使用率 > 70% 时自动触发

## 执行流程

### 1. 分析当前上下文构成

```javascript
// 读取当前会话状态
const status = await session_status();
const totalTokens = status.totalTokens;
const contextTokens = status.contextTokens;
const usagePercent = (totalTokens / contextTokens) * 100;
```

### 2. 执行优化项

#### 2.1 Daily Memory 精简（当天）

**规则：**
- 保留：活跃任务、关键决策、待办事项
- 归档：详细内容到 `archive/YYYY-MM-DD-detail.md`
- 触发：当天 daily memory > 1KB

#### 2.2 历史 Session Memory 清理（全部日期）

**规则：**
- 匹配所有 `YYYY-MM-DD-description.md` 格式的 session 文件
- 跳过当天日期的文件（可能仍在活跃）
- 3-13 天前的文件：检查活跃标记（⏳/TODO/进行中等），有则保留
- **>14 天的文件：强制归档**（无论是否有活跃标记）
- 归档到 `archive/sessions/`

#### 2.3 旧 Daily Memory 归档

**规则：**
- 匹配所有 `YYYY-MM-DD.md` 格式的 daily memory
- >7 天前且 >1KB → 检查活跃标记
- **>14 天前 → 强制归档**（无论标记）
- 归档到 `archive/`

#### 2.4 DREAMS.md 维护

**规则：**
- 保持摘要格式（< 1KB）
- 归档旧日记到 `archive/dream-diary/`

### 3. 生成优化报告

**报告内容：**
```markdown
## Context Optimization Report

**日期：** 2026-04-28
**时间：** 23:00 CST

### 优化前
- 总上下文：109k / 262k (42%)
- 基础内容：~61k (56%)
- Daily Memory：15k
- Session Memory：10k
- DREAMS.md：36k

### 优化后
- 总上下文：17k / 262k (6%)
- 基础内容：~17k (50%)
- Daily Memory：0.5k ⬇️ 97%
- Session Memory：0 ⬇️ 100%
- DREAMS.md：0.4k ⬇️ 99%

### 释放空间
- 可用上下文增加：~92k tokens
- 预计可多处理：~50 轮对话

### 归档文件
- memory/archive/2026-04-28-detail.md
- memory/archive/dream-diary/2026-04-28.md
```

### 4. 发送通知

**条件：**
- 优化释放 > 50k tokens → 发送飞书通知
- 发现异常大文件 → 发送告警

**消息格式：**
```
🦞 上下文优化完成

释放空间：92k tokens
当前使用：17k / 262k (6%)

归档：
- Daily Memory → archive/2026-04-28-detail.md
- Dream Diary → archive/dream-diary/2026-04-28.md

明天可以继续高效工作啦～
```

## 配置项

```json
{
  "contextOptimizer": {
    "enabled": true,
    "schedule": "0 23 * * *",
    "timezone": "Asia/Shanghai",
    "thresholds": {
      "dailyMemoryMaxSize": 1024,
      "dreamsMaxSize": 512,
      "sessionMemoryMaxAge": 86400,
      "contextUsageAlert": 70
    },
    "archive": {
      "enabled": true,
      "path": "memory/archive/",
      "retentionDays": 30
    },
    "notification": {
      "enabled": true,
      "channel": "feishu",
      "minReleaseTokens": 50000
    }
  }
}
```

## 手动触发

```bash
# 立即执行优化
/optimize-context

# 查看当前上下文构成
/context-status

# 强制归档所有历史
/context-archive-all
```

## 注意事项

1. **备份优先**：所有归档操作先备份再删除
2. **活跃任务保护**：标记为活跃的内容不会被清理
3. **错误处理**：优化失败时发送告警，不破坏现有上下文
4. **安静时段**：23:00-08:00 期间优化不发送非紧急通知

## 集成方式

### 作为 Cron 任务

```json
{
  "name": "context-optimizer",
  "schedule": "0 23 * * *",
  "payload": {
    "kind": "systemEvent",
    "text": "Run context optimization: node skills/context-optimizer/optimize.js"
  }
}
```

### 作为 Skill 安装

```bash
clawhub install context-optimizer
```

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.1 | 2026-04-29 | 修复历史 session memory 清理（全日期扫描）、新增 14 天强制归档 |
| 1.0 | 2026-04-28 | 初始版本，支持 Daily Memory、Session Memory、DREAMS.md 优化 |

## 相关文件

- `scripts/cleanup-sessions.js` — 会话清理
- `scripts/cleanup-ephemeral-sessions.js` — Ephemeral 会话自动清理
- `scripts/cleanup-sessions-aggressive.js` — 激进清理（>24h 不活跃）
- `AGENTS.md` — Session Startup 规则（已更新）
