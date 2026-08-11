## Description:

Guides agents through using ~alter's hosted MCP tools to post, inspect, cancel, and poll standing identity-trait requirements and manage opt-in match participation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true-alter](https://clawhub.ai/user/true-alter)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill when an agent needs an ongoing standing search for people matching identity-trait ranges, rather than a one-time lookup. It helps create, review, cancel, and poll owned requirements while respecting the opt-in match pool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive identity matching and opt-in identity reveals.

Mitigation: Use only authenticated, ownership-checked calls and confirm that matching participants have opted into the standing-match pool.

Risk: Polling can charge $0.01 for each delivered fill.

Mitigation: Set an operator-approved budget before polling and avoid unattended polling loops.

Risk: Using the wrong endpoint or credential can expose access to a non-canonical service.

Mitigation: Connect only to https://mcp.truealter.com/api/v1/mcp and provide a valid ALTER_API_KEY through the configured secret path.

## Reference(s):

- [~Alter Identity Orderbook ClawHub page](https://clawhub.ai/true-alter/skills/alter-identity-orderbook)
- [~alter publisher profile](https://clawhub.ai/user/true-alter)
- [~alter MCP server](https://mcp.truealter.com/api/v1/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, API calls]

**Output Format:** [Markdown instructions with tool names, JSON-shaped arguments, and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ALTER_API_KEY and the hosted alter MCP server; poll_requirement_matches can spend $0.01 when a fill is delivered.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
