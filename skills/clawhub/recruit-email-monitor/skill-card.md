## Description:

Monitors configured mailboxes for recruitment-related email, uses an agent to classify candidates, records results in Excel, sends Feishu notifications, and generates daily briefings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haoxianniu528-bit](https://clawhub.ai/user/haoxianniu528-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Users who manage recruiting pipelines use this skill to monitor personal or team mailboxes, identify recruiting messages, keep an Excel-based application tracker current, and receive Feishu alerts and daily status briefings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive mailbox contents and can send summaries to external Feishu recipients.

Mitigation: Use a dedicated mailbox authorization code, configure a narrowly scoped Feishu app, confirm the recipient ID, and disable BRIEFING_SEND_API or scheduled jobs until the data flow is reviewed.

Risk: Local configuration stores mailbox credentials and Feishu delivery settings.

Mitigation: Keep scripts/config.json out of version control, use least-privilege credentials where possible, and rotate authorization codes if the configuration is exposed.

Risk: Automation can change tracker state, including automatically archiving pending items after 30 days.

Mitigation: Review the 30-day auto-archive behavior before enabling scheduled execution and periodically audit the Excel tracker for incorrectly completed items.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haoxianniu528-bit/skills/recruit-email-monitor)
- [README.md](README.md)
- [INSTALL.md](INSTALL.md)
- [RELEASE_NOTES.md](RELEASE_NOTES.md)

## Skill Output:

**Output Type(s):** [text, json, files, shell commands, configuration]

**Output Format:** [Markdown and plain text guidance with JSON judgment files, Excel workbook updates, Feishu messages, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local mailbox and Feishu configuration; generated briefings and tracker files may contain sensitive recruiting email content.]

## Skill Version(s):

1.3.0 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
