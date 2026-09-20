# 进度追踪说明（progress-tracker）

> Skill 的进度数据源是 `<workspace>/.workbuddy/psychology-study/progress.json`。
> 本文件说明读写约定，供处理器遵循（完整结构见 `schemas/progress-schema.json`）。

## 读写约定
- **读**：每次对话开始先 Read 该 JSON；不存在→视为新用户进 Onboarding。
- **写**：只在处理器末尾做一次 Write；先读最新内容、合并变更再写回。
- **容错**：解析失败→备份为 `progress.json.bak` 并以空 state 重建。

## 关键字段更新点（速查）
| 事件 | 字段变化 |
|---|---|
| Onboarding 完成 | 创建 userConfig / currentStage（按 levelOffset 映射）/ modules 初值 / milestones |
| 学完一个概念 | modules.theory.completed+1（确认懂了） |
| TPR 练习结束（出报告） | stats.practiceCount+1；modules.counseling.completed+1；stats.dialogues+1 |
| 逐字稿分析完成 | stats.analyses+1；modules.counseling.completed+1（触发点「对话分析」）；cases 首次 +1 |
| 认知记录完成（record） | modules.counseling.completed+1（触发点「认知记录」，首次达标）；logs[] 追加 |
| 心情打卡（record） | moodLog[] 追加 {date, mood, energy, note} |
| 自测记录 | stats.assessments+1；assessments[] 追加 |
| 写完阶段总结 | stageSummary=文本；stageCompleted=true；stats.reflections+1；推进下一阶段 |
| 读完一书 | stats.booksRead+1；readings[] 追加 |
| 费曼输出 | stats.feynmanOutputs+1 |
| 任意学习动作 | 按 XP 表加 xp 并计算 level（见 SKILL.md §10）；daily 时按日期去重累计 stats.totalDays；必要时更新 learnerProfile |
| 任意写后 | checkMilestones：达标里程碑 reached=true |

> **备注**：stats.dialogues 仅统计练习对话（结束一次练习 +1）；stats.analyses 独立统计对话分析篇数；里程碑 m4（完成第一次对话分析）以 stats.analyses>=1 为准（与 roadmap.json 一致）。

## 与独立进度页面的关系
- `学习进度汇总.html` 用 localStorage，是独立可视化工具。
- Phase 2+：Skill 可导出 JSON 供该页面导入（用户手动同步）。
- MVP：Skill 负责记录/查询，HTML 作高级视图。
