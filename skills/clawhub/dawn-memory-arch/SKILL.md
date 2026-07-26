---
name: dawn-memory-arch
description: "三层存储+四大机制的 Agent 长期记忆架构 v7.1。MEMORY.md中央索引、memory/core/结构化事实、本地向量DB语义检索，配合Engramory策展纪律、WAL协议、Working Buffer、短期自动升格四大机制。零外部API依赖。"
metadata:
  tags: [memory, architecture, engramory, wal, context-management]
  author: chen6896qqwee
---

# Dawn Memory Architecture v7

## 一句话

**三层存储 + 四大机制** — 中央索引做入口，分层文件存细节，向量DB做语义检索，四条铁律管质量。

---

## 目录结构

```
workspace/
├── MEMORY.md               # 中央索引（硬上限200行）
├── session-state.json       # 热数据缓存
├── HEARTBEAT.md             # 定期任务清单
├── AGENTS.md                # 启动手册 + 技能路由
├── SOUL.md                  # 灵魂/性格
├── memory/
│   ├── core/                # 结构化事实（JSON）
│   │   ├── identity.json
│   │   ├── lessons.json
│   │   ├── preferences.json
│   │   ├── strategies.json
│   │   └── strategy_status.json
│   ├── daily/               # 每日日志
│   ├── archive/             # 打包归档
│   ├── context-saves/       # 会话保存
│   ├── working-buffer.md    # 危险区日志
│   └── INDEX.md             # 目录索引
├── .learnings/              # 结构化学习日志
│   ├── LEARNINGS.md
│   ├── ERRORS.md
│   └── FEATURE_REQUESTS.md
└── memory-architecture-v7-guide.md  # 完整指南
```

---

## 三层存储

### 第一层：MEMORY.md（中央索引）
- 所有记忆的导航入口
- 硬上限 200行 / 25KB
- 每次启动必须读
- 内容：核心信息、近期大事、系统能力、关键结论、Promoted记忆

### 第二层：memory/core/（结构化事实）
- JSON 文件，每个主题一个
- 版本号管理：v5.1, v6.1 等
- 包含：身份、经验教训、偏好、策略、策略状态

### 第三层：本地向量DB（语义检索）
- LanceDB + all-MiniLM-L6-v2（384维）
- 零外部API依赖
- @ localhost:19999

---

## 四大机制

### 1. Engramory策展纪律
- 写前查重
- 能改不增（更新优先于新增）
- 错了就删（不标记过期）
- 硬上限200行
- 记忆必须带 type/description/Why+How to apply

### 2. WAL协议（Write-Ahead Logging）
检测到修正/决策/偏好/数值→先写 session-state.json 再回复

### 3. Working Buffer
上下文>60%时，每轮对话摘要写入 memory/working-buffer.md

### 4. 短期→长期自动升格
高价值记忆（score>0.8）自动从 daily 日志 promote 到 MEMORY.md

---

## 相关文件

本技能包含：
- `SKILL.md` — 技能说明
- `memory-architecture-v7-guide.md` — 完整部署指南（含模板+checklist）

---

## 快速部署（10步）

1. 创建 `memory/` 目录和子目录
2. 创建 `MEMORY.md`（含核心信息+系统能力+文件架构）
3. 创建 `session-state.json`
4. 创建 `HEARTBEAT.md`
5. 部署本地向量DB（LanceDB + all-MiniLM-L6-v2）
6. 在启动手册注册 Engramory策展纪律
7. 在灵魂文件写入记忆信条
8. 配置 WAL 协议触发器
9. 配置 Working Buffer 阈值（60%）
10. 配置 .learnings/ 目录及自动升格规则

---

**版本**: v7.1
**作者**: 曙光 (chen6896qqwee)
**血泪教训**: 能写到文件里的，别赌上下文记得住。
