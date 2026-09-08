# MOA HTTP Contract

Set these values in the calling service's secret/configuration system, never in browser state or source control:

```text
MOA_BASE_URL=http://moa-service.ai.biwin.com:31080
MOA_TOKEN=<server-side bearer token when authentication is enabled>
```

For local use of this package, copy `credentials.local.env.example` to `credentials.local.env` and fill the value on the local machine. The real file is ignored by Git. Prefer a platform-managed environment Secret whenever the Agent runtime supports one.

## Current Agent Service Address

This package targets the currently approved MOA Service endpoint:

```text
http://moa-service.ai.biwin.com:31080
```

The calling Agent runtime must have network and DNS access to this endpoint. Do not replace the address with a guessed IP, Kubernetes Service DNS name, or hostname.

All examples below use the common headers:

```http
Authorization: Bearer {MOA_TOKEN}
Content-Type: application/json
X-MOA-Actor: calling-service-or-user-id
```

`Authorization` is required only when the deployment has configured MOA bearer authentication. `X-MOA-Actor` is optional, but recommended for auditability.

Never print the resolved `MOA_TOKEN` or the final `Authorization` header. Redact them from HTTP debug logs and Agent responses.

## Create a Design Run

```http
POST {MOA_BASE_URL}/v1/designs
```

```json
{
  "requestId": "UPSTREAM-TASK-123",
  "multicaTask": "UPSTREAM-TASK-123",
  "prompt": "Describe the required technical design and acceptance scope.",
  "repositories": [
    {
      "name": "service-repository",
      "url": "https://git.example.internal/group/service.git",
      "commit": "0123456789abcdef0123456789abcdef01234567"
    }
  ],
  "callbackUrl": "https://caller.example.internal/api/integrations/moa/events"
}
```

`multicaTask`, `prompt`, and `repositories` are required. `requestId` is optional but should be stable across create retries. `callbackUrl` is optional, must be HTTPS, and its host must be allow-listed by MOA.

Successful creation returns HTTP `202`:

```json
{ "designId": "MOA-42", "version": 1, "status": "CREATED" }
```

This confirms persistence and queueing only.

## Track and Retrieve Results

```http
GET {MOA_BASE_URL}/v1/designs/{designId}
GET {MOA_BASE_URL}/v1/designs/{designId}/result?version={version}
```

Key terminal states:

- `READY_FOR_REVIEW`: retrieve artifacts and present them for human review.
- `APPROVED`: the approved version is frozen.
- `FAILED`: inspect and persist `lastError`; do not continue polling as though success were possible.

The result response includes `packageHash` and artifact records with relative `url` and `sha256`. Prefix each artifact URL with `MOA_BASE_URL`, use the same authorization, and verify the downloaded bytes against `sha256`. Standard final artifacts are `spec.md`, `design.md`, `cases.json`, `cases.xlsx`, `open-questions.md`, and `manifest.json`.

For an authorized operator or diagnostic Agent, sanitized invocation records are available at:

```http
GET {MOA_BASE_URL}/v1/admin/designs/{designId}/runs?version={version}
```

The response reports stage, model, attempt, duration, exit code, retry count, token usage, and parse/schema flags. It intentionally omits raw prompts, command lines, workspaces, manifests, stdout, stderr, and credentials.

## Model catalog and bounded CC checks

These endpoints are operational preflight tools, not part of ordinary design submission:

```http
GET  {MOA_BASE_URL}/v1/admin/model-center
POST {MOA_BASE_URL}/v1/admin/model-center/models/refresh
POST {MOA_BASE_URL}/v1/admin/diagnostics/claude-code/fixed-test
```

Fixed-test request:

```json
{ "model": "deepseek-v4-pro" }
```

The catalog snapshot can be empty after service restart until refreshed. Refreshing the catalog does not change the persisted seven-route configuration. A fixed test is tool-free and low effort; passing it does not prove formal Research compatibility.

## Revise and Approve

```http
POST {MOA_BASE_URL}/v1/designs/{designId}/revisions
POST {MOA_BASE_URL}/v1/designs/{designId}/approve
```

Revision request shapes:

```json
{ "baseVersion": 1, "mode": "STANDARD", "feedback": "Clarify compatibility and failure cases." }
```

```json
{
  "baseVersion": 1,
  "mode": "REBASE",
  "feedback": "Re-evaluate against the new fixed commits.",
  "repositories": [{ "name": "service-repository", "url": "https://git.example.internal/group/service.git", "commit": "fedcba9876543210fedcba9876543210fedcba98" }]
}
```

```json
{ "baseVersion": 1, "mode": "FULL", "prompt": "A materially changed design brief." }
```

- `STANDARD`: needs `baseVersion` and `feedback`; do not send `prompt` or `repositories`.
- `REBASE`: needs `baseVersion`, `feedback`, and the full repository set with changed fixed commits; do not send `prompt`.
- `FULL`: needs `baseVersion` and `prompt`; repositories are optional.

Approve only after review:

```json
{ "version": 1, "approvedBy": "reviewer-id" }
```

Both create and revision calls normally return `202`; poll status afterward.

## Error Handling

MOA errors have `{ "code", "message", "details" }`.

| Code | HTTP | Client behavior |
| --- | --- | --- |
| `MOA-1001` | 400 | Correct the request, fixed commit, or revision matrix. |
| `MOA-1002` | 401 | Refresh/check the server-side token; do not expose it. |
| `MOA-1003` | 404 | Check the design ID, version, or artifact reference. |
| `MOA-2001` / `MOA-2002` | 409 | Re-query status; stale state or version needs user/integration resolution. |
| `MOA-2004` | 429 | Apply bounded backoff; do not create unbounded retries. |
| `MOA-5001` | 503 | Service is unavailable or shutting down; retry only when authorized. |

Runner failures appear in `lastError`, including `TIMEOUT`, `NON_ZERO_EXIT`, `OUTPUT_PARSE_FAILED`, and `SCHEMA_INVALID`. `TIMEOUT` is not retried; spawn/non-zero-exit and format/schema categories may retry once. Treat the invocation ID and attempt number as authoritative.
