---
name: dataify-task-result
description: 根据任务 ID 下载已完成的 Dataify scraper 任务 JSON 结果。当 $dataify-task-status 返回 `成功`，或用户明确要求获取指定 Dataify 任务 ID 的结果时使用。
---

# Dataify 任务结果下载

从 Dataify `/download` 接口获取单个已完成任务的 JSON 结果。API Key 仅从 `DATAIFY_API_TOKEN` 环境变量读取，绝不输出。

## 工作流

1. 要求提供任务 ID；当上一轮任务状态查询明确返回 `成功` 时，可以复用该 ID。
2. 状态未知时，优先用 `$dataify-task-status` 查询；但用户明确要求直接获取结果时可以直接下载。
3. 确认环境变量 `DATAIFY_API_TOKEN` 已设置；不要要求用户在聊天中粘贴 Key，也不要通过命令行传递 Key。
4. 运行 `scripts/download_task_result.py --task-id TASK_ID`。脚本固定传递 `type=json`。
5. 返回 JSON 响应。服务方返回错误时，返回错误信息但不要自动重试任务。

## 命令

```bash
python3 -X utf8 scripts/download_task_result.py --task-id "TASK_ID"
```

接口细节见 `references/task_result_api.md`。
