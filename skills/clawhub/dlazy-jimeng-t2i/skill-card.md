## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images. 使用即梦 (Jimeng) 进行文生图创作，快速将文字转化为高质量图像。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to create images from text prompts with Jimeng, optionally providing reference images and selecting output dimensions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan has partial coverage and flags a mismatch between the image-generation description and reported login behavior.

Mitigation: Review the CLI login flow and the available referenced material before installing, as advised by the scan guidance.

Risk: Prompts and parameters are sent to dLazy's hosted API, and local reference images are uploaded to its media storage.

Mitigation: Send only prompts and images that are appropriate to share with the hosted service.

Risk: The skill requires a dLazy API key, which the CLI stores in its user configuration when using the login flow.

Mitigation: Keep the API key private and rotate or revoke it through the dLazy dashboard if needed.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [JSON with generated image URLs and metadata; generated images are hosted files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local save path; asynchronous requests may return a task ID before the image is ready.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
