# Latency — Why It Feels Slow, And Which Part Is Actually Slow

Spend and latency share causes but not fixes: a big context costs money on every turn *and* adds assembly time, while a hung integration costs nothing and ruins the experience. Measure before trimming. Token accounting lives in `cost.md`; this file is about wall-clock time.

**Before this pass**, read `## System Baseline` in `~/Clawic/data/analysis/memory.md` (or the file its `## Boxes` line names) for previously measured timings. "Slow" is a comparison; with no prior number the first job of this pass is to create one.

**Contents:** [Decompose The Wait](#decompose-the-wait) · [Round Trips Dominate](#round-trips-dominate) · [Read Amplification](#read-amplification) · [Startup Cost](#startup-cost) · [Filesystem Traps](#filesystem-traps) · [Waiting On Something External](#waiting-on-something-external) · [Host-Level Causes](#host-level-causes) · [The Bisection](#the-bisection) · [Sweep](#sweep) · [Write It Down](#write-it-down)

## Decompose The Wait

Four components, measurable separately. Attribute first; each has a different fix and three of the four are not about the model at all.

| Component | Measure | Typical fix |
|---|---|---|
| Context assembly | Time from request to the first outbound call | Trim the always-loaded set, remove slow file discovery |
| Model time | Time to first token, then tokens per second | Fewer input tokens; a smaller model for mechanical steps |
| Tool execution | Duration of each tool call | Fix the slow tool, or stop calling it |
| Round trips | Count of sequential tool calls in the task | Batch independent calls — the biggest lever, below |

If the user cannot say which one feels slow, ask nothing: run one representative task and time the four. A measurement takes a minute and settles what an hour of speculation cannot.

## Round Trips Dominate

Every sequential tool call is a full cycle: send the whole context, wait for the model, run the tool, send everything again. Twelve sequential calls cost twelve round trips *and* a context that grew twelve times.

- **Independent calls run together.** Reading four files to compare them is one batch, not four turns. This is usually the single largest latency win available and it costs nothing in quality.
- **Dependent calls cannot be batched** — but they can often be collapsed: one command that produces the answer beats three that narrow toward it.
- **Signature of a round-trip problem**: total wall time far larger than the sum of the tool durations, and a transcript that alternates tool-call and tool-result with almost no reasoning between.

## Read Amplification

The same file read three or more times in one session is a finding: it is latency, spend, and a correctness risk (which copy is current). Causes are usually structural — the content is not in the entry point where it would be read once, or a chain of pointers forces a re-read at each hop (`workspace.md`).

Also count reads that were never needed: whole-file reads used to check one value, directory listings of trees the task never touches.

## Startup Cost

Everything paid before the first useful action: instruction files loaded, discovery of the workspace, integrations connected, tool servers started, memory read.

| Cause | Signal | Fix |
|---|---|---|
| Large always-loaded set | Startup grows with the file that was added last | SKILL.md Rule 8 |
| Slow tool server handshake | One server dominates startup | Start it lazily, or drop it (`integrations.md`) |
| Discovery over a huge tree | Startup scales with repository size | Scope the roots in `workspace_paths`; exclude vendor and cache directories |
| Network call at startup | Startup varies with connectivity | Defer it to first use |

Write the measured startup time into `## System Baseline` in `memory.md`. It is the number users notice most and the one nobody tracks.

## Filesystem Traps

- **Vendor and cache directories** (`node_modules`, `.venv`, `target`, `build`, `.git/objects`) dominate any unfiltered traversal. Exclude by name before searching, not after.
- **Network and synced filesystems** — cloud-synced folders, mounted shares, virtualized bind mounts — can be one to two orders of magnitude slower per file operation than a local disk. A workspace that lives inside a sync folder explains slowness that no amount of context trimming will fix.
- **Enormous single files** (multi-MB logs, generated data) turn a routine grep into a stall; cap search by file size.
- **Watchers** on a big tree burn CPU continuously and slow everything else; count them (`sessions.md`).

## Waiting On Something External

An integration with no timeout can stall a run indefinitely, and the user experiences it as "the agent froze". Every external call in a health check or a job gets an explicit connect and total timeout — 3s and 10s are workable defaults for checks — and note that some clients, `curl` among them, have no default total timeout at all (`integrations.md`).

Second pattern: a retry with a long fixed sleep. Three retries at 30s is a 90-second freeze with no output. Bound total retry time, and emit something between attempts.

## Host-Level Causes

Cheap to check, and they invalidate every other measurement while true.

| Check | Threshold worth reporting |
|---|---|
| Free disk | Under 10%, or under 5 GB — near-full disks slow writes and break caches |
| Memory pressure and swapping | Any sustained swap activity; a swapping machine makes everything look like an agent problem |
| CPU saturation by another process | A build, an indexer, or an orphan watcher holding a core (`sessions.md`) |
| Clock and time sync | Skew breaks signed calls, which then look like slowness through retries |
| Thermal throttling on a laptop | Sustained heavy load; the symptom is gradual, whole-machine slowdown |

## The Bisection

When attribution is unclear, halve the environment rather than theorizing:

1. Reproduce with the smallest input that still feels slow. If a trivial prompt is slow, the cause is startup or the always-loaded set, not the task.
2. Halve the always-loaded set and re-time. The half that restores speed contains the cause.
3. Disable non-essential tool servers and re-time.
4. Run the same task in a scratch directory with no workspace. Fast there means the workspace is the problem; slow there means the environment or the network is.
5. Time one representative tool call by hand. Slow by hand means the tool, not the agent.

Each step is one measurement, and each halves the search space; four steps cover a 16× range.

## Sweep

| Check | Passing looks like |
|---|---|
| Startup time measured | Recorded and comparable to the last baseline |
| Wall time attributed | Assembly / model / tools / round trips, with numbers |
| Independent tool calls batched | No alternating single-call turns in the transcript |
| No file read more than twice per session | Zero amplification findings |
| Search and discovery scoped | Vendor and cache directories excluded |
| Every external call bounded | Explicit connect and total timeouts |
| Host healthy | Disk above 10%, no sustained swap, no rogue CPU consumer |

## Write It Down

Same turn as the pass:

- Measured startup time, p95 for a representative task, per-integration latency, host headroom → `## System Baseline` in `memory.md`. A latency claim with no stored baseline is an opinion.
- Attributed slowness not yet fixed → `## Open Findings`, naming the component and its measurement.
- A slowness the user accepts (a synced workspace they need, a heavy tool server) → `## Accepted` with a review date.
- A tuning procedure that worked, with before and after numbers → `~/Clawic/data/analysis/artifacts/tuning-<kebab>.md`, plus its `## Boxes` line.
