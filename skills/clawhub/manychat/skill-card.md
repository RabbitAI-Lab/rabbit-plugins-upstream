## Description:

Helps agents manage ManyChat subscribers, tags, custom fields, flows, and messages through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and developers use this skill to retrieve or update ManyChat subscriber information, manage tags and fields, and send messages or run approved automations through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account access or writes may affect the wrong ManyChat connection or send messages to unintended recipients.

Mitigation: Use the narrowest available scopes, verify the target connection, and obtain explicit user approval before writes or sends.

Risk: Hosted functions, triggers, or destinations may continue acting or forwarding data after setup.

Mitigation: Review each automation and destination before enabling it; remove it when no longer needed.

## Reference(s):

- [ManyChat skill release](https://clawhub.ai/byungkyu/skills/manychat)
- [Maton homepage](https://maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [ManyChat API key guide](https://help.manychat.com/hc/en-us/articles/14959510331420)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain subscriber details; disclose only the fields needed for the task.]

## Skill Version(s):

1.2.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
