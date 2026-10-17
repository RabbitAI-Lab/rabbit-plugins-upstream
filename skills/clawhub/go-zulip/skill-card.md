## Description:

Guides Go developers using an unofficial Zulip REST API client for messages, users, channels, subscriptions, events, and administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working on Go projects use this skill to integrate Zulip API access, including reading messages and users, managing subscriptions, and performing requested organization actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zulip API credentials or request data may be exposed to an untrusted server or logs.

Mitigation: Use a trusted HTTPS Zulip server, keep the API key out of code and logs, and grant the bot or account only needed permissions.

Risk: Sending, editing, deleting, or administering Zulip resources can change organization data.

Mitigation: Confirm the requested action and target resources before running mutating code.

## Reference(s):

- [go-zulip setup and reference](artifact/references/setup.md)
- [ClawHub go-zulip release](https://clawhub.ai/psyb0t/skills/go-zulip)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Go project and credentials for a trusted Zulip server.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
