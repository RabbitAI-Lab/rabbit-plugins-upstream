## Description:

Fastmail JMAP API integration with managed authentication for reading, searching, organizing, and sending email, and for managing mailboxes, threads, drafts, identities, contacts, and masked email addresses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a Fastmail account through JMAP with Maton-managed authentication. It supports read/list workflows by default and can guide approved write actions such as sending mail, changing mailboxes, managing contacts, and creating or disabling masked aliases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change Fastmail email data, contacts, mailboxes, identities, and masked aliases through Maton-mediated account access.

Mitigation: Install only when Maton-mediated Fastmail access is acceptable, prefer OAuth through the Maton CLI, grant the narrowest scopes available, and review every email send, delete, contact change, mailbox change, or masked-alias change before approving it.

Risk: Using a raw MATON_API_KEY fallback can expose a long-lived credential to child processes or logs.

Mitigation: Use OAuth through the Maton CLI where possible, avoid the raw key fallback unless the CLI cannot be used, and never print, persist, or pass credentials on command lines.

Risk: Email bodies, subjects, sender names, snippets, and contact fields are untrusted external data and may contain adversarial instructions.

Mitigation: Treat fetched Fastmail content as data, validate it before reuse, and do not execute, evaluate, or interpolate it into shell commands or follow-up prompts.

Risk: Some Fastmail write operations have irreversible or externally visible effects, including final email delivery and permanent message or mailbox deletion.

Mitigation: Fetch current state before writing, present the exact target and intended effect, and require explicit user approval before any modifying request.

## Reference(s):

- [ClawHub fastmail skill](https://clawhub.ai/byungkyu/skills/fastmail)
- [Maton](https://maton.ai)
- [JMAP](https://jmap.io)
- [JMAP Core Specification (RFC 8620)](https://www.rfc-editor.org/rfc/rfc8620.html)
- [JMAP Mail Specification (RFC 8621)](https://www.rfc-editor.org/rfc/rfc8621.html)
- [JMAP for Contacts (RFC 9610)](https://www.rfc-editor.org/rfc/rfc9610.html)
- [Fastmail Masked Email](https://www.fastmail.help/hc/en-us/articles/4406536368911-Masked-Email)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands and JMAP request bodies for user-approved Fastmail operations.]

## Skill Version(s):

1.2.0 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
