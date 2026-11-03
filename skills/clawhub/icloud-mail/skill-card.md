## Description:

Provides authenticated iCloud Mail access and optional approved automations for reading, searching, sending, and managing messages, drafts, threads, and folders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to access and manage their iCloud Mail mailbox through authenticated requests. They can also set up approved functions and triggers to run mailbox actions as part of scheduled or event-driven workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting grants access to the selected mailbox, and sending, deleting, or automating mail can have lasting effects.

Mitigation: Use a separate app-specific password, verify the target mailbox, and review each send, deletion, and ongoing automation before approving it.

Risk: Hosted functions can access every connection in the deploying Maton account.

Mitigation: Prefer a dedicated account with only the intended connection, and keep function network access disabled unless a specifically reviewed function requires it.

Risk: Triggers and event replays can repeatedly forward event data or rerun mailbox actions.

Mitigation: Review the exact trigger, destination URL, and replayed event before approval, and remove unused automation.

Risk: The local bridge, CLI, and hosted service have behavior outside the artifact security review.

Mitigation: Install the bridge only on the intended computer and follow the documented version and security guidance for the CLI and hosted functions.

## Reference(s):

- [iCloud Mail skill release on ClawHub](https://clawhub.ai/maton/skills/icloud-mail)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Apple: app-specific passwords](https://support.apple.com/en-us/102654)
- [Apple: iCloud Mail server settings](https://support.apple.com/en-us/102525)
- [Apple: iCloud Mail sending limits](https://support.apple.com/en-us/102198)
- [RFC 3501: IMAP4rev1](https://www.rfc-editor.org/rfc/rfc3501)
- [RFC 5321: SMTP](https://www.rfc-editor.org/rfc/rfc5321)
- [Time trigger reference](artifact/references/time/triggers.md)
- [Calendly trigger reference](artifact/references/calendly/triggers.md)
- [GitHub trigger reference](artifact/references/github/triggers.md)
- [Google Mail trigger reference](artifact/references/google-mail/triggers.md)
- [HubSpot trigger reference](artifact/references/hubspot/triggers.md)
- [Linear trigger reference](artifact/references/linear/triggers.md)
- [Notion trigger reference](artifact/references/notion/triggers.md)
- [Slack trigger reference](artifact/references/slack/triggers.md)
- [Stripe trigger reference](artifact/references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration]

**Output Format:** [Natural-language guidance with shell commands, API examples, code snippets, and structured mailbox results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include private mailbox content or configuration for user-approved automations, depending on the request.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
