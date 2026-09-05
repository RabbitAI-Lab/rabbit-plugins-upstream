## Description:

Helps teachers design assessments from a two-way specification table, including exam blueprints, item selection or adaptation, difficulty balance, scoring rubrics, and post-exam item revision lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External teachers use this skill to design unit tests, exam blueprints, two-way specification tables, scoring standards, and item revision lists. It is intended for teacher-facing assessment planning, not automatic grading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-generated assessment items may be incorrect, ambiguous, or misaligned with the intended standard.

Mitigation: Require teachers to solve and verify each AI-generated item before using it in a formal test.

Risk: Persistent class-workspace records could contain sensitive student or classroom information.

Mitigation: Keep the skill's data controls enabled and avoid storing real student names in exam blueprints, item text, scoring standards, or saved records.

Risk: Assessment design may accidentally copy restricted guidebook or past-exam content.

Mitigation: Record copyright status for each item and store only indexes for guidebook originals or past-exam questions.

Risk: Users may over-rely on the skill for grading or post-exam statistics.

Mitigation: Use the skill for scoring rubrics and item revision guidance only; post-exam statistics are handled by the linked student analysis workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-exam-designer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [试卷蓝图与双向细目表模板](references/exam-blueprint.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown with structured assessment records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exam blueprints, two-way specification tables, item metadata, scoring rubrics, and revision or review lists; AI-generated items require teacher verification before formal use.]

## Skill Version(s):

2.1.6 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
