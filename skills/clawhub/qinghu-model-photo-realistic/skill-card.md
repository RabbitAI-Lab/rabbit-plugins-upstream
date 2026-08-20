## Description:

青虎AI 模特图去 AI 感超写实：上传模特图一键去除 AI 感，提亮肤色、修复细节、还原真实皮肤质感并做高清超分，专为电商模特图优化设计。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents handling authorized e-commerce model or portrait photos use this skill to quote, submit, poll, and deliver Qinghu image-processing results that reduce AI-like skin artifacts, brighten skin, repair detail, and upscale the image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads model or portrait photos to an external paid image-processing service.

Mitigation: Use only images the user owns or has permission to process, and confirm the quoted credits before generation.

Risk: The qhkit CLI may store or read a Qinghu API token for future use.

Mitigation: Use the documented token configuration path or environment variable intentionally, and avoid exposing the token in prompts, logs, or shared files.

Risk: The skill is tuned for model and portrait photos, not product-only or scene images.

Mitigation: Route non-portrait images to a more appropriate Qinghu workflow before spending credits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-model-photo-realistic)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides qhkit workflow calls that return one-line JSON status data and image result URLs after polling.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
