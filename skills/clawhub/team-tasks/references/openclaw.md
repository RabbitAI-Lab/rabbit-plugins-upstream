# OpenClaw 可选适配

这是一个可选接入，不是 `team-tasks` 的运行时依赖。安装者应在 OpenClaw Gateway 所在主机实现一个受控适配器，并自行提供身份验证、规则备份和通知授权。

每个专项 automation/cron 的 prompt 或受保护元数据只保存 task ID、触发规则与投递引用。运行时调用 `reminder_engine.py --task-id ... --reserve`，只有 `action=deliver` 才发送返回的文本。不要把任务标题、负责人或截止日期固化在 prompt。

适配器 worker 消费 `sync_claim` 事件，并在执行外部 cron 改动前重新读取 `task_store.py read`：

- `done` / `cancelled`：禁用关联的一次性规则；周期规则留存但动态解析会静默。
- 截止时间变化：仅在该平台规则语义确实是精确定时且规则声明可更新时更新调度时间。
- 其他任务字段变化：不更新静态文本，因为规则不应包含静态文本。

将每次 OpenClaw API/CLI 调用的事件 ID、规则 ID、结果和错误写入适配器自身审计日志；只有外部操作成功后才 `sync_ack`。不要把 Gateway URL、token、群组 ID 或用户 ID 放入本技能或公开的规则导出文件。
