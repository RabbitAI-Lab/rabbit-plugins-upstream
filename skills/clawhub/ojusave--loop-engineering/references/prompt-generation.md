# Prompt-Generation Loop

## Contents

- [Outcome](#outcome)
- [Understand the downstream environment](#understand-the-downstream-environment)
- [Define the portable loop contract](#define-the-portable-loop-contract)
- [Make the downstream loop adaptive](#make-the-downstream-loop-adaptive)
- [Carry domain protocols](#carry-domain-protocols)
- [State behavior](#state-behavior)
- [Downstream specialist handoffs](#downstream-specialist-handoffs)
- [Prompt simulation](#prompt-simulation)
- [Anti-bloat check](#anti-bloat-check)
- [Assignment status and evidence state](#assignment-status-and-evidence-state)
- [Return criteria](#return-criteria)


## Outcome

Create a downstream prompt that causes an uninformed model or agent to perform the requested task through a bounded, evidence-backed loop.

The prompt must not depend on the receiver already understanding the phrase `loop engineering`.

## Understand the downstream environment

Determine from available context:

- receiving model or agent
- tools and repository access
- ability to execute code
- ability to browse current sources
- ability to use a browser or screenshots
- ability to persist files
- human approval boundaries
- requested artifact

Do not promise tools the receiver does not have.

When the request is to rewrite a specific prompt, brief, workflow, or other source artifact, require that source before drafting. If it is missing, ask for it and stop. Do not replace the requested rewrite with a generic placeholder template unless the user explicitly requests a template.

## Define the portable loop contract

The prompt should establish:

- outcome owner, class, baseline, target state, intended context, primary measure, threshold, and guardrails
- required evidence state and strongest feasible evidence
- next decision or use
- constraints and non-goals
- initial context inspection
- artifact-verification and outcome-validation evidence
- bounded action and verification cycles
- a hypothesis, predicted observation, actual observation, measured delta, and learning for each meaningful cycle
- compact state when supported
- diagnosis after failure
- change of approach after repeated failure
- specialist routing by failure class
- explicit human boundaries
- separate assignment status and evidence state
- permission to adapt strategy but not to weaken or redefine success criteria, evidence, guardrails, or authority boundaries

Keep the contract compact enough that the task remains central.

## Make the downstream loop adaptive

Do not generate a rigid universal checklist. The downstream prompt must tell the receiver to derive the outcome contract, acceptance criteria, evidence plan, specialist composition, sequence, and stop conditions from the actual task and environment.

It may include stable invariants and example failure modes, but examples must not become compulsory steps. Require the agent to remove irrelevant checks and revise routing when new evidence changes the risk model.

## Carry domain protocols

### Coding

Require:

- repository inspection
- current behavior or reproduction
- smallest coherent implementation
- tests, type checks, build, runtime, and diff inspection where available
- current dependency and portability checks

### Product and UI

Require:

- user and job definition before code
- experience contract
- rendered primary-flow inspection
- mobile and desktop checks
- loading, empty, validation, error, success, and recovery states
- accessibility and keyboard verification

A build cannot be the only success gate.

Require the downstream agent to distinguish artifact verification from intended-use validation and to report the strongest evidence state actually reached.

### Research

Require:

- a task-specific evidence plan
- primary sources and reproducible observation where appropriate
- freshness dates
- claim ledger or equivalent
- source class, commercial incentive, independence, and optimization-risk review
- skepticism toward SEO, AEO, GEO, affiliate, PR, and vendor marketing content
- tracing statistics and repeated claims to the original source
- counterevidence
- explicit uncertainty

### Writing

Require:

- thesis and evidence before prose
- a commodity baseline, supported knowledge advantage, audience delta, and substitution test when the artifact must earn attention
- no imitation of named writers
- factual review
- editorial anti-slop pass
- punctuation rules, including no em dashes when requested
- earned ending
- people-first value before SEO, AEO, GEO, or marketing optimization
- rejection of filler, fake FAQs, keyword coverage, and vendor claims presented as neutral evidence

### Strategy

Require:

- decision and constraints
- materially different alternatives
- tradeoffs
- feasibility
- smallest reversible test

## State behavior

When the receiving environment supports files and multi-cycle state is useful, instruct it to use `.loop/` or another local non-committed state location. Prefer a repository-local exclude mechanism; do not edit a tracked `.gitignore` unless explicitly authorized.

The prompt must say not to store secrets, private data, or hidden reasoning.

When persistent files are unavailable, instruct it to maintain a compact visible operational ledger in context.

## Downstream specialist handoffs

For complex tasks, direct one parent orchestrator to route work to check owners and integrate results. Define what a specialist means in the receiving environment:

- use a real subagent, independent reviewer, or purpose-built checker when available
- otherwise use a cold same-session pass with a file handoff
- otherwise use a compact in-memory request/return receipt

Do not let the receiver claim a handoff occurred when no recipient or cold pass actually performed the check.

Do not instruct specialists to call one another freely.

Require a request containing the goal, artifact, inherited parent success criteria, current state, verified facts, remaining uncertainty, constraints, specialist task, acceptance checks, and predicted contribution.

Require a separate return section containing one status, findings, changes, evidence, actual observation, evidence state, unresolved uncertainty, and recommended next step. The parent must record a disposition and recheck the integrated result before closing the handoff.

## Prompt simulation

Before delivering the prompt, simulate at least:

1. A normal case
2. A failure or blocked case
3. A case where artifact checks pass but the intended outcome is not observed

For UI prompts, also simulate the downstream agent trying to declare success after a passing build without inspecting the interface.

For writing prompts, simulate a factual but generic draft that passes grammar checks, a public abstract whose vivid copy hides commodity takeaways, plus a polished SEO/AEO/GEO-shaped draft that launders vendor claims or adds filler for discoverability.

Revise the prompt if the agent can claim `COMPLETE`, `OUTCOME VALIDATED`, or `DECISION READY` without the relevant evidence.

Also simulate a failing strategy. The prompt must cause diagnosis, a bounded strategy change, or an honest stop. It must not permit the receiver to make the failure disappear by rewriting its target, verifier, rubric, guardrails, or authority boundary. Persistent self-improvements require representative before-and-after evaluation and appropriate approval.

## Anti-bloat check

Remove instructions that:

- repeat the same rule
- explain loop engineering historically
- prescribe irrelevant specialist loops
- bury the assignment
- demand hidden chain-of-thought
- create fixed iteration targets instead of ceilings
- invent tools, frameworks, or project details

## Assignment status and evidence state

The downstream prompt must define:

- `COMPLETE`
- `NEEDS HUMAN JUDGMENT`
- `BLOCKED`
- `NOT FEASIBLE`
- `STAGNATED`

It must also define `NO RELIABLE EVIDENCE`, `ARTIFACT VERIFIED`, `OUTCOME VALIDATED`, and `DECISION READY`.

It must state that exhausted budget, failed verification, partial output, or passing artifact checks alone is not `COMPLETE` unless the original outcome contract is satisfied at its required evidence state.

## Return criteria

Return `PASS` when the prompt is self-contained, tool-realistic, domain-specific, bounded, carries the outcome contract and two-dimensional result model, and resists false success in simulation.

Return `REWORK_REQUIRED` when simulation reveals a loophole.
Return `BLOCKED` when the downstream environment is unknown and materially changes feasibility.
Return `NEEDS_HUMAN_JUDGMENT` when strictness or autonomy depends on user preference.
