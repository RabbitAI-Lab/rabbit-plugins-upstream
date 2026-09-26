## Description:

Helps agents use connected third-party services through the Maton gateway for API requests and approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can read or update resources in connected apps, and configure event-driven workflows when explicitly authorized. A Maton account, network access, and a connection to each target service are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected services may expose sensitive data or grant broad account permissions.

Mitigation: Review OAuth scopes, choose narrow connections, and prefer read-only operations.

Risk: Writes, deletions, and automations can change external resources or send information to recipients.

Mitigation: Require explicit approval for each action with exact resource IDs and destinations.

Risk: Webhook destinations and local event handlers can continue forwarding data or running code unattended.

Mitigation: Avoid persistent destinations and --exec handlers unless specifically needed and separately approved.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include data returned by connected services.]

## Skill Version(s):

1.2.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
