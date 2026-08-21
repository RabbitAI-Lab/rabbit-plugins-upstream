## Description:

Enhances one non-portrait AI-generated image with Qinghu AI to reduce artificial-looking artifacts, improve realism, sharpen details, and return one or more candidate outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run a Qinghu AI image-enhancement workflow for AI-generated images that look overly synthetic, oily, distorted, blurry, or visually inconsistent. The skill guides setup, estimation, explicit paid-generation approval, polling, and delivery of the resulting image candidates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected image is uploaded to Qinghu for processing.

Mitigation: Use the workflow only with images the user owns or is authorized to process, and disclose the upload before proceeding.

Risk: Paid generation may spend Qinghu credits.

Mitigation: Run an estimate first, report the expected credits or credits notice, and submit generation only after explicit user approval.

Risk: The workflow depends on a Qinghu API token and qhkit CLI configuration.

Mitigation: Use the documented qhkit configuration flow and avoid exposing tokens in responses, logs, or shared files.

Risk: The workflow is intended mainly for non-portrait images and may be a poor fit for model or portrait skin-texture restoration.

Mitigation: Route portrait or model-image requests to the dedicated portrait-oriented Qinghu skill when that is the user's goal.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-deai-hd)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and one-line JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return multiple image candidates; generation requires status polling after submission.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
