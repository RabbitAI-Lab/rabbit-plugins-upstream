## Description:

Uses Qinghu AI through qhkit to upscale and sharpen a single image while preserving the original style and content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to upscale authorized product, portrait, scenery, print, or old-photo images with Qinghu AI. The workflow estimates paid credits, confirms the submission details with the user, submits one image at a time, and polls for resulting image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency setup may install global Node packages or download a Node runtime directly.

Mitigation: Install prerequisites through approved package-management processes and avoid global installs or direct runtime downloads unless the user or environment policy permits them.

Risk: The workflow uploads image inputs to Qinghu AI and can consume paid credits.

Mitigation: Use only authorized images, run an estimate first, disclose the selected application, fields, inputs, and expected credits, and wait for explicit user confirmation before generation.

Risk: The skill requires Qinghu API credentials for generation.

Mitigation: Provide only credentials intended for this workflow and avoid exposing tokens in chat, command history, or shared logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-upscale-detail)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline qhkit shell commands and JSON command examples; completed runs return image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, Qinghu API credentials, one input image, estimate before paid generation, explicit user confirmation before generate, and status polling after submission.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
