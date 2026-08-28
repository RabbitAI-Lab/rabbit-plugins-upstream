## Description:

Use when someone wants to upscale or sharpen an existing image for print, large crops, or higher-quality delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide an agent through uploading an existing source image, choosing upscale settings, and calling Pruna's p-image-upscale API to produce a higher-resolution or sharper image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images are sent to Pruna's external API.

Mitigation: Avoid uploading confidential, personal, or regulated images unless privacy, retention, and permission requirements have been reviewed.

Risk: The workflow requires PRUNA_API_KEY for API calls.

Mitigation: Use the key only through the runtime environment and avoid exposing it in prompts, logs, or shared command history.

## Reference(s):

- [p-image-upscale model docs](https://docs.api.pruna.ai/guides/models/p-image-upscale)
- [p-image-upscale on ClawHub](https://clawhub.ai/pruna-ai/skills/p-image-upscale)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with bash and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to upload source images, create Pruna predictions, poll for completion, and download image outputs.]

## Skill Version(s):

1.0.10 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
