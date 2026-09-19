## Description:

Use when someone wants to upscale or sharpen an existing image for print, large crops, or higher-quality delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to collect a source image and target settings, then call Pruna's p-image-upscale API to upscale or sharpen images for print, large crops, or higher-quality delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends the selected image to Pruna's API.

Mitigation: Use the skill only with images that are approved for transfer to Pruna, and avoid regulated or sensitive images unless that transfer is permitted.

Risk: The workflow requires PRUNA_API_KEY for API requests.

Mitigation: Keep the API key in environment configuration or a secret manager, and avoid pasting it into prompts, logs, or shared files.

Risk: The documented installation commands can pull referenced Pruna skill versions at install time.

Mitigation: Review or pin the referenced Pruna skill versions before installation in stricter environments.

## Reference(s):

- [p-image-upscale model docs](https://docs.api.pruna.ai/guides/models/p-image-upscale)
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-upscale)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with curl command examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY and a user-provided image URL; may upload the selected image to Pruna's API.]

## Skill Version(s):

1.0.13 (source: server release metadata, released 2026-09-17; artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
