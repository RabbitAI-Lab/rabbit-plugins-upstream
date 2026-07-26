# systems-thinking

> [中文](README_CN.md) | **English**

---

## About

`systems-thinking` is a thinking-mode skill. It installs a control-theoretic cognitive operating system in the LLM—shaping how the model *thinks* about systems (state, observability, stability, bounds, coupling) before writing or changing code.

> **One-line pitch: Control-theoretic thinking for code—know your state before you touch it.**

This is not a vocabulary test for humans, and not a bug-hunting playbook. It is a scaffold that reframes every non-trivial change from *"write the smallest patch and hope"* to *identify the state, measure the trajectory, stabilize the plant, then steer*.

Derived from Qian Xuesen (Tsien Hsue-shen‌) & Song Jian, *Engineering Cybernetics* (工程控制论). Language- and framework-agnostic. Self-contained.

## What it solves

The default approach to coding is: start typing, then pray the tests pass. This skill changes that order.

Use it when:

- You're changing legacy code you don't fully understand
- You're debugging something that breaks intermittently and can't be reproduced reliably
- You're refactoring modules that are tangled together
- A change needs to be both correct and robust

In these situations, "write the smallest patch" is often not enough. You need to understand the system's state first.

## Core idea

One sentence: **a program is a dynamical system, and you are the controller.**

Every change injects a control signal. You only partially observe the true state. Bugs are unstable or poorly-damped trajectories. Debugging is state estimation. Tests are sensors feeding a feedback loop. **Closed loop beats open loop.**

## Installation

This skill is designed for AI coding agents that support custom skills (Kilo, Claude Code, Aider, Cursor, etc.).

### npx one-command install (recommended)

```bash
npx skill-systems-thinking install
```

By default, the installer scans for installed agents on your machine and links the skill into their directories at both global and project-local paths. Only agents that are actually detected will be installed.

- Install for specific agents: `npx skill-systems-thinking install --agents kilo,claude-code`
- Global install only: `npx skill-systems-thinking install --global`
- Project-local install only: `npx skill-systems-thinking install --local`
- Force overwrite existing links: `npx skill-systems-thinking install --force`

### npm install (download only)

```bash
npm install skill-systems-thinking
```

This only **downloads** the package into `node_modules/skill-systems-thinking`; it does not link anything into your agent skill directories. After this, still run the install step:

```bash
npx skill-systems-thinking install
```

### GitHub download

```bash
git clone https://github.com/ShrimpLeon/systems-thinking.git
cp -r systems-thinking <agent-skills-dir>/
```

### Gitee download

```bash
git clone https://gitee.com/leon0903/systems-thinking.git
cp -r systems-thinking <agent-skills-dir>/
```

### Symlink (development)

```bash
ln -s /absolute/path/to/systems-thinking <agent-skills-dir>/
```

### Agent-specific setup

npx install automatically links the skill into each agent's skill directory. For manual installation, below are the paths for each supported agent.

| Agent | Skill directory |
|---|---|
| Kilo | `~/.config/kilo/skills/` or project `.kilo/agent/` |
| Claude Code | `~/.claude/plugins/custom-skills/` or project `.claude/` |
| Aider | `--skills-dir` path |
| Cursor | Project `.cursor/rules/` or global settings |
| OpenAI Codex | `~/.codex/skills/` |
| GitHub Copilot | `~/.copilot/skills/` |
| Windsurf | `~/.windsurf/skills/` |
| Zed | `~/.zed/skills/` |

> **Note:** If your agent does not appear above, check its documentation for custom skill/plugin paths.

### Verify installation

```bash
pwsh init.ps1
```

Look for `Verification Complete — OK`.

## Compatibility

The npm package `skill-systems-thinking` is compatible with the following AI agents:

| Agent | npm install compatible | Notes |
|---|---|---|
| Kilo | ✅ | Link via `~/.config/kilo/skills/` or `.kilo/agent/` |
| Claude Code | ✅ | Link via `~/.claude/plugins/custom-skills/` or `.claude/` |
| Aider | ✅ | Link via `--skills-dir` flag |
| Cursor | ✅ | Link via `.cursor/rules/` or global settings |
| OpenAI Codex | ✅ | Link via `~/.codex/skills/` |
| GitHub Copilot | ✅ | Link via `~/.copilot/skills/` |
| Windsurf | ✅ | Link via `~/.windsurf/skills/` |
| Zed | ✅ | Link via `~/.zed/skills/` |

The npx install automatically links the skill into each agent's skill directory.

## Usage

### 1. When to load

Load this skill when the task involves:

- Architecture design
- Debugging non-deterministic behavior
- Cross-module refactoring
- Any change where correctness AND robustness both matter

### 2. Read SKILL.md

Read `SKILL.md` first. The runtime prompt block installs the cognitive laws. The workflow below follows naturally.

### 3. Name things before touching code

Before proposing any change, the LLM must name four things:

- `x` — the controlled variable (what must stay correct)
- `u` — the control variable (the lever you will actually move)
- Observability — how will you know the current value of `x`?
- Bounds — every actuator saturates; no unbounded loop is acceptable

### 4. Seven-step loop

| Step | Principle | Reference |
|---|---|---|
| 1 | Identify — name `x`, `u`, observability, bounds. | `references/state-and-control.md` |
| 2 | Analyze — reproduce, measure, locate fault, state the model. | `references/modeling.md` |
| 3 | Stabilize — kill divergence / oscillation / leaks before features. | `references/stability.md` |
| 4 | Synthesize — minimal `u`; decouple what hurts, coordinate what helps. | `references/multivariable.md` |
| 5 | Close the loop — observe actual result; correct until bounded. | `references/closed-loop-workflow.md` |
| 6 | Compensate — feedforward measurable disturbances; clamp the actuator. | `references/disturbance.md` |
| 7 | Optimize — only then tune secondary indicators. | `references/bounded-control.md` |

For sampled-system and test-cadence concerns, also see `references/discrete-systems.md`.

### 5. Templates

These files are located in the skill's `templates/` directory (relative to the skill
installation root).

- **Debugging**: copy `templates/debugging-checklist.md` into the session.
- **Planning**: use `templates/change-proposal.md` to write a control plan.

### 6. Self-audit

Before declaring done, pass all MUST checks in `evals/checks.json`.

## Cognitive laws

The skill enforces 8 cognitive laws:

1. Name `x` before `u`. Unnamed targets are unregulated.
2. Observe before you guess. Measure current behavior before synthesizing the fix.
3. Stabilize before you optimize. Divergence under perturbation is failure.
4. Close the loop. Observe the actual result; correct until deviation is bounded.
5. Feedforward measurable disturbances; feedback the rest. Never crank gain on delay.
6. Decouple harmful coupling. Coordinate beneficial coupling. Regulate relations, not just absolutes.
7. Minimal control. The smallest `u` that moves `x` to target. No speculative extras.
8. Convergence: corrections must shrink. If they grow, you are unstable — stop and re-identify.

## Worked example

**Symptom:** an API endpoint intermittently returns 500 under load.

| Step | Control-theoretic action |
|---|---|
| Identify | `x` = error rate; `u` = retry/timeout/cache logic; bound = request budget. |
| Analyze | Reproduce under load; measure that error rate climbs with concurrency (unstable). |
| Stabilize | Add circuit breaker + bounded retries with backoff → error rate bounded. |
| Synthesize | Minimal change; don't rewrite the service. |
| Close the loop | Load-test again; error rate now converges to ~0. |
| Compensate | Feedforward on measurable dependency outage (fail fast) + feedback on the rest. |
| Optimize | Only now trim p99 latency. |

**Without this lens:** add retries with no bound → retry storm (an unstable delay loop) → worse than before.

## References

8 deep-dive references, each anchored to the original text with LLM behavior patterns:

| Topic | File |
|---|---|
| Closed-loop workflow | `references/closed-loop-workflow.md` |
| State, control, observability, bounds | `references/state-and-control.md` |
| Stability | `references/stability.md` |
| Modeling and model validity | `references/modeling.md` |
| Multivariable: decouple and coordinate | `references/multivariable.md` |
| Disturbance compensation and time-delay | `references/disturbance.md` |
| Bounded control | `references/bounded-control.md` |
| Discrete systems and test cadence | `references/discrete-systems.md` |

## Self-audit

`evals/checks.json` lists concrete MUST/SHOULD checks an LLM or reviewer applies to confirm the discipline was followed. All MUST items must pass before a task is called done.

## Contributing

- Every claim in `SKILL.md` must trace to a reference file.
- Every reference link must resolve to an existing file.
- Keep the skill small and aligned to the book.
- Run `./init.ps1` before submitting.

See `AGENTS.md` for the full working rules and definition of done.

## Version

This skill follows [Semantic Versioning](https://semver.org/) (`X.Y.Z`).

| Version | Date | Notes |
|---|---|---|
| 0.2.0 | 2026-07-26 | Added agent selection and location flags to install CLI |
| 0.1.5 | 2026-07-25 | Split README.md / README_CN.md for bilingual GitHub experience; unified version numbers |
| 0.1.4 | 2026-07-25 | Bug fix |
| 0.1.3 | 2026-07-25 | Unified version numbers across project; added XYZ version convention to AGENTS.md; removed postinstall script |
| 0.1.2 | 2026-07-25 | Added Gitee download link; updated repository and homepage to Gitee |
| 0.1.1 | 2026-07-24 | Fixed repository.url; expanded keywords; added homepage and bin field |
| 0.1.0 | 2026-07-24 | Initial public release |

Full history: [CHANGELOG.md](CHANGELOG.md).

## License

MIT License. See [LICENSE](LICENSE) for details.

## Source

Derived from Qian Xuesen (钱学森) & Song Jian (宋健), *Engineering Cybernetics* (工程控制论). The original book and its mathematical foundations are the authoritative source; this skill is a faithful interpretation, not a replacement.
