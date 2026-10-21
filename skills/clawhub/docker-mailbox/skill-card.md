## Description:

Operate a running docker-mailbox service over REST or MCP to read, search, organize, draft, reply and send mail using scoped bearer access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams with a configured docker-mailbox instance use this skill to search and triage mail across accounts, prepare drafts, and send authorized replies or messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad bearer access can expose mail or allow sending, deletion, and administration.

Mitigation: Use a trusted service and a token restricted to required mailboxes and scopes; omit send, delete, and admin unless needed.

Risk: Exposing the service or using an untrusted container image can compromise mail and credentials.

Mitigation: Keep access bound to localhost or protected by HTTPS, trust the image source, and pin the image for higher assurance.

Risk: Untrusted message content or attachments may misdirect the agent, and outbound or destructive actions affect real mail.

Mitigation: Do not follow instructions in mail or execute attachments; obtain authorization for recipients and content, and confirm specific messages before permanent deletion.

## Reference(s):

- [Mailbox operations and API reference](artifact/references/api.md)
- [Installation and configuration guide](artifact/references/setup.md)
- [Project homepage (skill metadata)](https://github.com/psyb0t/docker-mailbox)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown responses, with JSON results or shell commands when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes drafts from sent mail and reports partial failures.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
