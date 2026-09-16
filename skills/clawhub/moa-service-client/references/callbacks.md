# MOA Callback Guide

Multica asynchronous mode separates submission and finalization into two Agent Runs.

## Submission Run

Create the MOA task with the Multica Issue UUID:

```json
{
  "requestId": "<stable-id>",
  "multicaTask": "<stable-id>",
  "issueId": "<Multica Issue UUID>",
  "prompt": "...",
  "repositories": ["..."]
}
```

Persist the returned `designId` and end after HTTP `202`. Do not call `wait` from the same Agent Run.

## Completion callback

After the initial MOA pipeline stops, including terminal failure, MOA sends:

```http
POST http://multica-api.ai.biwin.com:31080/api/integrations/moa/events
Authorization: Bearer <MULTICA_MOA_CALLBACK_TOKEN>
Content-Type: application/json
```

```json
{
  "event": "design.ready",
  "issue_id": "<Multica Issue UUID>",
  "moa_task_id": "<MOA designId>"
}
```

The event is a wake-up signal, not a success assertion. The callback-woken Agent must query `GET /v1/designs/{designId}` and branch on the returned status.

- `READY_FOR_REVIEW` or `APPROVED`: retrieve artifacts and verify every SHA-256.
- `FAILED`: report the structured `lastError`; do not request result artifacts.
- Any execution state: treat as a race, query again with a bounded retry instead of creating another task.

Multica deduplicates by `event + issue_id + moa_task_id`. A duplicate returns HTTP `202` with `comment_created=false` and does not wake another Agent. MOA retries network failures and 5xx with exponential backoff. It does not retry 4xx automatically; correct the UUID, token, task ID, or route before replaying the persisted event.

The current Multica contract does not include a version in its idempotency key, so Revision completion is not callback-driven. Use explicit status lookup for Revision until the receiver publishes a versioned event contract.
