## Description:

Helps secondary-school math teachers design assessment blueprints, select and attribute questions, and analyze item-level results with teacher-approved record updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Math teachers use this skill to plan junior- and senior-secondary assessments aligned with the Chinese curriculum, prepare question blueprints and attribution, and summarize item difficulty, discrimination, and reliability after testing. It does not grade students or finalize a complete examination.

### Deployment Geography for Use:

China (curriculum focus)

## Known Risks and Mitigations:

Risk: Assessment context can contain sensitive student information.

Mitigation: Review tenant locale and student-data consent settings; use aliases and confirm the task before accessing or saving assessment records.

Risk: Drafted questions or item-level statistics may be incorrect.

Mitigation: Have teachers verify generated questions and calculations before use; require confirmation for each record update.

Risk: Unlicensed or confidential examination questions could be disclosed or reused.

Mitigation: Check attribution and permissions; do not input unreleased unified-exam questions or copy restricted question text.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-exam-designer)
- [Assessment blueprint template](artifact/references/blueprint-template.md)
- [Assessment design process](artifact/references/exam-design-process.md)
- [Item-level analysis rubric](artifact/references/result-analysis-rubric.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, JSON]

**Output Format:** [Markdown blueprints, item statistics and summaries; teacher-confirmed structured records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft questions require teacher verification; record updates require teacher confirmation.]

## Skill Version(s):

2.10.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
