## Description:

The MX skill helps agents operate MX through an OOMOL-connected account, inspect connector schemas, and run MX user management actions with confirmation for write or destructive operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent list, read, create, update, and delete MX Platform API users through the OOMOL oo CLI connector. It is suited for MX account workflows where the agent must inspect live schemas before constructing payloads and get confirmation before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified remote installer commands that could run arbitrary local code.

Mitigation: Review the oo CLI installation path before use and prefer a trusted, documented, verifiable CLI release instead of piping a remote script directly into a shell.

Risk: MX create, update, and delete actions can change or remove user data.

Mitigation: Require explicit user confirmation for the exact target, payload, and expected effect before running write or destructive MX actions.

## Reference(s):

- [ClawHub MX skill page](https://clawhub.ai/oomol/skills/oo-mx)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [MX homepage](https://www.mx.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect the live connector schema before building action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
