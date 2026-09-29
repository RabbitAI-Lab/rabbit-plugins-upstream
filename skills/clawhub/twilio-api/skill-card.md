## Description:

Guides agents in using a connected Twilio account through Maton for messaging, calls, phone numbers, and approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to inspect Twilio resources, send messages, place calls, manage phone numbers, or set up explicitly approved automations through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton mediates access to the user's Twilio account.

Mitigation: Install only if that access is intended; connect only the account and permissions needed.

Risk: Messages, calls, deletions, and hosted functions can have consequential effects.

Mitigation: Confirm recipients, numbers, resources, and intended effects before each write or deployment.

Risk: Trigger destinations can continuously forward matching events to a URL.

Mitigation: Get separate approval for the exact destination, scope events narrowly, and forward only necessary fields.

## Reference(s):

- [Twilio skill on ClawHub](https://clawhub.ai/byungkyu/skills/twilio-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Twilio API overview](https://www.twilio.com/docs/usage/api)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to read and list operations; writes and ongoing automations require user approval.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata; skill frontmatter states 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
