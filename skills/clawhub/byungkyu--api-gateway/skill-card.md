## Description:

Helps agents use the Maton gateway to work with a user's connected third-party apps and manage associated automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with a Maton account can read or update information in connected apps, such as mailboxes, CRMs, and project tools. With explicit approval, they can also set up event triggers, webhook destinations, and functions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected apps grant the agent access to third-party account data and actions.

Mitigation: Start with read-only requests, use only the intended connection, and obtain fresh approval for each write or send with its target and payload.

Risk: Webhook destinations and event triggers can forward future account data or perform actions automatically.

Mitigation: Confirm the destination URL, recipient, event data, and ongoing delivery before enabling them; remove unused connections and automations.

Risk: Functions and local event handlers can execute actions using connected-account authority or untrusted event data.

Mitigation: Require explicit approval for deployments and local handlers, review code and permissions, and avoid exposing credentials.

## Reference(s):

- [ClawHub API Gateway release](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton](https://maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and a connection to the target app.]

## Skill Version(s):

1.2.28 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
