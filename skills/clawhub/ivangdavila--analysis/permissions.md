# Authority — What The Setup Can Do, Not What It Did

**Before auditing grants**, read `## System Baseline` in `~/Clawic/data/analysis/memory.md` (or the file its `## Boxes` line names) for the last recorded allowlist and tool surface. A grant that appeared since the last baseline, with no decision behind it, is the finding.

The question this file answers is never "what did the agent do". It is: **if a hostile instruction arrived inside a file, a web page, an issue comment, or a tool result, what would it be able to do without asking anyone?** The transcript shows what was used; the grant shows what was possible.

**Contents:** [The Grant Surface](#the-grant-surface) · [Wildcards That Cancel The Allowlist](#wildcards-that-cancel-the-allowlist) · [Commands That Are Shells In Disguise](#commands-that-are-shells-in-disguise) · [Self-Modification](#self-modification) · [The Exfiltration Pair](#the-exfiltration-pair) · [Scope Ladder](#scope-ladder) · [Unused Grants](#unused-grants) · [Subagents And Delegated Authority](#subagents-and-delegated-authority) · [Audit Checklist](#audit-checklist) · [Write It Down](#write-it-down)

## The Grant Surface

Enumerate all seven; a review that covers only the first is the most common gap in this whole skill.

| Surface | What to read | Failure it produces |
|---|---|---|
| Command allowlist / auto-approve | Every pattern, including inherited defaults and per-project overrides | Arbitrary execution behind a pattern nobody re-read |
| Filesystem scope | Which roots are readable and writable, and whether `~` or `/` is one of them | A single instruction reads the whole home directory |
| Network egress | Whether outbound requests are limited to named hosts | The exfiltration half of the pair below |
| Credential exposure | Which environment variables and credential files are visible to the process | Every allowlist becomes irrelevant if the token is already in the environment |
| Self-modification | Write access to the config, allowlist, instructions, or skills the agent loads | No permission model at all — see below |
| Delegated authority | What a spawned subagent inherits, and whether it can spawn further | The narrow grant you reviewed is not the grant that ran |
| Third-party tool servers | Each connected server's declared capabilities and where its process runs | A tool named `read_file` is only as honest as its implementation (`skill-audit`) |

## Wildcards That Cancel The Allowlist

A pattern is safe only if every string it matches is safe. Test each entry by asking what the *worst* matching invocation does.

| Pattern | What it actually permits | Narrower form |
|---|---|---|
| `*` or an empty allowlist with auto-approve on | Everything; the rest of the list is decoration | Enumerate the ten commands actually used |
| `git *` | Hooks, `-c core.pager=<cmd>`, `-c alias.x=!<cmd>`, `--upload-pack=<cmd>` — all of which execute | `git status`, `git diff`, `git log`, each without arguments that start with `-c` |
| `npm *`, `pip *`, `brew *` | Package installs run lifecycle scripts from the network as the user | `npm ci` on a committed lockfile only, install steps proposed not auto-approved |
| `docker *` | `-v /:/host` plus `--privileged` is host root | Read-only subcommands; runs proposed |
| `curl *`, `wget *` | Fetch anything, write anywhere with `-o`, upload with `-d @file` | Named hosts, no `-o`, no `-d @` |
| `find *` | `-exec` and `-delete` | `find <path> -name <glob>` without `-exec`/`-delete` |
| `ssh *`, `rsync *` | Remote execution; `rsync -e '<cmd>'` runs locally | Named hosts, no `-e` |
| Anything ending in a bare `*` after a subcommand | Flags are arguments too; the dangerous ones are always flags | Pin the flags, not just the binary |

Rule of thumb with teeth: if the pattern can be satisfied by a string containing `-e`, `-c`, `--exec`, `!`, `$(`, or a backtick, it is an execution grant regardless of which binary it names.

## Commands That Are Shells In Disguise

Approving any one of these is approving arbitrary execution, and each is routinely added to allowlists as "harmless":

`bash -c` / `sh -c` / `zsh -c` · `env` (runs its argument) · `awk` (`system()`, `|& getline`) · `sed` with `e` in GNU · `perl`/`python`/`ruby`/`node` with `-e` · `xargs` · `find -exec` · `make` (targets are shell) · `tar --to-command` / `--use-compress-program` · `rsync -e` · `ssh` · `less`/`man`/`vi` (`!cmd`, and pagers spawn from other tools) · `git` (above) · any `*-run`, `*-exec`, or task-runner binary.

The audit output for this is one line per matching allowlist entry, severity CRITICAL when auto-approve is on, WARNING when each call still prompts.

## Self-Modification

If the agent can write to the files that define its own permissions, instructions, or loaded skills, then every other control on this page is advisory. Check the write scope against: the allowlist/settings file, the top-level instruction files, the skills directory, hook or startup scripts, and anything sourced by them.

Two honest positions exist: some setups need self-editing because that is the workflow (writing skills, editing prompts). The mitigation is not prohibition, it is **review**: those files live in version control, and a change to them is a diff a human reads. A self-editable config that is not in version control is CRITICAL; one that is tracked and reviewed is INFO with a note.

## The Exfiltration Pair

Neither half is a finding alone; together they are the whole threat model of a compromised instruction.

- **Read reach** — every path the process can read, including credential files and environment variables.
- **Outbound reach** — any way bytes leave: HTTP, DNS lookups of attacker-chosen names, git push, a package publish, an email or chat tool, a webhook.

If read reach includes credentials or private data and outbound reach is unconstrained, the setup's security rests entirely on the model never following a hostile instruction. Report it as one CRITICAL finding naming both halves, with the cheaper half to close named as the action — almost always the outbound half, via an egress allowlist or by removing a tool nobody uses.

## Scope Ladder

Grant at the lowest rung that gets the work done, and write which rung was chosen into `artifacts/permission-posture.md` so the next audit sees a decision instead of an accident.

1. Read-only, project directory only, no network, prompts for everything else. The default for anything unattended.
2. Read-only plus an enumerated command list; writes limited to the project; egress to named hosts.
3. Writes plus a fixed set of side-effecting commands; still no shell, no package manager.
4. Broad grants inside a sandbox or a disposable machine, where blast radius is bounded by the container rather than by the list.
5. Broad grants on the real machine — only with a human watching in real time, and never for scheduled or triggered runs.

Unattended work (scheduled jobs, webhooks, anything triggered by content someone else can write) never runs above rung 2. That is the single highest-value rule on this page: attended risk is bounded by attention, and a scheduled run has none.

## Unused Grants

Grants accumulate; nothing removes them. Compare the allowlist against what was actually invoked in the retained run history: an entry with no invocation in 30 days is INFO with the action "remove and see what breaks", and entries never invoked since they were added are the cheapest security win in the whole audit — no behavior changes, and the blast radius shrinks.

## Subagents And Delegated Authority

- A spawned agent inherits the parent's grants unless the platform narrows them; assume inheritance and verify rather than the reverse.
- Whether a subagent can spawn further agents decides whether depth is bounded — unbounded depth turns one bad instruction into a fan-out that also shows up in `cost.md` and `sessions.md`.
- Content a subagent fetches (a page, an issue, a file) is untrusted input arriving inside a trusted context. The grant that matters is the one held at fetch time, not at prompt time.

## Audit Checklist

| Check | Passing looks like |
|---|---|
| Auto-approve list enumerated, per project and global | Every entry recognizable and justified by a task someone still does |
| No shell-in-disguise entry | None of the binaries above appear with free-form arguments |
| No bare `*`, and no pattern satisfiable by `-e`, `-c`, `!`, `$(` | Flags pinned, not just binaries |
| Filesystem write scope | Project directories only; `~` and `/` are not writable roots |
| Config, instructions, and skills | Either not writable, or writable and tracked in version control |
| Outbound reach | Enumerable; named hosts where the platform supports it |
| Credentials visible to the process | Only the ones this work needs, and each in the inventory (`secrets.md`) |
| Unattended paths (schedules, webhooks, triggers) | At rung 2 or below |
| Subagent inheritance and depth | Known, bounded, and written in the baseline |
| Third-party tool servers | Each one's origin and capabilities identified (`skill-audit` for the code question) |

## Write It Down

In the same turn as the pass:

- The current grant surface — allowlist size, write roots, egress posture, self-edit status, subagent depth → `## System Baseline` in `memory.md`.
- Every open hole with its rung and the narrower form → `## Open Findings`.
- A deliberate broad grant the user defends → `## Accepted`, with the scope, the reason, and a review date (default `secret_rotation_days`).
- The chosen posture and what it rejected — rung, egress rule, which commands were deliberately allowed and why → `~/Clawic/data/analysis/artifacts/permission-posture.md`, plus its `## Boxes` line. Without it, the next audit re-litigates every entry.
