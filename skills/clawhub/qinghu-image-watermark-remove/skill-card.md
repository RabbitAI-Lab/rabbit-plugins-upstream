## Description:

青虎AI 图片去水印 is an AI image workflow skill that helps remove full-image, local logo, text, and graphic watermarks from a single image while attempting to restore background texture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to route authorized image watermark or text removal requests through the Qinghu AI qhkit workflow, including estimation, user confirmation, job submission, polling, and result delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be used to remove copyright, attribution, or ownership marks from third-party images.

Mitigation: Use it only with self-owned or authorized images, and confirm rights before commercial use.

Risk: Local images are uploaded to the qhkit service for processing.

Mitigation: Avoid submitting sensitive images unless the user accepts the third-party processing and privacy implications.

Risk: The workflow is paid and credits can vary by image size.

Mitigation: Run an estimate first, disclose the quoted credits, and wait for explicit user approval before submitting a generation job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-watermark-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with qhkit shell commands, JSON parameters, and result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow processes one image per job and returns generated image URLs after polling; final credits should be reported from the completed status response.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
