## Description:

Connects an agent to an organization's tools and Danube's service catalog for discovery and execution over MCP or HTTP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use Danube to find, inspect, and run connected organization tools and catalog services through one API key, with user approval for consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected key may expose organization tools, credentials, workflows, wallet actions, and skill management.

Mitigation: Install only if you trust Danube with the key's reachable resources; use a restricted key with allowed services and tools.

Risk: OAuth scopes, Personal workspace selection, and tool-list filters are not reliable permission boundaries.

Mitigation: Apply restrictions to the API key itself rather than relying on those controls.

Risk: Writes, batches, spending, credential changes, and persistent skill, workflow, or context changes can have lasting effects.

Mitigation: Require explicit confirmation of the exact action and parameters; review scheduled workflows before enabling them.

Risk: An API key stored in committed configuration can be exposed.

Mitigation: Keep API keys out of committed files and store them securely.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube API keys](https://danubeai.com/dashboard/api-keys)
- [Danube release on ClawHub](https://clawhub.ai/preston-thiele/skills/danube)
- [REST API reference](artifact/references/rest-api.md)
- [Troubleshooting guide](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tool results and requests for explicit user confirmation.]

## Skill Version(s):

8.1.37 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
