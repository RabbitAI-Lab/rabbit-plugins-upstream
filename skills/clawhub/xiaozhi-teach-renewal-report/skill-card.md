## Description:

用学员真实的学习记录汇总课后记录、作业错因和进步证据，生成事实、进步、计划三段式阶段报告与续课建议话术。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to prepare evidence-based learning progress reports and renewal conversation drafts for a named student. It supports mid-course, renewal, term-end, milestone, and parent-question scenarios while keeping parent-visible output authorization-gated.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill reads minors' longitudinal learning records and may write new progress evidence.

Mitigation: Confirm profileEnabled consent, valid grantor requirements, and active student status before any longitudinal read or progressEvidence write.

Risk: Parent-visible reports or renewal scripts could disclose learning or classroom state without proper authorization.

Mitigation: Require parentCommunicationAllowed before any parent-visible output and emotionSharingWithParent before including classroom-state or emotion-related content.

Risk: Renewal reports could overstate progress or create misleading pressure if unsupported data is used.

Mitigation: Use only records tied to the named student, require every number or claim to be traceable to workspace evidence, and keep sending decisions manual with the teacher.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-renewal-report)
- [Stage Report Templates](references/stage-report-templates.md)
- [Renewal Communication Scripts](references/renewal-communication-scripts.md)
- [Platform Conventions](shared/platform-conventions.md)
- [Solo Teacher Workspace Schema](shared/solo-teacher-workspace.schema.json)
- [Vocabulary](shared/vocab.md)
- [Crisis Referral Protocol](shared/crisis-referral-protocol.md)
- [Crisis Exception](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown reports, text scripts, and structured workspace guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Parent-visible content is authorization-gated; the skill does not send messages, schedule communications, delete records, or change student status.]

## Skill Version(s):

2.1.6 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
