## Description:

AI-Image-Matting removes backgrounds from one or more user-provided images through the Flyelep AI Tool API and returns new image URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to remove image backgrounds, extract product subjects, and create transparent-background assets from public image URLs or uploaded local image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected images and a Flyelep API key to the Flyelep API.

Mitigation: Ask the user to provide the API key only at runtime and avoid storing it in files, examples, or persistent configuration.

Risk: Local image uploads may become externally hosted permanent URLs.

Mitigation: Avoid uploading sensitive images unless the user accepts that the uploaded file may remain available through an external hosted URL.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-ai-image-matting)
- [Flyelep open platform](https://www.flyelep.cn/controlboard)
- [Flyelep AI image matting API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/aiImageMatting)
- [Flyelep file upload API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON payloads and shell command examples; successful runs return image URLs as text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Flyelep secretKey at runtime and one or more image URLs or local image paths.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
