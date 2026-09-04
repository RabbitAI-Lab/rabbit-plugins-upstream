## Description:

Designs Chinese-language differentiated homework task cards with estimated time, grading rubrics, feedback templates, and completion summaries for classroom teachers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to turn one-size-fits-all homework requests into differentiated A/B/C task cards, grading criteria, and brief feedback templates. It is intended for Chinese-language classroom workflows where teachers remain responsible for validating generated questions and using student data appropriately.

### Deployment Geography for Use:

Global, with localization required for crisis-response phone numbers and jurisdiction-specific student-data practices.

## Known Risks and Mitigations:

Risk: Locale-specific crisis-response phone numbers and wording may be inappropriate outside mainland China.

Mitigation: Adapt crisis-response contacts and jurisdiction-specific wording before deployment in another locale.

Risk: Student data, parent feedback, or emotional-context fields could be shared beyond the intended audience.

Mitigation: Review student-data sharing settings and enforce parentSharingConsent and emotionSharingWithParent controls before generating parent-facing feedback.

Risk: AI-generated assignment items can be incorrect, misleveled, or unsuitable for formal homework.

Mitigation: Use the included AI item self-check, label AI-generated items, and require teacher verification before adding items to formal assignments.

Risk: The skill provides grading rubrics but does not perform authoritative automatic grading.

Mitigation: Keep teachers responsible for scoring decisions or use a dedicated grading engine where automated grading is required.

## Reference(s):

- [作业评分标准与分层任务卡模板](references/assignment-rubric.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)
- [Class Teaching Workspace Schema](shared/class-teaching-workspace.schema.json)
- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-assignment-designer)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese-language Markdown or structured task-card text with grading rubric sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include estimated minutes, difficulty bands, A/B/C task-card variants, grading criteria, feedback templates, and completion-summary fields.]

## Skill Version(s):

2.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
