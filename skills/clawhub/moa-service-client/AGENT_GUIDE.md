# MOA Service Agent Guide

This is the framework-neutral entrypoint for any AI Agent that must call MOA Service. It works as project knowledge, system instructions, or a runbook and does not require Codex, Claude Code, MCP, or a particular SDK. If the Agent supports Skills, `SKILL.md` routes to the same workflow.

## What MOA does

MOA converts a detailed design brief plus repositories pinned to exact commits into a versioned technical-design package:

- `spec.md`
- `design.md`
- `cases.json`
- `cases.xlsx`
- `open-questions.md`
- `manifest.json`

The fixed workflow is three parallel Research calls, Research Merge, Project Analysis, three parallel Design calls, Judge, Cases, and programmatic rendering. MOA is read-only: it does not modify business code, create commits, push Git, run CI, execute SQL, deploy services, or approve its own result.

## Configuration

The approved service address is:

```text
MOA_BASE_URL=http://moa-service.ai.biwin.com:31080
```

Protected APIs require `Authorization: Bearer <MOA_TOKEN>`. Resolve the token from the runtime environment first, then this installed package's `credentials.local.env`. Never print the resolved value or Authorization header. The included Python client follows this rule automatically.

If this package has been copied without its local credential file and `MOA_TOKEN` is absent, stop and ask the operator to provision the token in the Agent runtime. Do not ask for it in chat.

## Inputs that must exist before submission

1. A concrete design brief with scope, constraints, acceptance criteria, and explicit exclusions.
2. At least one read-only HTTP(S) Git repository URL.
3. An exact 40-character lowercase commit SHA for every repository. Branches and tags are forbidden because they move.
4. A stable correlation ID.

When there is no Multica task, create a stable local ID such as:

```text
LOCAL-<owner>-<YYYYMMDD>-<short-id>
```

Use it for both `requestId` and `multicaTask` throughout the run. If the work later receives an upstream task ID, record a mapping; do not rewrite historical MOA artifacts.

## Fastest reliable execution

From this package directory, first run:

```text
python scripts/moa_client.py doctor
```

Require `/ready` to report `ready=true`, production `runnerBackend=claude-code`, and ready `db`, `repo_cache`, and `claude_code` dependencies.

Save the brief to a UTF-8 text or Markdown file, then execute:

```text
python scripts/moa_client.py run \
  --request-id LOCAL-alice-20260825-cache \
  --prompt-file design-brief.md \
  --repo biwin-cowork=http://172.17.24.20:8002/ai-group/biwin-cowork.git@2225aea7cb6c4df549aa84abe7f731ef6778a32a \
  --out moa-output
```

On PowerShell, place the command on one line or use PowerShell backticks instead of backslashes. Multiple `--repo` arguments are allowed.

The command:

1. validates repository URL and commit syntax;
2. submits `POST /v1/designs`;
3. persists the returned `designId` in its output;
4. polls until a terminal status, with a four-hour client wait ceiling;
5. stops immediately on `FAILED` and prints `lastError`;
6. on success, downloads all artifacts and verifies every SHA-256.

The client wait timeout never cancels the server run. If the client stops waiting, query the saved `designId` rather than creating a duplicate blindly.

## Manual commands

Use these when the combined `run` command is not appropriate:

```text
python scripts/moa_client.py create --request-id <id> --prompt-file <file> --repo <name>=<url>@<sha>
python scripts/moa_client.py status <designId>
python scripts/moa_client.py wait <designId>
python scripts/moa_client.py runs <designId>
python scripts/moa_client.py result <designId> --out <directory>
```

`create` returning HTTP `202` means queued only. Never report success until the server reaches `READY_FOR_REVIEW` or `APPROVED` and artifacts verify successfully.

## Model-routing preflight

Ordinary callers should not change routing. An operator or acceptance Agent should perform this preflight after deployment or whenever any model changes:

```text
python scripts/moa_client.py models --refresh
python scripts/moa_client.py fixed-test --model <each-distinct-routed-model>
```

The model catalog is an in-memory snapshot and can be empty immediately after a Pod restart. Refreshing it does not change routing. Confirm all seven routed values appear in the refreshed list.

A fixed test proves only basic tool-free model reachability. It does not prove compatibility with the formal Research Profile, which also uses repository tools, web tools, high effort, and JSON Schema. Require a new full run after any route change.

Read `references/operations.md` for the currently validated route and the evidence behind it.

## Status and failure handling

Terminal states:

- `READY_FOR_REVIEW`: artifacts exist and await human review.
- `APPROVED`: an explicitly reviewed version is frozen.
- `FAILED`: retain `lastError`; stop waiting and diagnose the failed stage.

Use sanitized run records:

```text
python scripts/moa_client.py runs <designId>
```

They provide invocation ID, stage, model, duration, retry count, exit code, and error category without exposing prompts, credentials, workspaces, or raw command lines.

Interpret evidence before changing configuration:

- `TIMEOUT` ends at `attempt-1`; timeouts are not retried. Compare duration with the stage budget.
- `NON_ZERO_EXIT` can retry once. Two failures within seconds for one model while peer models succeed point to Profile/model compatibility, not a short timeout.
- `OUTPUT_PARSE_FAILED` or `SCHEMA_INVALID` can retry once with a correction Prompt.
- Repository errors occur before model work. Caller-side Git reachability does not prove the MOA Pod can clone the repository.

Do not resubmit indefinitely. One deliberate rerun is appropriate only after changing the demonstrated external cause, such as model routing, repository reachability, or a malformed brief.

## Result handoff

A complete report contains:

- `designId`, version, terminal status, and wall-clock duration;
- exact repository URL and commit for each repository;
- the stage/model/duration table and retry count;
- six artifact names with verified SHA-256 values;
- `packageHash` and model-routing snapshot;
- any route or catalog action performed before the run.

Research and Design lanes are parallel. Do not present the sum of invocation durations as wall-clock duration.

## Revisions and approval

Read `references/http-contract.md` before revision or approval.

- `STANDARD` revises a complete design from feedback.
- `REBASE` advances repository commits and reruns repository-dependent stages.
- `FULL` uses a materially changed brief.
- Every revision creates a new version.
- Approval is never automatic. Approve only the current `READY_FOR_REVIEW` version with explicit reviewer authorization.

For callback integration, read `references/callbacks.md`. Polling remains required as compensation for delayed, duplicate, or missing callbacks.
