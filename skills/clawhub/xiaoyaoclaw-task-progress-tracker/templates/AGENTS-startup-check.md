# 任务续跑检查（xiaoyaoclaw-task-progress-tracker 配套段）

> 追加到 AGENTS.md 的「Session Startup」章节，位于启动必读列表之后。

## Session Startup（追加）

5. **任务续跑检查**：扫描 `tasks/` 与 `projects/` 下的 `PROGRESS.md`；存在状态为「进行中」的 → 读取并向用户汇报（未完成任务 + 各自进度 + 下一步）；用户确认前不擅自继续执行。

> 规则细节见技能 `xiaoyaoclaw-task-progress-tracker` 的 SKILL.md（Step 3 完成即写 / Step 4 恢复 / Step 5 归档）。