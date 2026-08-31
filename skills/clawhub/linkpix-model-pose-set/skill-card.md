## Description:

Generates ecommerce clothing model image sets in multiple poses and viewing angles from a single model or garment reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and ecommerce operators use this skill to create pose and angle variants for clothing product detail pages and social media assets. Agents use it to prepare qhkit image-batch commands, estimate credits, request user approval, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask the user to provide an API key through chat and store it for CLI use.

Mitigation: Use a local secret store, QHKIT_TOKEN, or a non-echoing local prompt; avoid pasting tokens into the conversation and review local qhkit configuration.

Risk: The skill can install npm packages and may write qhkit configuration locally.

Mitigation: Review the package source and install path before installation, prefer approved package sources, and run with least-privilege local permissions.

Risk: Generated pose variants may change product details such as text, logos, fabric structure, or garment shape.

Mitigation: Review generated images against the source product before publishing them in ecommerce or marketing channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-pose-set)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON parameters; generated results are image URLs returned by the CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, a configured token or QHKIT_TOKEN, one uploaded image, and one to ten pose actions; estimate credits before generate.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
