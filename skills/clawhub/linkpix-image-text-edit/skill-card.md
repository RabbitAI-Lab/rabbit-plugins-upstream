## Description:

Helps agents replace text, prices, and promotional copy in ecommerce images using reference images and targeted instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and other external users can update titles, prices, and promotional copy on product images without redesigning each image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update the qhkit npm package and requires an API token.

Mitigation: Confirm the dependency and token setup before use; handle the token as a secret.

Risk: Input images and prompts are sent to the qhkit/iqinghu service.

Mitigation: Use only images and text appropriate to send to that service.

Risk: Generative image editing may change product details or render prices and text incorrectly.

Mitigation: Visually check spelling, prices, logos, and product details before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-image-text-edit)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iqinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with image links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Delivers generated image URLs; verify edited text, prices, and visual details before publishing.]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
