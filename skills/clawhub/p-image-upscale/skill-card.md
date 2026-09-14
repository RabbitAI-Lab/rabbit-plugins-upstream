## Description:

Use when someone wants to upscale or sharpen an existing image for print, large crops, or higher-quality delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative production agents use this skill to upscale or sharpen an existing image with Pruna's p-image-upscale model for print, large crops, or higher-quality delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and requests are sent to Pruna's API using PRUNA_API_KEY.

Mitigation: Use only with images approved for Pruna processing and confirm credential handling before upload.

Risk: Repeated unpinned npx skills add commands with non-interactive -y installs create supply-chain review risk.

Mitigation: Review the referenced skills and prefer pinned versions or reviewed commit hashes before installation.

## Reference(s):

- [p-image-upscale model docs](https://docs.api.pruna.ai/guides/models/p-image-upscale)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with curl examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY and an input image URL; generated image outputs are produced by Pruna's API.]

## Skill Version(s):

1.0.12 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
