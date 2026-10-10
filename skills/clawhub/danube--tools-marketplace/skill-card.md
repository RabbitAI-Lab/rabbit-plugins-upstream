## Description:

Enables agents to discover and use an organization's tools and Danube's service catalog through MCP or curl with a Danube API key and consent for consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Danube to find, inspect, and invoke organizational and catalog tools while managing permissions, costs, and confirmation for consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Danube API key can grant broad access to remote tools, including actions that write or spend.

Mitigation: Use a key restricted to needed services or tools and require explicit confirmation before writes, spending, or other consequential actions.

Risk: The skill instructs agents to save reusable service parameters without first asking the user.

Mitigation: Review and remove unwanted saved parameter defaults in the Danube dashboard.

Risk: OAuth scopes alone may not limit the tools an agent can access.

Mitigation: Do not rely on OAuth scopes for tool-level restrictions; use a restricted Danube API key where possible.

## Reference(s):

- [Danube OpenClaw integration guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API examples](artifact/references/rest-api.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with curl commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results depend on the user's key and available services.]

## Skill Version(s):

8.1.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
