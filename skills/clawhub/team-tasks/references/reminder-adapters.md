# 调度适配器契约

`team-tasks` 不调度或发送通知。调度平台适配器负责保存规则、调用提醒解析器和投递消息；台账仍是提醒内容及状态的唯一事实源。

## 规则与关联

适配器应在自身受保护的配置存储中维护关联，不写入任务对象：

```json
{
  "taskId": "T-260918-001",
  "reminderJobIds": ["scheduler-job-123"],
  "oneShot": false
}
```

专项规则只能保存 `taskId`、调度表达式、投递目标引用和 `oneShot`；不得缓存标题、负责人、截止日期、状态或提醒正文。规则触发时调用：

```sh
python3 scripts/reminder_engine.py --data-dir /local/team-tasks \
  --task-id T-260918-001 --slot 2026-09-18T14:00+08:00 \
  --delivery-reference channel-ref --reserve
```

仅当 JSON 输出的 `action` 为 `deliver` 时发送 `text`。`silent`（任务结束、暂停、消失、重复占位或状态竞争）必须不投递旧文本。`taskId + slot` 是外部发送方的幂等键。

## 同步 outbox

`create`、`update`、`status`、`reopen`、`comment` 成功提交时，会与任务变更原子地把事件写入主台账的 `_reminderSyncEvents`。适配器 worker 使用：

```json
{"op":"sync_claim","actor":"scheduler-adapter","limit":20,"leaseSeconds":300}
```

处理成功后才确认：

```json
{"op":"sync_ack","actor":"scheduler-adapter","eventIds":["event-id"]}
```

租约过期后事件可由其他 worker 重试；适配器必须按事件 ID 去重自己的外部修改日志。处理事件时再读取当前台账，不应相信事件中的旧字段。结束任务的 one-shot 规则应禁用；周期规则可保留，但每次运行前仍需动态解析。仅改标题、负责人或评论时不改写规则正文。

## 迁移 dry-run

适配器先导出规范化规则 JSON，例如：

```json
{"rules":[{"id":"job-1","taskId":"T-260918-001","oneShot":true,"dynamic":false}]}
```

再运行：

```sh
python3 scripts/reminder_migration.py --data-dir /local/team-tasks --rules exported-rules.json
```

它只输出报告，不访问、创建、禁用或删除任何规则。无显式 `taskId`、或 ID 在活动台账中不存在的规则被列为孤儿并建议暂停；绝不根据标题猜测关联。适配器应先备份规则，人工确认报告后再执行变更并保留回退副本。
