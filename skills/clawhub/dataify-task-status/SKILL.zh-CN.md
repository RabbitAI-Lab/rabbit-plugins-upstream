---
name: dataify-task-status
description: 根据任务 ID 查询 Dataify scraper 异步任务状态。用户提供 Dataify Builder 任务 ID、询问抓取任务是否完成，或需要确认任务成功、处理中或失败时使用。
---

# Dataify 任务状态查询

通过已创建的任务 ID 查询 Dataify `/task_status` 接口。API Key 仅从 `DATAIFY_API_TOKEN` 环境变量读取，绝不输出。

## 工作流

1. 要求提供任务 ID；仅在上下文中的任务 ID 明确时复用。
2. 确认环境变量 `DATAIFY_API_TOKEN` 已设置；不要要求用户在聊天中粘贴 Key，也不要通过命令行传递 Key。
3. 运行 `scripts/get_task_status.py --task-id TASK_ID`。需要预览时使用 `--dry-run`，其输出会脱敏 API Key。
4. 根据响应中的 `data.status` 返回状态：`处理中` 或 `失败` 时返回状态；返回 `成功` 时，状态查询脚本会使用同一任务 ID 立即发送 `GET /download` 请求并输出 `type=json` 的结果。
5. 对失败或无权限响应，返回服务方错误并建议检查任务 ID 和账户权限；不要自动重试付费任务。

## 命令

```bash
python3 -X utf8 scripts/get_task_status.py --task-id "TASK_ID"
```

参数和响应详情见 `references/task_status_api.md`。
