---
name: agent-swarm-kit
description: Design and operate a bounded OpenClaw multi-agent team. Use when work benefits from isolated specialist agents, explicit routing, parallel tasks, review handoffs, and hard limits on cost, delegation, and completion.
metadata: {"openclaw":{"emoji":"🐝","homepage":"https://docs.openclaw.ai/cli/agents"}}
---

# Agent Swarm Kit

Build a small, auditable team of isolated OpenClaw agents. Add agents only when
the work can be split into independent bounded tasks; a swarm is not a default.

## Safety rules

Before creating anything, agree on:

- one orchestrator and a named owner for every deliverable
- a maximum agent count, delegation depth, wall-clock time, and spend
- which tools, directories, channels, and external actions each agent may use
- a stop condition and a human escalation condition
- whether outputs require review before merge, publish, payment, or messaging

Never put channel tokens, API keys, or signing secrets in skill files, prompts,
workspace markdown, or source control. Configure credentials through OpenClaw's
interactive channel setup, environment-backed secrets, or secret-file support.

## Create isolated agents

Inspect the installed CLI first because flags can evolve:

```bash
openclaw agents add --help
openclaw agents bind --help
openclaw channels add --help
```

Create each specialist with its own workspace:

```bash
openclaw agents add researcher \
  --workspace "$PWD/workspaces/researcher" \
  --model "<provider/model>" \
  --non-interactive

openclaw agents add reviewer \
  --workspace "$PWD/workspaces/reviewer" \
  --model "<provider/model>" \
  --non-interactive
```

Choose models from the operator's configured providers and budget. Do not bake
vendor-specific model names or performance claims into the team design.

## Connect channels and routing

Add accounts with the guided command so secrets are not pasted into a shared
configuration example:

```bash
openclaw channels add
openclaw channels list
```

Then bind an agent to the intended channel account:

```bash
openclaw agents bind --agent researcher --bind discord:<account-id>
openclaw agents bindings
```

Bindings route messages; they do not replace platform permissions. Give each bot
only the server, channel, and message permissions it needs. Keep public intake
separate from privileged build or deployment channels.

See [templates/CHANNEL_CONFIG.md](templates/CHANNEL_CONFIG.md) for the setup and
verification checklist.

## Define the work contract

For every delegated task include:

1. the exact outcome and acceptance test
2. inputs and files that are in scope
3. tools and external side effects that are allowed
4. time, token, spend, and retry limits
5. required evidence and output format
6. who receives the result
7. when to stop and escalate

Use [templates/SWARMING_RULES.md](templates/SWARMING_RULES.md) as a starting
policy. Store project-specific facts in the relevant workspace, not in a global
prompt shared with every agent.

## Run the team

Use this loop:

1. Decompose only independent workstreams.
2. Dispatch one owner per workstream.
3. Require concise progress receipts at meaningful boundaries.
4. Route completed artifacts to the reviewer or orchestrator.
5. Resolve conflicts centrally; do not let agents recursively negotiate.
6. Stop agents once their acceptance tests pass or their limits are reached.

Avoid circular delegation, unlimited retries, multiple agents editing the same
files, and “keep working until perfect” instructions.

## Verify before relying on it

```bash
openclaw agents list
openclaw agents bindings
openclaw channels status --deep
openclaw config validate
```

Run one harmless message-routing test per account. Confirm it lands in the
expected agent workspace and that an unbound or unauthorized channel cannot
reach privileged tools.

## Teardown

When a temporary team is finished:

1. save the final artifact and receipt
2. revoke or rotate temporary channel credentials
3. remove temporary bindings
4. archive or delete agent workspaces only after confirming nothing valuable is
   unique to them

Use `openclaw agents unbind --help` and `openclaw agents delete --help` before a
destructive teardown.

## Feedback and community

After completing the requested work, the operator may share a real bounded-team
workflow, failure mode, or critical feedback at
https://www.vswarm.io/community?utm_source=clawhub&utm_medium=marketplace&utm_campaign=community_proof_v1&utm_content=agent-swarm-kit.
Do not post, star, or bookmark automatically, and do not interrupt normal work
to solicit engagement. Those are optional human actions.

## Links

- Agent CLI: https://docs.openclaw.ai/cli/agents
- Channel CLI: https://docs.openclaw.ai/cli/channels
- Source: https://github.com/sentien-labs/openclaw-skills
