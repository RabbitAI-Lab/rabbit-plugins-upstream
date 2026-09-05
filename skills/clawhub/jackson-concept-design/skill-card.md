## Description:

Models or reviews requirements as Jackson concepts defined by Purpose, OP, State, and Actions, then composes them with Syncs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and requirements reviewers use this skill to turn requirements discussions into Jackson-style concept models, including purposes, operational principles, state/actions, synchronizations, dependency notes, and unresolved decisions. It is intended to stop at model confirmation unless the user explicitly asks for downstream PRD, architecture, or code work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate for broad requirements discussions and may steer work into a Chinese-language Jackson concept-modeling workflow when that is not desired.

Mitigation: Use explicit routing or language preference rules, and invoke the skill only when concept modeling or requirements review is intended.

Risk: Concept models produced by the skill may contain incorrect boundaries, missing error cases, or misleading synchronizations.

Mitigation: Review the model with stakeholders before converting it into PRD, architecture, code, or implementation tasks.

## Reference(s):

- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [WYSIWID Paper](https://arxiv.org/abs/2508.14511)
- [Essence of Software Tutorials](https://essenceofsoftware.com/tutorials/)
- [Concept Criteria](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Sync Composition](https://essenceofsoftware.com/tutorials/concept-basics/sync/)
- [Dependency and Subsets](https://essenceofsoftware.com/tutorials/concept-basics/dependency/)
- [Concept Design Distillation](https://essenceofsoftware.com/posts/distillation/)
- [Design Moves](https://essenceofsoftware.com/posts/design-moves/)
- [6.1040 Concept Rubric](https://61040-fa25.github.io/resources/concept-rubric)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured concept specifications and sync notation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Chinese-language prose, code-style concept blocks, dependency notes, and unresolved-decision tables.]

## Skill Version(s):

0.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
