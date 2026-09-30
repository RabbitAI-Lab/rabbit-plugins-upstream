## Description:

Helps agents manage Instantly outreach campaigns, leads, email accounts, and analytics through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and operations teams use this skill to review Instantly outreach data and, with approval, manage campaigns, leads, accounts, emails, and related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign changes, email sends, forwarding, or new connections can have unintended effects.

Mitigation: Default to reading data; confirm the target and effect of each write, send, forward, or connection with the user before acting.

Risk: Functions, triggers, or destinations can repeatedly act or forward events after setup.

Mitigation: Request separate approval for deployments, triggers, and destinations; scope event sources and recipients narrowly.

Risk: Mailbox passwords or API keys may be exposed if pasted into a conversation or command.

Mitigation: Prefer device authentication and provider authorization; never request secrets in chat, and use the documented fallback only when necessary.

## Reference(s):

- [Instantly skill on ClawHub](https://clawhub.ai/byungkyu/skills/instantly)
- [Maton homepage](https://maton.ai)
- [Instantly API v2 documentation](https://developer.instantly.ai/api-reference)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton API gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and authorization for the requested Instantly actions.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
