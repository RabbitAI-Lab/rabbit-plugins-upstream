## Description:

Routes e-commerce image requests to LinkPix/qhkit modes for product hero images, carousel image sets, detail-page long images, and prompt- or reference-based commercial image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to help an agent select the right LinkPix image mode, prepare qhkit commands, estimate credits, request confirmation, and return generated e-commerce image links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may direct agents to install or upgrade Node/qhkit automatically.

Mitigation: Review installation steps before deployment and run the skill only in environments where agent-managed Node and qhkit installs are allowed.

Risk: The skill may reuse an existing OpenClaw qhkit configuration or persist qhkit tokens.

Mitigation: Use dedicated qhkit credentials, limit token scope where possible, and avoid deploying in environments where persisted qhkit tokens are not acceptable.

Risk: The skill uploads product images to the qhkit service and can spend account credits after user confirmation.

Mitigation: Use it only when external image processing is acceptable and require the documented estimate-and-confirm step before any generation request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ecom-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON responses, credit estimates, and generated image URLs after user-confirmed generation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
