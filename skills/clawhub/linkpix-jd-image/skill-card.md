## Description:

Helps JD ecommerce operators, advertising optimizers, and brand teams use LinkPix/qhkit to generate JD product main images, carousel sets, detail images, white-background images, retouched product visuals, premium posters, marketing key visuals, multi-angle displays, and 3C/home-appliance parameter images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, advertising teams, and brand teams use this skill to prepare JD-compatible product images, detail pages, and promotional campaign visuals. The skill guides agents through qhkit option lookup, cost estimation, user confirmation, generation, polling, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request an API key for a paid external image-generation service.

Mitigation: Use a secure secret mechanism when available, avoid pasting keys into normal chat, and verify the qhkit configuration before generation.

Risk: The skill includes broad local setup steps for npm, Node, pip, npx, PATH, and shell-profile changes.

Mitigation: Review proposed installation and environment changes before execution, and install qhkit only in environments approved for LinkPix use.

Risk: Image generation can consume paid credits once generation commands are submitted.

Mitigation: Run qhkit estimate first and require explicit user approval of model, image count, size, quality, reference images, and estimated credits before submitting generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-jd-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit command plans, configuration steps, estimate requests, generation requests, status handling guidance, and final image delivery instructions.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
