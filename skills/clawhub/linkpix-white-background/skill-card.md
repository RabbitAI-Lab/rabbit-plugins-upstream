## Description:

Generates clean white-background ecommerce product images in batches by removing cluttered backgrounds through LinkPix/qhkit image editing commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agent users use this skill to prepare marketplace product images with clean white backgrounds, including batch processing through qhkit/LinkPix.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential setup can expose qhkit API keys if users paste secrets into chat or logs.

Mitigation: Use qhkit config or QHKIT_TOKEN locally, avoid sharing API keys in conversation, and review credential handling before installation.

Risk: Product images are uploaded to the qhkit/LinkPix service for generation.

Mitigation: Confirm that uploaded images are appropriate for the service before processing and avoid submitting sensitive product media without approval.

Risk: Generation consumes credits and may alter product details because the workflow uses generative image editing.

Mitigation: Run estimate before generate, require user confirmation before credit-consuming actions, and review final images for text, logos, and product structure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-white-background)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local setup steps, qhkit estimates, generation commands, and delivery guidance for white-background product image outputs.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
