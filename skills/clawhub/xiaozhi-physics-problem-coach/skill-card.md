## Description:

A Chinese-language physics tutor that guides middle-school and first-year high-school students through one problem using diagrams, modeling, calculations, and reflection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use this tutor to work through a specific physics problem step by step rather than receive an immediate answer. Optional learning-profile lookup, wrong-answer handoff, and review reminders require separate consent.

### Deployment Geography for Use:

Mainland China (designed for the Chinese K–12 curriculum; other regions require localization of emergency contacts, curriculum, and minor-consent rules)

## Known Risks and Mitigations:

Risk: Inconsistent optional profile-memory rules could expose a student's learning profile without the intended consent.

Mitigation: Keep the skill session-only unless the platform checks profileEnabled=true, memoryPaused=false, crossSkillSharing=true, current-session consent, and any required guardian consent before profile access.

Risk: Optional wrong-answer records or reminders could retain student learning information unexpectedly.

Mitigation: Require separate, explicit confirmation for each wrong-answer handoff and reminder; do not treat silence as consent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach)
- [Four-step physics problem-solving workflow](artifact/references/physics-4step-statemachine.md)
- [Physics diagram guide](artifact/references/physics-diagram-guide.md)
- [Socratic questioning guide](artifact/references/physics-socrates-guide.md)
- [First-year high-school worked examples](artifact/references/physics-hs1-worked-examples.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Chinese-language conversational text, optionally formatted as Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Problem diagrams may be explained in text; optional record or reminder handoffs follow explicit confirmation.]

## Skill Version(s):

2.4.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
