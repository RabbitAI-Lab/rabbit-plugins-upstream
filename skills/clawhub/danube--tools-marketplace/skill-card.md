## Description:

Gives agents governed access to an organization's tools and a catalog of services through Danube, with confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can discover available tools, inspect their requirements, and invoke permitted services through Danube using an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may save service parameter defaults that change future calls without first asking the user.

Mitigation: Before saving defaults, show the service, parameter names and values, explain their effect on future calls, and obtain explicit approval.

Risk: A Danube API key may allow access to the user's permitted tools, including consequential actions.

Mitigation: Scope the key tightly in Danube and keep confirmation requirements enabled where possible.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands]

**Output Format:** [Text or Markdown with tool calls and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tool results, confirmation requests, and error guidance.]

## Skill Version(s):

8.1.21 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
