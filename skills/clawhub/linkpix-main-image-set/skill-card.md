## Description:

Generates e-commerce main-image carousel sets from a product image or marketing copy by guiding an agent through LinkPix qhkit image options, estimates, generation, and delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketplace operators, and commerce teams use this skill to create product main images, carousel images, and platform-adapted image sets from a small set of product inputs. The skill helps an agent install and configure qhkit, estimate paid generation cost, request user approval, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and marketing copy may be uploaded to the qhkit/LinkPix service.

Mitigation: Use only product inputs approved for upload to that service, and review sensitive or confidential content before generation.

Risk: Generation can consume paid credits.

Mitigation: Run an estimate with the same parameters and obtain explicit user approval before submitting a paid generation task.

Risk: A qhkit API key may be stored locally or supplied through the environment.

Mitigation: Store credentials using qhkit configuration or QHKIT_TOKEN only in trusted environments and avoid exposing token values in logs or shared outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-set)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit command parameters, cost-confirmation text, troubleshooting guidance, and generated image URLs when generation succeeds.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
