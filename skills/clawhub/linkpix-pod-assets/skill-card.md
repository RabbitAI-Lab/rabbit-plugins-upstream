## Description:

Generates POD ecommerce design assets for sellers, including print extraction, pattern variations, mockup fitting, and product visuals across apparel, home goods, and accessories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External POD sellers and ecommerce operators use this skill to plan qhkit image-generation workflows for extracting prints, creating design variants, fitting designs onto products, and producing listing mockups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad POD-related requests may activate an external image-generation CLI that can use credentials, upload local images, and consume credits.

Mitigation: Review before installation and require explicit user confirmation for setup changes, credential use, local image uploads, and credit-consuming generation.

Risk: Generated print or mockup outputs may differ from source details, and commercial use of copied or branded designs can create IP risk.

Mitigation: Have users review key design elements after generation and confirm they have rights to any source pattern, brand, or reference image before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with qhkit shell command examples and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include local image paths, model labels, image counts, size presets, estimate results, generated image URLs, and credit usage when the agent executes the external CLI workflow.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
