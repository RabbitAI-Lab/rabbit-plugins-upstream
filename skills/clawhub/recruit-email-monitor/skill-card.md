## Description:

Monitors configured recruitment mailboxes, has an agent classify candidate emails, records results in an Excel workbook, and sends Feishu notifications and daily briefings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haoxianniu528-bit](https://clawhub.ai/user/haoxianniu528-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to automate recruitment email triage across configured mailboxes, maintain a local application-tracking workbook, and receive Feishu reminders or daily summaries for pending items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to configured mailboxes and may process recruitment-email metadata, previews, links, and deadlines.

Mitigation: Use app-specific mailbox authorization codes, keep local config files private, and install only for mailboxes whose recruitment data may be processed by this workflow.

Risk: Notifications and daily briefings can send recruitment information to a Feishu recipient or configured agent workflow.

Mitigation: Verify the Feishu recipient before enabling delivery and disable or adjust full-briefing delivery if the privacy posture is too broad.

Risk: The skill writes local Excel and briefing files at configured paths, which may expose sensitive job-search information on shared systems.

Mitigation: Review the configured workbook and briefing paths, restrict filesystem access, and move outputs to a private location when needed.

Risk: Automatic stale-message archival may hide older pending recruitment emails from daily briefings.

Mitigation: Review the archival threshold and disable or adjust it if older pending items must remain visible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haoxianniu528-bit/skills/recruit-email-monitor)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with shell commands and JSON records; generated artifacts include an Excel workbook and text briefing.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local recruitment email summaries, processed-mail state, agent judgment JSON, and Feishu notification content when configured.]

## Skill Version(s):

1.3.0 (source: server release metadata and artifact _meta.json; release notes dated 2026-08-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
