## Description:

Helps agents discover and use organizational and catalog tools through Danube with explicit consent before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Danube to find, inspect, and run permitted services, including their organization's connected tools, over MCP or HTTP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broadly authorized connection may allow actions beyond what users expect.

Mitigation: Prefer a narrowly scoped Danube API key over OAuth where possible; do not treat Personal workspace or MCP tool-list filters as security boundaries.

Risk: Tool calls can write, send, delete, or spend funds, including in batches.

Mitigation: Show the exact tool and parameters and obtain explicit confirmation before any write or batch action.

Risk: Credential storage, saved defaults, and spending controls can change future tool behavior.

Mitigation: Review scope and existing settings before modifying them; confirm proposed changes with the user.

Risk: Scheduled workflows and downloaded skills can have effects beyond the immediate interaction.

Mitigation: Review the schedule or downloaded content and obtain explicit consent before enabling or using it.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown with tool results and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include discovered tool schemas, results, and consent prompts.]

## Skill Version(s):

8.1.32 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
