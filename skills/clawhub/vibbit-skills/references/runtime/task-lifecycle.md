# Task lifecycle and recovery

Create with `POST /tasks` and query with `GET /tasks/{task_id}`. Translation editing uses `PUT /tasks/{task_id}/translation`; storyboard approval uses `POST /tasks/{task_id}/storyboard/confirm`. These mutate existing tasks, not create new parents. Determine synchronous/asynchronous behavior from the response; require both HTTP success and business `code=200`.

## Submission and journals

Resolve essential inputs/downstream dependencies and submit once within the authorized scope. The client creates a journal before submission under `.vibbit/tasks/<random-id>.json` in the working directory. `--state` selects a new file; `VIBBIT_STATE_DIR` changes the directory.

Records contain command, environment, input digest, stage, task ID, and request ID. Translation also stores mode, source-URL hashes, and expected languages. Keys, complete prompts, media URLs, and temporary upload credentials are excluded. Records are not server idempotency keys.

| State | Action |
| --- | --- |
| SUBMITTING / SUBMIT_UNKNOWN without task_id | Preserve journal/request_id and investigate acceptance; do not resubmit |
| MUTATION_UNKNOWN | Preserve parent ID; do not repeat the write. Successful GET alone cannot prove an uncertain mutation applied |
| REJECTED | Correct the cause; decide on a new request within original task/cost scope |
| ACKNOWLEDGED / PENDING / RUNNING | Save task_id and query only |
| COMPLETED | Parse `task_result.result` and verify result type/media |
| FAILED | Report actual cause/IDs; do not regenerate automatically |
| INSUFFICIENT_POINTS | Terminal failure: stop polling, retain exact state/IDs, resolve balance before deciding on another task |

## Waiting

~~~bash
node "$VIBBIT_SKILL_DIR/scripts/vibbit.js" status --task-id task-RETURNED_ID
node "$VIBBIT_SKILL_DIR/scripts/vibbit.js" wait --task-id task-RETURNED_ID --timeout-seconds 50
node "$VIBBIT_SKILL_DIR/scripts/vibbit.js" resume --state /absolute/path/task-record.json
~~~

Each wait defaults to 50 seconds. Poll Seedance at least 5 seconds apart, subtitle removal at least 10 seconds, and unknown types conservatively at 10 seconds. The client raises shorter intervals to the minimum. Retry transient read-only failures/rate limits within the deadline. Each request is bounded by 30 seconds and the remaining wait budget. Exit 3 means this wait expired, not failure/cancellation.

Let the client complete a wait window instead of replanning, rereading the same documents, or authenticating at every poll. If the host supports concurrency, perform authorized independent asset preparation while waiting; dependent generation still waits for its input. Change the plan when status, a concrete error, or required input warrants it. For timing diagnosis, add stage start/end times, generation counts, and wait/production/check categories to existing records without credentials or full requests.

Follow work to a terminal state. After 10 minutes of continuous waiting, return the recoverable ID/journal and explain processing continues; do not promise unsupported background work. Longer requested follow-up continues the same task. Interrupting local waiting does not cancel the server task. No general cancellation, webhook, or idempotent-submission contract is defined.

## Results

Parse the outer result and breakdown `sub_results[].result`. Translation extracts final `output_video_url` from items/results_by_language and preserves successful videos even when the parent is FAILED or INSUFFICIENT_POINTS. Check all children; do not describe partial completion as complete success.

Project URLs are entry points. For analysis, distinguish artifact roles source / analysis_segment / reference from generated. Even generated media and COMPLETED require quality review. Unknown status, non-JSON, or completion without results is a protocol problem; retain IDs.

For synchronous responses without IDs, results are returned but not journaled. Save needed outputs in the current task; repeating POST is not recovery.

Exit codes: 0 success/accepted; 1 service/execution/protocol error; 2 input/configuration; 3 wait expired; 4 uncertainty/recovery impossible without ID; 5 partial failure with successful outputs.

[Credits/limits](limits-and-credits.md) · [Troubleshooting](troubleshooting.md)

## Translation review and mutations

Set `auto_translate=true` explicitly for automatic production. Manual mode (false) returns `review_context_required` and hands control back after at most one successful recovery query.

If `task_result.result` contains a review phase and allowed details, output includes `review_visibility=available` and `review`; otherwise unavailable. This is client visibility, not the server phase. RUNNING/progress alone cannot establish readiness; 100% may include failures. Follow [translation](../capabilities/processing/video-translation.md).

Edits/approvals create separate journals without overwriting creation records. Resume only sends GET, never replays PUT/POST. After explicit batch approval, use its returned journal; one-item approval may leave others pending. The original record's review_mode is unchanged by other records. `mutation_outcome` records whether the write received a definite response.

Large integers in outer/nested JSON retain precision. Public outputs use strings for large IDs; validated long fields are sent as exact integer tokens. Avoid JSON tools that round them.
