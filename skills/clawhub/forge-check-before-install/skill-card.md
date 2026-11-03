## Description:

Checks skill, plugin, MCP server, or README install text with The Agent Forge scanner and reports the verdict and matched rule locations before the user decides whether to install.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dinikejayamaha-hash](https://clawhub.ai/user/dinikejayamaha-hash)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill before installing or updating skills, plugins, or MCP servers, or running install commands from README files. It submits selected installation material to The Agent Forge scanner and reports its verdict and matched locations so the user can decide what to install.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected installation material is sent to an external scanner whose privacy and retention practices could not be independently verified.

Mitigation: Submit only public or non-sensitive material; never include secrets.

Risk: A clear scan does not guarantee that the material is safe.

Mitigation: Treat the verdict as one input, review the material, and make the installation decision yourself.

## Reference(s):

- [The Agent Forge scanner](https://theagentforge.io/scan)
- [ClawHub skill listing](https://clawhub.ai/dinikejayamaha-hash/skills/forge-check-before-install)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the scanner verdict, matched rule IDs, and line numbers; the user decides whether to install.]

## Skill Version(s):

1.0.0 (source: frontmatter; release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
