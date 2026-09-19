## Description:

Formsite connector for reading, creating, updating, and deleting Formsite data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Formsite account through the OOMOL oo CLI, including listing forms, retrieving form details and results, and managing webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that can execute changing code on a user's machine.

Mitigation: Use an already installed, trusted oo CLI when possible, or verify the installer source and prefer a signed or version-pinned installation method before running installer commands.

Risk: Write and destructive Formsite actions can change or delete webhook configuration.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-formsite)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Formsite homepage](https://www.formsite.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs direct oo CLI commands and safety guidance for read, write, and destructive Formsite actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
