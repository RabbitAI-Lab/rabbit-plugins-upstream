## Description:

A Chinese-language guide for drafting and troubleshooting educational agent skills using a four-layer structure, a five-step workflow, and explicit safety and privacy boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Skill developers and high-school students with programming or prompt-writing experience use it to draft or revise learning-related SKILL.md instructions, define boundaries and memory fields, and diagnose inconsistent behavior. It does not provide subject tutoring or generate exercises.

### Deployment Geography for Use:

Designed for mainland China K–12 authoring; adapt curriculum, child-privacy rules, and emergency contacts before using generated student-facing templates elsewhere.

## Known Risks and Mitigations:

Risk: Student-facing templates assume mainland China curriculum, privacy rules, and crisis contacts.

Mitigation: Localize those assumptions and verify local requirements before deploying templates outside mainland China.

Risk: Real student examples used to test a draft could expose personal information.

Mitigation: Remove names, school details, contact information, and family events; obtain separate consent before retaining examples.

Risk: Generated skill instructions may be incorrect or misleading.

Mitigation: Review and scan each draft skill before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-creator)
- [Skill templates library](references/skill-templates-library.md)
- [Shared vocabulary and thresholds](shared/vocab.md)
- [Platform conventions and regional scope](shared/platform-conventions.md)
- [Crisis response exceptions](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance and draft SKILL.md text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-only authoring aid; does not access student profiles or run platform actions.]

## Skill Version(s):

2.11.1 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
