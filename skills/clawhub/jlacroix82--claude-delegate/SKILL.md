---
name: claude-delegate
version: 0.1.0
description: Delegate coding, repository analysis, file edits, test runs, or code review to the local Claude Code CLI without embedding an Anthropic API key. Works with Claude Pro/Max/Enterprise accounts that authenticate via OAuth and have no API key. Invokes claude -p with the existing Claude CLI login and returns Claude's final output.
license: MIT
metadata: {"openclaw":{"requires":{"bins":["claude"]}}}
---

# Claude Delegate

Use this skill when the user wants OpenClaw to hand a coding or repository task to Claude Code and receive a result back. It is meant for local, trusted operator setups where `claude` is already installed and signed in.

## Preconditions

- `claude` (Claude Code CLI) is installed on `PATH`.
- Claude CLI has already been authenticated by the operator with `claude auth login` (browser OAuth — works for Pro, Max, and Enterprise accounts). **No API key is required or used.** Enterprise accounts sign in with their org credentials/SSO; some orgs route through a corporate gateway (`claude gateway --config`), which the CLI handles automatically once configured.
- Do not ask the user for an API key.
- Run inside the target repository or pass `--cwd`.
- OpenClaw must allow this agent to use `exec` for the wrapper script.

If Claude is not authenticated, tell the operator to run `claude auth status` then `claude auth login` once and complete the browser sign-in. Do not request, print, copy, or inspect `~/.claude/.credentials.json`.

## Wrapper

Prefer the bundled wrapper:

```bash
{baseDir}/scripts/claude-delegate.sh --cwd /path/to/repo --prompt "summarize the repository and list the riskiest files"
```

For file creation or edits (auto-accept workspace edits):

```bash
{baseDir}/scripts/claude-delegate.sh \
  --cwd /path/to/repo \
  --sandbox workspace-write \
  --prompt "Create docs/architecture.md explaining the current service layout."
```

For machine-readable event logs while still returning the final Claude answer:

```bash
{baseDir}/scripts/claude-delegate.sh \
  --cwd /path/to/repo \
  --sandbox workspace-write \
  --json-log .openclaw/claude-runs/last.jsonl \
  --output .openclaw/claude-runs/last.md \
  --prompt "Review the auth changes and fix any failing tests."
```

To pass CLI-style context:

```bash
npm test 2>&1 | {baseDir}/scripts/claude-delegate.sh \
  --cwd /path/to/repo \
  --sandbox workspace-write \
  --prompt "Summarize the failing tests and make the smallest safe fix."
```

Use `--prompt-file path` when a generated prompt is already on disk. Use `--stdin-file path` when another tool wrote context to a file. Use `--allowed-tools "Read,Edit,Bash(git *)"` to restrict which tools Claude may call, and `--model sonnet` (or `opus`) to pick a model.

## Delegation Workflow

1. Restate the exact Claude task in one compact prompt.
2. Choose the narrowest permission level:
   - `read-only` (maps to Claude `plan` mode) for analysis, review, summaries, planning.
   - `workspace-write` (maps to `acceptEdits`) for creating or editing files in the repo.
   - `danger-full-access` (maps to `bypassPermissions`) only on an isolated machine/container with explicit operator approval.
3. Run the wrapper from the repository root or with `--cwd`.
4. Return Claude's final answer to the user.
5. If edits were allowed, inspect `git diff --stat` and relevant diffs before claiming files were changed.

## Safety Rules

- Never pass `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, or raw tokens to Claude. The wrapper unsets API-key env vars before invoking `claude`, forcing the saved OAuth login.
- Never read, reveal, summarize, or copy `~/.claude/.credentials.json`.
- Do not run this skill from public or untrusted chat channels.
- Do not give Claude secrets, credentials, private keys, or production data unless the operator explicitly approved that exact data flow.
- Prefer an isolated checkout or git worktree for write tasks.
- Treat Claude output as another agent's report; verify important claims locally.

## Failure Handling

- `claude: command not found`: ask the operator to install Claude Code CLI (`claude install` or npm).
- Authentication failure (exit 4/33/34): ask the operator to run `claude auth status` / `claude auth login` with their Pro/Max/Enterprise sign-in, then retry. No API key needed.
- Permission errors (exit 5/11): retry with `--sandbox workspace-write` only if file changes are intended, or narrow `--allowed-tools`.
- Non-zero exit codes other than above: report the code; Claude Code uses distinct codes for network errors (3), config errors (6), budget/turn limits (16/25), and API/server overload (17/27/28).
