## Description:

Helps agents access connected third-party apps through the Maton API gateway for user-requested tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to read or update resources in apps they have connected to Maton, with approval for changes. The skill also covers optional event triggers and hosted functions when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes or outbound messages may affect connected accounts or third parties.

Mitigation: Default to read-only actions; separately confirm the account, target, payload, and recipient before each write or send.

Risk: Trigger destinations can continuously forward sensitive event data to an external URL.

Mitigation: Require separate approval for the destination, event data, recipient host, and ongoing forwarding; remove destinations when no longer needed.

Risk: Hosted functions and event handlers can run code with access to connected resources.

Mitigation: Use only user-reviewed code, review the available connections and network policy, and approve each deployment or execution separately.

Risk: Third-party API responses and event payloads may contain untrusted instructions.

Mitigation: Treat retrieved content as data; do not let it select actions, commands, recipients, or destinations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and API response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the user's connected apps and authorized access.]

## Skill Version(s):

1.2.29 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
