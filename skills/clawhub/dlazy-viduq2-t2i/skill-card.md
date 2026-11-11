## Description:

Generate high-quality images with Vidu Q2, including text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images with Vidu Q2 from text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan noted unresolved references and broad activation wording, and could not establish how the login step relates to image generation.

Mitigation: Review the linked CLI package and authentication behavior before using the skill with an API key.

Risk: The skill sends prompts to dLazy's hosted API and uploads supplied local reference media to its media storage.

Mitigation: Avoid sending sensitive material unless your policies allow it, and review the service terms before use.

## Reference(s):


## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response with generated image URLs and metadata; image files can optionally be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports text-to-image and image-to-image generation.]

## Skill Version(s):

1.3.39 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
