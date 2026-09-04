<!-- handoff:begin -->
## Agent 接力协议

开工前必须先读 `.agents/tasks/current.md`。文件不存在时，或 `status` 为 `done` 且 `Next` 已清空、
现场无新的未提交改动时，视为无进行中任务，正常开工。`status` 为 `draft` 时先按
`.agents/skills/handoff/SKILL.md`「起第一根任务棒」一节处理，经用户确认后才能转 `in_progress`
并继续下面的步骤。其余情况（`in_progress`、`blocked`，或 `status: done` 但 `Next` 未清空/现场有
新的未提交改动）：

1. 在你的第一段回复里复述该任务的 **Intent** 与 **Next 第一条**，用你自己的话，不要复制原文。
2. 把同一句复述写进 frontmatter 的 `ack` 字段（一到两句、压成一行）。只说在回复里不算数——
   输出会被截断或丢弃，写进任务棒才留得下痕。
3. 若复述与文件内容有出入，停下来向用户确认，不要开始动手。
4. 若 Next 第一条的前置条件不成立，在文件的 **Open questions** 追加一条并告知用户。

任务棒只活在**任务分支**上：起一个新任务先 `git checkout -b`，主干上不应存在 `current.md`。
归档之后才能合并回主干——否则第二条任务分支合并时会撞上 `CONFLICT (add/add)`。

结束工作前必须更新 `.agents/tasks/current.md`：勾掉已完成的 Done 项、改写 Next、
把本次做出的判断追加进 Decisions、把 `hop` 加一、把 `owner` 与 `ack` 置空。

提交时带上 trailer。三行必须在同一个 `-m` 参数里、彼此换行——git 只把 message 的最后一个
段落识别为 trailer 块，拆成多个 `-m` 会让前面的降级成正文：

    git commit -m "<英文单行总结>" -m "Task-Id: <任务棒 frontmatter 里的 task>
    Hop: <当前 hop>
    Agent: <claude-code | codex | zcode | kimicode>"

`Agent` 填**你自己是哪个 CLI**，不要从任务棒的 `owner` 字段抄——那个字段记的是上一个持棒者。

`Agent` 是内部账本的归属标识。只有在符合适用规则时才填写当前 CLI 的标准标识；若准确归属与
更高优先级规则冲突，或无法合规写入，就在提交前停止，向用户说明冲突并请用户决定，不得自行声明例外。

详细规程见 `.agents/skills/handoff/SKILL.md`。
<!-- handoff:end -->
