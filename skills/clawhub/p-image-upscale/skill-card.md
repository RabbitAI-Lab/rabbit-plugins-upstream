## Description:

Use when someone wants to upscale or sharpen an existing image for print, large crops, or higher-quality delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through upscaling or sharpening an existing image with Pruna's p-image-upscale API. It is aimed at print preparation, large crops, and higher-quality image delivery after a source image has already been selected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends source images to Pruna's external API under the user's API key.

Mitigation: Do not upload confidential or sensitive images unless the user is comfortable sending them to Pruna under their own API key.

Risk: The skill suggests installing related Pruna skills with mutable npx targets.

Mitigation: Install only the related skills needed for the task and review install targets before running them.

Risk: Detail or realism enhancement settings can change the visual character of the source image.

Mitigation: Confirm target megapixels, output format, and enhancement settings before running the upscale, and reserve realism enhancement for already-photoreal sources.

## Reference(s):

- [p-image-upscale model docs](https://docs.api.pruna.ai/guides/models/p-image-upscale)
- [p-image-upscale ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-upscale)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl examples and concise configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Pruna API upload, prediction creation, polling, and download steps.]

## Skill Version(s):

1.0.11 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
