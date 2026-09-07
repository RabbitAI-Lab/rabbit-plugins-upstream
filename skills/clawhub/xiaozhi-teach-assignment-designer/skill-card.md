## Description:

把“全班同一份作业”变成分层、可批改、时长可控的任务卡。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to turn lesson topics and class learning context into differentiated homework task cards, grading rubrics, feedback templates, and teacher-confirmed completion summaries. It supports elementary middle grades, elementary upper grades, and middle school settings.

### Deployment Geography for Use:

China Mainland by default; use in other regions requires localized emergency resources, curriculum alignment, and minor-data consent review.

## Known Risks and Mitigations:

Risk: Generated homework items may contain incorrect wording, invalid assumptions, or unverified answers.

Mitigation: Use the bundled AI item self-check, mark AI-generated items for teacher review, and require teacher verification before adding items to formal homework or a resource bank.

Risk: Student aliases, tiering data, review plans, exam blueprints, and parent-facing summaries can expose sensitive education data if platform controls are weak.

Mitigation: Confirm the platform enforces the stated read/write boundaries, parent-sharing consent, emotion-sharing consent, anonymization, and aggregation rules before use.

Risk: Crisis or student-safety signals could be mishandled, especially outside the default China Mainland deployment context.

Mitigation: Stop the homework workflow when crisis signals appear, follow the crisis referral protocol, ask for region when uncertain, and localize emergency resources before deployment outside China Mainland.

Risk: Differentiated homework could overload or stigmatize students if tiers are exposed or task volume is increased without review.

Mitigation: Keep assignments concise, include estimated time for each task, keep tier task durations comparable, and label student-facing versions as task cards rather than tier labels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-assignment-designer)
- [作业评分标准与分层任务卡模板](references/assignment-rubric.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI item self-check protocol](shared/ai-item-check.md)
- [Platform capability and localization conventions](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown task cards, grading rubrics, feedback templates, and structured homework-assignment fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes estimated minutes per task, estimated total minutes, tier-aware assignment variants, and teacher-confirmed writeback guidance.]

## Skill Version(s):

2.1.12 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
