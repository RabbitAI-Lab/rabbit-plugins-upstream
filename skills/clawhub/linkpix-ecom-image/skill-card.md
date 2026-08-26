## Description:

LinkPix helps an agent route e-commerce image requests to qhkit workflows for product image sets, long-form product detail images, and prompt- or reference-image-based commercial images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce operators use this skill through an agent to generate marketplace-ready product imagery, detail-page assets, and marketing visuals from text prompts or product reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload product images to the qhkit/LinkPix service.

Mitigation: Use the skill only when sharing those product images with the service is acceptable.

Risk: The workflow requires an API key for qhkit/LinkPix.

Mitigation: Configure credentials through qhkit or an environment variable and avoid exposing the token in prompts, logs, or generated artifacts.

Risk: Image generation can consume account credits.

Mitigation: Run an estimate and obtain explicit user confirmation before submitting a credit-consuming generation request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ecom-image)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated image URLs through the qhkit CLI after user confirmation for credit-consuming generation.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
