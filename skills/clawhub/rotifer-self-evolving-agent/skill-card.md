## Description:

Rank an Agent's Rotifer Genes against the Arena and swap in stronger ones. Invoked explicitly via /evolve — scan local capabilities, compare Genes, inspect fitness scores, and replace weak ones with user approval. Not for capabilities outside Rotifer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and Agent operators use this skill to inspect local Rotifer Genes, compare their fitness with Arena rankings, and review proposed replacements. It can also create and run local Agents from Genes when explicitly invoked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gene replacements use unsigned third-party code and can change Agent behavior.

Mitigation: Before approving a replacement, review the Gene publisher, source, Arena grade, and V(g) safety scan report.

Risk: Running an Agent executes its Genes and writes local run and fitness records.

Mitigation: Keep sandbox escapes disabled and review Gene code before running it.

Risk: Usage reporting is enabled for logged-in users, and rollback preserves only the last replacement.

Mitigation: Set ROTIFER_TELEMETRY=0 to disable usage reporting and install counting; use rollback promptly if a replacement needs to be undone.

## Reference(s):

- [Rotifer Playground repository](https://github.com/rotifer-protocol/rotifer-playground)
- [Rotifer MCP Server package (v0.19.6)](https://www.npmjs.com/package/@rotifer/mcp-server/v/0.19.6)
- [Rotifer MCP Server source](https://github.com/rotifer-protocol/rotifer-mcp-server)
- [Rotifer Protocol specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer Capability Marketplace](https://rotifer.ai)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Configuration files, Agent execution results]

**Output Format:** [Text and Markdown reports, with project files when creating an Agent or approving a Gene replacement]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Invoked with /evolve commands; replacement requires user approval. Running an Agent executes its Genes inside the configured WASM sandbox.]

## Skill Version(s):

2.4.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
