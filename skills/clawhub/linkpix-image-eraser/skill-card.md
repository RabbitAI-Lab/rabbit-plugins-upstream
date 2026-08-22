## Description:

智能擦除商品图片中的人物、水印、文字及杂物，并自动补全背景，完成商品修图与素材优化。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to remove selected watermarks, text, people, or clutter from product images through LinkPix/qhkit image inpainting workflows. The skill guides setup, option checks, cost confirmation, generation, and delivery review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are uploaded to the qhkit/LinkPix service for editing.

Mitigation: Use the skill only with images that are appropriate to send to that service, and avoid submitting sensitive or restricted content.

Risk: Generation can spend LinkPix credits after task submission.

Mitigation: Run estimates when available and require explicit user confirmation of model, image count, size, reference images, and expected credits before generation.

Risk: Generated inpainting may alter product details, text, logos, or other rights-sensitive areas.

Mitigation: Review outputs before use, especially for product accuracy, branding, text, logos, watermark removal, and other rights-sensitive edits.

## Reference(s):

- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-eraser)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON responses, generated image URLs, confirmation prompts, and credit usage details.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
