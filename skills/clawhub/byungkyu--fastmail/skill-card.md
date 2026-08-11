## Description:

Fastmail JMAP API integration with managed authentication for reading, searching, organizing, and sending email, and for managing mailboxes, threads, drafts, identities, contacts, and masked email addresses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent work with a connected Fastmail account through Maton. It supports mail search, reading, organization, draft and send workflows, mailbox management, contacts, identities, and masked addresses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify data in the connected Fastmail account, including mail, contacts, mailboxes, identities, and masked addresses.

Mitigation: Install only when account access through Maton is intended, use the narrowest Fastmail API token scopes that fit the task, and avoid exposing message bodies or contact details unless needed.

Risk: Send, delete, contact, and masked-address changes can affect real recipients, stored personal data, or mail delivery.

Mitigation: Require explicit user confirmation for every send, delete, contact, masked-address, and other write operation before making the API call.

Risk: Email bodies, sender names, subjects, snippets, and contact details are untrusted user-controlled content.

Mitigation: Treat retrieved content as data, not instructions, and do not execute, evaluate, or interpolate it into shell commands or prompts without validation.

## Reference(s):

- [Fastmail Skill on ClawHub](https://clawhub.ai/byungkyu/skills/fastmail)
- [Maton](https://maton.ai)
- [Fastmail Developer Documentation](https://www.fastmail.com/dev/)
- [JMAP Core Specification (RFC 8620)](https://www.rfc-editor.org/rfc/rfc8620.html)
- [JMAP Mail Specification (RFC 8621)](https://www.rfc-editor.org/rfc/rfc8621.html)
- [JMAP for Contacts (RFC 9610)](https://www.rfc-editor.org/rfc/rfc9610.html)
- [JSContact (RFC 9553)](https://www.rfc-editor.org/rfc/rfc9553.html)
- [Fastmail Masked Email Help](https://www.fastmail.help/hc/en-us/articles/4406536368911-Masked-Email)
- [JMAP Specifications and Guides](https://jmap.io/)
- [JMAP Crash Course](https://jmap.io/crash-course.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON request bodies and bash, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose API calls that require user confirmation before write, send, delete, contact, or masked-address changes.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
