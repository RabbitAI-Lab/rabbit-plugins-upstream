## Description:

Guides agents to discover and use an organization's tools and Danube's service catalog through MCP or HTTP, with confirmation before actions that change data or spend funds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use Danube to find, inspect, and run permitted organization and catalog tools, while requesting user approval for writes, purchases, and other consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Danube key can expose connected services and powerful remote tools to an agent.

Mitigation: Install only if you trust Danube and use a narrowly scoped key where possible.

Risk: Tool calls may write or delete data, spend funds, or create workflows.

Mitigation: Keep confirmation enabled for writes and paid actions; obtain explicit approval for the exact action and parameters.

Risk: Credential-handling tools may persist secrets unintentionally.

Mitigation: Do not let the agent store or reuse secrets unless the user explicitly intends it.

## Reference(s):

- [Danube OpenClaw documentation](https://docs.danubeai.com/sdk/openclaw)
- [Danube on ClawHub](https://clawhub.ai/preston-thiele/skills/danube)
- [Danube REST API guide](references/rest-api.md)
- [Danube troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with HTTP and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live tool responses depend on the connected services and the user's access.]

## Skill Version(s):

8.1.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
