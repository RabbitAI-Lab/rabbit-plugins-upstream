## Description:

Helps agents discover and use an organization's tools and Danube's service catalog through MCP or REST, with user confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to find, inspect, and invoke connected services and organizational tools, while seeking approval for writes, spending, credential changes, and other consequential operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad OAuth or API-key access can expose organizational tools and credentials.

Mitigation: Prefer a key restricted to needed services and tools; enable confirmation requirements and approve credential or organization changes yourself.

Risk: Scheduled workflows can keep acting with the author's credentials after the conversation ends.

Mitigation: Explicitly approve workflow changes and regularly review scheduled workflows in the Danube dashboard.

Risk: Saved parameter defaults can alter later tool calls.

Mitigation: Review saved defaults in the Danube dashboard and confirm changes before applying them.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with inline commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tool results returned by connected services.]

## Skill Version(s):

8.1.32 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
