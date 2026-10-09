## Description:

Helps commerce and brand teams create promotional videos with Happy Horse 1.1 through 青虎AI, using text prompts and optional reference media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, brand teams, and content creators use this skill to plan and generate product showcases and short promotional videos from prompts and optional images, video, or audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can prompt users to share an API key in chat.

Mitigation: Configure QHKIT_TOKEN locally instead of sending the key in chat.

Risk: Installation or upgrades may run unpinned npm tooling.

Mitigation: Review the qhkit package source and version before installing or upgrading.

Risk: Generation uploads selected media and can consume credits.

Mitigation: Confirm the exact media, generation parameters, and estimated credits before submitting a task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-happyhorse-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [青虎AI API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report a task ID, generated video URL, and credits spent after execution.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
