# Self-Improving Agent V2 — OpenSpace 优化版

> 八步学习法 + LLM 语义分析 + OpenSpace 自动维护

## 八步闭环（优化后）

| 步骤 | 旧版 | 优化版 | 工具 |
|------|------|--------|------|
| 1. 预防 | 关键词匹配 | **语义搜索**（LLM 匹配相关教训） | `learnings-precheck-v2.sh` |
| 2. 记录 | recurrence≥2 才记 | **首次即记** + LLM 自动分类/关联 | `learnings-record-v2.sh` |
| 3. 报告 | 纯计数统计 | **LLM 叙事报告**（趋势+洞察+建议） | OpenSpace agent |
| 4. 度量 | 简单计数 | **效果追踪**（错误率变化、晋升率、复发率） | `learnings-metrics-v2.sh` |
| 5. 反馈 | 手动 promote | **LLM 自动评估**晋升候选 + 一键固化 | `learnings-feedback-v2.sh` |
| 6. 版本化 | 裸 git commit | **智能 commit**（带上下文+影响范围） | 同上 |
| 7. 归档 | 30天一刀切 | **LLM 价值评估**后再归档 | OpenSpace agent |
| 8. 过期 | 手动标记 | **LLM 自动检测**过时教训 | OpenSpace agent |

## 新增能力

- **语义去重**：LLM 判断两条是否同一教训，自动合并
- **自动关联**：新记录自动链接相关条目（See Also）
- **模式检测**：跨条目发现系统性问题
- **效果验证**：追踪"记录后是否真的没再犯"

---

## 文件结构

```
.learnings/
├── LEARNINGS.md          # 主库存（LRN + promoted 标记）
├── ERRORS.md             # 错误库存
├── FEATURE_REQUESTS.md   # 能力请求
├── archive/              # 归档目录
│   └── ERRORS-archive-YYYYMMDD.md
└── index.json            # 新增：语义索引（LLM 生成）

scripts/
├── learnings-precheck-v2.sh   # 语义 precheck
├── learnings-record-v2.sh     # 智能记录
├── learnings-metrics-v2.sh    # 效果度量
├── learnings-feedback-v2.sh   # 自动晋升
├── learnings-dedup.sh         # LLM 去重合并
└── learnings-llm-analysis.js  # OpenSpace MCP 客户端
```

---

## Step 1：语义预防（Precheck V2）

旧版用关键词+标签匹配，命中率低。V2 用 LLM 做语义相关度评分。

```bash
# 用法：bash scripts/learnings-precheck-v2.sh "任务描述"
# 内部：调用 OpenSpace 对每条历史教训做 0-5 分相关度评分，只返回 ≥3 分的
```

## Step 2：智能记录（Record V2）

旧版 recurrence<2 不记，导致首次教训丢失。V2：
- 首次即记（recurrence=1）
- LLM 自动判定 category/priority/tags
- 自动关联已有条目（See Also）
- 自动检测是否与现有条目重复

## Step 3：LLM 报告（OpenSpace Agent）

每日报告不再只是计数，而是：
- "本周 WSL 相关教训新增 3 条，建议关注 npm 多目录问题"
- "LRN-20260928-001 已晋升但 AGENTS.md 未更新，建议同步"
- "ERRORS.md 中 5 条 resolved 但未归档"

## Step 4：效果度量（Metrics V2）

追踪核心指标：
- **错误复发率**：同类错误重复出现的比例（目标：持续下降）
- **晋升率**：pending → promoted 的转化比例
- **预检命中率**：precheck 后实际避坑的比例
- **库存健康度**：pending / promoted / archived 的比例

## Step 5：自动晋升（Feedback V2）

LLM 评估晋升候选：
1. 读取 recurrence≥3 的 pending 条目
2. LLM 判断：是否通用教训？是否值得写入 AGENTS.md/MEMORY.md？
3. 自动生成晋升文案 + 更新目标文件 + 改状态为 promoted
4. 一键 git commit

## Step 6：智能归档（OpenSpace Agent）

LLM 评估每条待归档条目：
- 教训是否已被 MEMORY.md 吸收？→ 直接归档
- 仍有独立价值？→ 保留
- 技术环境已变化？→ 标记 expired

## Step 7：过期检测（OpenSpace Agent）

定期扫描：
- 条目涉及的技术/配置是否仍存在？
- 相关教训是否已晋升到长期记忆？
- 超过 60 天未 recurrence 且无晋升价值？

---

## OpenSpace 集成

核心维护任务通过 OpenSpace `execute_task` 执行：

```json
{
  "tool": "execute_task",
  "arguments": {
    "task": "分析 .learnings/ 库存：1) 找出重复条目建议合并 2) 识别晋升候选 3) 检测过时条目 4) 生成维护报告",
    "workspace_dir": "/mnt/c/Users/Admin/.openclaw/workspace"
  }
}
```

优势：
- LLM 理解语义，不是盲匹配
- 可以跨文件分析模式
- 自动生成结构化输出
- 可定时执行（cron 触发）

---

## 状态流转（V2）

```
pending → resolved → promoted → [archived]
   ↓          ↓         ↓
invalidated  archived  expired
```

新增状态：
- `resolved`：已解决但未晋升（等待 LLM 评估）
- `expired`：技术变更导致失效（自动检测）

---

## 执行原则

1. **首次即记**：不等 recurrence，先记再说
2. **语义优先**：用 LLM 理解含义，不用关键词匹配
3. **自动维护**：OpenSpace 定期审计，减少人工
4. **效果闭环**：记录→验证→晋升/归档，每条都有归宿
5. **库存控制**：pending 不超过 20 条，超了触发清理
