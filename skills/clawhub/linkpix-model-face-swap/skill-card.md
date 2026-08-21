## Description:

Helps agents use LinkPix through qhkit to replace ecommerce model faces in images or videos while preserving clothing, pose, and scene context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to prepare localized product images or videos by swapping model faces through LinkPix/qhkit. It is intended for authorized likeness use and includes confirmation before credit-consuming generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may direct agents to make persistent host runtime changes when qhkit, Node, or npm dependencies are missing.

Mitigation: Review before installing, prefer pre-provisioned Node and qhkit managed by the deployment environment, and restrict use to hosts where runtime modification is authorized.

Risk: Face replacement can misuse a real person's likeness or consume LinkPix credits without adequate user awareness.

Mitigation: Require authorization for real-person likeness use and confirm key generation parameters and estimated credits before submitting any generate task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-face-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image or video URLs from qhkit task results.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
