## Description:

Gmail API integration with managed OAuth for reading, sending, and managing emails, threads, labels, and drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT

## Use Case:

External developers and agents use this skill to interact with Gmail through managed OAuth, including mailbox search, message retrieval, sending mail, draft handling, thread access, and label management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-privilege mailbox actions such as sending email, trashing messages, changing labels, deleting connections, and sending drafts.

Mitigation: Require explicit user confirmation before taking destructive or externally visible Gmail actions.

Risk: The skill depends on a Maton API key and troubleshooting steps could expose credentials if outputs are copied or logged.

Mitigation: Avoid printing, logging, or sharing API keys; verify only that the required environment variable is present.

Risk: When multiple Gmail accounts are connected, using the default connection could affect the wrong mailbox.

Mitigation: Ask the user to select the intended Gmail connection and include the Maton-Connection header when account choice matters.

## Reference(s):

- [ClawHub Gmail skill page](https://clawhub.ai/seanford/skills/gmail)
- [Gmail API REST reference](https://developers.google.com/gmail/api/reference/rest)
- [Gmail messages.list](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list)
- [Gmail messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send)
- [Maton account](https://maton.ai)
- [Maton connection management](https://ctrl.maton.ai)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with inline bash, Python, JavaScript, HTTP, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a valid Maton API key, and an active Gmail OAuth connection.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
