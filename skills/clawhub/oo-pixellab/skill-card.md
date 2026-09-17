## Description:

PixelLab helps agents operate PixelLab through the OOMOL-connected oo CLI to read, create, update, delete, generate, edit, convert, animate, and manage pixel-art assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, artists, and agents use this skill to inspect PixelLab action schemas and run validated PixelLab connector actions for pixel-art image generation, editing, conversion, animation, asset retrieval, and asset management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an unverified remote installer that executes downloaded code locally.

Mitigation: Review the setup path before installation, trust the OOMOL installer endpoint before use, and prefer a signed or checksum-verified installation method when available.

Risk: PixelLab actions can create, update, delete, or overwrite persisted assets.

Mitigation: Confirm exact payloads and effects before write actions, and require explicit approval for destructive actions.

## Reference(s):

- [PixelLab homepage](https://www.pixellab.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pixellab)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON payloads and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs PixelLab connector actions through the oo CLI and may return JSON responses, generated asset references, balances, job status, or exported files.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
