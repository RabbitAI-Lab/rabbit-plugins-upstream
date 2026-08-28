## Description:

Retrieves email from configured IMAP mailboxes for a requested time range and produces a structured Chinese summary of important messages, sent mail, communication statistics, follow-ups, and attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jams-hub](https://clawhub.ai/user/jams-hub)

### License/Terms of Use:

MIT-0

## Use Case:

Employees or external users with configured mailboxes use this skill to answer mailbox-summary requests for a specific date range. The agent can retrieve messages, summarize key inbound and sent mail, highlight follow-up items, and list attachments without exposing raw account configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads mailbox credentials from accounts.json and uses them to access configured mailboxes.

Mitigation: Protect accounts.json like a password file, keep it out of sync and source-control workflows, and configure only accounts that are appropriate for mailbox-summary use.

Risk: The skill retrieves sensitive message bodies and metadata from configured mailboxes.

Mitigation: Install only when mailbox read access is acceptable, and use the skill only for explicit mailbox-summary requests.

Risk: The documented trigger scope is broad for requests involving email-related keywords.

Mitigation: Tighten trigger handling operationally so the skill runs only when the user clearly requests mailbox retrieval or summarization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jams-hub/skills/email-query-summary)
- [ClawHub publisher profile](https://clawhub.ai/user/jams-hub)
- [Setup guide](artifact/SETUP.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Simplified Chinese Markdown summary, with setup guidance when mailbox configuration is missing.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries should omit credentials, raw message JSON, and execution details; attachment details are included only when messages contain attachments.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
