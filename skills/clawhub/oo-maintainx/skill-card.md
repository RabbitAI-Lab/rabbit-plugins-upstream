## Description:

MaintainX enables agents to read, create, update, and delete MaintainX data through the OOMOL oo CLI and a connected MaintainX account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate MaintainX locations, users, work orders, statuses, and comments from an agent-connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can require running remote installer scripts for the oo CLI.

Mitigation: Review the installer path first and prefer a verified package, pinned release, checksum, or signed installer.

Risk: Create, update, and delete actions can change MaintainX records.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub MaintainX Skill](https://clawhub.ai/oomol/skills/oo-maintainx)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [MaintainX Homepage](https://www.getmaintainx.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
