---
name: team-dev
description: Multi-agent team development. Triggered by team-dev or team development. Orchestrates 6 specialist agents for spec-to-delivery with quality gates.
user-invocable: true
disable-model-invocation: true
intent: Orchestrates a multi-agent software development team through staged quality gates — from requirements specification through architecture design, implementation, testing, audit, and delivery.
metadata: { "openclaw": { "emoji": "👥" } }
---

# team-dev — Multi-Agent Development Workflow

> **Command-only invocation**: triggered exclusively by the `team-dev` slash command. `disable-model-invocation: true`, `user-invocable: true`. Not auto-invoked by the model.

User provides requirements → main orchestrates 6 specialist agents via `sessions_spawn` through staged gates. Each agent self-identifies their role and acts only on their stages. All results flow back to main for next-stage dispatch.

---

## Complexity Assessment

main evaluates at launch and declares S/M/L before execution begins.

| Dimension | S (Simple) | M (Medium) | L (Large) |
|-----------|-----------|-----------|-----------|
| Lines of Code | <200 | 200–1000 | >1000 |
| File Count | 1–3 | 4–10 | >10 |
| Modules/Interfaces | Single module | 2–3 modules | Multi-module/service |
| External Dependencies | 0–1 | 2–3 | Multiple |
| Security Sensitivity | None | Low | Medium/High |
| Requirement Ambiguity | Clear | Minor ambiguities | Multiple clarifications needed |

---

## Process Stages by Complexity

| Stage | S | M | L | Input | Output | Executor |
|-------|---|---|---|-------|--------|----------|
| 0: Assessment + Constitution | ✅ | ✅ | ✅ | User requirements | Complexity assessment (S/M/L), constitution.md (L-level), `docs/journey.md` (from `main/journey-template.md`), `docs/todo.md` (from `main/todo-template.md`), examples/ (M+ best-practice search) | main |
| 1: Spec + Style Guide | ✅ | ✅ | ✅ | User requirements, complexity level | spec.md, style-guide.md (include non-functional requirements from §Non-Functional Requirements — all 8 items) | main |
| 2: Pre-Audit + Clarify | △① | ✅ | ✅ | spec.md, style-guide.md | Audit report, clarification items | spawn auditor (S: main self-check) |
| 3: Main Gate Check | — | ✅ | ✅ | Audit report, spec.md, clarified requirements | Go / no-go decision, updated spec | main |
| 4: Design + Testable Items | △② | ✅ | ✅ | spec.md, style-guide.md | design.md, testable items list (S: verbal description only). Coder proactively follows NFRs in design: #3 exception coverage — document exception handling strategy; #4 non-intrusive framework — document module boundaries, decouple business logic from framework; #5 pluggable & testable — document test strategy, stub/mock points | spawn coder |
| 4b: Design Review (🔴 gate) | — | ✅ | ✅ | design.md, spec.md | Review report → approved / needs revision | spawn reviewer |
| 5: Analyze Consistency | — | ✅ | ✅ | design.md, spec.md, style-guide.md | Consistency analysis report | main |
| 6: Implementation | ✅ | ✅ | ✅ | design.md, testable items, style-guide.md | Source code (implementation). Coder proactively follows NFRs in code: #2 structured logging — implement DEBUG/INFO/WARN/ERROR levels; #3 exception coverage — catch and handle all exception paths; #7 precise error location — logs include file, line number, call stack, and context state | spawn coder |
| 6b: Code Review | — | ✅ | ✅ | Source code, design.md | Code review report → pass / needs fix. Reviewer also covers NFR #3 (exception coverage), #4 (non-intrusive framework), #5 (pluggable & testable): check exception handling completeness, framework non-intrusion into business logic, and module testability/stub/mock ease | spawn reviewer |
| 7: Testing | ✅ | ✅ | ✅ | Source code, testable items | Test report must include: defects, coverage percentage, AND uncovered execution paths analysis (which lines/paths are not covered and why). Tester **must** run coverage tools (see §Non-Functional Requirements #8) | spawn tester |
| 8: Final Audit + Checklist | △③ | ✅ | ✅ | All stage outputs | Audit report + checklist (S: simplified ~8–12 items). Auditor checklist must include NFR compliance: #1 docs-code sync, #2 structured logging levels, #3 exception path coverage, #4 framework non-intrusion, #5 pluggability/testability/mock, #6 background alerting + on-site logs, #7 precise error location, #8 coverage tool execution + report pass/fail. Each NFR item in the checklist must include specific evidence (e.g., file path, line number, log sample) — not just ✅/❌ symbols. | spawn auditor |
| 9: Release + README | ✅ | ✅ | ✅ | All approved deliverables | Tagged release, README.md | main |
| 10: Publicist Polish | — | — | ✅ | All deliverables, audit report | Polished documentation | spawn publicist |
| 11: Retrospective | — | — | ✅ | Full session history, all deliverables | retrospective.md | main |

① **S-level pre-audit**: main reads `projects/ma/auditor/audit-report-template.md` as the self-check template and fills it in directly.
② **S-level design**: main verbally describes the design approach and records it in `docs/journey.md`.
③ **S-level checklist**: main reads the checklist template and simplifies it to ~8–12 items.

**M+ projects**: stage 0 includes best-practice search → collect into `examples/`. See runtime skill §4.0.5.

> `examples/` is free-form, supporting `.html` and `.md` files. Content is best-practice reference material: code snippets, design patterns, API usage examples.

---

## Git Workflow

- Project directory: `projects/<project-name>/`
- All operations are local — no remote push required
- Single branch `main` — no feature branches needed
- main runs `git init` + initializes project structure at Stage 0
- coder works directly on the `main` branch at Stage 4/6, running `git add && git commit`
- No merges needed — all operations are linear on `main`
- No remote push/pull — all agents inherit the same workspace via spawn

---

## Core Red Lines

From `main/AGENTS.md` §1.1. Inviolable — self-check before every action.

| # | Rule | Correct Approach |
|---|------|-----------------|
| 1 | Main does **not** code | Delegate to coder + reviewer |
| 2 | Main does **not** write docs | Delegate to publicist |
| 3 | Main does **not** audit | Delegate to auditor |
| 4 | Main does **not** test | Delegate to tester |
| 5 | Main **serves the user** | Respond promptly, don't get buried in tasks |

---

## Non-Functional Requirements

These requirements apply from design through delivery. main communicates them at Stage 1, coder follows them in Stages 4 & 6, reviewer checks #3–#5 at Stage 6b, auditor verifies all 8 at Stage 8, and tester runs coverage (#8) at Stage 7.

The following quality attributes apply across all process stages and all agents. Violations are treated as defects.

### 1. Documentation Freshness
Docs must be kept up-to-date with code changes. Stale docs are treated as bugs — they mislead the team and degrade the project's bus factor.

### 2. Structured Logging
Log output must be leveled (`DEBUG` / `INFO` / `WARN` / `ERROR`) and complete. Every significant operation, decision point, and error path must produce a log entry. Unstructured `print()` output is not a substitute.

### 3. Exception Coverage
All exception paths must be caught and handled. **No silent failures.** Unhandled exceptions that propagate to the user or crash a process are unacceptable regardless of severity.

### 4. Non-Intrusive Framework
Base frameworks and infrastructure must not leak into business logic. Business code should remain framework-agnostic, testable in isolation, and portable across infrastructure changes.

### 5. Pluggable & Testable Design
Code and modules must be easy to plug and unplug. Dependency injection, stubs, and mocks must be straightforward. Every module must be **independently testable** without requiring the full application stack.

### 6. Background Alerting
Runtime exceptions in background or daemon processes must:
- Trigger alerts (not silently swallowed)
- Preserve on-site logs for forensic analysis

### 7. Precise Error Location
Logs must enable precise error location. At minimum, include: file name, line number, call stack, and relevant contextual state at the point of failure.

### 8. Coverage-Driven Testing
Testing must use coverage tools (e.g., `coverage.py`, JaCoCo, Istanbul/nyc) to identify untested execution paths. **Coverage gaps are treated as test deficiencies** — they must be documented or closed before delivery.

---

## Agent Roster

| Agent | Role | Workspace |
|-------|------|-----------|
| **main** 🎓🏅📋 | Advisor · Coach · PM — sole user interface | `workspace` |
| **coder** 🏗️ | Architect · Driver — design + coding | `workspace-coder` |
| **reviewer** 🔍 | Inspector · Navigator — code review | `workspace-reviewer` |
| **tester** 🧪 | Tester — black-box + white-box + perf | `workspace-tester` |
| **auditor** 🔒 | Auditor · Gatekeeper — pre-audit + final audit | `workspace-auditor` |
| **publicist** ✍️ | Writer — technical docs | `workspace-publicist` |

> **Agents have their own workspaces** (`workspace-coder`, `workspace-tester`, etc.) which store their AGENTS.md and SOUL.md identity files. When spawned via `sessions_spawn(agentId: "coder")`, the system auto-loads these identities from the agent workspace (§Agent Identity Loading below). For code work, spawn inherits main's workspace, giving the subagent access to `projects/`, `docs/`, and source code. `projects` symlinks are maintained for non-spawn scenarios where an agent needs direct filesystem access to shared projects.

---

## Communication Model (v3)

### Core Principle

**main is the sole dispatcher.** All agent work is initiated by `sessions_spawn` from main. Results flow back to main, who decides the next step. No agent communicates directly with another agent.

```
User ⇄ main
main → sessions_spawn → agent (any)
agent completes → result auto-announced to main
main evaluates → sessions_spawn → next agent
```

### Spawn Inheritance

- Every `sessions_spawn` creates a **fresh subagent session**.
- For code access: the subagent inherits main's workspace — sees the same `projects/` directory, `docs/`, and source code as main.
- For identity: when `agentId` is specified (e.g., `sessions_spawn(agentId: "coder")`), the system loads AGENTS.md/SOUL.md from the agent's own workspace (`workspace-coder/`). See §Agent Identity Loading below.
- Subagent sessions are ephemeral — destroyed after completion, results stored in session history.

### Agent Identity Loading

When main dispatches work via `sessions_spawn(agentId: "coder")`:

1. The system resolves the agent's workspace — e.g., `~/.openclaw/workspace-coder/`.
2. It automatically loads AGENTS.md and SOUL.md from that workspace into the subagent's context.
3. This is why the initialization flow (§Interactive Initialization Flow) writes AGENTS.md/SOUL.md to the agent's own workspace — these files are the agent's identity and are loaded every time the agent is spawned.
4. Simultaneously, the subagent inherits main's workspace for code access.

> **Why two workspaces?** The agent's **own workspace** provides its identity (role, personality, rules). Main's **inherited workspace** provides the code and assets the agent works on. Together they give the spawned agent both its purpose and its materials.

### v2 → v3 Migration Summary

| Aspect | v2 (old) | v3 (current) |
|--------|---------|-------------|
| Dispatch mechanism | `sessions_send` (inter-agent messaging) | `sessions_spawn` (main-initiated) |
| Agent workspaces | Independent (`workspace-coder`, etc.) | Inherited from main via spawn |
| filesystem access | Required `projects` symlinks per agent | Automatic — spawn inherits parent FS |
| coder ↔ tester | Direct interaction (bug loop) | main spawns tester → result → main spawns coder (fix) → main spawns tester (regression) |
| coder ↔ reviewer | Direct interaction (review loop) | main spawns reviewer → result → main decides: pass or spawn coder (fix) → main spawns reviewer (re-review) |
| auditor → coder | Direct command (audit issues) | main receives audit → main spawns coder (fix) → main spawns auditor (re-audit) |
| tester → auditor | Direct via main relay (`sessions_send`) | main receives test report → main spawns auditor |
| publicist | Only via main | Only via main (unchanged — was already main-only) |

### Loop Closure under v3

**Bug Loop (coder ↔ tester):**
```
main spawns coder (implement)
  → coder completes, result auto-announced to main
  → main spawns tester (test)
  → tester finds bugs, result auto-announced to main
  → main spawns coder (fix bugs)
  → coder completes, result auto-announced to main
  → main spawns tester (regression)
  → loop until all pass or 3-round cap reached
```

**Review Loop (coder ↔ reviewer):**
```
main spawns coder (design/code)
  → coder completes, result auto-announced to main
  → main spawns reviewer (review)
  → reviewer finds issues, result auto-announced to main
  → main spawns coder (fix)
  → coder completes, result auto-announced to main
  → main spawns reviewer (re-review)
  → loop until pass or 2-round cap reached
```
NFR issues discovered during review follow the same review loop: main spawns coder to fix, then main spawns reviewer to re-review. No separate process is needed.

**Audit Fix Loop:**
```
main spawns auditor (final audit)
  → auditor finds issues, result auto-announced to main
  → main spawns coder (fix issues)
  → coder completes, result auto-announced to main
  → main spawns auditor (re-audit)
  → loop until all pass or main escalates to user
```

---

## Agent Availability Detection & Fallback

> **Trigger timing**: When the user triggers `/team-dev` or mentions "team development" or "multi-agent development", this check is the **first thing** main executes.

### Startup Check: Verify Agent Registration

Before dispatching any agent, main checks via `openclaw agents list` whether all of the following **5 agents** are registered:

| # | Agent ID | Role |
|---|----------|------|
| 1 | `coder` | Architect · Coding |
| 2 | `tester` | Testing · Black-box + White-box + Performance |
| 3 | `auditor` | Audit · Gatekeeper |
| 4 | `publicist` | Writer · Technical Documentation |
| 5 | `reviewer` | Review · Code Review |

Run command:

```bash
openclaw agents list
```

main parses the output and verifies each of the above 5 agent IDs.

> **Note**: This check targets agent **instances** (i.e., independent agents registered via `openclaw agents add`), not template files. main itself is not within scope — main is the current runtime environment.

### Three Possible Outcomes

#### Outcome 1: All Present ✅

All 5 agents are registered. main proceeds directly to §Process Stages with no initialization needed.

#### Outcome 2: Partial Missing ⚠️

main lists the missing agents and enters §Interactive Initialization Flow.

#### Outcome 3: All Missing ❌

None of the 5 agents are registered. main lists the full missing list and enters §Interactive Initialization Flow.

---

### Interactive Initialization Flow

If any agent is missing, main **must not fall back to single-agent mode** directly. Instead, execute the following steps:

#### Step 1: Report Missing Agents, Ask User

main explicitly lists the missing agents and presents three options:

> 🔍 The following agents are not registered:
>
> | Agent | Status |
> |-------|--------|
> | coder | ❌ Not registered |
> | reviewer | ❌ Not registered |
> | tester | ❌ Not registered |
> | auditor | ✅ Ready |
> | publicist | ✅ Ready |
>
> I can initialize the missing agents for you in one go.
>
> Choose:
> 1. **Initialize** — Auto-create missing agents, write behavior guides and personality files, set up project connections
> 2. **Go Solo** — Don't create agents; main takes over all missing roles
> 3. **Cancel** — Abort the current team development flow

main waits for the user's choice.

#### Step 2a: User Chooses "Initialize"

main initializes each missing agent in sequence. **Using coder as an example**, the full flow is:

**① Create Agent Instance**

```bash
openclaw agents add coder
```

This creates an independent agent workspace under `~/.openclaw/`, e.g.:

```
~/.openclaw/workspace-coder/
```

**② Write AGENTS.md — Behavior Guide**

- **Template source (priority)**: `skills/team-dev/coder/AGENTS.md` → fallback to `projects/ma/coder/AGENTS.md` if not found
- **Write target**: `~/.openclaw/workspace-coder/AGENTS.md`

Operation flow:

```
main attempts to read skills/team-dev/coder/AGENTS.md (priority)
       ↓ if not found
main reads projects/ma/coder/AGENTS.md (fallback)
       ↓
main writes to ~/.openclaw/workspace-coder/AGENTS.md
```

**③ Write SOUL.md — Personality Profile**

- **Template source (priority)**: `skills/team-dev/coder/SOUL.md` → fallback to `projects/ma/coder/SOUL.md` if not found
- **Write target**: `~/.openclaw/workspace-coder/SOUL.md`

Operation flow:

```
main attempts to read skills/team-dev/coder/SOUL.md (priority)
       ↓ if not found
main reads projects/ma/coder/SOUL.md (fallback)
       ↓
main writes to ~/.openclaw/workspace-coder/SOUL.md
```

**④ Create Project Symlink**

Allow the agent to access the shared project directory:

```bash
ln -s ~/.openclaw/workspace/projects ~/.openclaw/workspace-coder/projects
```

> This way, when the agent is dispatched, it can access project code and docs in main's workspace via `projects/`.

**⑤ Repeat for All Missing Agents**

Repeat steps ①–④ for each missing agent (reviewer, tester, auditor, publicist). Full mapping:

| Agent | AGENTS.md Template Source (priority) | SOUL.md Template Source (priority) | Write Target Workspace | Symlink Command |
|-------|--------------------------------------|------------------------------------|------------------------|-----------------|
| coder | `skills/team-dev/coder/AGENTS.md` → `projects/ma/coder/AGENTS.md` | `skills/team-dev/coder/SOUL.md` → `projects/ma/coder/SOUL.md` | `~/.openclaw/workspace-coder/` | `ln -s ~/.openclaw/workspace/projects ~/.openclaw/workspace-coder/projects` |
| reviewer | `skills/team-dev/reviewer/AGENTS.md` → `projects/ma/reviewer/AGENTS.md` | `skills/team-dev/reviewer/SOUL.md` → `projects/ma/reviewer/SOUL.md` | `~/.openclaw/workspace-reviewer/` | `ln -s ~/.openclaw/workspace/projects ~/.openclaw/workspace-reviewer/projects` |
| tester | `skills/team-dev/tester/AGENTS.md` → `projects/ma/tester/AGENTS.md` | `skills/team-dev/tester/SOUL.md` → `projects/ma/tester/SOUL.md` | `~/.openclaw/workspace-tester/` | `ln -s ~/.openclaw/workspace/projects ~/.openclaw/workspace-tester/projects` |
| auditor | `skills/team-dev/auditor/AGENTS.md` → `projects/ma/auditor/AGENTS.md` | `skills/team-dev/auditor/SOUL.md` → `projects/ma/auditor/SOUL.md` | `~/.openclaw/workspace-auditor/` | `ln -s ~/.openclaw/workspace/projects ~/.openclaw/workspace-auditor/projects` |
| publicist | `skills/team-dev/publicist/AGENTS.md` → `projects/ma/publicist/AGENTS.md` | `skills/team-dev/publicist/SOUL.md` → `projects/ma/publicist/SOUL.md` | `~/.openclaw/workspace-publicist/` | `ln -s ~/.openclaw/workspace/projects ~/.openclaw/workspace-publicist/projects` |

> **Note**: AGENTS.md and SOUL.md are written to the agent's own workspace root directory — these are the rule files the agent actually follows. Template sources have two paths: `skills/team-dev/<agent>/` (runtime copy, priority) and `projects/ma/<agent>/` (template source, fallback). Both are identical in content — `skills/team-dev/` is a deployed copy of the corresponding template from `projects/ma/`. Templates should not be modified; they are only used for initialization writes.

#### Step 2a Finish: Report Ready, Continue Flow

After all agents are initialized, main informs the user:

> ✅ All missing agents have been initialized.
>
> | Agent | AGENTS.md | SOUL.md | projects symlink |
> |-------|-----------|---------|-------------------|
> | coder | ✅ | ✅ | ✅ |
> | reviewer | ✅ | ✅ | ✅ |
>
> Team is ready. Starting team development workflow.

main then **proceeds directly** to §Process Stages without further user confirmation.

#### Step 2b: User Chooses "Go Solo"

main falls back to single-agent mode, taking over missing roles directly:

| Missing Role | How main Takes Over |
|-------------|---------------------|
| coder | main handles design and coding |
| reviewer | main handles code quality review |
| tester | main handles testing |
| auditor | main handles audit and checklist |
| publicist | main handles documentation |

**When main plays any agent role, it must first read that role's SOUL.md template** (try `skills/team-dev/{agent}/SOUL.md`, fallback to `projects/ma/{agent}/SOUL.md` if not found) to understand the role's responsibilities, behavioral style, and constraints. For example, to play coder: try `skills/team-dev/coder/SOUL.md` (priority), fallback to `projects/ma/coder/SOUL.md`, and so on.

**Red Line**: Even when falling back to single-agent mode, main must still honor the spirit of Core Red Lines — "main does not code / test / audit / write docs" — executing thoroughly without skipping steps. The only difference is that main becomes the executor.

main explicitly informs the user:

> ⚠️ Currently in single-agent mode. The following agents are not registered: [list].
> All roles are handled by main. You can have me initialize agents for full multi-agent collaboration at any time.

#### Step 2c: User Chooses "Cancel"

main confirms and terminates:

> Team development flow cancelled. Say "/team-dev" anytime to restart.

---

### Hybrid Scenario: Partial Agent Readiness

If only some agents are registered (e.g., coder and tester are ready, the rest missing), main follows the same interactive flow:

- **List ready agents**: e.g., "coder ✅, tester ✅"
- **List missing agents**: e.g., "reviewer ❌, auditor ❌, publicist ❌"
- **Present the same three options**: Initialize missing / Go Solo / Cancel

If user chooses "Initialize": only initialize the missing agents; do not touch already-ready agents (do not overwrite existing AGENTS.md and SOUL.md).
If user chooses "Go Solo": ready agents are dispatched normally via `sessions_spawn`; missing roles are handled by main.

### Integrity Check for Ready Agents

For agents already present in `openclaw agents list`, main should also quickly verify that key files in their workspace are intact:

| Check Item | Path | Action if Missing |
|-----------|------|-------------------|
| AGENTS.md | `~/.openclaw/workspace-{agent}/AGENTS.md` | Rewrite from `skills/team-dev/{agent}/AGENTS.md` (priority) or `projects/ma/{agent}/AGENTS.md` (fallback) |
| SOUL.md | `~/.openclaw/workspace-{agent}/SOUL.md` | Rewrite from `skills/team-dev/{agent}/SOUL.md` (priority) or `projects/ma/{agent}/SOUL.md` (fallback) |
| projects symlink | `~/.openclaw/workspace-{agent}/projects` | Run `ln -s ~/.openclaw/workspace/projects ~/.openclaw/workspace-{agent}/projects` |

> If an agent is registered but key files are missing (e.g., the agent was manually cleaned up), main should auto-repair and mark it as "⚠️ Restored" rather than "✅" in the initialization report.

---

## Agent Behavior Guide Sync

> **Design purpose**: Each agent's AGENTS.md/SOUL.md consists of two parts — MA framework unified rules (MA:CORE) + agent personalization. This section defines the merge mechanism, ensuring the framework rules evolve uniformly while preserving each agent's accumulated personalization.

### Core Principle: Merge, Don't Overwrite

Each agent's AGENTS.md and SOUL.md is divided into two regions:

- **MA Core region** — enclosed by `<!-- MA:CORE_START -->` and `<!-- MA:CORE_END -->` markers. These are MA framework-managed rules that ensure team collaboration consistency.
- **Custom region** — the free area outside the markers. Agents record notes, preferences, lessons learned, and personal habits here. **This content belongs to the agent and must not be touched during initialization.**

During initial setup, the agent may not have these files yet — simply write them. But on **subsequent updates**, only replace the content between the MA:CORE markers, preserving everything the agent has accumulated outside the markers.

### Template Sources

The MA framework has two sets of template paths, identical in content but with different purposes:

- **`skills/team-dev/<agent>/`** — Runtime copy, used by the agent initialization flow (read with priority).
- **`projects/ma/<agent>/`** — Template source, used for behavior guide sync. Both sets have identical content.

Behavior guide sync uses the following `projects/ma/<agent>/` paths:

| Agent | AGENTS.md Template | SOUL.md Template |
|-------|-------------------|------------------|
| main | `projects/ma/main/AGENTS.md` | `projects/ma/main/SOUL.md` |
| coder | `projects/ma/coder/AGENTS.md` | `projects/ma/coder/SOUL.md` |
| reviewer | `projects/ma/reviewer/AGENTS.md` | `projects/ma/reviewer/SOUL.md` |
| tester | `projects/ma/tester/AGENTS.md` | `projects/ma/tester/SOUL.md` |
| auditor | `projects/ma/auditor/AGENTS.md` | `projects/ma/auditor/SOUL.md` |
| publicist | `projects/ma/publicist/AGENTS.md` | `projects/ma/publicist/SOUL.md` |

### Operation Flow

**Step 1: main Studies the Project**

main reads the following files to fully understand the MA framework:
- `projects/ma/SKILL.md` — This document, to understand execution flow and merge mechanism
- `projects/ma/README.md` — Team overview, quick start
- `projects/ma/docs/multi-agent-design.md` — Architecture design: agent design, communication matrix, three-document system, configuration reference

**Step 2: main Merges AGENTS.md**

For each agent (coder, reviewer, tester, auditor, publicist), main executes:

1. Read `projects/ma/<agent>/AGENTS.md` — this is the role template
2. Send to the corresponding agent via `sessions_spawn`, with a message like:

   > Please merge the following AGENTS.md template into your workspace.
   > - If an AGENTS.md already exists in your workspace: only update the content between `<!-- MA:CORE_START -->` and `<!-- MA:CORE_END -->`, keeping custom content outside the markers unchanged
   > - If no AGENTS.md exists yet: write it directly
   > - Reply to confirm when done

3. The agent receives and performs the merge operation in the current session
4. The agent replies to main confirming completion

**Step 3: main Merges SOUL.md**

The flow is the same as AGENTS.md, but with extra care:
- SOUL.md records the agent's personality traits. Agents accumulate unique character and experience through long-term work.
- Initial setup: write the template content directly
- Subsequent updates: only sync newly added personality traits from the template. **Never overwrite the agent's accumulated personalization.**
- If the agent has already developed its own understanding and expression of its personality, main should respect and preserve it.

**Step 4: Verification**

main confirms with each agent one by one:

> Please read your AGENTS.md and SOUL.md, and confirm that the MA:CORE regions are correctly synced and custom content is intact.

Each agent replies to confirm. Initialization complete.

This design ensures: framework rules evolve uniformly, agent personalization persists continuously — the two run in parallel without conflict.

---

## Documentation Map

### Template Files

| Document | Purpose |
|----------|---------|
| `main/AGENTS.md` | Main controller code of conduct (authoritative) |
| `docs/multi-agent-design.md` | Full architecture, agent design, communication matrix |
| `CHANGELOG.md` | Version history |
| `main/constitution-template.md` | Project constitution template (L-level) |
| `main/todo-template.md` | Task board template (WBS, resume from breakpoint) |
| `main/journey-template.md` | Process journal template |
| `auditor/audit-report-template.md` | Issue registration, tracking, verification, closure |
| `tester/test-report-template.md` | Defect report & verification loop |

### Runtime Artifacts

| Document | Purpose | Output Stage |
|----------|---------|-------------|
| `docs/spec.md` | Requirements specification | Stage 1 |
| `docs/design.md` | Design document | Stage 4 |
| `docs/audit-report.md` | Audit report | Stage 2/8 |
| `docs/test-report.md` | Test report | Stage 7 |
| `docs/bugs.md` | Defect log | Stage 7 |
| `docs/checklist.md` | Quality checklist | Stage 8 |
| `docs/journey.md` | Process journal | Created at Stage 0, updated throughout |
| `docs/todo.md` | Task board | Created at Stage 0 |

> **Full workflow, agent AGENTS.md files, doc templates**: all under `projects/ma/`.
> **SKILL.md** (this file) is the project-level entry point. All stage definitions with Input/Output/Executor are self-contained in §Process Stages above.
> **Agent Behavior Guide Sync**: see §Agent Behavior Guide Sync above.
