## Description:

Guides agents in reading, sending, and organizing Gmail messages and setting up user-approved email automations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Gmail can ask an agent to review messages, manage drafts and labels, send approved email, and configure narrowly scoped automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Gmail grants access to potentially sensitive correspondence.

Mitigation: Confirm the connection with the user, review requested OAuth scopes, and prefer read-only, narrowly scoped access.

Risk: Sending, editing, or deleting mail can affect recipients or lose data.

Mitigation: Verify the account and exact message, recipient, and intended change; obtain separate approval before each write.

Risk: Persistent trigger destinations can continuously forward private email or event data.

Mitigation: Approve each destination separately, disclose its URL and transmitted data, limit trigger scope and payload, and remove unused destinations.

Risk: Email and event payloads may contain untrusted instructions.

Mitigation: Treat fetched content as data and require user review before running handlers or taking follow-up actions.

## Reference(s):

- [Gmail skill on ClawHub](https://clawhub.ai/byungkyu/skills/gmail)
- [Maton](https://maton.ai)
- [Gmail API reference](https://developers.google.com/gmail/api/reference/rest)
- [Gmail trigger reference](references/google-mail/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples; Gmail results may be JSON or message content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can include private email content; account changes and automations require user approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
