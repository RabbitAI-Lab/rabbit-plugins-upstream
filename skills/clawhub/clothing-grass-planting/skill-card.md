## Description:

Guides agents in turning an outfit photo into social-media-style lifestyle images with a different model, pose, and setting while preserving the clothing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and merchants use the skill to plan and generate lifestyle promotional images of an existing outfit across different scenes, using an outfit photo and optionally a model or scene reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts may reproduce a reference person's identity, creating an unauthorized likeness or implied endorsement.

Mitigation: Use a real person's reference image only with clear authorization; do not portray generated images as their genuine endorsement or experience.

Risk: Prompts and reference images may be sent to the configured image provider.

Mitigation: Check the selected provider and obtain permission before submitting photos of real people or sensitive images.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Model flags](artifact/references/model-flags.md)
- [Provider CLI and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with image-generation prompts and bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated image files; review outfit fidelity and image authenticity before publication.]

## Skill Version(s):

1.0.21 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
