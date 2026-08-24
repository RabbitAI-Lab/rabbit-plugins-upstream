## Description:

Generates multiple ecommerce product-image marketing variants from one reference image, with different backgrounds, layouts, and visual styles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce marketers, marketplace operators, and creative teams use this skill to turn a product image into multiple advertising or A/B testing variants. It helps an agent prepare prompts, estimate billable usage, run qhkit image generation commands, and deliver generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images are sent to LinkPix/qhkit for generation.

Mitigation: Use the skill only when sharing those images with the provider is acceptable, and review generated outputs before publication.

Risk: The provider account may incur billable API usage.

Mitigation: Run the estimate command and obtain explicit user confirmation before generation.

Risk: API keys may be requested during setup.

Mitigation: Configure credentials locally with a secure environment variable or provider credential flow; do not paste API keys into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-variations)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and credit usage returned by qhkit.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
