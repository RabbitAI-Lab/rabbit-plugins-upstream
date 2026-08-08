---
name: "taskforce-loop-engineering"
description: "Document complete Loop Engineering install, upgrade, scheduler, and verification lifecycle."
---

# Taskforce Loop Engineering

Use this skill only when the user explicitly invokes Loop Engineering, says `走 loop`, `loop engineering`, `丢进 Ironman loop`, `loop Ironman`, `task-runner`, names a loop queue, or asks to operate an existing loop.

Do not route ordinary chat, research, explanations, or simple direct tasks into a loop unless the user explicitly invokes it.

## Upgrade Intent

Interpret upgrade requests by product scope, not by the word “skill” alone:

- `升级 Loop Engineering`, `更新 Loop Engineering`, or equivalent product-level wording means a **complete managed upgrade** by default: update the ClawHub skill, npm package/CLI, OpenClaw integration files and queue configuration, and per-queue scheduler units. Then verify all layers.
- `只升级 Skill`, `只更新 ClawHub 技能`, or equally explicit wording means update only the ClawHub skill content. Warn that this does not update the CLI, integration, queue configuration, or scheduler.
- If the request says only `升级技能` while clearly referring to Loop Engineering as an installed system, treat it as the complete managed upgrade unless the user explicitly narrows the scope.
- Never report “Loop Engineering upgraded” after changing only one layer. Report the version/status of Skill, npm/CLI, OpenClaw integration/queue config, and scheduler separately.

Complete managed upgrade flow:

1. Inspect current Skill, npm/CLI, integration, queue, and scheduler versions/state.
2. Update the ClawHub skill and npm package from their official distributions.
3. Upgrade the managed OpenClaw integration:

```bash
loop-engineering-openclaw-manage \
  --root /path/to/openclaw/workspace \
  --action upgrade \
  --confirm-upgrade
```

4. Run doctor and the disposable smoke test, then verify the per-queue systemd timer is enabled and active.
5. Treat `scheduler_missing`, a stale heartbeat, or queued project work not reclaimed by a later tick as an incomplete upgrade.

Updating the npm package or ClawHub skill alone must never be presented as completing the managed OpenClaw integration upgrade.

## Distribution and CLI Installation

A ClawHub installation may provide only this `SKILL.md`; it does **not** prove that the Loop Engineering CLI or OpenClaw integration is installed. Before running loop commands, check the deployment explicitly:

```bash
command -v loop-engineering
loop-engineering --help
```

Official distribution:

- npm package: `taskforce-loop-engineering`
- GitHub repository: `https://github.com/ambitioncn/taskforce-loop-engineering`
- ClawHub skill: `https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering`
- license: Apache-2.0
- runtime requirement: Node.js 22 or newer

Install the CLI globally from npm:

```bash
node --version
npm install -g taskforce-loop-engineering
loop-engineering --help
```

For a temporary read-only invocation without a global install:

```bash
npx -p taskforce-loop-engineering loop-engineering --help
```

For source-based development, clone the official repository and install its dependencies:

```bash
git clone https://github.com/ambitioncn/taskforce-loop-engineering.git
cd taskforce-loop-engineering
npm install
npm run check
node bin/loop-engineering.mjs --help
```

Do not guess a workspace source path. Use `node packages/loop-engineering/bin/loop-engineering.mjs ...` only after confirming that exact path exists in the current workspace.

### OpenClaw Integration

Installing the npm package exposes the CLI, but it does not automatically route conversations, select a worker agent, or create queue wrappers. First generate a read-only installation plan:

```bash
loop-engineering-openclaw-install \
  --root /path/to/openclaw/workspace \
  --queue agent-tasks
```

Review the detected agents and planned files. Then install with an existing worker-agent id:

```bash
loop-engineering-openclaw-install \
  --root /path/to/openclaw/workspace \
  --queue agent-tasks \
  --worker-agent main \
  --confirm-install
```

The installer never creates the worker agent. Confirmed installs and managed upgrades also create and enable a per-queue systemd user scheduler. The queue requires a fresh scheduler heartbeat, so queued project work reports `scheduler_missing` instead of waiting indefinitely. Managed uninstall disables and removes the scheduler units while retaining queue runtime. After installation, verify wiring before using a real task:

```bash
loop-engineering-openclaw-doctor \
  --root /path/to/openclaw/workspace \
  --queue agent-tasks \
  --worker-agent main

loop-engineering-openclaw-smoke \
  --root /path/to/openclaw/workspace \
  --queue agent-tasks \
  --worker-agent main
```

If the CLI or integration is missing and the user requested installation or repair, install it within the authorized host/workspace scope, then run doctor and the disposable smoke. If the user only asked what is missing, report the exact package, repository, commands, and current deployment state without mutating the system.

## Conversation Contract

Interpret explicit loop language as follows:

- `走 loop：<task>`: enqueue and immediately execute one runner tick with notification.
- `走 loop 并立刻执行`: synonym for the default above.
- `走 loop，只入队`, `只排队`, `暂不执行`, or `不立即执行`: enqueue without starting a tick.
- `继续当前 loop，补充要求：…`: amend the active task in place. Preserve the task id and worker session, write a versioned amendment, update the task contract/dev plan/acceptance plan, and require the worker to reread the latest amendment before checkpoints and completion.
- A new explicit `走 loop` request while another task is active is a correction/replacement, not ordinary backlog. Supersede the active task at a safe boundary, retain its evidence and lineage, then start the replacement after the lock is released.
- Status, progress, evidence, or failure questions are read-only and must not start another tick unless the user explicitly asks to continue/run.

In this workspace, the default queue is `ironman-task-runner` when no queue is named. Use the installed workspace wrapper when present:

```bash
node scripts/loops/ironman-task-runner.mjs route --message "<original user message>" --confirm-execute [source options]
node scripts/loops/ironman-task-runner.mjs run-once --notify
node scripts/loops/ironman-task-runner.mjs status --json
node scripts/loops/ironman-task-runner.mjs peek --json
```

Pass the original request faithfully. Preserve source channel, target, account, message id, and reply-to metadata so progress, human gates, and terminal results return to the originating conversation. Missing delivery routing must fail closed.

## Task vs Project Classification

Classify scope before enqueueing.

### Scoped task

A bounded change, diagnosis, review, or deliverable with a clear local acceptance target can use one task contract.

### Project-level objective

Treat a request as project-level when the user asks to build/develop/finish a complete product or system, achieve an overall outcome, or otherwise describes a multi-milestone terminal goal.

For a project-level objective:

1. Run project intake and create a project spec.
2. Write an explicit terminal-state/completion contract.
3. Build a complete backlog covering every requirement and known acceptance dimension.
4. Link queue tasks to the project backlog and terminal contract.
5. Continue through implementation, verification, revisions, and the next actionable backlog item within the authorized safety boundary.
6. Stop only when total project acceptance passes, or a genuine human authorization/product decision/external-state blocker prevents meaningful progress.

Never silently narrow a complete-project request into “first milestone” and call that the Loop complete. A single queue task or milestone may be complete while the project remains active.

Recommended commands:

```bash
loop-engineering project-intake --root <workspace> --name <project> --brief "<full brief>" --type auto
loop-engineering project-plan --root <workspace> --project <project>
loop-engineering project-status --root <workspace> --project <project>
```

The project completion contract must contain:

- terminal user-visible outcome;
- in-scope and explicitly out-of-scope capabilities;
- complete requirement/backlog mapping;
- acceptance checks and evidence locations;
- operational/security/data/deployment requirements when relevant;
- unresolved decisions and required authority;
- a rule that milestone completion cannot satisfy project completion;
- final acceptance status with unmet items and blockers.

If implementation reveals missing work, amend the project backlog/contract before continuing. Do not redefine the terminal goal downward to fit completed work.

## Completion Semantics

Use precise language:

- `阶段完成` or `任务完成`: one task/milestone passed its own acceptance checks.
- `项目完成` or `Loop 跑完`: only when the project completion contract is fully accepted and no required work remains.
- `blocked`: only for a concrete blocker requiring human authority/input or an external state change, with evidence and a specific unblock request.
- `needs_revision`: acceptance found actionable gaps; create a changed-strategy revision rather than claiming completion.
- `superseded`: a newer explicit loop request replaced the task; preserve lineage and evidence.

Final reporting for project work must always state both task/milestone status and total-project status.

## Safety and Authority

Loop invocation authorizes the requested workflow, not unlimited external action.

Require separate explicit confirmation for:

- external messages, publication, social posting, or outreach;
- destructive deletion or difficult-to-recover changes;
- production configuration/deployment changes not already clearly requested;
- credential creation/change/exposure;
- paid model/API usage beyond an established budget;
- memory deletion or migration;
- device/process instrumentation such as `frida`, `tcpdump`, `adb`, `mitmproxy`, hooks, attach/spawn, decrypt, `su`, `kill`, or `pkill`.

Human permission prompts and missing authorization are stop conditions, not retryable failures. `INSTALL_FAILED_USER_RESTRICTED`, device unauthorized, permission denied, and equivalent states require a concrete human-action gate.

Timeouts must terminate the spawned process group. After instrumentation timeouts, verify that no child instrumentation/proxy process remains.

## Operating Flow

1. Read existing project docs, loop configs, queue state, and relevant dirty worktree state.
2. Classify task vs project and define the correct contract before execution.
3. Use `route-message` or the installed conversation wrapper to preserve source metadata and apply immediate/queue-only/amend/supersede semantics.
4. Run preflight before mutable work.
5. Execute one bounded tick or the project’s next actionable backlog item.
6. Emit ordered progress: planning, preflight, worker start, checkpoints, verification, acceptance, final judgement.
7. Inspect run artifacts; never infer success only from dispatcher exit code.
8. If acceptance fails, write a revision request with changed diagnosis/tactic/evidence/verification.
9. Run `doctor` after configuration or queue changes.
10. For projects, re-read project status and completion contract, then automatically advance to the next safe actionable item.
11. Report terminal status with evidence, unmet items, blockers, and next action.

Do not add cron/timers until one manual tick passes.

## Core CLI

Prefer the installed CLI:

```bash
loop-engineering verify --root <workspace>
loop-engineering doctor --root <workspace> [--json]
loop-engineering summarize --root <workspace> --limit 20
loop-engineering route-message --root <workspace> --message "<message>" --queue <queue> --route --confirm-execute [--supersede-active | --amend-active] [source options]
loop-engineering queue-status --root <workspace> --queue <queue>
loop-engineering queue-peek --root <workspace> --queue <queue>
loop-engineering run-queue --root <workspace> --config configs/loops/queues/<queue>.json
loop-engineering queue-revision-next --root <workspace> --queue <queue> --task-id <id>
loop-engineering queue-lineage --root <workspace> --queue <queue> --task-id <id>
loop-engineering queue-lineage-bundle --root <workspace> --queue <queue> --task-id <id>
loop-engineering queue-human-decision --root <workspace> --queue <queue> --task-id <id> --decision approve|request_changes|reject
loop-engineering queue-human-input-resolve --root <workspace> --queue <queue> --gate-id <task:checkpoint> --input "<response>"
loop-engineering queue-terminal-notify --root <workspace> --queue <queue> (--notify-command "<command>" | --dry-run)
loop-engineering queue-human-input-notify --root <workspace> --queue <queue> (--notify-command "<command>" | --dry-run)
```

If the package is available only in the workspace:

```bash
node packages/loop-engineering/bin/loop-engineering.mjs <command>
```

Use `run-queue-drain` only when batch draining is explicitly intended. Conversation routing normally runs one task/tick and uses supersede/amend behavior.

## Revision Discipline

A dispatcher-successful run is not automatically accepted. Inspect `final_judgement.json`, acceptance reviews, checkpoints, and verification evidence.

When acceptance needs changes:

- mark `needs_revision`;
- retain the failed source task;
- use `queue-revision-next`;
- require a changed diagnosis, implementation tactic, evidence source, or verification step;
- inspect lineage before forcing repeated attempts.

Default revision policy may stop after three rounds, two repeated goal signatures, or repeated unchanged strategy. `--force` requires an explicit human override after lineage review.

## Code Work

For L2 code-changing tasks, prefer isolated worktrees. The runner prepares reviewable local changes and verification evidence; it does not implicitly commit, push, publish, deploy, merge, or delete branches.

Safe review flow:

```bash
loop-engineering code-task-status --root <workspace> --queue <queue>
loop-engineering code-worktree-inspect --root <workspace> --queue <queue> --task-id <id>
loop-engineering code-worktree-diff --root <workspace> --queue <queue> --task-id <id>
loop-engineering code-task-autoflow --root <workspace> --queue <queue> --task-id <id> --until closeout
loop-engineering code-patch-apply-plan --root <workspace> --patch <patch> --json
```

Applying a patch and cleaning a worktree require their explicit confirmation flags. Preserve unrelated user changes and never treat a dirty worktree as disposable.
