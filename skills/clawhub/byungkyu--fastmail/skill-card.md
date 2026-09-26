## Description:

Fastmail JMAP API integration with managed authentication for reading, searching, organizing, sending, and managing mail, mailboxes, threads, drafts, identities, contacts, and masked email addresses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Fastmail account through Maton, including mailbox search, message review, drafting, sending, contact management, and masked email management. It is also used to prepare approved Fastmail automations through Maton functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify real Fastmail data, including sensitive email and contact content.

Mitigation: Use OAuth where possible, grant only the scopes needed for the task, and limit reads and output to the specific content the user requested.

Risk: Sending email and permanent deletion can create irreversible side effects.

Mitigation: Confirm every write, send, delete, connection change, or automation with the user, including the exact target resource and intended effect.

Risk: Third-party trigger destinations can forward event data outside the trusted account context.

Mitigation: Avoid third-party destinations unless the user explicitly trusts the destination host and understands what data will be forwarded.

Risk: Local event handlers can execute code on untrusted trigger payloads.

Mitigation: Use user-authored or user-reviewed handlers only, treat payloads as data, and avoid interpolating external content into shell commands or executable code.

## Reference(s):

- [ClawHub Fastmail Skill](https://clawhub.ai/byungkyu/skills/fastmail)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Fastmail Developer Documentation](https://www.fastmail.com/dev/)
- [JMAP Specifications and Guides](https://jmap.io/)
- [JMAP Core Specification (RFC 8620)](https://www.rfc-editor.org/rfc/rfc8620.html)
- [JMAP Mail Specification (RFC 8621)](https://www.rfc-editor.org/rfc/rfc8621.html)
- [JMAP for Contacts (RFC 9610)](https://www.rfc-editor.org/rfc/rfc9610.html)
- [Masked Email](https://www.fastmail.com/dev/maskedemail)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Fastmail connection authorized for the requested task.]

## Skill Version(s):

1.2.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
