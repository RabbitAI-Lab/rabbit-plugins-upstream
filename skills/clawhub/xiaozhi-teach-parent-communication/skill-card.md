## Description:

Drafts clear, low-anxiety Chinese-language messages for independent teachers to communicate with parents about learning progress, concerns, and course renewal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent K–12 teachers use this skill to draft parent-facing updates, replies, and group announcements grounded in teaching records. Teachers review and send messages themselves; the skill may record the communication channel and send status.

### Deployment Geography for Use:

Mainland China (Chinese-language K–12 workflows); localize emergency contacts, academic standards, and data defaults before use elsewhere.

## Known Risks and Mitigations:

Risk: A parent-facing draft or group announcement could disclose a student's private information.

Mitigation: Check parent-communication consent before drafting, require separate consent for emotional observations, and keep individual feedback in private messages without names, contact details, or family information.

Risk: A draft could be mistaken for a message already reviewed or sent by the teacher.

Mitigation: Have the teacher review and send every message; mark a communication as sent only after the teacher confirms it.

Risk: Mainland-China emergency contacts and educational or data assumptions may be unsuitable elsewhere.

Mitigation: Use the skill for Chinese-language mainland-China K–12 workflows unless local emergency contacts, academic standards, and legal/data defaults are adapted for the deployment region.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-parent-communication)
- [Communication principles and examples](artifact/references/communication-principles-examples.md)
- [Typical parent-communication scripts](artifact/references/typical-scenario-scripts.md)
- [Weekly group-announcement template](artifact/references/weekly-group-announcement-template.md)
- [Crisis exception and regional guidance](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language message drafts and brief guidance; structured communication-log entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts only; the teacher reviews and sends messages. Logs record communication channel and send status, not contact details.]

## Skill Version(s):

2.10.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
