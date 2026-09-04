## Description:

Uses the Flyelep hot-image replication API to generate product images that follow the style of reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit product images and reference images to Flyelep, poll the asynchronous task, and present generated product image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product and reference images, plus the Flyelep API key, are sent to a third-party service.

Mitigation: Use the skill only with images and credentials approved for Flyelep processing, and provide the API key only at runtime.

Risk: Local image uploads may become permanently accessible through public URLs.

Mitigation: Do not upload confidential, personal, or unreleasable images unless permanent public hosting is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/gen-hot-image)
- [Flyelep controlboard](https://www.flyelep.cn/controlboard)
- [Flyelep generateHotImage API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/aiTool/generateHotImage)
- [Flyelep queryTaskResult API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/queryTaskResult)
- [Flyelep file upload API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Markdown, Guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces asynchronous task IDs and generated image URLs; local image uploads may create public externally hosted URLs.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
