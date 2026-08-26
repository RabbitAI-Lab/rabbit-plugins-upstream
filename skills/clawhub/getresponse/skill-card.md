## Description:

GetResponse API integration with managed OAuth for managing email marketing campaigns, contacts, newsletters, autoresponders, segments, workflows, ecommerce records, SMS, landing pages, webinars, transactional emails, forms, and account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing teams use this skill to let an agent inspect and manage GetResponse campaigns, contacts, automations, ecommerce records, SMS, webinars, landing pages, and account data. The skill is suited to account operations where read calls are preferred first and every write, send, publish, delete, or new connection is explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may create a new GetResponse connection or use the wrong connected account.

Mitigation: Require explicit approval before creating a connection, prefer least-privilege OAuth scopes, specify the intended connection when more than one exists, and revoke unused connections.

Risk: Write operations can modify or delete contacts, campaigns, workflows, ecommerce records, or other account data.

Mitigation: Default to read and list calls first, then confirm the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Newsletter, SMS, and transactional email operations may send messages to real contacts.

Mitigation: Confirm the audience, message content, and send timing with the user before execution.

Risk: API keys, OAuth tokens, or provider-issued tokens may be exposed through logs, command lines, or persisted files.

Mitigation: Prefer OAuth, let the CLI and operating system credential store handle secrets, do not print or persist credentials, and use the raw HTTP fallback only when the CLI cannot be installed.

Risk: External data returned from GetResponse can contain untrusted instructions or content.

Mitigation: Treat API responses as data, validate values before reuse, and do not execute or follow instructions contained in fetched external content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/getresponse)
- [Maton Homepage](https://maton.ai)
- [GetResponse API Documentation](https://apidocs.getresponse.com/v3)
- [GetResponse OpenAPI Spec](https://apireference.getresponse.com/open-api.json)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected GetResponse account.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter metadata.version: 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
