## Description:

Generates realistic, high-quality ecommerce product scene images for home goods, beauty, apparel, digital products, and lifestyle product presentations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to guide an agent through generating product lifestyle and scene images with LinkPix/qhkit, including model selection, sizing, credit estimation, user confirmation, and delivery checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update an npm-based qhkit CLI and configure a qhkit API token.

Mitigation: Install only when the user accepts the qhkit dependency and configure tokens through the documented qhkit configuration or environment variable flow.

Risk: Selected product images are uploaded to LinkPix for generation.

Mitigation: Confirm the referenced files and avoid submitting sensitive or unauthorized product imagery.

Risk: Image generation may consume paid credits and generated product details can differ from the reference.

Mitigation: Before generation, confirm model, image count, reference files, size, and estimated credits, then review generated text, logos, and product structure before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-scene-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix login](https://www.iqinghu.com/workbench/login?urlCode=agentch)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides generation requests that return product scene image URLs and credit usage details from qhkit.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
