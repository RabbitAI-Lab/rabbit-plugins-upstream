## Description:

Generates Daniel Jackson concept models with purposes, operational principles, state, actions, and synchronizations only when explicitly invoked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and requirements reviewers use this skill to convert requirements, interviews, or existing models into concept models with boundary critiques, synchronizations, dependency views, MVP subsets, and unresolved tradeoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can shape the agent's response format and modeling frame when explicitly invoked.

Mitigation: Use it only for concept-design modeling tasks and review generated models before relying on them for product or implementation decisions.

Risk: Generated concept models may leave product tradeoffs or external dependencies unresolved.

Mitigation: Track unresolved items in the output's decision table and require human review before treating the model as complete.

## Reference(s):

- [Concept Design homepage](https://github.com/ontology-of-everything/SemanticSkills/tree/main/skills/concept-design)
- [criteria.md](references/criteria.md)
- [sync-notation.md](references/sync-notation.md)
- [example-reserving.md](references/example-reserving.md)
- [sources.md](references/sources.md)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [WYSIWID paper](https://arxiv.org/abs/2508.14511)
- [Concept criteria tutorial](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Sync composition tutorial](https://essenceofsoftware.com/tutorials/concept-basics/sync/)
- [Dependency tutorial](https://essenceofsoftware.com/tutorials/concept-basics/dependency/)
- [Concept design distillation](https://essenceofsoftware.com/posts/distillation/)
- [Design moves](https://essenceofsoftware.com/posts/design-moves/)
- [6.1040 concept rubric](https://61040-fa25.github.io/resources/concept-rubric)
- [Making Software Meaningful](https://arxiv.org/abs/2606.11051)
- [Verified LLM-Driven Synthesis for Concept Design](https://arxiv.org/abs/2607.15718)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured text blocks and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explicit invocation only; outputs are modeling guidance and specifications, not executable code.]

## Skill Version(s):

0.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
