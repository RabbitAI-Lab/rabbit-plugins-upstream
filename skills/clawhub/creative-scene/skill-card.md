## Description:

Helps create original images from scene descriptions and make targeted changes to models, poses, or outfits using optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and e-commerce teams use the skill to draft image prompts and generate scene or product imagery, with optional reference images for focused edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud image generation may upload prompts and supplied reference images, including sensitive local files or private image URLs.

Mitigation: Do not supply confidential files or private/internal image URLs; confirm the chosen provider before generating.

Risk: Image generation can consume paid credits, especially when generating batches or larger images.

Mitigation: Use --dry-run first to inspect the request and estimated cost, then choose size and batch count deliberately.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider setup and output reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Text prompts, Shell commands, Image files]

**Output Format:** [Text guidance and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional reference images; output size, aspect ratio, and batch count are configurable.]

## Skill Version(s):

1.0.20 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
