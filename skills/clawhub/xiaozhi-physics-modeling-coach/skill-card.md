## Description:

A Chinese-language middle-school physics coaching skill that guides students through identifying physical phenomena, selecting an appropriate model, and expressing the model mathematically.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, guardians, and education agents use this skill to coach Chinese middle-school students on physics model selection rather than rote formula matching. It supports phenomenon identification, model-choice checks, equation framing, and model-transfer practice while deferring full problem solving, experiment design, and error-log counting to companion skills.

### Deployment Geography for Use:

Mainland China; localize crisis-referral channels, school-context assumptions, and minor-data consent practices before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill can participate in optional learner profile, cross-skill sharing, parent-sharing, and reminder workflows for minors.

Mitigation: Confirm learner and guardian understanding of the long-term profile, sharing controls, parent visibility, and reminders before installation or use.

Risk: Crisis-referral and school-context guidance is designed for a mainland China K12 setting.

Mitigation: Localize emergency resources, school-context assumptions, and minor-data consent rules before deploying in another region.

Risk: Generated practice items or advanced physics explanations could mislead students if they are ill-posed or outside middle-school scope.

Mitigation: Apply the bundled AI item self-check before presenting generated questions and keep high-school-only models to brief boundary notes.

## Reference(s):

- [Physics Modeling Patterns](artifact/references/physics-modeling-patterns.md)
- [Platform Conventions](artifact/shared/platform-conventions.md)
- [AI Item Check Protocol](artifact/shared/ai-item-check.md)
- [Handover Protocol Schema](artifact/shared/handover-protocol.schema.json)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Chinese-language Markdown conversational guidance with JSON-compatible handoff records when profile writeback or reminder queueing is authorized.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses current-session tutoring by default and only relies on persistent memory, OCR, cross-skill sharing, parent sharing, or reminders when the host platform provides those capabilities and the relevant consent is present.]

## Skill Version(s):

2.1.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
