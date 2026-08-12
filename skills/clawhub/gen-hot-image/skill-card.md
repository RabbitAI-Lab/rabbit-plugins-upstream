## Description:

Uses the Flyelep hot-image replication API to generate product images in the visual style of provided reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare Flyelep API calls that blend product image URLs into the visual style of reference images and retrieve asynchronous image-generation results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, reference images, prompts, and API credentials are sent to Flyelep as part of the intended API workflow.

Mitigation: Use only data that is appropriate to share with Flyelep, provide API keys at runtime, and avoid submitting confidential product assets or sensitive prompts.

Risk: Temporary payload files can contain image URLs, prompts, and request parameters when the Windows workflow is used.

Mitigation: Delete temporary payload files after the API request completes and avoid storing real API keys in files or persistent configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/gen-hot-image)
- [Flyelep generateHotImage API](https://www.flyelep.cn/prod-api/poster-design/api/v1/aiTool/generateHotImage)
- [Flyelep queryTaskResult API](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/queryTaskResult)
- [Flyelep controlboard](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns task identifiers first and generated image URLs after polling.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
