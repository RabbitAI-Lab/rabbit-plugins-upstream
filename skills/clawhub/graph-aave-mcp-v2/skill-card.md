## Description:

Aave V2/V3/V4 MCP server for reserves, positions, cross-chain liquidation risk monitoring with live health-factor confirmation, governance, V4 hubs and spokes, exchange rates, swap quotes, rewards, protocol history, and durable findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query Aave V2, V3, and V4 market, account, governance, reward, swap quote, and liquidation-risk data through an MCP server. It supports investigation workflows that need The Graph data, Aave V4 API responses, on-chain health-factor confirmation, and persisted findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GRAPH_API_KEY exposure could allow unauthorized use of the associated The Graph account.

Mitigation: Keep GRAPH_API_KEY out of commits, logs, shared terminals, and screenshots; prefer secret management for configured agents.

Risk: The findings store can retain wallet watchlists or monitoring preferences beyond a single interaction.

Mitigation: Use the findings deletion tool or remove the local state file when saved context should not persist.

Risk: Running a global npm MCP server gives the package local execution and expected network access.

Mitigation: Review the package before installation, pin the intended version, and run it only in an environment approved for MCP servers with external network access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/paulieb14/skills/graph-aave-mcp-v2)
- [Project Homepage](https://github.com/PaulieB14/graph-aave-mcp)
- [npm Package](https://www.npmjs.com/package/graph-aave-mcp)
- [The Graph Studio](https://thegraph.com/studio/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and text responses with inline shell commands and MCP tool outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GRAPH_API_KEY; may persist per-session findings such as wallet watchlists or monitoring preferences.]

## Skill Version(s):

4.2.1 (source: server evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
