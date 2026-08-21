## Description:

Helps agents analyze a reference ecommerce product detail page and generate similarly structured product-detail images for the user's own product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce creators use this skill when they want an agent to follow a competitor or reference product-detail page layout and visual style while replacing the product and copy with their own materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit or Node on the host.

Mitigation: Run it in a controlled environment with qhkit already provisioned, or require explicit approval before any host-level installation or upgrade.

Risk: The skill may reuse an existing root-stored OpenClaw qinghu API credential.

Mitigation: Confirm credential use with the user and prefer scoped environment credentials when available.

Risk: Image generation can consume paid credits.

Mitigation: Run an estimate when supported and require user confirmation of key parameters and expected credit use before submitting generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-detail-page-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent through image-generation estimates, user confirmation, command execution, and delivery of generated image URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
