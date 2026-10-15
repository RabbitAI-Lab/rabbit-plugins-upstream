## Description:

Helps cross-border sellers and content teams create short product-promotion videos from product images and selling points using Qinghu AI's video tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border sellers and content teams use this skill to plan and generate short, narrated product videos for social-commerce campaigns from product images and selling points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sharing an API key in chat could expose account credentials.

Mitigation: Provide the token through a protected environment variable or secret manager rather than chat.

Risk: Selected product images or other media are uploaded to the Qinghu service.

Mitigation: Review and approve media before upload; avoid sending sensitive assets.

Risk: Video generation consumes paid credits and submitted tasks cannot be canceled.

Mitigation: Confirm the chosen model, inputs, estimated credits, and other parameters before submitting a task.

Risk: Installing or running unpinned packages can change the local Node/npm environment.

Mitigation: Preinstall trusted, pinned tool versions in a controlled environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-grok-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report task status, generated video URLs, and credit usage.]

## Skill Version(s):

0.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
