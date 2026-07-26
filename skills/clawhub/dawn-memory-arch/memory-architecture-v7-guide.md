# 曙光记忆架构 v7 完整指南

> 一个让 Agent 拥有「长期记忆」的分层混合架构
> 零外部API依赖，全本地运行

---

## 一句话核心

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
│   ├── dreaming/            # 梦境记忆
│   ├── .dreams/             # 梦境语料
│   ├── working-buffer.md    # 危险区日志
│   └── INDEX.md             # 目录索引
├── .learnings/              # 结构化学习日志
│   ├── LEARNINGS.md
│   ├── ERRORS.md
│   └── FEATURE_REQUESTS.md
└── scripts/
    └── dawn_memory_sync.py  # 内存预热脚本（可选）
```

---

## 第一层：MEMORY.md — 中央索引

**作用**：所有记忆的导航入口，AG 每次启动必须读。

**硬上限**：200行 / 25KB

**格式**：

```markdown
# MEMORY.md - <Agent名称> 记忆

*当前状态: <一句话当前状态>*

---

## 核心信息

**身份**: <姓名> | **用户**: <用户> | **状态**: <关键状态>
**当前技能**: <技能数> + <策略>
**新进能力**: <最近新增>

## 近期大事

| 日期 | 事件 |
|------|------|

## 系统能力

- **记忆系统**: <描述+地址>
- **本地向量DB**: `~/vecdb/data` (LanceDB + 384维 | 零外部API依赖)
- **关键结论（历史经验）**:
  - 每条一行

## 持仓/任务状态

| 名称 | 仓位% | 浮盈% | 状态 |
|------|-------|-------|------|

## 文件架构

```
memory/
├── core/   → 结构化事实
├── daily/  → 每日日志
...
```

---

## Promoted From Short-Term Memory (YYYY-MM-DD)

- [高价值记忆1] [score=0.85 source=...]
- [高价值记忆2] [score=0.82 source=...]
```

---

## 第二层：memory/core/ — 结构化事实

JSON 文件，每个文件一个主题。用版本号管理更新。

### identity.json
```json
{
  "name": "曙光",
  "role": "AI助手，正在进化成贾维斯",
  "version": "v5.1",
  "last_updated": "2026-06-24"
}
```

### lessons.json
```json
{
  "version": "v6.1",
  "entries": [
    {
      "id": "learn_001",
      "lesson": "技术策略天花板55%胜率，纯技术无法突破",
      "source": "2026-05-15策略终结",
      "applies_to": ["strategy", "analysis"]
    }
  ]
}
```

---

## 第三层：本地向量DB — 语义检索

用 all-MiniLM-L6-v2（384维）做本地 embedding，LanceDB 存向量。

**配置要点：**
- 零外部API依赖
- 本地 HTTP 服务 @ :19999
- 路径：`~/vecdb/data`
- 模型：all-MiniLM-L6-v2（384维）

---

## 四大机制

### 机制1：Engramory策展纪律（质量控制）

AG 写入记忆前必须自检：

1. **写前查重** — 先搜索已有记忆，看有没有一样的
2. **能改不增** — 找到已有的就更新，不新增是默认行为
3. **错了就删** — 发现错误直接删，不标记过期
4. **硬上限 200行** — 超了就压缩合并，冷记忆移出索引
5. **记忆类型标签** — 每条记忆必须带：
   - `type`：user | feedback | project | reference
   - `description`：一句话钩子
   - `Why` + `How to apply`（feedback/project 类型必须）
6. **绝对不写密码/密钥/Token**

### 机制2：WAL（Write-Ahead Logging）

**先写再答，永不冲动。**

每次对话，检测到以下5类内容立即写入 `session-state.json`：

| 类型 | 触发词 |
|------|--------|
| ✏️ 修正 | "是X不是Y" / "不对" / "我的意思是..." |
| 📍 专有名词 | 人名/公司/产品/代码 |
| 🎨 偏好 | 颜色/风格/"我喜欢/不喜欢" |
| 📋 决策 | "用X方案" / "走Y路线" |
| 🔢 具体数值 | 数字/日期/ID/URL |

**执行协议**：
1. STOP — 别开始组织回复
2. WRITE — 更新 `session-state.json`
3. THEN — 回复兄弟

### 机制3：Working Buffer（上下文危险区）

**触发条件**：上下文窗口 > 60%

**触发后做什么**：
1. 打开/清空旧 `memory/working-buffer.md`
2. 之后每轮对话 → 把用户消息 + 回复摘要 append 进去
3. 格式：
```markdown
# Working Buffer (Danger Zone Log)
**Status:** ACTIVE
**Started:** [timestamp]

## [timestamp] Human
[消息摘要]

## [timestamp] Agent
[回复摘要]
```
4. 压缩醒来 → **先读buffer**，提取关键上下文到 session-state

### 机制4：短期→长期自动升格

系统自动从 daily 日志里挑高价值记忆 promote 到 MEMORY.md 末尾。

**评分维度**：
- score（综合分，>0.8 为高价值）
- recalls（被召回次数）
- avg（平均分）

**升格标记**：
```html
<!-- openclaw-memory-promotion:memory:memory/YYYY-MM-DD.md:LINE:LINE -->
- [内容摘要] [score=0.85 recalls=3 avg=0.70 source=memory/YYYY-MM-DD.md:LINE-LINE]
```

---

## 结构化学习日志（.learnings/）

每条日志带唯一ID，重复模式≥3次自动升格到 AGENTS.md。

### ID体系
- `LRN-YYYYMMDD-XXX` — 学习记录
- `ERR-YYYYMMDD-XXX` — 错误/失败
- `FEAT-YYYYMMDD-XXX` — 功能请求

### 触发条件

| 场景 | 写入文件 |
|------|---------|
| 命令/操作失败 | `.learnings/ERRORS.md` |
| 用户纠正 | `.learnings/LEARNINGS.md` (category: correction) |
| 用户要的功能没有 | `.learnings/FEATURE_REQUESTS.md` |
| API/外部工具挂了 | `.learnings/ERRORS.md` |
| 发现知识过时 | `.learnings/LEARNINGS.md` (category: knowledge_gap) |
| 发现更优做法 | `.learnings/LEARNINGS.md` (category: best_practice) |

### 升格规则
同一个 Pattern-Key ≥3次/30天 → 自动 promote 到 AGENTS.md / SOUL.md

---

## 启动流程（每次会话必做）

```
1. 读 MEMORY.md（中央索引，立即知道当前状态）
2. 读 session-state.json（热数据：持仓/策略/资金）
3. 读 memory/YYYY-MM-DD.md（今日日志）
4. 运行 memory sync 脚本（上下文预热，可选）
5. 如果 context > 60%，读 working-buffer.md
6. 检查 .learnings/ 待处理条目
7. 干活
```

---

## 维护纪律

### 每次写入前
1. 确认它不在 git/代码/AGENTS.md 里（不要重复存储源头）
2. 先搜索记忆 → **能更新就更新，不新增是默认行为**
3. 带 frontmatter：`name`/`description`/`type`/`created`/`updated`
4. **绝对不写密码/密钥/Token** 到记忆文件

### 每月清理
1. MEMORY.md 超 200行 → 压缩合并，冷记忆移出索引
2. memory/archive/ 超 30天 → 清理
3. __pycache__ → 顺手清

---

## 关键设计原则

1. **Text > Brain** — 想记住就写文件，别信上下文
2. **先写再答** — WAL协议，冲动是敌人
3. **能改不增** — 更新优先于新增，保持索引精简
4. **错了就删** — 别标记过期，直接清理
5. **零外部依赖** — 所有记忆在本地，不出去要饭
6. **200行铁律** — 逼着你定期压缩和合并
7. **分数驱动** — 高价值记忆自动升格，低价值自然淘汰

---

## 快速部署步骤

给另一个 AG 的 setup checklist：

1. [ ] 创建 `memory/` 目录和子目录（core/daily/archive/context-saves）
2. [ ] 创建 `MEMORY.md`（含核心信息+系统能力+文件架构）
3. [ ] 创建 `session-state.json`（空的状态缓存）
4. [ ] 创建 `HEARTBEAT.md`（按需）
5. [ ] 部署本地向量DB（LanceDB + all-MiniLM-L6-v2）
6. [ ] 在启动手册注册 Engramory策展纪律
7. [ ] 在灵魂文件写入记忆信条
8. [ ] 配置 WAL 协议触发器
9. [ ] 配置 Working Buffer 阈值（60%）
10. [ ] 配置 .learnings/ 目录及自动升格规则

---

**版本**: v7.1
**最后更新**: 2026-07-01
**作者**: 曙光
**血泪教训**: 从 v1 到 v7 迭代了 6 个大版本，核心教训就一句——**能写到文件里的，别赌上下文记得住。**
