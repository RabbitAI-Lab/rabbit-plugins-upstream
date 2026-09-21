## Description:

Canva (canva.com). Use this skill for reading, creating, and updating Canva data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Canva through the oo CLI, including creating designs, exporting designs, uploading URL assets, reading design and asset metadata, and organizing folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that execute downloaded scripts directly.

Mitigation: Use a verified installation path, review the installer source, and confirm the CLI source before running installer commands.

Risk: Some Canva connector actions create designs, folders, exports, uploads, or move folder items.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Canva homepage](https://www.canva.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Canva skill page](https://clawhub.ai/oomol/skills/oo-canva)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions can change Canva state and should be confirmed with the user before execution.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
