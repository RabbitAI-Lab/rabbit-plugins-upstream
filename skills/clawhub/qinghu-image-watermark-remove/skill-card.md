## Description:

青虎AI 图片去水印 is an AI image watermark-removal skill that helps an agent remove watermarks, logos, text, and graphic marks from a single image while restoring affected background texture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare authorized image assets by removing visible watermarks, logos, or text through the Qinghu AI qhkit workflow. It is suited to single-image ecommerce material and social media image cleanup when the user has rights to edit the source image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Watermark, logo, or text removal can be misused on images the user does not own or have permission to edit.

Mitigation: Confirm the image is owned by the user or authorized for editing before running estimate or generate.

Risk: Generate jobs use a paid service and may consume more credits than the initial pre-deduction.

Mitigation: Run an estimate with the exact parameters, disclose the expected credit notice, and require explicit user approval before submitting the generate job.

Risk: The text-removal mode can remove intended product or design text in addition to watermarks.

Mitigation: Use the watermark-only mode unless the user clearly asks to remove image text, and confirm the selected mode before submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-image-watermark-remove)
- [autoagc publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Image URLs]

**Output Format:** [Markdown guidance with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submits one image per workflow job and returns generated image URLs after status polling completes.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
