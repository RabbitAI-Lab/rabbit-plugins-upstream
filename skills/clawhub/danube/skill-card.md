## Description:

Helps agents discover, inspect, and use organizational and catalog tools through Danube, with user confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find and invoke Danube tools for an organization's connected services, while asking users to approve writes, spending, and other consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access broad Danube account and organization tools, and available permission scopes may be weak.

Mitigation: Use a restricted API key with allowed_services or allowed_tools where possible; grant only the services needed.

Risk: Actions may write data, change credentials or configuration, or spend funds.

Mitigation: Keep confirmation enabled and review the exact action and parameters before approving writes, credential storage, skill or workflow changes, wallet funding, or saved defaults.

## Reference(s):

- [Danube skill release](https://clawhub.ai/preston-thiele/skills/danube)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API guide](references/rest-api.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Text and Markdown with command and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool responses depend on the connected services and the user's permissions.]

## Skill Version(s):

8.1.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
