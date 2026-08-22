## Description:

LinkPix uses qhkit to generate e-commerce main-image and carousel image sets from a product image, using platform-style presets and quote-before-generation checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to create product main images, carousel images, and image sets for e-commerce platforms from a reference product image and optional marketing copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images may be uploaded to the provider for generation.

Mitigation: Confirm the user intends to share the selected product images before generation and use only the referenced files or URLs.

Risk: The workflow uses an API token for qhkit access.

Mitigation: Use the configured token or environment variable without exposing it in chat, logs, or generated files.

Risk: Billable credits may be consumed when generation is submitted.

Mitigation: Run an estimate with the same parameters and obtain explicit user approval before submitting the generation request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-set)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with qhkit shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent should estimate credits, ask for explicit user approval before billable generation, and return generated image URLs with actual credit usage.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
