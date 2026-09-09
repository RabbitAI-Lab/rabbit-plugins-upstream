## Description:

Models or reviews requirements as concepts using Daniel Jackson's concept design structure of Purpose, OP, State, Actions, and Syncs, stopping at model confirmation unless the user explicitly asks for downstream PRD, architecture, or code work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Product teams, requirements authors, and agent users use this skill to turn requirements, interviews, or existing concept models into concise concept models with purposes, state, actions, operational principles, synchronizations, coordination graphs, dependency graphs, and open decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow is primarily Chinese-language, which can create review or adoption friction for teams that do not work in Chinese.

Mitigation: Have a Chinese-fluent reviewer confirm the generated concept model or translate the model before relying on it in a product process.

Risk: The skill operationalizes concept-design methodology and may diverge from source texts if users need strict source fidelity.

Mitigation: Review the bundled methodology references and external source links when source fidelity matters.

## Reference(s):

- [Concept Design Skill Page](https://clawhub.ai/agenticweb4/skills/concept-design)
- [Criteria](references/criteria.md)
- [Sources](references/sources.md)
- [Sync Notation](references/sync-notation.md)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [WYSIWID Paper](https://arxiv.org/abs/2508.14511)
- [Concept Criteria Tutorial](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Sync Composition Tutorial](https://essenceofsoftware.com/tutorials/concept-basics/sync/)
- [Dependency Tutorial](https://essenceofsoftware.com/tutorials/concept-basics/dependency/)
- [Concept Design Distillation](https://essenceofsoftware.com/posts/distillation/)
- [Design Moves](https://essenceofsoftware.com/posts/design-moves/)
- [6.1040 Concept Rubric](https://61040-fa25.github.io/resources/concept-rubric)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown concept model with structured text blocks and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stops at model confirmation unless the user explicitly asks for PRD, architecture, or code output.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
