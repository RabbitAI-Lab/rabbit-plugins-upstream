## Description:

PixelLab helps agents operate PixelLab through the OOMOL-connected oo CLI for reading, creating, updating, deleting, generating, editing, converting, and animating pixel-art assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to inspect PixelLab action schemas and run PixelLab connector actions for generating, editing, converting, animating, and managing pixel-art assets through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says first-time setup includes an unverified remote installer script.

Mitigation: Install the oo CLI through a verified method the user trusts and review installer commands before execution.

Risk: The skill can run PixelLab actions that create, update, remove, or overwrite account data.

Mitigation: Confirm the exact payload, target resource, and expected effect with the user before write or destructive actions.

## Reference(s):

- [PixelLab homepage](https://www.pixellab.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub PixelLab skill](https://clawhub.ai/oomol/skills/oo-pixellab)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before payload construction; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
