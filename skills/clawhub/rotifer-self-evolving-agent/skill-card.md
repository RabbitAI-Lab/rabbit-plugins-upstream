## Description:

Rank an Agent's Rotifer Genes against the Arena and swap in stronger ones when invoked explicitly with /evolve, with user approval required before replacements are installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agent maintainers use this skill to compare local Rotifer Genes against Arena rankings, inspect stronger alternatives, and approve upgrades or rollbacks. It also helps compose and run local Agents from installed Genes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime tooling is fetched from npm, and run-agent may use an unpinned @rotifer/playground fallback if the reviewed CLI is not installed.

Mitigation: Review and pin the Rotifer packages before use; install the Rotifer CLI at a fixed reviewed version so run-agent does not need the unpinned fallback.

Risk: Upgrades can install unsigned third-party Genes into the current project.

Mitigation: Treat each proposed Gene like a dependency: review the publisher, source, Arena grade, and safety scan before approving, and use rollback if an upgrade behaves unexpectedly.

Risk: When logged in, usage telemetry can be sent to Rotifer Cloud, and installs update a public install counter.

Mitigation: Stay logged out or set ROTIFER_TELEMETRY=0 when telemetry is not desired.

Risk: run-agent executes local Agent Genes.

Mitigation: Keep execution inside the WASM sandbox and do not run Genes unsandboxed from a terminal unless the code has been separately reviewed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xiaoba-dev/skills/rotifer-self-evolving-agent)
- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Capability Marketplace](https://rotifer.ai)
- [Rotifer MCP Server package](https://www.npmjs.com/package/@rotifer/mcp-server/v/0.17.0)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and local file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces recommendations from live Arena data and can write project Genes, Agent definitions, rollback snapshots, local run logs, and an update-check cache after user-approved actions.]

## Skill Version(s):

2.4.8 (source: frontmatter, clawhub metadata, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
