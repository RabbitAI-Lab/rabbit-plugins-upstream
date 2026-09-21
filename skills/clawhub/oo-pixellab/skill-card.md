## Description:

PixelLab (pixellab.ai). Use this skill for PixelLab requests that read, create, update, or delete PixelLab data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, artists, and teams use this skill to operate PixelLab through a connected OOMOL account for pixel-art image generation, conversion, editing, animation, asset retrieval, and asset management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can run a remote installer for the OOMOL oo CLI.

Mitigation: Review or install the CLI manually from a trusted source before allowing an agent to execute setup commands.

Risk: PixelLab write and destructive actions can modify, overwrite, or delete persisted assets.

Mitigation: Require explicit user confirmation for the exact action, target, payload, and expected effect before running write or destructive actions.

Risk: The skill operates through an OOMOL-connected PixelLab account with server-side credentials.

Mitigation: Install only when the user is comfortable granting the connector access to their PixelLab account and review account permissions, billing, and connection state before use.

## Reference(s):

- [PixelLab homepage](https://www.pixellab.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pixellab)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke the oo CLI to call PixelLab connector actions and return JSON responses, generated image asset references, transit files, or job status details.]

## Skill Version(s):

1.0.3 (source: server metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
