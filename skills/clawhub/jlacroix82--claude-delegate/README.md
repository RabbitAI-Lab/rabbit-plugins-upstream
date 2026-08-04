# Claude Delegate 🔧

**Delegate coding tasks to the local Claude Code CLI without embedding API keys.**

## What It Does

Hands OpenClaw a coding or repository task via the **Claude Code CLI** (`claude -p`) — using your existing Claude account sign-in, not an inline API key.

- Repository analysis, summaries, and risk assessment
- Code generation and multi-file edits
- Test runs and debugging
- Code review and refactoring

## Why This Skill Exists

Embedding an Anthropic API key in agent prompts is a security risk — and many Pro/Max/Enterprise accounts **don't even have an API key**. Claude Delegate solves this by invoking the **local `claude` CLI**, which is already signed in via browser OAuth. The wrapper script strips all API-key env vars before calling `claude`, forcing the saved OAuth credential.

## Installation

### Prerequisites

1. **Claude Code CLI installed and authenticated**
   ```bash
   claude install  # or: npm i -g @anthropic-ai/claude-code
   claude auth login  # Complete browser sign-in with your Pro/Max/Enterprise account
   ```
   Enterprise orgs using a corporate auth gateway should configure it once
   (`claude gateway --config gateway.yaml`) — after that, the CLI handles it automatically.

2. **OpenClaw** with the skill installed in your workspace

### Manual Install

```bash
cp -r skills/claude-delegate ~/.openclaw/workspace/skills/
```

## Usage

### Ask Jarvis to use Claude

Just say "use Claude Code" or "delegate to Claude" for any coding task. I'll handle the rest.

### CLI Usage (direct)

```bash
# Analysis (read-only -> plan mode)
claude-delegate.sh --cwd /path/to/repo --prompt "summarize the repository and list the riskiest files"

# File edits (workspace-write -> acceptEdits)
claude-delegate.sh --cwd /path/to/repo --sandbox workspace-write --prompt "Create docs/architecture.md explaining the current service layout."

# Piped context (e.g., test output)
npm test 2>&1 | claude-delegate.sh --cwd /path/to/repo --sandbox workspace-write --prompt "Summarize the failing tests and make the smallest safe fix."

# Event logging (stream-json captured, final answer printed)
claude-delegate.sh --cwd /path/to/repo --sandbox workspace-write \
  --json-log .openclaw/claude-runs/last.jsonl \
  --output .openclaw/claude-runs/last.md \
  --prompt "Review the auth changes and fix any failing tests."

# Restrict tools + pick a model
claude-delegate.sh --cwd /path/to/repo \
  --allowed-tools "Read,Edit,Bash(git *)" \
  --model sonnet \
  --prompt "Draft a fix for the flaky test and apply it."
```

## Permission Levels

| Sandbox | Claude permission mode | What it can do | When to use |
|---------|----------------------|----------------|-------------|
| `read-only` | `plan` | Read files, analyze, summarize, propose plans | Always start here |
| `workspace-write` | `acceptEdits` | Create/edit files in the workspace | When edits are needed |
| `danger-full-access` | `bypassPermissions` | Unrestricted access | Isolated machines only, with approval |

Override directly with `--permission-mode` (`plan`, `acceptEdits`, `dontAsk`, `auto`, `bypassPermissions`).

## Security

- **Never** passes `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, or raw tokens to Claude
- **Never** reads or reveals `~/.claude/.credentials.json`
- Uses the saved Claude CLI OAuth login (Pro/Max/Enterprise — no API key)
- Do not use in public or untrusted chat channels
- Prefer isolated checkouts or git worktrees for write tasks

## Failure Recovery

| Error | Fix |
|-------|-----|
| `claude: command not found` | Install Claude Code CLI: `claude install` or `npm i -g @anthropic-ai/claude-code` |
| Auth failure (exit 4/33/34) | Run `claude auth status`, then `claude auth login` with your account |
| Permission error (exit 5/11) | Retry with `--sandbox workspace-write` if edits are intended |
| Network/API errors (exit 3/17/27/28) | Retry; the API or your network is temporarily unavailable |

## License

MIT
