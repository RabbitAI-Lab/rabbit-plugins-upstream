## Description:

Daytona (daytona.io) support for reading, creating, updating, and deleting Daytona resources through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Daytona sandboxes through the OOMOL-connected oo CLI. It helps inspect live action schemas and perform read, write, and destructive sandbox actions with confirmation controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can ask the agent to run an unverified remote installer on the user's machine.

Mitigation: Review setup instructions before installing; prefer a verified package manager or documented installer with integrity checks.

Risk: Write and destructive Daytona actions can change or delete sandbox state.

Mitigation: Confirm the exact sandbox, payload, and expected effect with the user before allowing write or destructive actions.

## Reference(s):

- [ClawHub Daytona Skill](https://clawhub.ai/oomol/skills/oo-daytona)
- [Daytona Homepage](https://www.daytona.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector commands; write and destructive Daytona actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
