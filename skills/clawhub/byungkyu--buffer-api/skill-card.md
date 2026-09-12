## Description:

Buffer API integration with managed authentication for scheduling and managing social media posts across supported platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Buffer through Maton, inspect Buffer account, organization, channel, post, and idea data, and create or schedule social content with explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Maton connection can access Buffer account data and perform actions allowed by the connected account, including endpoints beyond the examples in the skill.

Mitigation: Use OAuth where possible, select the narrowest Buffer scopes offered, connect only the account needed for the task, and specify the intended connection when multiple accounts are available.

Risk: Creating or scheduling social posts can publish content publicly or affect brand reputation.

Mitigation: Default to read and list operations first, then confirm the target channel, payload, schedule, and intended effect with the user before any write operation.

Risk: Deleting a connection is irreversible and can break automation using that connection.

Mitigation: List connections, match the exact connection identifier with the user, and avoid deletion unless the user has confirmed the specific connection.

Risk: Raw API-key use can expose a long-lived Maton credential through environment variables, logs, shell history, or pasted output.

Mitigation: Prefer the Maton CLI OAuth flow; where raw HTTP is required, keep the key in the process environment, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

Risk: Buffer API responses may contain personal or sensitive account, channel, post, or message data.

Mitigation: Extract only fields needed for the task and avoid dumping full raw responses into logs, files, or user-visible output unless explicitly requested.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/buffer-api)
- [Maton homepage](https://maton.ai)
- [Buffer API Documentation](https://developers.buffer.com/reference.html)
- [Buffer API Getting Started](https://developers.buffer.com/guides/getting-started.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions and API request examples; runtime calls may return JSON from Buffer through Maton.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
