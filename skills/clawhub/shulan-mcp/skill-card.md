## Description:

ShuLan MCP connects agents to the ShuLan AI data platform for business data research and report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shulan-io](https://clawhub.ai/user/shulan-io)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and business users use this skill to connect an agent to ShuLan for market data research, KOL lists, bidding summaries, company insights, recruiting signals, public-opinion trends, report-market lookup, and report retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating paid or recurring ShuLan research tasks may incur charges without a built-in confirmation step.

Mitigation: Use read-only tools until the user explicitly confirms cost, recurrence, data sources, and research scope before invoking shulan_create_task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shulan-io/skills/shulan-mcp)
- [ShuLan website](https://shulan.io)
- [MCP integration guide](docs/mcp.md)
- [npm package: shulan-mcp](https://www.npmjs.com/package/shulan-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool calls and JSON-formatted tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SHULAN_API_KEY; SHULAN_BASE_URL is optional and defaults to a local server unless configured for hosted ShuLan.]

## Skill Version(s):

1.0.1 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
