---
name: dataify-task-status
description: Check the execution status of a Dataify scraper task by task ID. Use when the user provides a Dataify Builder task ID, asks whether an asynchronous scraping task is still processing, or needs to determine whether a task succeeded or failed.
---

# Dataify Task Status

Query the documented Dataify `/task_status` endpoint for one task. The API key is read only from `DATAIFY_API_TOKEN` and is never included in output.

## Workflow

1. Require a task ID. Reuse an ID returned earlier in the conversation only when it is unambiguous.
2. Ensure `DATAIFY_API_TOKEN` is set. Do not ask the user to paste a key into chat or pass it on the command line.
3. Use `scripts/get_task_status.py --task-id TASK_ID` to call the endpoint. Use `--dry-run` first only when a request preview is needed; it redacts the API key.
4. Return the response body without exposing the key. Interpret documented statuses as follows:
   - `处理中`: the task has not completed.
   - `成功`: the status script immediately sends `GET /download` with the same task ID and `type=json`, then prints the JSON result.
   - `失败`: the task finished with an error.
5. For a failed or unauthorized request, return the provider response and recommend checking the task ID and account access. Do not retry paid tasks automatically.

## Commands

```bash
python3 -X utf8 scripts/get_task_status.py --task-id "TASK_ID"
```

To verify parameters without making a request:

```bash
python3 scripts/get_task_status.py --task-id "TASK_ID" --dry-run
```

## Reference

Read `references/task_status_api.md` for endpoint parameters, response fields, and HTTP error behavior.
