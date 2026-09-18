## Description:

Y.GY lets agents operate the Y.GY short-link service through the OOMOL-connected oo CLI for reading, creating, updating, and deleting links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Y.GY connector schemas and operate short links through an OOMOL-connected account. It supports listing and retrieving links, creating links with QR, security, and routing options, and updating or deleting links with confirmation controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance suggests executing remote installer scripts directly in a shell.

Mitigation: Review the installer source before running it, or use a safer package-manager or manual installation path when available.

Risk: Write and destructive actions can change or delete Y.GY short links.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running create, update, or delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-y-gy)
- [Y.GY homepage](https://app.y.gy)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes action names, confirmation guidance for write and destructive actions, and setup troubleshooting.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
