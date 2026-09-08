## Description:

Gmail API integration with managed OAuth for reading, sending, and managing emails, threads, labels, and drafts through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to interact with a connected Gmail account through managed OAuth, including listing and reading messages, sending email, managing labels, and working with drafts. It is intended for workflows where the agent should default to read/list actions and ask for explicit approval before authorization changes or writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests sensitive Gmail access through Maton.

Mitigation: Confirm the user is comfortable granting Gmail access through Maton and choose the narrowest Gmail scopes available.

Risk: Messages can be sent, drafts can be created or sent, labels can be changed, and messages can be trashed.

Mitigation: Review the exact target account, connection, resource identifiers, and payload before approving any write operation.

Risk: Multiple Maton accounts or Gmail connections can make the target account ambiguous.

Mitigation: Specify the intended profile or connection when more than one exists.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Gmail API Overview](https://developers.google.com/gmail/api/reference/rest)
- [Gmail List Messages](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list)
- [Gmail Get Message](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get)
- [Gmail Send Message](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send)
- [Gmail List Threads](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/list)
- [Gmail List Labels](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/list)
- [Gmail Create Draft](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/create)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance and commands for Gmail API calls through Maton; write actions require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
