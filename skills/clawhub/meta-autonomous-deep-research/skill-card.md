## Description:

A distilled autonomous deep-research meta-skill that guides agents through question decomposition, retrieval, synthesis, self-verification, reflection, orchestration, and learner-backed improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill to structure autonomous deep-research tasks, synthesize evidence-backed answers, and add self-checking and reflection loops. It is intended for workflows where persistent local learner notes and local RAG or web access are acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research tasks may leave cross-session learner notes that are not tightly scoped or user-controlled.

Mitigation: Use the skill only where skill-owned memory is acceptable, and avoid sending sensitive data to learner notes unless retention and redaction controls are added.

Risk: The skill combines broad autonomous research guidance with local RAG or web access.

Mitigation: Review the skill before installation and deploy it only in environments where local RAG and web access are acceptable.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/qq435912743/skills/meta-autonomous-deep-research)
- [Distillation report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with optional JSON learner updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update skill-owned learner notes when the learner script records outcomes.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
