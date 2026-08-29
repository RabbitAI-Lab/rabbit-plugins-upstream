## Description:

Generates multiple POD print-pattern design variations from a reference image, including color, style, theme, and element-composition variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External POD sellers, designers, and agent users use this skill to turn one print pattern into a family of related designs for SKU expansion, colorway exploration, seasonal themes, and element-density variations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if a user pastes raw credentials into chat or stores them insecurely.

Mitigation: Prefer QHKIT_TOKEN or qhkit credential configuration through a trusted secret-management mechanism; avoid sharing raw keys and revoke or remove credentials when finished.

Risk: Reference images may be uploaded to an external LinkPix/qhkit service during image generation.

Mitigation: Use only images approved for that service and review privacy, intellectual-property, and customer-data constraints before upload.

Risk: Image generation can consume paid credits after submission.

Mitigation: Run an estimate when available, present the model, image count, size, reference images, and expected credits, and require explicit user approval before running generate.

Risk: Generated redraws may change important print details.

Mitigation: Review generated outputs for key pattern elements, brand constraints, and production suitability before using them in POD listings or manufacturing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-variations)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and qhkit JSON request examples; qhkit image generation returns one-line JSON with generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require local qhkit setup, a configured QHKIT_TOKEN or qhkit credential, reference image paths or URLs, model/size options resolved at runtime, and explicit user approval before paid generation.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
