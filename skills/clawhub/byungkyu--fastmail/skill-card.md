## Description:

Helps agents read, search, organize, and send Fastmail messages and manage mailboxes, drafts, contacts, and masked email addresses through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Fastmail can guide an agent to find and organize email, compose and send messages, manage contacts and masked addresses, and set up approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting a Fastmail account grants access to private mail and account data.

Mitigation: Obtain explicit approval for the connection, use only necessary access, and prefer the CLI login flow over handling raw API keys.

Risk: Sending, deleting, or changing mail, mailboxes, contacts, or masked addresses can have lasting effects.

Mitigation: Review the exact recipient, target, and change with the user before each write; draft messages before sending.

Risk: Functions, triggers, and destinations can cause continuing actions or forward event data.

Mitigation: Review automation behavior and destination URLs, and obtain separate explicit approval before enabling them.

## Reference(s):

- [Fastmail skill on ClawHub](https://clawhub.ai/byungkyu/skills/fastmail)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Fastmail developer documentation](https://www.fastmail.com/dev/)
- [JMAP mail specification](https://www.rfc-editor.org/rfc/rfc8621.html)
- [Trigger event references](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON request examples, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read and list by default; request approval before connecting accounts or changing data.]

## Skill Version(s):

1.2.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
