## Description:

Enables agents to discover and use an organization's tools and Danube's service catalog through MCP or REST, with confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use Danube to find and invoke permitted external or organization-specific tools, while reviewing sensitive actions before they run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broadly privileged Danube API key can expose connected tools and accounts to consequential actions.

Mitigation: Use a narrowly scoped key and review its account permissions before enabling the skill.

Risk: Tool calls can write, delete, send, or spend on the user's behalf.

Mitigation: Require explicit confirmation for destructive or paid actions and inspect the exact tool and parameters before execution.

Risk: Stored defaults or credentials may grant access beyond what the user expects.

Mitigation: Review saved defaults and credentials in the Danube dashboard; provide third-party secrets only when intentionally authorizing Danube to store them.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube REST API recipes](artifact/references/rest-api.md)
- [Danube troubleshooting](artifact/references/troubleshooting.md)
- [Danube ClawHub release](https://clawhub.ai/preston-thiele/skills/danube)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown text with optional command and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May present tool results and request user confirmation before actions.]

## Skill Version(s):

8.1.20 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
