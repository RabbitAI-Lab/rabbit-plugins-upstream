# Discovery and low-effort interaction

Read this reference when starting complete IA work, selecting questions, deciding whether to stop, or planning an IA audit.

## Principle

The agent carries the IA method. The user supplies product knowledge in ordinary language. Never transfer professional quality-control work to a user who may not know IA.

Do not ask the user to choose Guided/Quick modes, approve jargon-heavy models, select a checkpoint, or restate “stop and wait.”

## Adaptive sufficiency loop

Run the sufficiency gate before every consequential architecture step, not only at intake. New objects, relationships, permissions, lifecycle rules, locale signals, evidence, and export requests can reveal a new blocking question.

Before each consequential step, classify open issues:

- **Blocking:** proceeding could select a materially different architecture, expose sensitive information, or create an expensive mistake. Ask and stop.
- **Important but assumable:** one default is defensible and reversible. State the assumption and continue.
- **Detail:** it will not affect the current IA decision. Defer it.

Do not use a numerical completeness score. Judge sufficiency against the decision being made.

An unknown blocks only the decision that depends on it. Continue useful independent analysis, but do not finalize, export, or imply certainty for the affected part.

## Host memory and prior preferences

Persistent memory can help with language and harmless presentation preferences, but it is not a current request or reliable product evidence.

- Do not create files or artifacts because another chat established an “always give me a file” preference.
- Do not reuse remembered roles, rules, research, approvals, or architecture decisions without current evidence.
- When memory conflicts with the current request, follow the current request.
- When a remembered preference would materially change effort, format, scope, or an external action, ask at the point of decision or use the non-mutating conversational default.

## First turn

### No usable brief

Ask a compact product-language round covering the minimum needed to begin:

- What product or service is being designed?
- Who mainly uses it and what are they trying to accomplish?
- Is it new, a redesign, or an audit of an existing product?
- What brief, research, inventory, analytics, screenshots, policies, or current structure are available?

Then stop. Do not create a placeholder architecture or artifact.

### Partial or substantial brief

First inspect all provided material. Reflect the product and scope in a few lines. Ask only questions that distinguish plausible architectures, normally no more than five. Then stop.

### Sufficient brief

Proceed, but reassess sufficiency when the model reaches another consequential decision. Do not ask a ritual confirmation merely because a workflow template contains a checkpoint.

## High-impact question lenses

Use only the lenses relevant to the product:

- outcome, audience, priority tasks, scope, and costly failures;
- core objects/content, relationships, states, and lifecycle;
- independent versus organization-scoped identities and ownership;
- visibility, permissions, consent, retention, and legal constraints;
- global versus contextual findability;
- audience vocabulary, organization logic, browse versus search needs;
- language, geography, jurisdiction, cultural convention, and local operating model when they change structure or terminology;
- scale, volatility, governance, and change authority;
- evidence that can confirm or challenge the proposed structure.

For sensitive or regulated domains, prioritize access, consent, retention, ownership, jurisdiction, and auditability before selecting architecture.

## Ask in product language

Questions must describe consequences the user can recognize.

Avoid:

> Is the role-context permission model correct?

Prefer:

> Can a doctor belong to more than one clinic, and should their access change depending on which clinic they are working in?

Avoid:

> Does the navigation model match your mental model?

Prefer:

> Should patients search across every clinic, or begin inside one clinic and see only its doctors?

Do not include hints that teach the user how to police the skill. The skill must perform its own scope, evidence, and completeness checks.

## Handling weak answers

“Everyone” or “all content types” is an incomplete prioritization, not evidence of equal needs or approval for every feature. Ask about the first useful audience outcome or first release when it affects structure. Distinguish accepting a recommendation from authorizing unrelated capabilities. Preserve the decision history so later diagrams and exports do not promote assumptions into confirmed scope.

If the user replies “yes,” “continue,” “I don't know,” or gives no new product detail:

1. do not repeat the same approval request;
2. offer a small set of plausible patterns when the user needs help recognizing the choice;
3. infer or recommend a defensible default from the brief and domain evidence;
4. state the default and its user-visible consequence briefly;
5. mark it Proposed or Inferred;
6. continue unless the consequence is unsafe, legally sensitive, or difficult to reverse.

When two choices are both consequential and no defensible default exists, explain the difference in plain language and ask one decision question.

## Decision pauses

Pause only for a real decision, not at a fixed number of checkpoints. A useful pause contains:

- a brief description of the product consequence;
- the smallest concrete choice needed;
- at most a few answer options when they genuinely simplify the decision.

Do not lead with internal section names such as “Checkpoint 3,” “Navigation Model,” or “Governance” unless the audience requested technical process detail.

## Export request

An export request is another consequential step. Before creating a semantic file, diagram prompt, or visual-builder handoff:

- verify that every visible item belongs to a domain;
- verify that important containment and cross-domain relationships are explicit;
- verify that role combinations, local conventions, and lifecycle transitions are not hidden guesses;
- ask and stop if a remaining unknown would materially change the requested artifact;
- otherwise export a clearly marked Proposed or Approved model according to the user's intent.

Confirm the requested deliverable from the current conversation. A remembered output preference does not authorize a presentation, diagram, canvas, prototype, or other file.

## Quick provisional work

Use only after an explicit request for speed, assumptions, or no questions. Keep the result compact: product understanding, candidate objects/content, initial organization and retrieval direction, material assumptions, and the next best check. Do not imitate a complete report.

## Redesign and audit intake

Inspect current navigation, content inventory, analytics, search logs, user research, support issues, permissions, governance, and upcoming changes when available. Distinguish current-state evidence from target-state recommendations.

## User control

The user may skip questions, change sequence, request more or less depth, or focus on one IA component. Follow that direction. If skipped discovery weakens a high-impact claim, provide provisional work and make that limitation visible rather than silently claiming certainty.
