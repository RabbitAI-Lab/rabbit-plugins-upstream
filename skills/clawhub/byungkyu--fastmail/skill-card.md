## Description:

Fastmail JMAP API integration with managed authentication for reading, searching, organizing, and sending email, and managing mailboxes, threads, drafts, identities, contacts, and masked email addresses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent work with a connected Fastmail account through Maton for email, mailbox, draft, contact, and masked alias workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read private email and contacts.

Mitigation: Use it only for intended Fastmail account tasks, request only needed data, and avoid exposing message bodies, recipient addresses, or contact details unless the user explicitly asks.

Risk: The skill can send email, delete mail, create connections, and change masked aliases.

Mitigation: Require explicit user confirmation for every write, send, delete, masked alias change, or new connection, including the target resource and intended effect.

Risk: Long-lived API keys increase credential exposure if printed, logged, or persisted.

Mitigation: Prefer OAuth through the Maton CLI and never print, log, persist, or pass credentials on a command line.

## Reference(s):

- [Fastmail Skill Page](https://clawhub.ai/byungkyu/skills/fastmail)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [Fastmail Developer Documentation](https://www.fastmail.com/dev/)
- [JMAP Specifications and Guides](https://jmap.io/)
- [JMAP Core Specification (RFC 8620)](https://www.rfc-editor.org/rfc/rfc8620.html)
- [JMAP Mail Specification (RFC 8621)](https://www.rfc-editor.org/rfc/rfc8621.html)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request bodies, CLI commands, and user-confirmation prompts for sensitive actions.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
