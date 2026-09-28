## Description:

Gives agents governed access to an organization's tools and Danube's service catalog through MCP or curl, with confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can discover, inspect, and call permitted organization and catalog tools through Danube, while reviewing costs and confirming actions that change data or spend funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Danube API key may grant broad access to organization tools and context.

Mitigation: Use a restricted key and enable confirmation requirements where available.

Risk: Organization or personal context may be loaded into the agent's session, and personal context can be updated.

Mitigation: Avoid broad sessions where that context should not be loaded; review proposed context updates before approving them.

Risk: Saved parameter defaults or tool calls may change data or incur costs.

Mitigation: Review saved defaults and exact tool inputs, then explicitly approve consequential or paid actions.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Danube API key; tool responses and available actions depend on the connected account.]

## Skill Version(s):

8.1.17 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
