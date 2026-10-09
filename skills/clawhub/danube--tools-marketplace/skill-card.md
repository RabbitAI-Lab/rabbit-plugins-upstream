## Description:

Enables agents to discover, inspect, and use an organization's tools and a catalog of services through Danube using MCP or curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can search for available services, inspect tool capabilities, and run permitted tools through a Danube connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may have broad access to services through the provided Danube credential.

Mitigation: Use a restricted API key when least privilege matters; confirm the effective access before installation.

Risk: The skill directs agents to save recurring service identifiers as persistent parameter defaults without asking first.

Mitigation: Review and remove saved defaults in the Danube dashboard if installed.

## Reference(s):

- [Danube ClawHub release](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command and API examples; tool responses vary by service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Danube API key and curl for REST access; MCP access is also described.]

## Skill Version(s):

8.1.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
