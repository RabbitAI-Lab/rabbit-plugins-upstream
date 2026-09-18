## Description:

TRIGGERcmd helps agents list available TRIGGERcmd commands and trigger saved commands through the OOMOL oo CLI with managed account credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect TRIGGERcmd connector schemas, list saved commands, and trigger commands on named computers from an OOMOL-connected account. Write actions should be confirmed with the user before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents direct execution of a remote installer.

Mitigation: Prefer an official verified package when available, or inspect and verify the installer before running it.

Risk: The trigger_command action can run saved commands on a connected computer.

Mitigation: Confirm each trigger_command request, including target computer, command name, parameters, and expected effect, before execution.

Risk: TRIGGERcmd actions are mediated through OOMOL-managed account credentials.

Mitigation: Install only when the user is comfortable with OOMOL mediating these actions and reviewing setup manually.

## Reference(s):

- [TRIGGERcmd ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-triggercmd)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [TRIGGERcmd Homepage](https://www.triggercmd.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before actions; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
