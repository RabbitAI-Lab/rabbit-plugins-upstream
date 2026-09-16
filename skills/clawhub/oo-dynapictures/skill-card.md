## Description:

DynaPictures helps agents inspect templates, retrieve template details, and generate hosted images through an OOMOL-connected DynaPictures account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate DynaPictures via the OOMOL-connected oo CLI, including listing API-ready templates, retrieving template layers, and generating hosted images from templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image generation can create hosted output and may consume account credits.

Mitigation: Require clear user intent and confirm payload details before running generation actions.

Risk: The setup guidance includes pipe-to-shell installer commands.

Mitigation: Prefer a signed or checksum-verified installation path and run installer commands only after independently trusting the source.

## Reference(s):

- [DynaPictures homepage](https://dynapictures.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL DynaPictures connection](https://console.oomol.com/app-connections?provider=dynapictures)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dynapictures)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs, template metadata, and connector execution IDs from DynaPictures actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
