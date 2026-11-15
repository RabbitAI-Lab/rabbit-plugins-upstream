---
name: "self-improving-agent"
description: "记录错误、纠正、能力缺口与最佳实践，形成可复用的持续改进闭环。V2 = 八步学习法 + LLM 语义分析 + OpenSpace 自动维护。"
---

# Self-Improving Agent V2

> 八步闭环：预防→记录→报告→度量→反馈→版本化→归档→过期

**本文件为 MIT 许可发布**（Copyright © self-improving-agent 贡献者）。可自由使用、修改、再分发，保留本版权声明即可。

## 触发时机

1. 命令/操作失败 → 立即记录
2. 用户纠正 → 立即记录
3. 用户提出新能力需求 → 记 FEATURE_REQUESTS.md
4. 外部服务失败 → 立即记录
5. 发现可复用更优流程 → 记 best_practice
6. 任务前 → 必跑 precheck

---

## 四道硬约束（先读，再走八步）

规则 1-8 是日常流程，下面四条是**不可跳过的红线**。它们在真实工作日各被违反过，代价是"记了也没用"。

### 约束 A — promoted 不等于完成，落地文本才算

`promoted` 是**状态字段**，不是**交付物**。唯一下游消费者是 **AGENTS.md 里的正文**。字段为 promoted 但 AGENTS.md 中查无此条 = 该教训从未存在过。

- 晋升的定义 = **内容出现在 AGENTS.md 中**，不是 DB/状态改成 promoted。
- 收工前必跑**回声检查**：随机抽取当日 promoted 的条目，grep AGENTS.md 正文，命中率必须 **100%**。查无 → 该条**回滚为 pending**并记一条新的 ERR（教训不是"忘了推进"，是"把状态当成了落地"）。
- **Why**：曾出现 **5 条**教训被标 promoted，但 AGENTS.md 里一个字都没有——状态被当成了完成，下一次会话根本读不到。

### 约束 B — 教训已在 AGENTS.md 却仍复发 → 升级为硬阻断

记录**不会**阻止复发。若某教训**已存在于 AGENTS.md**、错误却**再次发生**，禁止再开一条记忆——记忆是同一层级的重复，不会生效。

升级阶梯（逐级，越级无效）：
1. 工具级护栏（precheck 直接拒绝 / 脚本参数硬校验 / 写死禁用路径）
2. 阻塞项（开工前必须显式解除的 gate）
3. 流程阻断（该命令进入人工确认队列）

**复发 ≥3 次** → 必须写明"为何现有护栏未生效"，并把护栏**前移一层**（从"提醒"移到"阻断"）。

**Why**：同一根因错误在**一天内、8 个不同任务**上重复 8 次，而教训当天早上就已经写进 AGENTS.md。**How to apply**：先 grep 确认教训已在 AGENTS.md，再决定升级到哪一级；若仍走"记一条新的"，视为流程违规。

### 约束 C — precheck 是提示器，不是证明器

V1 `learnings-precheck.sh` 用**整串正则**匹配（`grep -q "$kw"`，awk `~ query`），已知缺陷：

- 子串/边界不一致：查 "CAD导出PDF" 与查 "CAD" 结果不同——查询是整串 regex，不做分词。
- 误命中：标签映射里 "MCP" → integration，会把 MCP 条目当 CAD 相关误报。
- **precheck 未命中 ≠ 该教训不存在**。未命中只说明关键词没对上，不构成"安全"证据。

因此：**V2 语义 precheck 为准**（`learnings-precheck-v2.sh`，LLM 相关度评分 ≥3/5）；V1 仅在无 OpenSpace 时作为粗筛 fallback，且必须**人工复核**。调用方不得把 V1 结果当作结论。

### 约束 D — 度量只认 v2，v1 结果不可信

V1 `learnings-metrics.sh` 用 `grep -c ... || echo 0`：无匹配时 `grep -c` 仍打印 `0` 并返回非零，`|| echo 0` 再追加一行，变量变成 `"0\n0"`，算术运算直接 `syntax error`。结果是**至少两项统计静默为空/报错**，但脚本仍在被运行。

- **禁止**把 v1 的输出用于任何决策。
- 一律使用 **V2** `learnings-metrics-v2.sh`（其 `count_pattern()` 用 `grep -c | head -1` 安全取值）。
- 若必须跑 v1，先声明"结果仅参考、已知有误"。

---

## 八步闭环

### Step 1: 预防（Precheck）— 任务前必跑

```bash
# V2 语义匹配（LLM 评分 ≥3/5 才返回）—— 默认且唯一可信
bash scripts/learnings-precheck-v2.sh "任务描述关键词"
```

- 先用标签+关键词粗筛（fast path），再用 LLM 做语义相关度评分（0-5 分）。
- 只返回 ≥3 分的条目 + 修复建议。
- precheck 命中后：先读教训 → 按 Suggested Action 避坑 → 标记 `helpful`。
- 详见**约束 C**：V1 匹配有限，未命中不是安全证明。

### Step 2: 记录（Record）

```bash
bash scripts/learnings-record-v2.sh LRN "摘要" "详情" "修复建议"
bash scripts/learnings-record-v2.sh ERR "摘要" "报错" "修复方案"
```

V2 改进：
- **首次即记**（不等 recurrence≥2）
- **自动分类**：LLM 判定 category/priority/area/tags
- **自动关联**：写入时检索相似条目，添加 `See Also`
- **去重检测**：写入前先查相似度，≥50% 提示合并而非新建

> 记录前先查 AGENTS.md 是否已有同一教训。已有 → 走**约束 B** 升级，不要再开新条。

### Step 3: 报告（Report）— 每日

```bash
# 基础健康报告
bash scripts/learnings-report.sh

# V2 LLM 叙事报告（需 OpenSpace）
# 通过 OpenSpace execute_task 生成：趋势 + 洞察 + 行动建议
```

V2 报告内容：新增/晋升/归档数量、趋势对比（与上周同期）、系统性问题识别、下一步行动建议。
报告须包含**约束 A 的回声检查结果**（promoted 是否真的可读）。

### Step 4: 度量（Metrics）— 每周

```bash
bash scripts/learnings-metrics-v2.sh --trend --action   # 唯一可信版本
```

追踪指标：
| 指标 | 计算方式 | 目标 |
|------|---------|------|
| 晋升率 | promoted / total | ≥30% |
| 重复率 | recurrence≥2 / total | ≤15% |
| 超期 pending | 待处理 >14天 | ≤5 条 |
| 库存健康度 | pending / promoted / archived 比例 | 20/30/50 |

> V1 `learnings-metrics.sh` 已知会静默算错（见**约束 D**），不得用于决策。

### Step 5: 反馈（Feedback）— 闭环验证

```bash
# precheck 命中且成功避坑
bash scripts/learnings-feedback-v2.sh helpful <ID>

# 批量晋升候选（recurrence≥3）
bash scripts/learnings-feedback-v2.sh promote-candidates

# 晋升到长期记忆
bash scripts/learnings-feedback-v2.sh promote <ID>

# 标记失效
bash scripts/learnings-feedback-v2.sh invalidate <ID> "原因"
```

> 晋升触发后**必须**走完 Step 6 的落地+回声检查，否则不算 promoted（**约束 A**）。

### Step 6: 版本化（Versionize）— 晋升即落地

晋升自动触发（三步缺一不可）：
1. **更新 AGENTS.md / MEMORY.md 正文**（这才是落地）
2. `git commit --no-verify -m "promote: <ID> — <摘要>"`
3. 状态改为 `promoted`

顺序固定：**先写正文 → 再改状态**。反了就会重演约束 A 的失败。

### Step 7: 归档（Archive）— LLM 评估后

```bash
# 自动归档（30天未复发 + 已 resolved）
bash scripts/learnings-archive.sh

# V2: 归档前 LLM 评估
# OpenSpace agent 判断：是否仍有独立价值？
# 有价值 → 保留 | 已被吸收 → 归档 | 技术变更 → expired
```

- 归档前校验：该条曾在 AGENTS.md 承接过（约束 A）才允许归档。
- 归档目录：`.learnings/archive/ERRORS-archive-YYYYMMDD.md`

### Step 8: 过期（Expire）— 自动检测

- 超过 60 天未 recurrence
- 涉及的技术/配置已不存在
- 相关教训已晋升到长期记忆
- 标记为 `invalidated`，移入 `invalidated.log`

---

## 状态流转

```
pending ──→ resolved ──→ promoted(正文落入 AGENTS.md 才算) ──→ [archived]
   │            │            │
   └──→ invalidated ←────────┘
          (技术变更/已吸收)

复发且已写入 AGENTS.md ──→ 升级硬阻断（约束 B），不再开新条
```

---

## 去重维护（每周一次）

```bash
bash scripts/learnings-dedup.sh --dry-run   # 预览
bash scripts/learnings-dedup.sh               # 交互式合并
```

---

## 库存控制

- pending 超过 20 条 → 触发晋升/归档清理
- promoted 超过 50 条 → 审查 MEMORY.md 是否需瘦身
- ERRORS.md 条目与 LEARNINGS.md 重复率 >50% → 归档 ERR 保留 LRN

---

## OpenSpace 集成

复杂分析任务通过 OpenSpace `execute_task`：

```
任务: 分析 .learnings/ 库存：
1) 语义去重（跨文件检测重复教训）
2) 晋升候选评估（recurrence + 通用性）
3) 过期检测（技术变更/长期未用）
4) 回声检查（promoted 条目是否真在 AGENTS.md 正文中）
5) 生成维护报告（JSON 格式）
```

优势：LLM 语义理解 > 关键词匹配，跨文件模式检测，自动执行维护。

---

## 文件结构

```
.learnings/
├── LEARNINGS.md          # 主库存
├── ERRORS.md             # 错误库存
├── FEATURE_REQUESTS.md   # 能力请求
├── archive/              # 归档目录
│   └── ERRORS-archive-YYYYMMDD.md
├── invalidated.log       # 过期记录
├── .metrics-history.json # 度量历史（V2 新增）
└── index.json            # 语义索引（V2 新增）

scripts/
├── learnings-precheck-v2.sh   # V2 语义 precheck（默认）
├── learnings-record-v2.sh     # V2 智能记录
├── learnings-metrics-v2.sh    # V2 效果度量（唯一可信）
├── learnings-feedback-v2.sh   # V2 自动晋升
├── learnings-dedup.sh         # V2 去重合并
├── learnings-archive.sh       # 自动归档
├── learnings-close-fr.sh      # 关闭 FR
├── learnings-precheck.sh      # V1（粗筛 fallback，匹配有局限）
└── learnings-metrics.sh       # V1（不推荐，统计会静默出错）
```

---

## 执行原则

1. **立即记录**：不等"下次"，信息会丢
2. **首次即记**：不等 recurrence，先记再说
3. **语义优先**：用 LLM 理解含义，不用关键词匹配
4. **落地才算完**：promoted 的终点是 AGENTS.md 正文（约束 A）
5. **复发即升级**：已写仍犯 → 上护栏，不再开新条（约束 B）
6. **工具须诚实**：V1 的匹配/度量局限要声明，别让调用方过度信任（约束 C/D）
7. **库存控制**：pending ≤ 20，超了触发清理
8. **自动维护**：OpenSpace 定期审计，减少人工

---

## V1 → V2 迁移

| 场景 | V1 | V2 |
|------|----|----|
| precheck | 关键词+标签匹配（整串 regex，有误判） | LLM 语义评分 ≥3/5（默认） |
| 记录 | recurrence≥2 才记 | 首次即记 + 自动分类 |
| 报告 | 纯计数 | LLM 叙事报告 + 趋势 + 回声检查 |
| 度量 | 简单计数（无匹配时静默出错） | 晋升率/重复率/健康度（安全计数） |
| 晋升 | 手动 | LLM 评估 + 一键落地 AGENTS.md |
| 归档 | 30天一刀切 | LLM 价值评估后归档 |
| 去重 | 无 | LLM 语义去重 + 合并 |
