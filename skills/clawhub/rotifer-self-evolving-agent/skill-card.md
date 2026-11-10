## Description:

Rank an Agent's Rotifer Genes against the Arena and swap in stronger ones. Invoked explicitly via /evolve — scan local capabilities, compare Genes, inspect fitness scores, and replace weak ones with user approval. Not for capabilities outside Rotifer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and Agent operators use this skill to inspect Rotifer capabilities, compare their fitness with Arena rankings, and review possible upgrades. It can also create and run local Agents built from Genes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Upgrades install unsigned third-party Genes that can change Agent behavior; Arena rankings are not a security guarantee.

Mitigation: Review the publisher, safety scan, source, and destination before approving an upgrade. The most recent replacement can be rolled back from its snapshot.

Risk: Running an Agent executes Gene code, and the runtime downloads software; external executable dependencies were not audited in this review.

Mitigation: Run only Agents and Genes you trust, review and pin dependencies, and keep sandboxing enabled.

Risk: When logged in, usage details are reported to Rotifer Cloud; Gene installations also increment the public install count.

Mitigation: Set ROTIFER_TELEMETRY=0 before launch to disable the reporting described in the skill.

## Reference(s):

- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer Protocol specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer MCP Server 0.19.6](https://www.npmjs.com/package/@rotifer/mcp-server/v/0.19.6)
- [MCP Server source repository](https://github.com/rotifer-protocol/rotifer-mcp-server)
- [Rotifer Capability Marketplace](https://rotifer.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration]

**Output Format:** [Markdown reports and project-local Gene and Agent definition files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upgrade installation requires user approval; run-agent executes Gene code.]

## Skill Version(s):

2.4.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
