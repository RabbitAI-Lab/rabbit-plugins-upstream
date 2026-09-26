## Description:

帮助独立教师以诊断式试听了解新学员需求，并在确认监护人同意后建立最小化学员档案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking independent teachers use this skill to plan and record trial lessons, assess learning needs, and create pseudonymous student profiles with guardian consent. It stops at intake and does not manage scheduling or ongoing lessons.

### Deployment Geography for Use:

Global (Chinese-language workflow)

## Known Risks and Mitigations:

Risk: Student intake records may contain information about minors without appropriate consent.

Mitigation: Confirm guardian consent before creating a profile; do not record information if consent is unconfirmed.

Risk: Retaining identifiable or outdated student information could expose student privacy.

Mitigation: Use pseudonyms, keep names and contact details outside the workspace, and review retention and deletion prompts with the teacher.

## Reference(s):

- [Student basic information form](artifact/references/student-basic-info-form.md)
- [Trial lesson structure](artifact/references/trial-lesson-5-segment-structure.md)
- [Formal student profile template](artifact/references/formal-student-profile-template.md)
- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language Markdown guidance and structured intake or student-profile records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pseudonymous records; no contact details]

## Skill Version(s):

2.6.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
