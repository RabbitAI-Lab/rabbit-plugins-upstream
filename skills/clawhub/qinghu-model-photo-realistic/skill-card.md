## Description:

Qinghu/LinkPix model-photo enhancement skill for removing AI-like appearance, brightening skin tone, restoring realistic skin texture, repairing details, and producing high-resolution upscaled portrait or e-commerce model images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run a Qinghu/LinkPix workflow that makes authorized model or portrait images look more realistic for e-commerce use. The skill guides setup, estimate confirmation, generation, polling, and delivery of resulting image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and uses a third-party npm CLI that may change over time.

Mitigation: Review the CLI before deployment and prefer a pinned, reviewed version when available.

Risk: The CLI handles API-token configuration and uploads model photos to Qinghu/LinkPix.

Mitigation: Protect tokens, use only authorized portrait or model images, and confirm provider handling is acceptable for the intended use.

Risk: The workflow is a paid, subscription-oriented image generation service.

Mitigation: Run an estimate with the exact generation parameters and get user confirmation before submitting the job.

Risk: The workflow is tuned for model and portrait images and may produce poor results for product or scenery images.

Mitigation: Confirm the input image type before use and route non-portrait enhancement requests to a more suitable skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-model-photo-realistic)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs after the external workflow completes; credit usage is reported from the workflow status response.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
