## Description:

独立教师工作台只读聚合课表、学员卡、作业、家长沟通和课时包信息，生成一张包含七个区块、风险学员标记和今日三件事的教师日工作台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External teachers use this skill to turn existing solo-teacher workspace records into a daily operating dashboard. It helps prioritize lessons, homework follow-up, parent communication, course-package status, risk signals, and the three most important actions for the day.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dashboard can surface sensitive student, homework, parent-communication, and course-package information.

Mitigation: Use the skill only with an existing teacher workspace that has appropriate consent and access controls; the artifact requires aliases, consent checks, and omission of high-sensitivity details.

Risk: Non-mainland-China deployments may need different crisis or safety contact channels.

Mitigation: Localize emergency and support-channel guidance before use outside mainland China; the artifact instructs the agent to ask for location when uncertain.

Risk: Risk labels or renewal prompts could be misleading if they are based on impressions rather than workspace fields.

Mitigation: Keep risk signals tied to explicit field values and dates, mark subjective teacher input as subjective, and route any record-changing action to the appropriate write-capable skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [dashboard-template.md](references/dashboard-template.md)
- [daily-dashboard-block-templates.md](references/daily-dashboard-block-templates.md)
- [daily-dashboard-full-sample.md](references/daily-dashboard-full-sample.md)
- [solo-teacher-workspace.schema.json](shared/solo-teacher-workspace.schema.json)
- [crisis-exception.md](shared/crisis-exception.md)
- [crisis-referral-protocol.md](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown dashboard with structured text sections and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only aggregation; uses aliases and field-backed risk rationales; routes write actions to other teacher skills.]

## Skill Version(s):

2.3.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
