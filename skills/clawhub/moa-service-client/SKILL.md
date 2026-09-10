---
name: moa-service-client
description: Call the internal MOA Service to create repository-pinned technical designs, monitor asynchronous runs, diagnose stage/model failures, and download verified artifacts. Use for MOA design execution or integration, not for implementing the resulting design or changing MOA deployment.
metadata:
  short-description: Run and verify MOA technical-design workflows
---

# MOA Service Client

Use MOA as an asynchronous, read-only technical-design service. It consumes a detailed brief plus repositories pinned to exact commits and returns a versioned review package. It does not edit repositories or implement the design.

## First use

1. Read [AGENT_GUIDE.md](AGENT_GUIDE.md). It is also the standalone entrypoint for Agents that do not support Skills.
2. Run `python scripts/moa_client.py doctor` before the first business request.
3. For an operator-led end-to-end test or after model routing changed, read [references/operations.md](references/operations.md) and complete its model preflight. A basic fixed Prompt test does not prove compatibility with tools, high effort, and JSON Schema.
4. Read [references/http-contract.md](references/http-contract.md) when constructing requests directly instead of using the client script.

## Required workflow

- Require a meaningful design brief and at least one HTTP(S) repository URL pinned to an exact 40-character lowercase commit SHA. Never substitute a branch or tag.
- Resolve the bearer token from `MOA_TOKEN` or this installed package's ignored `credentials.local.env`. Never print or return the token or Authorization header.
- Use a stable `requestId`; persist the returned `designId` and poll status. A `202` response means queued, not complete.
- Stop polling only at `READY_FOR_REVIEW`, `APPROVED`, or `FAILED`. On failure, report `lastError` and inspect the sanitized run records when authorized.
- On success, download all result artifacts, verify every advertised SHA-256, and retain the `packageHash` with the repository snapshot and model-routing snapshot.
- Never approve automatically. Approval requires explicit review authorization.

For the normal create-wait-download path, prefer:

```text
python scripts/moa_client.py run --request-id <stable-id> --prompt-file <brief.md> --repo <name>=<url>@<40-char-sha> --out <directory>
```

The current approved endpoint is already the script default: `http://moa-service.ai.biwin.com:31080`.

## Failure decision rule

Do not treat all failures as timeout problems. Use the stage, model, attempt, duration, and error code together:

- `TIMEOUT` at `attempt-1`: the stage exhausted its one continuous budget; it is not retried.
- `NON_ZERO_EXIT` twice within seconds for one model while peers succeed: suspect formal Profile/model compatibility before increasing timeouts.
- A fixed CC test proves only basic model reachability. Formal Research additionally uses tools, high effort, repository context, and JSON Schema.
- Changing model routing does not repair an existing run; submit a new run and verify its immutable routing snapshot.

Use [references/operations.md](references/operations.md) for the tested baseline, diagnostics, timeout expectations, and failure playbook. Read [references/callbacks.md](references/callbacks.md) only when implementing a callback receiver.
