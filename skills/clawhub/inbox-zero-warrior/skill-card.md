## Description:

Triage, categorize, and conquer email overload. Classifies emails by urgency, generates quick replies, detects newsletters for bulk unsubscribe, and produces daily digests. Use when facing an overflowing inbox or wanting to maintain inbox zero.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Knowledge workers, freelancers, consultants, and small business owners use this skill to analyze exported inbox data, prioritize urgent messages, identify newsletters, draft quick replies, and produce action lists or digests for inbox cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email exports may contain private messages, financial details, or account-related content.

Mitigation: Use only exports the user is comfortable processing locally and avoid sharing generated reports beyond the intended review context.

Risk: Suggested unsubscribe, delete, archive, filter, or reply actions may be incorrect or too broad.

Mitigation: Review recommendations in the mail client before acting on them.

Risk: Generated quick replies may not fully match the user's intent or relationship with the sender.

Mitigation: Edit suggested replies before sending and confirm any dates, deadlines, or commitments.

## Reference(s):

- [Email Triage Classification Reference](references/triage_rules.md)
- [Server-resolved GitHub provenance](https://github.com/voronindenis5/inbox-zero-warrior)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/inbox-zero-warrior)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text reports with JSON outputs and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes user-provided email exports locally and produces suggested actions; it does not send email or automatically modify mailboxes.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
