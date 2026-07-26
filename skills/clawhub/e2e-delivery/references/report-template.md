# 报告模板与生成规则

## 输出

- **本地路径**：`docs/e2e-reports/<workitem-id>-<yyyymmdd>.md`（相对当前项目根目录；若不在 git 仓库则写入 `~/.claude/e2e-reports/`）
- **REDoc**：调用 `Skill(hi-docs)` 创建到 `~/.claude/e2e-delivery/config.json` 里的 `redocParentId` 目录下
- 两处产物均记录到 `session.report`

## Markdown 模板

模板中 `{{...}}` 是从 session 提取的字段。生成时全部替换为实际值。

```markdown
# 端到端交付报告：{{workItem.title}}（#{{workItem.id}}）

> **生成时间**：{{now}} · **工作项类型**：{{workItem.type}}（{{workItemTypeName}}） · **复杂度**：{{complexity.stars}}（{{complexity.label}}）

## 交付概览

- **工作项**：[#{{workItem.id}} {{workItem.title}}]({{workItem.url}})
- **仓库**：{{repo.path}} · **分支**：{{repo.branch}}
- **MR**：[#{{mr.iid}}]({{mr.url}}) · 状态 {{mr.state}}
- **提测单**：#{{testSubmission.id}}
- **开始时间**：{{startedAt}} → **完成时间**：{{completedAt}}
- **总耗时**：{{totalDuration}} · **人工阻塞时长**：{{humanWaitDuration}}
- **AI 完成步骤**：{{aiCompletedCount}} 项 · **人工介入步骤**：{{humanRequiredCount}} 项
- **自动化覆盖率**：{{automationRate}}

## 五阶段执行明细

### ① 准备
| step | 状态 | 耗时 | 备注 |
|---|---|---|---|
{{prepareTable}}

### ② 开发
| step | 状态 | 耗时 | 备注 |
|---|---|---|---|
{{developTable}}

### ③ 提交
| step | 状态 | 耗时 | 备注 |
|---|---|---|---|
{{submitTable}}

### ④ 验证
| step | 状态 | 耗时 | 备注 |
|---|---|---|---|
{{verifyTable}}

### ⑤ 交付
| step | 状态 | 耗时 | 备注 |
|---|---|---|---|
{{deliverTable}}

## 发现的问题

{{issuesSection}}
（若无失败事件，此节输出 "本次流程未发现问题"）

## 能力缺失清单

{{cliMissingSection}}
（从 session.capabilities.cliMissing 生成表格；若为空，输出 "本次流程未遇到能力缺失"）

## 附录：完整事件流

<details>
<summary>点击展开原始 events JSON</summary>

\`\`\`json
{{eventsJson}}
\`\`\`

</details>
```

## 复杂度自动评估

依据下列信号打分（每项满足加对应分数），最终取分数段：

| 信号 | 分数 |
|------|------|
| 改动文件数 > 10 | +2 |
| 改动文件数 5~10 | +1 |
| 代码行数 > 500 | +2 |
| 代码行数 100~500 | +1 |
| 涉及模块数 > 2 | +1 |
| 存在 SQL/DDL 文件变更 | +2 |
| 出现回滚事件（revert） | +2 |
| 有部署失败重试 | +1 |

分数段 → 星级：0-1 ★☆☆☆☆（简单）；2-3 ★★☆☆☆；4-5 ★★★☆☆；6-7 ★★★★☆；≥8 ★★★★★（复杂）。

`complexity.label` 取值：`简单 / 偏简 / 中等 / 偏复杂 / 复杂`。

## REDoc 同步

用 `Skill(hi-docs)` 调用其 `docs:create` 能力：

```
Skill(hi-docs) → 
  在 ~/.claude/e2e-delivery/config.json 里的 redocParentId 目录下，
  创建文档 title="端到端交付报告：<title>（#<id>）"，
  content=上面生成的 Markdown 全文（不含 title 一级标题）。
```

同步成功 → 回写 `session.report.redocShortcutId` + 输出链接给用户。
同步失败 → 在报告顶部添加提示："REDoc 同步失败：<原因>；报告已保存在本地。"
