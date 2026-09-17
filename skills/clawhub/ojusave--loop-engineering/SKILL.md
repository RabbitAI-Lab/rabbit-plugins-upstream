---
name: loop-engineering
description: Run an adaptive, bounded, evidence-backed work loop when the user explicitly invokes it, asks it to remain active for the current task or thread, or when active personal, workspace, or project instructions declare it the default. Once active, use it for substantive follow-ups without requiring the tag again. Apply it across coding, product, UI, UX, accessibility, research, strategy, public writing, and reusable prompts that need task-specific checks, measured self-correction, honest evidence, and clean stopping. Keep narrow tasks light and do not trigger from incidental mentions of for-loops, event loops, or feedback loops.
---

# Loop Engineering

Do the requested work now through the smallest trustworthy feedback loop. Keep the task central. Do not teach loop theory, expose hidden reasoning, or turn the workflow into paperwork.

## Activate and continue cleanly

Run this workflow when the user explicitly invokes it, asks to keep it active for the current task or thread, or when an applicable personal, workspace, or project instruction says to use it by default. Once activated for a task, keep it active for substantive follow-ups in that task until the user opts out or clearly replaces the task. The user does not need to repeat the skill tag. Carrying the preference into unrelated new threads still requires an applicable persistent instruction; do not pretend thread memory is global configuration.

When loop-by-default is active, match the loop to the work. Use Light for a narrow answer, clarification, or reversible edit. Escalate to Standard or Deep only when stronger evidence, iteration, or coordination can materially improve the outcome.

Treat a follow-up in the same task as a delta to the current outcome contract: retain the main outcome, guardrails, proof requirement, completed work, and unresolved asks; change only what the new message adds, corrects, or replaces. Start a new contract when the user clearly replaces the task. Never use continuity to preserve a stale assumption after the user has corrected it.

## Start with a success card

Understand the request before choosing research, tools, agents, subagents, workflows, or graphs. Preserve the user's raw request as evidence, then identify the intended stakeholder, outcome or decision, current state, constraints, authority boundaries, evidence gaps, and required next use. Treat proposed mechanisms as hypotheses until they are justified by that outcome.

For a narrow, clear request, do not rewrite it into a larger prompt. Proceed with the obvious Light loop. For a complex request, compile the understanding into the success card below. Ask only when a missing choice would materially change the outcome, risk, or authority required. When the user asks to rewrite a specific artifact but has not supplied it, request the artifact and stop. Do not substitute a generic template unless the user explicitly asks for one.

Record only what will change the work:

```text
Starting point:
Target:
Measure and threshold:
Proof required: ARTIFACT VERIFIED | OUTCOME VALIDATED | DECISION READY
Guardrails and exclusions:
Next use or decision:
```

Infer obvious fields. Ask only when a missing choice is consequential or impossible to infer safely. Do not let later failures weaken the target, proof requirement, guardrails, or authority boundaries.

## Choose the smallest loop

- **Light:** one narrow, reversible change with an obvious check. Work in memory; no handoff or state files.
- **Standard:** a normal feature, diagnosis, bounded research task, or substantial revision. Use up to four evidence-producing cycles. Persist state only when it will materially help across cycles.
- **Deep:** cross-cutting, ambiguous, high-risk, or multi-specialist work. Use compact persistent state and up to six parent cycles.

Do not manufacture iteration. If feedback cannot change the next action, perform one pass and verify it.

Deep is not automatically graph-shaped. Complete the outcome contract before selecting an execution mechanism. When a Deep task has genuinely independent workstreams, distinct authority or failure boundaries, branching work that must converge, or durable dependencies across artifacts or sessions, read `references/orchestration.md` and declare an execution topology before creating handoffs. Otherwise keep one parent loop with the smallest necessary checks.

## Detect the execution mode

Before planning specialists, use the strongest mode actually available:

1. **Real specialist:** A subagent, independent reviewer, or purpose-built checker can receive a bounded task and return evidence. Create and deliver a handoff; the parent integrates the result.
2. **Cold same-session pass:** No independent specialist is available, but files are. Save the handoff, reopen only the request and artifact needed for that failure class, and review without relying on the maker's narrative. Say that independence was limited.
3. **In-memory pass:** Neither specialists nor useful file state are available. Use a compact request/return receipt in context and report the limitation.

A named role or undelivered template is not a handoff. Do not claim a specialist participated unless something actually received the task and returned findings.

## Route by the failure that matters

Use the smallest set of checks capable of observing material failure. A specialist is a check owner, not automatically another agent.

- Code, bugs, refactors, architecture: read `references/engineering-loop.md`.
- Product behavior, flows, or information architecture: read `references/product-ux-loop.md` before implementation.
- Rendered interface or visual design: read `references/ui-visual-loop.md` after implementation.
- Accessibility: read `references/accessibility-loop.md`.
- Framework, library, API, protocol, service, database, build, or deployment choice: read `references/freshness-portability.md` before choosing.
- Research or factual synthesis: read `references/research-loop.md`.
- Recommendations, comparisons, market claims, or incentive-shaped sources: also read `references/source-integrity.md`.
- Strategy or prioritization: read `references/strategy-loop.md`.
- Talks, abstracts, positioning, or public arguments that must earn attention: read `references/audience-value-loop.md`.
- Blogs, essays, or thought leadership: read `references/article-loop.md`, then `references/editorial-loop.md`.
- A prompt, agent brief, rule, or reusable workflow: read `references/prompt-generation.md`.

Read `references/orchestration.md` only when more than one check owner participates or a handoff is needed. Read `references/verification.md` when proof is ambiguous, subjective, high-impact, or easy to fake. Read `references/foundations.md` and `references/adaptive-task-design.md` only for deep loops, loop-design work, or when the initial route fails. Use `references/examples.md` only when an example would resolve uncertainty.

## Run the cycle

For each meaningful cycle:

1. **Observe:** Establish the current result or strongest baseline.
2. **Predict:** State what should change and why.
3. **Act:** Make one coherent, reversible intervention or collect one decisive fact.
4. **Measure:** Compare the observation with the prediction, target, and guardrails.
5. **Learn:** Record the delta or decision-relevant learning.
6. **Decide:** Adopt, adapt, abandon, escalate, or stop.

A failed attempt can be useful when it eliminates a material hypothesis. A new artifact without measured change or useful learning is not progress. Change strategy after the same direction fails twice; stop `STAGNATED` when no credible alternative remains.

## Keep state proportional

Use memory by default. For deep or genuinely multi-cycle work, run:

```bash
python3 <skill-directory>/scripts/init_loop_state.py --task "<concise task>" --mode deep
```

The script keeps `.loop/` outside version control without editing the tracked `.gitignore` unless `--edit-gitignore` is explicitly supplied. Never store secrets, credentials, personal data, copied production data, or hidden reasoning in loop state.

## Make handoffs executable

Create a handoff only when another check owner will actually receive it:

```bash
python3 <skill-directory>/scripts/create_handoff.py \
  --from-loop "<source>" \
  --to-loop "<recipient>" \
  --objective "<bounded task>" \
  --artifact "<path or artifact>" \
  --uncertainty "<what remains unknown>" \
  --acceptance "<observable checks>" \
  --state-dir "<.loop task directory>"
```

The generated artifact inherits the parent success criteria and separates the request, specialist return, and parent closure. Deliver it through the selected execution mode. Record the return and closure with `scripts/complete_handoff.py`; run `--help` for the bounded fields. Validate each phase:

```bash
python3 <skill-directory>/scripts/validate_handoff.py <handoff> --stage request
python3 <skill-directory>/scripts/validate_handoff.py <handoff> --stage return
python3 <skill-directory>/scripts/validate_handoff.py <handoff> --stage closed
```

The specialist returns exactly one status: `PASS`, `REWORK_REQUIRED`, `BLOCKED`, or `NEEDS_HUMAN_JUDGMENT`, plus evidence and one evidence state. `PASS` never makes the whole assignment complete by itself. The parent records its disposition and rechecks the integrated result.

## Preserve the non-negotiable gates

- **Technology:** Verify current official support, compatibility, license, project health, and migration surface. Prefer a fit existing convention, open standard, maintained open source, or thin adapter before custom infrastructure.
- **Visible product work:** Define the user, job, entry point, primary path, decisions, states, and recovery before code. After code, exercise the real flow at representative desktop and mobile widths, including relevant loading, empty, error, success, permission, destructive, and recovery states. Check keyboard use, focus, semantics, names, contrast, zoom, and reduced motion. Without rendered inspection, do not claim visual acceptance.
- **Research and recommendations:** Audit author, date, method, source class, independence, and commercial incentive. Vendor, affiliate, PR, SEO, AEO, and GEO material can document claims but cannot independently validate comparative quality or outcomes.
- **Public writing:** Establish the audience, arguable thesis, evidence, fair counterargument, reason now, and earned ending. When attention matters, identify what the audience already knows and what supported evidence, access, demonstration, synthesis, or judgment they gain here. Never invent privileged evidence. Run `scripts/check_blog_slop.py` for article drafts, then perform editorial review; the script is only a warning tool.
- **Reusable prompts:** Make the downstream instructions self-contained, tool-realistic, bounded, and resistant to false success. Simulate a normal case, a blocked or failing case, and a case where artifact checks pass but the intended outcome does not.
- **Authority:** Require approval before production changes, deployments, destructive operations, purchases, external publication or messages, permission changes, privacy-sensitive access, or migrations without tested rollback.

## Verify and stop honestly

Verification asks whether the artifact meets its specification. Validation asks whether it works for the intended stakeholder and context. Prefer direct observation of the contracted outcome; deterministic checks are not automatically stronger than representative use.

Report one evidence state:

- `NO RELIABLE EVIDENCE`
- `ARTIFACT VERIFIED`
- `OUTCOME VALIDATED`
- `DECISION READY`

Report one assignment status:

- `COMPLETE`: the scoped target and required proof are reached, guardrails pass, and no required work remains.
- `NEEDS HUMAN JUDGMENT`: the remaining choice depends on taste, priorities, risk, values, or authority.
- `BLOCKED`: a required external dependency, access, permission, or evidence source is unavailable.
- `NOT FEASIBLE`: the requested outcome cannot be achieved safely or credibly within the constraints.
- `STAGNATED`: two consecutive parent cycles produced neither measurable progress nor decision-relevant learning, the hypothesis changed, and no credible intervention remains.

Do not use model confidence or a self-authored score as the only approval. For persistent changes to this workflow, its prompt, rubric, routing, or evaluator, require representative before-and-after cases and an independent or cold check.

## Respond to the user

Lead with the delivered result. Mention files changed, decisive checks, and material limitations only when useful. Keep detailed state, handoff receipts, cycle logs, and internal vocabulary out of the response unless the user asks for them.

Honor any active response-shaping skill as a presentation constraint rather than copying its instructions into this workflow. When the user activates `i-have-adhd`, use its loaded contract for progress and final responses while Loop Engineering continues to own task execution, evidence, and stopping. Do not make the optional companion skill a prerequisite for Loop Engineering.

End with the assignment status and evidence state, but do not force a nine-part process report onto a simple task.
