## Description:

Helps agents discover and use an organization's tools and Danube's service catalog over MCP or HTTP, with confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Danube to discover available organizational and third-party tools, inspect their capabilities, and execute authorized tasks through a Danube account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent access to the Danube account may extend to tools, credentials, workflows, and wallet or spending controls.

Mitigation: Use a restricted API key limited to the needed services and tools; review credentials, workflows, and spending limits in the Danube dashboard after use.

Risk: Write or spending actions can have real-world effects, and permission scopes may not provide the expected limits.

Mitigation: Require explicit confirmation for every write or spending action and review the exact tool and inputs before execution.

Risk: Scheduled workflows may act later without direct user oversight.

Mitigation: Avoid scheduling workflows unless their actions and permissions are fully understood and controlled.

## Reference(s):

- [Danube on ClawHub](https://clawhub.ai/preston-thiele/skills/danube)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](artifact/references/rest-api.md)
- [Troubleshooting guide](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with commands and tool results as applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Danube account and API key; consequential tool actions should be confirmed with the user.]

## Skill Version(s):

8.1.33 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
