## Description:

Rank an Agent's Rotifer Genes against the Arena and swap in stronger ones. Invoked explicitly via /evolve — scan local capabilities, compare Genes, inspect fitness scores, and replace weak ones with user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to inspect an Agent's Rotifer Genes, compare them with Arena rankings, and review upgrade recommendations. They can approve Gene replacements, create local Agent definitions, and run local Agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clawscan marks the release suspicious because it reports agent creation and local Agent execution commands beyond the stated evaluation and upgrade purpose; its analysis was partial and does not establish those commands' behavior.

Mitigation: Follow the scanner guidance: review the suspicious verdict and high-severity recommendation not to install, and inspect the commands and their local references before use.

Risk: An approved upgrade installs unsigned third-party Gene code, and run-agent executes local Gene code.

Mitigation: Review the Gene publisher, Arena grade, safety scan, and source before approving installation; use the documented sandboxed run path.

## Reference(s):

- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Capability Marketplace](https://rotifer.ai)
- [Rotifer MCP Server on npm](https://www.npmjs.com/package/@rotifer/mcp-server/v/0.20.0)
- [Rotifer MCP Server source](https://github.com/rotifer-protocol/rotifer-mcp-server)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer Playground](https://github.com/rotifer-protocol/rotifer-playground)
- [ClawHub release](https://clawhub.ai/xiaoba-dev/skills/rotifer-self-evolving-agent)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance, Configuration, Code]

**Output Format:** [Markdown responses and project Agent or Gene files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read local Gene and Agent definitions, install an approved Gene replacement, create Agent definitions, or execute a local Agent.]

## Skill Version(s):

2.4.14 (source: SKILL.md frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
