## Description:

Creates original scene images from text prompts and optionally edits a reference image to change a model, pose, or outfit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and commerce teams use this skill to generate scene imagery from descriptions or make focused changes to a reference image for product and editorial visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid image generation may incur unexpected charges.

Mitigation: Preview requests with --dry-run and confirm image size and batch count before paid calls.

Risk: Prompts and supplied local or linked reference images may be sent to dLazy or a configured third-party provider.

Mitigation: Do not provide private files or sensitive image URLs; check the selected provider and review bundled generator tasks before granting broad agent access.

## Reference(s):

- [Creative Scene on ClawHub](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider and CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands; generated images saved as JPEG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional reference images; image size, aspect ratio, and batch controls.]

## Skill Version(s):

1.0.24 (source: ClawHub release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
