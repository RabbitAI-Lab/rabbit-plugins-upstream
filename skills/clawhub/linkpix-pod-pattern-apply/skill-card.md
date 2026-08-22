## Description:

LinkPix helps agents create realistic POD mockup images by applying print designs to apparel, hats, mugs, cups, and other product photos with natural perspective, folds, lighting, and placement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce and POD operators use this skill to generate product mockups that show a supplied print design on garments, hats, mugs, or similar carrier products. Agents use it to prepare qhkit image-generation requests, confirm cost-bearing parameters with the user, and return generated mockup image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product or design reference images are uploaded to the qhkit service during generation.

Mitigation: Use only images the user is comfortable sending to the service, and avoid sensitive or confidential assets.

Risk: Generation can spend credits after submission.

Mitigation: Confirm the model, image count, size, reference images, and estimated credits with the user before running a generation request.

Risk: Generative redraws may alter print details, placement, or colors.

Mitigation: Review the generated mockup before using it commercially, especially key design elements and brand colors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-apply)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON request parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and credit usage after a user-confirmed qhkit generation request.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
