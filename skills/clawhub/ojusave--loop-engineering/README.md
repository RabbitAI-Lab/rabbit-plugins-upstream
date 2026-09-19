# Loop Engineering

An outcome-first agent skill for doing real work through bounded,
evidence-backed feedback loops.

Loop Engineering gives agents a compact operating system for understanding a
request, defining what success means, choosing the smallest useful execution
shape, correcting failed strategies, and stopping with an honest status and
evidence level.

Use it for engineering, product and UI work, accessibility, research, strategy,
public writing, and reusable agent prompts.

## Activation

Invoke Loop Engineering directly with `$loop-engineering`, `loop:`, or the
native skill command supported by your agent. A personal, workspace, or project
instruction may also declare it the default when the host supports implicit
skill selection.

Once activated for a task, substantive follow-ups continue the same outcome
contract until the user opts out or clearly replaces the task. Default
activation does not imply a Deep workflow: narrow answers and reversible
changes stay Light.

For complex work, the skill first compiles the user's request into an outcome
contract. It identifies decision-relevant evidence gaps before choosing a
direct pass, one adaptive loop, a fixed workflow, or graph-shaped execution.
Specialist prompts come after that choice, not before it.

An optional response-shaping skill such as `i-have-adhd` can remain active
alongside Loop Engineering. The companion shapes progress updates and final
communication; Loop Engineering still owns execution, evidence, authority, and
stopping. No companion skill is required.

## How the control flow works

Loop Engineering does not begin by turning the request into a large prompt or
an org chart of agents. It first separates the intended outcome from proposed
mechanisms such as research, tools, agents, workflows, or graphs.

Each substantive run:

1. Understands the user, desired change, current state, constraints, authority,
   evidence gaps, and next use.
2. Compiles a compact outcome contract with a target, measure, proof
   requirement, guardrails, and next use.
3. Chooses a direct pass, one adaptive loop, a fixed workflow, or graph-shaped
   execution.
4. Creates bounded specialist briefs only for work another owner will actually
   perform.
5. Runs observe → predict → act → measure → learn cycles when feedback can
   change the next action.
6. Separates artifact verification from validation of the intended outcome.
7. Stops with a separate assignment status and evidence state.

### Direct pass, loop, workflow, or graph?

Loop depth and execution shape are separate decisions. A task can be important
without needing a graph, and a graph can contain several local loops.

| Shape | Use when | Keep out |
| --- | --- | --- |
| **Direct pass** | The request is narrow, the path is known, and one obvious check can verify it | State files, handoffs, and specialist ceremony |
| **Single adaptive loop** | One parent can coherently inspect, act, measure, and correct | Artificial role splitting |
| **Fixed workflow** | The sequence or approval path is known in advance | Dynamic routing that adds no control |
| **Graph-shaped execution** | Independent or conditional branches, distinct permissions or failure boundaries, verified fan-in, or durable resume state materially improve the work | Graphs added only because a task is long, Deep, or mentions multiple perspectives |

A graph node is not automatically an agent. It may be a deterministic check,
script, tool call, API action, operator task, independent reviewer, or human
approval gate. The parent retains shared requirements, integration, and final
authority.

## What it protects against

Without a trustworthy loop, an agent can mistake activity for progress: a build
passes, a page renders, a draft sounds polished, every branch reports `PASS`,
or a detailed handoff template exists. Loop Engineering requires evidence tied
to the intended result.

It distinguishes:

- `ARTIFACT VERIFIED`: the deliverable meets its specification
- `OUTCOME VALIDATED`: representative use demonstrates the intended result
- `DECISION READY`: the evidence is sufficient for the named decision owner

It stops as `COMPLETE`, `NEEDS HUMAN JUDGMENT`, `BLOCKED`, `NOT FEASIBLE`, or
`STAGNATED`. A local check or specialist `PASS` does not complete the parent
assignment by itself.

## Install

### Recommended: Skills CLI

If you have Node.js installed, use the open-source
[Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add ojusave/loop-engineering
```

The installer downloads the skill directly from GitHub, detects supported
agents, and lets you choose project or global installation. This repository is
not an npm package and does not need a `package.json`; `npx` runs the installer,
not Loop Engineering itself.

For a non-interactive global installation to Codex:

```bash
npx skills add ojusave/loop-engineering \
  --skill loop-engineering --agent codex --global --yes
```

The Skills CLI collects anonymous installation telemetry by default. Set
`DISABLE_TELEMETRY=1` for the command if you prefer to opt out.

### Manual Git installation

The shared `.agents/skills` location is recognized by Codex, Cursor, GitHub
Copilot, Gemini CLI, OpenCode, and Windsurf / Devin Desktop.

#### Personal installation

Available across your projects:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/ojusave/loop-engineering.git \
  "$HOME/.agents/skills/loop-engineering"
```

PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.agents\skills"
git clone https://github.com/ojusave/loop-engineering.git `
  "$HOME\.agents\skills\loop-engineering"
```

#### Project installation

To version the skill with a project, add it as a submodule:

```bash
mkdir -p .agents/skills
git submodule add \
  https://github.com/ojusave/loop-engineering.git \
  .agents/skills/loop-engineering
```

If your agent does not scan `.agents/skills`, use its native path from the
table below.

## Installation by agent

Paths were checked against the linked first-party documentation on July 14, 2026.

| Agent | Project location | Personal/global location | Invoke | Documentation |
| --- | --- | --- | --- | --- |
| OpenAI Codex | `.agents/skills/loop-engineering` | `~/.agents/skills/loop-engineering` | Mention `$loop-engineering`, or choose it from `/skills` | [Codex skills](https://developers.openai.com/codex/skills) |
| Claude Code | `.claude/skills/loop-engineering` | `~/.claude/skills/loop-engineering` | `/loop-engineering` | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Cursor | `.cursor/skills/loop-engineering` or `.agents/skills/loop-engineering` | `~/.cursor/skills/loop-engineering` or `~/.agents/skills/loop-engineering` | `/loop-engineering` | [Cursor Agent Skills](https://cursor.com/docs/skills) |
| GitHub Copilot | `.github/skills/loop-engineering`, `.claude/skills/loop-engineering`, or `.agents/skills/loop-engineering` | `~/.copilot/skills/loop-engineering` or `~/.agents/skills/loop-engineering` | `/loop-engineering`; in Copilot CLI, use `/skills reload` after installing | [GitHub Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) |
| Gemini CLI | `.gemini/skills/loop-engineering` or `.agents/skills/loop-engineering` | `~/.gemini/skills/loop-engineering` or `~/.agents/skills/loop-engineering` | Ask Gemini to use `loop-engineering`; inspect or reload with `/skills` | [Gemini CLI skills](https://geminicli.com/docs/cli/using-agent-skills/) |
| OpenCode | `.opencode/skills/loop-engineering`, `.claude/skills/loop-engineering`, or `.agents/skills/loop-engineering` | `~/.config/opencode/skills/loop-engineering`, `~/.claude/skills/loop-engineering`, or `~/.agents/skills/loop-engineering` | Ask OpenCode to use `loop-engineering`; it loads through the `skill` tool | [OpenCode skills](https://opencode.ai/docs/skills) |
| Windsurf / Devin Desktop | `.windsurf/skills/loop-engineering` or `.agents/skills/loop-engineering` | `~/.codeium/windsurf/skills/loop-engineering` or `~/.agents/skills/loop-engineering` | `@loop-engineering` | [Cascade skills](https://docs.devin.ai/desktop/cascade/skills) |
| Cline | `.cline/skills/loop-engineering`, `.clinerules/skills/loop-engineering`, or `.claude/skills/loop-engineering` | `~/.cline/skills/loop-engineering` | `/loop-engineering` | [Cline skills](https://docs.cline.bot/customization/skills) |

### Gemini CLI installer

Gemini CLI can also install the repository directly:

```bash
gemini skills install https://github.com/ojusave/loop-engineering
```

Add `--scope workspace` to install it only for the current project.

### Native-path installation

Replace `<skills-directory>` with any directory from the table:

```bash
mkdir -p <skills-directory>
git clone https://github.com/ojusave/loop-engineering.git \
  <skills-directory>/loop-engineering
```

The final structure must keep the complete skill folder together:

```text
<skills-directory>/
└── loop-engineering/
    ├── SKILL.md
    ├── agents/
    ├── references/
    └── scripts/
```

Do not copy only `SKILL.md`. The skill routes work to its references and uses
bundled scripts for deterministic state, handoff, prompt, claim, and editorial
checks.

## Use it

Invoke the skill explicitly with the syntax your agent supports, then state the
actual task:

```text
loop: reproduce and fix this checkout bug, then verify the real flow
```

```text
use loop to add this onboarding flow with responsive and accessible UI
```

```text
loop this task: research and write the article without generic AI prose
```

```text
loop: create a reusable prompt for another coding agent and test its failure cases
```

```text
loop: run schema review, rehearsal, human approval, migration, and verification as a fixed workflow
```

```text
loop: compare these deployment options with independent cost, reliability, security, and migration evidence, then integrate one decision
```

Loop Engineering supports explicit invocation and persistent defaults on
compatible hosts. Its instructions tell agents not to trigger it for incidental
mentions of a programming loop, event loop, or feedback loop. Agent behavior
ultimately depends on the host and model.

## Update

For an installation managed by the Skills CLI:

```bash
npx skills update
```

For a personal clone, set the path to the directory where you installed the
skill:

```bash
skill_dir="$HOME/.agents/skills/loop-engineering"
git -C "$skill_dir" pull --ff-only
```

If you used an agent's native directory, change `skill_dir` to that location.

For a project submodule:

```bash
git submodule update --remote .agents/skills/loop-engineering
```

Reload skills using your agent's command or restart the agent if the update is
not detected automatically.

## Uninstall

For a project installation managed by the Skills CLI:

```bash
npx skills remove loop-engineering
```

Add `--global` if you installed the skill globally.

Delete the `loop-engineering` directory from the location where you installed
it. For a Git submodule, remove it using your project's normal
submodule-removal workflow.

Loop state is stored separately under a project's `.loop/` directory only for
deep or genuinely multi-cycle tasks. Removing the skill does not delete
existing loop state.

## Requirements and trust

- The core skill is Markdown and follows the
  [Agent Skills specification](https://agentskills.io/specification).
- Basic Markdown-only use does not require Python. Python 3 is required when
  the workflow uses bundled scripts for persistent state, handoffs, or
  deterministic checks. On Windows, substitute `py -3` when `python3` is
  unavailable.
- Review `SKILL.md` and the bundled scripts before installing any third-party
  skill. Skills can instruct an agent to execute commands and modify files.
- Loop Engineering does not grant broader authority. It still requires human
  approval for production deployment, destructive operations, purchases,
  external publication, permission changes, privacy-sensitive access, and
  unsafe migrations.

## Repository layout

```text
loop-engineering/
├── SKILL.md                  # Compact router and invariant gates
├── agents/openai.yaml        # Optional Codex UI metadata
├── references/               # Specialist protocols
├── scripts/                  # State, handoff, and deterministic checks
└── tests/                    # Contracts, failure cases, and forward trials
```

The skill uses progressive disclosure: the agent sees the name and description
first, loads `SKILL.md` when selected or activated, and reads specialist
references only when the task needs them.

## Verify a checkout

Run the contract and regression suite:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

The suite covers persistent activation, outcome-first task compilation,
direct-versus-workflow-versus-graph routing, Deep topology gates, false-success
cases, and recorded forward trials.

## License

Loop Engineering is available under the [MIT License](LICENSE).
