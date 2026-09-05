## Description:

家长沟通助手 helps independent K12 teachers draft low-anxiety parent messages, check communication consent, and record limited channel/status logs without sending messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent K12 teachers use this skill to draft parent updates for lesson feedback, progress changes, renewal conversations, family questions, and group announcements while keeping messages factual, low-anxiety, and actionable.

### Deployment Geography for Use:

Mainland China by default; localize curriculum, consent, and emergency-resource guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Parent messages may include student information without the required communication or emotion-sharing consent.

Mitigation: Verify consent fields before drafting and remove emotional or classroom-state details when emotion sharing is not authorized.

Risk: Operators outside the intended Mainland China Chinese K12 workflow may use unsuitable curriculum, consent, or emergency-resource assumptions.

Mitigation: Localize curriculum context, consent handling, and crisis-resource guidance before use in another region or workflow.

Risk: Drafted messages could be mistaken for sent communications or used to store sensitive contact details.

Mitigation: Keep the skill in draft-only use and limit records to communication time, channel enum, scenario, factual summary, action suggestion, and sent status.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-parent-communication)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [典型场景话术模板](references/typical-scenario-scripts.md)
- [家长群公告模板（每周固定）](references/weekly-group-announcement-template.md)
- [沟通三原则正误对照范例](references/communication-principles-examples.md)
- [全库统一词表（单一事实源）](shared/vocab.md)
- [危机例外（共享片段）](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Chinese text or Markdown drafts with optional structured communication-log entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Only drafts messages; does not send messages or store contact details.]

## Skill Version(s):

2.1.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
