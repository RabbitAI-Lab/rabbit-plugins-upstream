## Description:

Patsnap MCP helps agents use the OOMOL Patsnap connector to read, create, update, and analyze patent data through schema-checked oo CLI actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to work with Patsnap patent search, bibliographic, full-text, family, citation, legal status, and landscape actions through a connected OOMOL account. It supports read workflows and selected state-changing Patsnap actions when the user confirms the payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include mutable remote installer scripts.

Mitigation: Install the oo CLI from a verified package or downloaded artifact and validate checksums or signatures before execution.

Risk: Actions tagged [write] can change Patsnap MCP state.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

Risk: Connector calls may send patent, image, or business analysis data to OOMOL and Patsnap services.

Mitigation: Check data sensitivity and sharing approval before submitting confidential or regulated information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-patsnap-mcp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Patsnap MCP homepage](https://open.patsnap.com/marketplace/mcp-servers)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON and may include data plus meta.executionId.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
