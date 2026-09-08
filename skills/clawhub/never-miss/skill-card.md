## Description:

Turns schedules and deadlines from chat, screenshots, or email into macOS Calendar events with reminders; supports multi-account IMAP scanning, cross-account deduplication, and .ics invitation parsing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create, query, and maintain reminders from conversational input, screenshots, and configured mail accounts. It can run scheduled scans that read new IMAP messages, create Calendar events, and record local run reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read messages from configured IMAP accounts.

Mitigation: Configure only intended mail accounts and use sender allowlists or blocklists for sensitive or noisy mailboxes.

Risk: Scheduled scans can automatically create Calendar events from mail content.

Mitigation: Use conservative account settings, review run reports, and keep ambiguous or low-confidence messages out of automatic creation flows.

Risk: Local reports can contain event details and email-subject metadata.

Mitigation: Store the configured data directory in an appropriate local location and limit access to reports if mailbox subjects or event titles are sensitive.

Risk: Calendar write access and IMAP credentials are required for full operation.

Mitigation: Use client-specific mail passwords stored in macOS Keychain and run the built-in doctor checks before relying on scheduled scans.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/neuhanli/skills/never-miss)
- [Extraction rules](references/extraction-rules.md)
- [Automatic scan runbook](references/runbook-auto.md)
- [Mail setup guide](references/mail-setup.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON command inputs and outputs, shell commands, local configuration files, Calendar events, .ics files, and run reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates local config.yaml, state.json, journal entries, runs/*.md reports, and fallback ics/*.ics files under the configured data directory.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
