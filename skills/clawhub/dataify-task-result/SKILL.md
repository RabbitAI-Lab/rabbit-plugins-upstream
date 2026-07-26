---
name: dataify-task-result
description: Download the JSON result for a completed Dataify scraper task by task ID. Use after $dataify-task-status reports `成功`, or when the user explicitly asks to retrieve the result for a Dataify task ID.
---

# Dataify Task Result

Retrieve one completed task's JSON result from the Dataify `/download` endpoint. Read the API key only from `DATAIFY_API_TOKEN` and never include it in output.

## Workflow

1. Require a task ID. Reuse an unambiguous task ID from the preceding task-status response when its status is `成功`.
2. If the status is unknown, query it first with `$dataify-task-status` unless the user explicitly asks to retrieve the task result directly.
3. Ensure `DATAIFY_API_TOKEN` is set. Do not ask the user to paste an API key into chat or pass one on the command line.
4. Run `scripts/download_task_result.py --task-id TASK_ID`. The script always sends `type=json`.
5. Return the JSON response. If the provider reports an error, return the provider message without retrying the task automatically.

## Commands

```bash
python3 -X utf8 scripts/download_task_result.py --task-id "TASK_ID"
```

To preview the request without downloading the result:

```bash
python3 scripts/download_task_result.py --task-id "TASK_ID" --dry-run
```

## Reference

Read `references/task_result_api.md` for request parameters and response behavior.
