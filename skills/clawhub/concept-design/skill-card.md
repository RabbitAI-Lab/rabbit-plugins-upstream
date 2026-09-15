## Description:

Designs Daniel Jackson-style concept models and tests their application composition when explicitly invoked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use this skill to turn verified product needs into independent concept models, operational principles, actions, and synchronization rules. It supports concept-design review before PRD or implementation work proceeds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide the agent to read project files relevant to a design task.

Mitigation: Use explicit invocation and keep file review scoped to the requested concept-design work.

Risk: Concept models can be misleading when purposes, assumptions, or evidence are weak.

Mitigation: Require sources for facts, label inferences and unresolved decisions, and block only work that depends on unresolved assumptions.

Risk: Synchronization designs can omit required coordination or over-automate user control.

Mitigation: Check success and refusal behavior, under- and over-synchronization, concurrency, replay, and product-dependency closure before implementation.

## Reference(s):

- [Project homepage from ClawHub metadata](https://github.com/ontology-of-everything/concept-skills/tree/main/skills/en/concept-design)
- [Concept and Synchronization Specification Contract](references/spec-format.md)
- [Argument and Seam Criteria](references/criteria.md)
- [Synchronization Semantics and Composition Checks](references/sync-notation.md)
- [Reservation Transcription Example](references/example-reserving.md)
- [Sources and Scope](references/sources.md)
- [Concept Purposes and Synchronization](https://essenceofsoftware.com/posts/distillation/)
- [Jackson 2015 Concept Essay](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [WYSIWID](https://arxiv.org/abs/2508.14511)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with concept specifications, synchronization notation, diagrams, and open decisions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes application purpose, scenarios, concepts, synchronizations, synchronization and dependency diagrams, exclusions, and sourced open decisions.]

## Skill Version(s):

0.6.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
