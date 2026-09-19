## Description:

Make connector for reading and managing Make scenarios through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Make account context, list and view scenarios, check recent usage, activate or deactivate scenarios, and run a scenario once with appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that may execute unaudited shell or PowerShell code.

Mitigation: Review the oo CLI installation path before installing, prefer a verified or package-manager route when available, and do not allow an agent to run pipe-to-shell commands automatically.

Risk: Activating, deactivating, or running Make scenarios can change scenario state or trigger automations.

Mitigation: Inspect the live action schema, confirm the exact target and payload with the user, and require explicit approval before write, destructive, or run-once actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-make)
- [Make homepage](https://www.make.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before connector actions; state-changing actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
