# 操作、字段与结果

请求 JSON 不超过 256 KiB；日期范围最多 31 天，最多 50 名员工、10 个班次、1000 个岗位槽位。

## 生成排班

必填 `title`、`start_date`、`end_date`、`timezone`、`members`、`shifts`；`timezone` 使用 IANA 名称。

- 每个 `members` 项：包含 `member_id`、`name`，可选 `unavailable_dates`、`maximum_shifts`。
- 每个 `shifts` 项：包含 `shift_key`、`name`、`start`、`end`、`required_count`；跨午夜班次允许 `end` 早于 `start`。
- `rules` 字段：包含 `maximum_consecutive_days`、`minimum_rest_hours`、`maximum_shifts_per_member`。

结果 `schedule` 始终含 `schedule_id`、`version`、`assignment_count`、`unfilled_count`，并分别返回最多 25 项 `assignments`（排班分配）与 `unfilled`（未排班项）预览；对应 `*_truncated:true` 时通过 `schedule.export` 获取完整 PDF/CSV。无法满足的槽位以 `no_eligible_member`（无符合条件的人员）写入 `unfilled` 字段，任务状态为 `partial`（部分成功），不得隐藏或伪造人员填补。

## 读取排班

请求仅含 `schedule_id`，返回最新的结构化排班；读取免费。

## 更新排班

请求含 `schedule_id`、`expected_version`、`changes.assignments`。必须提交所有日期和班次的完整 `assignments`；平台重新验证不可用日期、每天一班、`maximum_shifts`、`maximum_shifts_per_member`、`minimum_rest_hours`、`maximum_consecutive_days` 和 `required_count`。成功后将 `version` 加一。

## 导出排班

请求仅含 `schedule_id`、`expected_version`，返回 `schedule-pdf` 与带 UTF-8 BOM 的 `schedule-csv` 产物。
