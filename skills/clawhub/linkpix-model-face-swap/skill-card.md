## Description:

This skill guides an agent to use LinkPix qhkit workflows to replace models or faces in ecommerce product images and videos while preserving clothing, pose, composition, and lighting for localized product presentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to localize ecommerce product media by replacing a model or face in images and videos through LinkPix qhkit workflows. The skill directs agents to confirm authorization for real likenesses and to have users review generated product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to install and run a mutable third-party npm CLI while handling user media and service tokens.

Mitigation: Review before installing, prefer a pinned trusted qhkit version, and use an isolated or project-local environment.

Risk: User media and QHKIT_TOKEN values may be sent to the LinkPix service during execution.

Mitigation: Only provide media and token values that are authorized for this service and avoid submitting sensitive or unauthorized likenesses.

Risk: Generative face or model replacement can alter product details such as text, logos, or structure.

Mitigation: Require user review of generated outputs before publication or commercial use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-model-face-swap)
- [AutoAGC Publisher Profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce image or video result URLs through qhkit command output when the agent executes the workflow.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
