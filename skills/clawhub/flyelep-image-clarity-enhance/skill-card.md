## Description:

Enhances one or more image URLs through the Flyelep AI Tool API and returns URLs for the clarified images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to enhance image clarity for single-image or batch workflows when they can provide public image URLs and a Flyelep API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local image uploads are converted into permanent public URLs.

Mitigation: Warn users before upload and proceed only when the image is not private, personal, confidential, or business-sensitive.

Risk: The skill sends selected images and a user-provided Flyelep API key to Flyelep.

Mitigation: Request the API key at runtime, avoid storing it, and use the skill only when sharing those images with Flyelep is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-image-clarity-enhance)
- [Flyelep open platform console](https://www.flyelep.cn/controlboard)
- [Flyelep image clarity enhance API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/imageClarityEnhance)
- [Flyelep file upload API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with HTTP, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns enhanced image URLs; batch results are comma-separated and should be presented as individual links.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
