## Description:

Creates social-commerce outfit images by keeping an outfit while changing the model, pose, scene, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and social-commerce creators use the skill to turn an outfit photo, optionally with a model or scene reference, into lifestyle-style promotional images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input photos and prompts are sent to the selected cloud provider.

Mitigation: Use only images you are authorized to upload and review the selected provider's privacy terms.

Risk: Image-generation requests may spend credits or overwrite existing output files.

Mitigation: Choose the intended provider, inspect the request with --dry-run, and save to a separate output path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider CLI reference](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Shell commands]

**Output Format:** [JPEG image files and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Portrait-oriented social-commerce imagery; outfit details are intended to remain consistent while the model, pose, scene, and lighting change.]

## Skill Version(s):

1.0.24 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
