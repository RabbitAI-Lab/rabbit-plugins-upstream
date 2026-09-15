## Description:

Fastmail JMAP API integration with managed authentication for reading, searching, organizing, and sending email, and managing mailboxes, threads, drafts, identities, contacts, and masked email addresses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to work with Fastmail mail, contacts, drafts, submissions, and masked email aliases through authenticated JMAP calls. It is suited for mailbox search and organization, message sending after explicit approval, and user-approved Fastmail automation through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fastmail mail, contacts, drafts, identities, and masked aliases are sensitive account data, and broad scopes or raw API keys can expose more data than needed.

Mitigation: Install only when Maton is trusted for the granted Fastmail scopes, prefer OAuth, select the narrowest available scopes, and avoid raw API keys unless the CLI cannot be used.

Risk: Sending email, deleting messages or mailboxes, changing masked aliases, and creating automation can have irreversible or persistent effects.

Mitigation: Review every send, delete, connection, destination, and automation action before approval; verify target IDs and intended effects before running write operations.

Risk: Third-party trigger destinations or local event handlers can create ongoing data egress or execute code on untrusted event content.

Mitigation: Use platform-hosted functions and Maton-controlled destinations by default, avoid third-party trigger destinations unless specifically needed, and require user-authored or user-reviewed handlers for any local execution.

## Reference(s):

- [ClawHub Fastmail Skill](https://clawhub.ai/byungkyu/skills/fastmail)
- [Maton Homepage](https://maton.ai)
- [Fastmail Developer Documentation](https://www.fastmail.com/dev/)
- [JMAP Core Specification (RFC 8620)](https://www.rfc-editor.org/rfc/rfc8620.html)
- [JMAP Mail Specification (RFC 8621)](https://www.rfc-editor.org/rfc/rfc8621.html)
- [JMAP for Contacts (RFC 9610)](https://www.rfc-editor.org/rfc/rfc9610.html)
- [Masked Email](https://www.fastmail.help/hc/en-us/articles/4406536368911-Masked-Email)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON, Python, JavaScript, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces authenticated API call guidance and user-confirmed command proposals rather than standalone files by default.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
