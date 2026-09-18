# Orchestration and Handoffs

## Contents

- [Parent and check owners](#parent-and-check-owners)
- [Execution modes](#execution-modes)
- [Understand before orchestrating](#understand-before-orchestrating)
- [Choose the smallest execution architecture](#choose-the-smallest-execution-architecture)
- [Choose execution topology](#choose-execution-topology)
- [Topology state and execution](#topology-state-and-execution)
- [Routing](#routing)
- [Handoff lifecycle](#handoff-lifecycle)
- [Return and integration](#return-and-integration)
- [Conflicts and stopping](#conflicts-and-stopping)

## Parent and check owners

Use one parent for the assignment. The parent owns the user outcome, success card, shared evidence, routing, budget, integration, approval boundaries, and terminal state.

A specialist is the owner of one material failure check. It is not automatically a separate agent. The parent must know what can actually receive and execute the check before creating a handoff.

Specialists inherit the parent target, measure, guardrails, and proof requirement. They may define local acceptance checks but must not weaken the assignment contract. They return to the parent rather than calling one another freely.

## Execution modes

Select the strongest available mode and record it when independence matters.

### Real specialist

Use when a subagent, human reviewer, independent context, or purpose-built checker can actually receive a bounded task.

1. Create and validate the handoff request.
2. Deliver it to the named recipient.
3. Require a completed return with evidence.
4. Validate the return.
5. Let the parent integrate and remeasure the overall target.

### Cold same-session pass

Use when no independent recipient is available but files can preserve a clean request.

1. Write the handoff.
2. Reopen the original request, success card, handoff request, and target artifact.
3. Ignore the maker's narrative and inspect from the named failure class.
4. Complete the return and disclose that maker/checker independence was limited.
5. Let the parent integrate and remeasure.

### In-memory pass

Use when neither an independent recipient nor useful file state exists. Keep a short request/return receipt in context. Do not claim independent review.

An undelivered template, a role label, or a statement that a specialist “participated” is not a handoff.

## Understand before orchestrating

Do not begin by rewriting the user's request into a detailed multi-agent prompt. First complete the parent outcome contract: the stakeholder and intended change, decision or deliverable, current state and verified facts, material unknowns, constraints and non-goals, authority boundaries, proof requirement, and next use.

Separate the outcome from the proposed mechanism. Research, tools, agents, subagents, workflows, and graphs are candidate means, not requirements merely because the user mentioned them. A requested diagram or architecture may still be a deliverable, but do not let its labels override the safer execution shape. Turn an unknown into a research question only when resolving it can change the decision, design, risk, or proof. Give that research a source standard, bounded budget, and observable return.

For coordinated work, compile one compact execution brief after the outcome contract:

| Brief field | Required meaning |
| --- | --- |
| Outcome and receiver | What changes, for whom, and what they do next |
| Known facts and unknowns | Verified context plus decision-relevant evidence gaps |
| Boundaries | Scope, non-goals, authority, privacy, safety, and approvals |
| Deliverables and proof | Observable outputs and the evidence needed to accept them |
| Cut line | Required work now, deferred work, and the trigger to resume it |
| Integration owner | Who resolves conflicts and owns the final result |

The execution brief is not a polished restatement of the conversation. It is the smallest operational contract needed to choose and control the work.

## Choose the smallest execution architecture

Choose only after the outcome contract and evidence gaps are clear:

1. **Direct pass:** The request is narrow, the path is known, and one obvious check can verify it.
2. **Single adaptive loop:** The path may require iteration, but one parent can coherently inspect, act, and verify.
3. **Fixed workflow:** The work has a known ordered sequence or approval path whose dependencies should not be decided dynamically.
4. **Graph-shaped execution:** Work is independent, conditional, permission-separated, failure-isolated, or durable enough that explicit nodes, edges, fan-in, and resume state materially improve control.

Do not promote work to a graph because the prompt is long, the task is Deep, or multiple perspectives sound useful. Prefer a fixed workflow when the sequence is known and a single loop when branch state would add no operational value.

After selecting the architecture, generate bounded node or specialist briefs only where another owner will actually do the work. A node is not automatically an agent. Prefer a deterministic check, script, tool call, API action, or human gate when interpretation is unnecessary or authority must remain human. A fixed workflow may be drawn as a graph without becoming dynamic graph-shaped execution.

Each brief must contain the goal, necessary shared context, inputs, constraints and authority, output contract, budget, dependencies, and return route. Keep parent requirements, decisions, shared facts, and final integration with the parent instead of copying the entire conversation into every branch. If missing context would materially change a safe or useful brief, obtain that context first. A requested provisional template must be labeled incomplete and must not authorize execution.

## Choose execution topology

Default to one adaptive parent loop. Do not create an explicit graph merely because the task is Deep or more than one checker exists.

Declare a topology before the first handoff when at least one condition is material:

- two or more genuinely independent workstreams can run concurrently
- different branches have distinct tools, permissions, failure boundaries, or approval gates
- branching work must converge through a verified integration or decision
- dependencies span multiple artifacts, environments, or sessions and must resume without restarting completed work

An execution topology is an operational contract, not a requirement to adopt a graph framework. If explicit topology cannot improve outcome quality, elapsed time, isolation, recovery, or authority control, keep the single parent loop.

## Topology state and execution

Record the smallest useful topology in parent state:

| Field | Required meaning |
| --- | --- |
| Node or check owner | Stable identifier and bounded responsibility |
| Depends on | Node identifiers whose verified outputs are required |
| Input and artifact | Required context plus the durable location read or written |
| Output contract | Observable return needed by the parent or merge |
| Status and budget | Current state plus bounded work, tool, token, or time allowance |
| Failure route | Retry, targeted rework, replan, escalation, or stop condition |
| Merge owner | Parent-owned integration point and compatibility checks |
| Approval gate | Human authority required before consequential action |

Execute the topology with these rules:

1. The parent activates only nodes whose dependencies are satisfied. Parallelize only nodes that do not require one another's unfinished work.
2. Each branch returns a bounded result or a durable artifact reference. Data may flow through artifacts, but control, approval, and terminal authority return through the parent.
3. Before fan-in, the merge owner checks that every required branch returned, conflicts are resolved, shared assumptions and state remain compatible, and guardrails still pass.
4. Retry only the failed or invalidated branch when recovery is safe and within budget. Propagate invalidation to dependent nodes; replan or escalate when the failure changes the topology.
5. On resume, re-read the topology and verify external state before repeating actions. Close only when required nodes are integrated or explicitly deferred with their outcome impact recorded.

## Routing

Start with the failure that could let the artifact pass while the intended outcome fails. Add only check owners able to observe a material risk.

Common compositions are hypotheses, not mandatory pipelines:

- **Visible product feature:** product UX before implementation; engineering; rendered UI and accessibility after implementation; parent rerun.
- **Backend-only change:** engineering; security, concurrency, or migration review only when relevant; parent integration.
- **Research-backed article:** research and source incentives; audience value when attention matters; article; editorial and factual verification; parent integration.
- **Public abstract:** evidence/access inventory; audience value; argument; editorial; promise verification; parent integration.
- **Strategy:** current research when needed; strategy; feasibility and counterargument; parent integration.
- **Downstream prompt:** task analysis; prompt generation; normal, failure, and false-success simulation; relevant domain review; parent integration.

Parallelize only genuinely independent checks with a clear integration contract. Do not parallelize work that depends on a shared experience contract or a single coherent argument.

## Handoff lifecycle

Use `scripts/create_handoff.py` when persistent files are available. It reads the parent state and refuses to create a handoff until the baseline, target, measure, guardrails, proof requirement, and constraints are populated.

The artifact has three phases.

### Request

The parent supplies:

- goal and artifact
- inherited parent success criteria
- current state and already verified facts
- remaining uncertainty
- constraints and preserve/change boundaries
- the bounded specialist task
- observable acceptance checks
- predicted contribution

Validate this phase with:

```bash
python3 scripts/validate_handoff.py <handoff> --stage request
```

### Return

The recipient supplies the fields below. Record them with `scripts/complete_handoff.py return`; run `--help` for the full command:

- one status: `PASS`, `REWORK_REQUIRED`, `BLOCKED`, or `NEEDS_HUMAN_JUDGMENT`
- findings and changes
- reproducible evidence
- actual observation or decision-relevant learning
- one evidence state
- unresolved uncertainty
- recommended next step

Validate this phase with:

```bash
python3 scripts/validate_handoff.py <handoff> --stage return
```

### Parent closure

After integration, the parent records exactly one disposition: `ACCEPTED`, `REWORK`, or `ESCALATED`, plus evidence from rechecking the integrated result. Use `scripts/complete_handoff.py close`, then validate with `--stage closed`.

The lifecycle status should move from `REQUESTED` to `RETURNED` to `CLOSED`. A valid return is not closed until the parent records its disposition.

## Return and integration

Specialist status and assignment status are different. A local `PASS` does not imply assignment `COMPLETE`.

Before accepting a return, confirm that:

- the recipient answered the bounded task
- evidence supports the selected status and evidence state
- remaining uncertainty is explicit
- protected constraints remain intact
- the return does not silently redefine success

After accepting or applying changes, the parent reruns the primary scenario and remeasures the parent target. For multi-specialist work, also check that terminology, assumptions, UX requirements, implementation states, accessibility, factual meaning, and technology constraints still agree.

If only artifact checks are possible, report `ARTIFACT VERIFIED` and preserve the validation gap.

## Conflicts and stopping

When checks conflict:

1. Identify the parent acceptance criterion affected.
2. Prefer evidence closest to the user's intended outcome.
3. Preserve non-negotiable safety and accessibility requirements.
4. Run a representative scenario when possible.
5. Escalate taste, cost, risk, values, or authority decisions.

Do not average incompatible recommendations. Route rework through the parent:

```text
specialist -> parent -> prioritized rework -> targeted verification -> parent
```

Stop rather than creating a circular chain. If two parent cycles yield neither measurable progress nor decision-relevant learning and no credible alternative remains, return `STAGNATED`.
