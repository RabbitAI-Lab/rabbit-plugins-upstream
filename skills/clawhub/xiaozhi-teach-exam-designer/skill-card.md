## Description:

测评设计师 helps teachers design exam blueprints, two-way specification tables, question revisions, difficulty balance, scoring rubrics, and post-exam item repair lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to turn ad hoc test assembly into assessment design based on exam purpose, curriculum targets, difficulty bands, cognitive levels, item metadata, scoring criteria, and repair decisions after item statistics are available.

### Deployment Geography for Use:

China mainland by default; localize curriculum assumptions, data-consent handling, and crisis referral channels before use in other regions.

## Known Risks and Mitigations:

Risk: AI-generated or skill-generated questions may contain invalid assumptions, ambiguous answers, or inappropriate difficulty for formal exams.

Mitigation: Run the documented AI item self-check and require teacher verification before any generated question enters a formal exam.

Risk: Workspace permissions that exceed the documented scope could expose or modify more classroom data than the skill needs.

Mitigation: Configure the platform so the skill writes examBlueprints only and reads aggregate teaching data only as documented.

Risk: The skill's curriculum assumptions, data consent defaults, and crisis referral channels are written for a China mainland K12 context.

Mitigation: Localize curriculum mappings, consent handling, and crisis referral channels before deploying outside that context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-exam-designer)
- [试卷蓝图与双向细目表模板](artifact/references/exam-blueprint.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)
- [班级教学工作空间 Schema](artifact/shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown templates, structured tables, scoring rubrics, and workspace-field guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces exam blueprints, item metadata, scoring standards, and repair lists; it does not automatically grade exams.]

## Skill Version(s):

2.1.12 (source: SKILL.md frontmatter and evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
