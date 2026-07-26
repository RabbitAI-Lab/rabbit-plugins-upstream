# team-dev

Multi-agent team development workflow.

## Invocation

Command-only: `team-dev` (slash command). Not auto-invoked by the model.

- `disable-model-invocation: true` — prevents auto-invocation
- `user-invocable: true` — exposes `team-dev` slash command

## Invocation

Command-only: `team-dev` (slash command). Not auto-invoked by the model.

| Field | Value | Purpose |
|-------|-------|---------|
| `disable-model-invocation` | `true` | Prevents auto-invocation by the model |
| `user-invocable` | `true` | Exposes `/team-dev` slash command |

## Usage

1. Run `team-dev` to start.
2. Main checks agent availability and optionally initializes missing agents.
3. Main orchestrates coder, reviewer, tester, auditor, and publicist through staged quality gates.
