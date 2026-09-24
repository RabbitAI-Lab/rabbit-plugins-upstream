## Description:

课后记录助手 helps independent teachers turn post-lesson observations into structured lesson records, mastery notes, pending course-hour confirmations, next-lesson handoff points, and optional internal parent-summary drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill after a class to capture what was taught, observed mastery, student reaction, progress, adjustments, and a next-lesson focus. It also prepares teacher-confirmed course-hour ledger entries and optional internal parent-summary drafts without sending messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive student lesson records and course-hour information.

Mitigation: Install it only in the intended teacher workspace and verify alias use, consent fields, retention settings, and teacher confirmation steps before use.

Risk: Parent-facing summaries could reveal student observations without proper authorization.

Mitigation: Generate parent summaries only as internal drafts after checking parent communication and emotion-sharing consent; the teacher decides whether and how to send anything.

Risk: Course-hour changes can affect billing or package balances.

Mitigation: Use pending confirmation entries and require explicit teacher confirmation before changing used or remaining course-hour totals.

Risk: Crisis or safety signals may appear in lesson-related conversations.

Mitigation: Stop the lesson-log flow for crisis signals, avoid diagnostic labels, refer the user to trusted adults and local emergency channels, and localize crisis wording outside mainland China.

Risk: AI-generated validation questions or examples may be incorrect.

Mitigation: Apply the bundled AI item self-check protocol and mark generated teacher-side items for human verification before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-log)
- [Lesson log template](references/lesson-log-template.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [Vocabulary and mastery scales](shared/vocab.md)
- [AI item check protocol](shared/ai-item-check.md)
- [Crisis exception protocol](shared/crisis-exception.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and text responses with structured workspace fields, preview drafts, and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records and course-hour entries are previewed for teacher confirmation before writing; parent summaries remain internal drafts.]

## Skill Version(s):

2.3.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
