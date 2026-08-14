## Description:

TRIGGERcmd lets an agent inspect TRIGGERcmd action schemas, list available commands, and trigger saved commands through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate TRIGGERcmd through an OOMOL-connected account, including listing available commands and triggering saved commands on named computers after reviewing the action schema and payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger user-configured remote commands on connected machines.

Mitigation: Review the target computer, command name, and parameters before approving trigger_command, and require explicit confirmation for write actions.

Risk: First-time setup may install or authenticate the oo CLI before TRIGGERcmd operations can run.

Mitigation: Run setup only after an auth, connection, or missing-command failure, and verify the oo CLI installer before first-time setup.

## Reference(s):

- [TRIGGERcmd homepage](https://www.triggercmd.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-triggercmd)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before command execution; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
