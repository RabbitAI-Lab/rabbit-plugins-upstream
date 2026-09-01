## Description:

Seedream 5.0 Pro | LinkPix helps ecommerce creative teams generate product images, posters, and marketing visuals through the qhkit image workflow using text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce designers, product photographers, brand visual teams, and commerce operators use this skill to prepare LinkPix/qhkit image generation workflows for product listing images, posters, platform marketing assets, and reference-image transformations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires installing or invoking the qhkit CLI and may require Node package installation.

Mitigation: Review the requested package installation before use and install only when the environment permits the qhkit CLI dependency.

Risk: Prompts and reference images may be uploaded to the LinkPix/qhkit service.

Mitigation: Use the skill only with inputs appropriate for that service and avoid uploading sensitive images or confidential prompt content unless approved.

Risk: Generation can consume service credits after a task is submitted.

Mitigation: Confirm the model, image count, quality, reference images, and estimated credits before running any generation command.

Risk: The workflow stores or uses a qhkit API token locally.

Mitigation: Store the token using the qhkit configuration flow or environment variable guidance and avoid exposing it in chat logs, scripts, or committed files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedream-5-pro)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated image URLs after confirmed qhkit generation requests.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
