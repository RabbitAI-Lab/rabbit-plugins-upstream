## Description:

apaleo (apaleo.com). Use this skill for ANY apaleo request: reading, creating, updating, and deleting data through the OOMOL apaleo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate apaleo property, unit, unit group, and unit attribute workflows through an OOMOL-connected account. It supports read operations and controlled write or destructive actions after schema inspection and user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that can execute code from a network URL.

Mitigation: Install only from trusted OOMOL sources and prefer a versioned installer with checksum or signature verification.

Risk: Write and destructive apaleo actions can change or delete business data.

Mitigation: Confirm the exact target, payload, and expected effect before execution; use least-privilege or test accounts where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-apaleo)
- [apaleo homepage](https://apaleo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before running apaleo actions.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
