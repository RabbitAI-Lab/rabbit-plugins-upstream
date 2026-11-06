## Description:

把一周的学习记录整理成有结论、有证据、有下一步的周报，并引导学生进行自我复盘。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

学生使用此技能回顾一周的学习内容、进步证据和下一步重点；家长或教师可在学生授权时使用家庭分享版支持复盘。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting guidance about sharing a student's learning history creates a privacy concern.

Mitigation: Reconcile the monthly-summary template with permitted handoff routes before enabling access to student history; keep cross-skill and family sharing disabled until needed and explicitly authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Review report templates](artifact/references/review-report-template.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)
- [Crisis exception guidance](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, JSON]

**Output Format:** [Chinese conversational prompts and weekly review reports, with structured handoff objects when authorized.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Weekly scope; report structure varies by school grade and available learning records. Family sharing and record handoffs require student consent as described in the skill.]

## Skill Version(s):

2.12.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
