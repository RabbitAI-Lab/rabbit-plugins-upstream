## Description:

Compares an agent's installed Rotifer Genes with Arena rankings and recommends stronger alternatives, installing replacements only with user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to assess installed Rotifer capabilities against Arena rankings, compare replacements, and upgrade or roll back Genes in their projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Upgrades install unsigned third-party Gene code and may replace existing project capabilities.

Mitigation: Review the proposed Gene's publisher, safety assessment, and source before approving; use rollback if a replacement causes problems.

Risk: Running an agent executes installed Gene code.

Mitigation: Review Genes before running them and keep execution in the default sandbox.

Risk: Usage logging and install counter updates may send activity to Rotifer.

Mitigation: Set ROTIFER_TELEMETRY=0 if you do not want these updates.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xiaoba-dev/skills/rotifer-self-evolving-agent)
- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer MCP server package](https://www.npmjs.com/package/@rotifer/mcp-server/v/0.19.3)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with comparisons and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upgrades require approval; creating or running agents can write local files or execute Gene code.]

## Skill Version(s):

2.4.10 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
