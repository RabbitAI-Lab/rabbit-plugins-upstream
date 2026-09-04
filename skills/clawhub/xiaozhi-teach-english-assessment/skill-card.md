## Description:

英语综合测评 helps Chinese K12 English teachers design four-skill assessments, build CSE-first learner profiles, and produce teaching intervention suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers in Chinese K12 English settings use this skill to turn a single exam into a listening, speaking, reading, and writing assessment with CSE-based ability profiles. It supports post-assessment intervention planning and teacher-confirmed record writeback.

### Deployment Geography for Use:

Mainland China for default use; localize standards, language, and crisis resources before use in other regions or non-Chinese settings.

## Known Risks and Mitigations:

Risk: Assessment records may contain student performance information.

Mitigation: Keep consent controls, teacher confirmation, export, correction, deletion, and no-writeback options enabled for assessment records.

Risk: Use outside mainland China or non-Chinese settings may misalign standards, language, or crisis resources.

Mitigation: Localize the assessment standards, language, and crisis referral resources before deployment in those contexts.

Risk: Generated assessment items or level suggestions could be mistaken for verified scores or official proficiency levels.

Mitigation: Require teacher review for AI-generated items and use CSE descriptor-based human judgment rather than direct score-to-level conversion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-assessment)
- [Assessment template](artifact/references/assessment-template.md)
- [Four-skill rubric](artifact/references/four-skill-rubric.md)
- [Student ability profile template](artifact/references/student-ability-profile-template.md)
- [CEFR four-skill descriptors](artifact/references/cefr-four-skill-descriptors.md)
- [CEFR can-do statements](artifact/references/cefr-can-do-statements.md)
- [AI item check protocol](artifact/shared/ai-item-check.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured teacher-facing text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use class assessment records and should generate writeback-ready entries only after teacher confirmation.]

## Skill Version(s):

2.1.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
