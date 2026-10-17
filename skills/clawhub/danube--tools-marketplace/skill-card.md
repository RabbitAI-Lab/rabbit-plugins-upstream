## Description:

Helps agents discover and use an organization's tools and Danube's service catalog over MCP or HTTP, with user confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can search available organizational and public tools, inspect their requirements, and perform authorized tasks through Danube using an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad access to external tools can enable unintended writes, spending, or data sharing.

Mitigation: Restrict the API key to needed services and tools, and require explicit approval of exact parameters before writes or batches.

Risk: Stored credentials, saved defaults, and scheduled workflows can affect later calls or run after the conversation ends.

Mitigation: Avoid storing plaintext secrets, review saved defaults, and confirm each schedule and its future effects before enabling it.

Risk: Organization context or sensitive data may be forwarded to third-party services.

Mitigation: Send only task-required data and review each destination and permission scope before execution.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube REST API reference](references/rest-api.md)
- [Danube troubleshooting](references/troubleshooting.md)
- [Danube skill on ClawHub](https://clawhub.ai/danube/skills/tools-marketplace)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command and configuration examples; tool responses may be JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available tools and results depend on the user's credentials, permissions, and current catalog.]

## Skill Version(s):

8.1.35 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
