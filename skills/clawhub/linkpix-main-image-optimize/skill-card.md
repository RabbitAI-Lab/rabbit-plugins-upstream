## Description:

Guides an agent to use LinkPix/qhkit to improve ecommerce main product images by preserving the product while refining composition, lighting, texture, and detail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, operators, and image-production teams use this skill to have an agent optimize, refresh, or regenerate product main images for better commercial presentation and click-through appeal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or upgrade commands may modify the host Node/npm environment.

Mitigation: Review before installing and run only in environments where global npm changes are acceptable; prefer a scoped or npx-based execution path when global install permissions are not appropriate.

Risk: Image generation can upload local images and consume LinkPix/qhkit credits.

Mitigation: Before any generate action, require explicit user confirmation after listing the model, image count, dimensions or quality settings, reference images, and estimated credits.

Risk: Generative redraws may slightly change product details such as text, logos, or structure.

Mitigation: Have the user inspect generated images for key product details before using them commercially.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-optimize)
- [autoagc publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image jobs may return image URLs and credit usage through the qhkit CLI.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
