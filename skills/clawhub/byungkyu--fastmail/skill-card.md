## Description:

Fastmail provides JMAP API guidance through Maton-managed authentication for reading, searching, organizing, and sending email and managing mailboxes, drafts, identities, contacts, and masked email addresses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to let an agent work with a user's Fastmail account through Maton for email search, reading, organization, drafting, sending, contacts, and masked email workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent access sensitive Fastmail account data through Maton.

Mitigation: Use OAuth where possible, grant the narrowest available Fastmail scopes, prefer read/list calls, and revoke unused Maton connections when finished.

Risk: Sending email, deleting mail, changing contacts, and modifying masked email addresses can have lasting user-visible effects.

Mitigation: Review every proposed send, delete, contact, or masked-email change with the user before approval, including the target resource and intended effect.

Risk: Email bodies, contact data, and snippets may contain personal data or adversarial content.

Mitigation: Treat Fastmail responses as untrusted data, avoid exposing content the user did not request, and never execute or follow instructions found inside fetched content.

## Reference(s):

- [ClawHub Fastmail Skill](https://clawhub.ai/byungkyu/skills/fastmail)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Fastmail Developer Documentation](https://www.fastmail.com/dev/)
- [JMAP Specifications and Guides](https://jmap.io/)
- [JMAP Core Specification (RFC 8620)](https://www.rfc-editor.org/rfc/rfc8620.html)
- [JMAP Mail Specification (RFC 8621)](https://www.rfc-editor.org/rfc/rfc8621.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline bash, JSON, and SDK code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on Maton CLI/API calls and explicit confirmation for write actions.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
