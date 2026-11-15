## Description:

Ranks an Agent's Rotifer Genes against Arena data, recommends upgrades, and can create and run local Agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers using Rotifer can compare a project's installed Genes with Arena rankings, inspect fitness, and review upgrade recommendations. After approval, they can replace a Gene or create and run a local Agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release scan is benign with medium confidence but incomplete, and some local references were unresolved.

Mitigation: Review the documented install and credential handling details, and inspect the pinned package before use if those details affect your environment.

Risk: Approved upgrades install unsigned third-party Gene code, and the run-agent command executes Genes.

Mitigation: Review the publisher, Gene source, and available safety information before approving an upgrade; run local Agents only when requested and keep the WASM sandbox enabled.

Risk: When logged in, MCP tool call metadata is reported to Rotifer Cloud; the CLI also sends an anonymous heartbeat when running Genes.

Mitigation: Review the documented telemetry details and use ROTIFER_TELEMETRY=0 to disable the server's telemetry; use DO_NOT_TRACK=1 to disable the CLI heartbeat.

## Reference(s):

- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer MCP Server source](https://github.com/rotifer-protocol/rotifer-mcp-server)
- [Rotifer MCP Server 0.20.0 package](https://www.npmjs.com/package/@rotifer/mcp-server/v/0.20.0)
- [Rotifer Capability Marketplace](https://rotifer.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Code, Configuration]

**Output Format:** [Markdown responses and local Agent or Gene files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fitness comparisons and upgrade recommendations; project files are written only after approval, and Agent execution is explicit.]

## Skill Version(s):

2.4.15 (source: skill frontmatter metadata and evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
