## Description:

Guides an agent through Qinghu AI's paid qhkit workflow for removing watermarks, logos, graphics, or optional text from one authorized image, including estimation, confirmation, submission, polling, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to remove watermarks, logos, or text from authorized image assets through Qinghu AI. The workflow is suited to single-image e-commerce and media asset cleanup where the user confirms the selected mode and estimated credits before spending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are uploaded to Qinghu's service for processing.

Mitigation: Install and use the skill only when the user is comfortable sending the selected images to that service.

Risk: The workflow is paid and may spend Qinghu credits when generation is submitted.

Mitigation: Run an estimate first, present the quoted credit cost and key parameters, and wait for explicit user confirmation before submitting generation.

Risk: Removing watermarks from images may create copyright or authorization issues.

Mitigation: Use the skill only on images the user owns or is authorized to edit.

Risk: The output may not preserve the original image dimensions exactly.

Mitigation: Warn users with strict size requirements before submission and verify the returned image dimensions after completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-watermark-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands, JSON parameter examples, and generated image result URLs when the workflow completes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports final Qinghu credit consumption after successful completion; command stdout is expected to be single-line JSON.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
