## Description:

把独立教师分散在课表、学员卡、作业、家长沟通和课时包里的信息，只读聚合成一张可执行的日工作台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to turn lesson schedules, student cards, homework follow-ups, parent communication records, course packages, and progress evidence into a daily 7-section work dashboard with prioritized next actions. It is a read-only aggregation and triage skill that points the teacher to other skills for scheduling, lesson logs, homework tracking, parent communication, and renewal reports.

### Deployment Geography for Use:

Global; localize safety, consent, and legal assumptions before using outside mainland Chinese K12 settings.

## Known Risks and Mitigations:

Risk: The dashboard summarizes sensitive student workspace records.

Mitigation: Install only where the teacher is authorized to view the workspace, keep exports as sensitive records, and use aliases instead of real student names.

Risk: Parent-facing sharing may expose student information or exceed consent.

Mitigation: Verify parent communication consent before sharing and require teacher review before any external message or record is used.

Risk: Safety and legal assumptions may not fit every region.

Mitigation: Localize crisis, consent, privacy, and education-law assumptions before use outside mainland Chinese K12 settings.

Risk: Risk flags could be treated as subjective judgments or automated decisions.

Mitigation: Base risk flags on documented field values and numeric thresholds, mark subjective teacher input explicitly, and route write actions to the responsible skill for teacher confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [7 区块日工作台输出模板](artifact/references/daily-dashboard-block-templates.md)
- [独立教师日工作台模板](artifact/references/dashboard-template.md)
- [完整日工作台输出示例](artifact/references/daily-dashboard-full-sample.md)
- [SoloTeacherWorkspace schema](artifact/shared/solo-teacher-workspace.schema.json)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown daily dashboard with tables, prioritized task lists, risk flags, and routing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; uses aliases instead of student real names; risk flags must cite source fields and numeric thresholds.]

## Skill Version(s):

2.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
