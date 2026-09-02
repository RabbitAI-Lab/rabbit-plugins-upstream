## Description:

Uses Qinghu AI's qhkit workflow to process a single AI-generated image into a more realistic, high-definition version with improved detail, consistency, and reduced synthetic-looking artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users invoke this skill when a user wants a non-portrait image to look less AI-generated, less glossy or distorted, and more realistic while preserving the subject. The workflow estimates credit cost, asks for explicit approval before paid submission, then polls for generated image results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may upload local image files to Qinghu for processing.

Mitigation: Install and use the skill only when the user intends to process images with Qinghu AI, and remind users to provide only images they own or are authorized to process.

Risk: Submitting a generation job can consume Qinghu credits and may require an API key or subscription entitlement.

Mitigation: Run an estimate first, present the expected cost and submitted parameters, and wait for explicit user approval before invoking generate.

Risk: Large images or changing online workflow fields can cause failed submissions or incorrect parameters.

Mitigation: Check live workflow options before uncertain submissions and compress images over the documented size limit before one retry.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-deai-hd)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, Files]

**Output Format:** [Markdown guidance with qhkit shell commands and returned image URLs or files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload a local image to Qinghu through qhkit, consume Qinghu credits after explicit approval, and return one or more generated image results.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
