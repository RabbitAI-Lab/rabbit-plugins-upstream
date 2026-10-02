## Description:

Helps agents discover, inspect, and use an organization's tools and Danube's service catalog through MCP or curl, with guidance for confirming sensitive actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents' users can connect their agents to Danube to find and run organizational or catalog tools, while reviewing sensitive actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad access to third-party tools can disclose data or cause external actions.

Mitigation: Trust Danube with the requested data and actions, use a narrowly scoped API key, and send only necessary data.

Risk: Tool calls may write, send, spend, or delete, and confirmation is not assured by every tool path.

Mitigation: Keep confirmation required for writes and spending; review each sensitive action before execution.

Risk: Credential, workflow, wallet, and skill management carry lasting or financial effects.

Mitigation: Carefully review credential-storage and workflow or skill-management requests; do not change spending limits or fund wallets without an explicit request.

Risk: The skill may save recurring service identifiers as defaults without asking first.

Mitigation: Review saved defaults and remove unwanted ones in the Danube dashboard.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube REST API reference](artifact/references/rest-api.md)
- [Danube troubleshooting](artifact/references/troubleshooting.md)
- [Danube on ClawHub](https://clawhub.ai/preston-thiele/skills/danube)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP or REST tool calls; responses depend on the selected service.]

## Skill Version(s):

8.1.22 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
