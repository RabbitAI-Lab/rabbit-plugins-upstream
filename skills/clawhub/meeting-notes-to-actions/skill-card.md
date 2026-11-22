## Description:

Turns raw US meeting notes into a decision log and an owned action list with due dates, left as a draft for the organizer to send. Use when the user asks for meeting notes to actions, action item list template, meeting notes summarizer. For US project managers, chief of staff and team leads running recurring internal meetings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rapidworker1](https://clawhub.ai/user/rapidworker1)

### License/Terms of Use:

MIT-0

## Use Case:

US project managers, chiefs of staff, and team leads can turn recurring meeting notes into a dated decision log, role-owned actions with due dates, open questions, and a follow-up draft for the organizer to review and send.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The security evidence reports file-writing capability with a missing declared tool scope, and scanner coverage is incomplete.

Mitigation: Review the intended output paths and the host’s file-write permissions before installing; inspect the skill and its references because coverage is incomplete.

Risk: Meeting notes may contain personal, medical, or compensation details that should not appear in shared action documents.

Mitigation: Remove home addresses, personal phone numbers, medical details, and pay figures before processing, as directed by the skill’s guardrails.

## Reference(s):

- [Meeting record rules](references/meeting-record-rules.md)
- [ClawHub release page](https://clawhub.ai/rapidworker1/skills/meeting-notes-to-actions)
- [Publisher homepage](https://github.com/rapidworker1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown decision log, action-item rows, open items, and follow-up draft]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Leaves follow-up as a draft for organizer review; does not send or distribute it.]

## Skill Version(s):

1.0.7 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
