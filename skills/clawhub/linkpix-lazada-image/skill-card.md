## Description:

Helps Lazada and LazMall sellers create localized product images, carousel image sets, detail-page images, and campaign posters through Qinghu AI and the qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agent users use this skill to prepare Lazada-ready product visuals, including square main images, carousel sets, detail-page images, localized selling-point graphics, white-background images, scene images, and campaign posters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys could be exposed if users paste qhkit tokens into chat.

Mitigation: Configure qhkit tokens locally through an environment variable, a local config command, or a secret manager instead of sharing the raw key in chat.

Risk: Product images and prompts may be sent to the Qinghu service during generation.

Mitigation: Use only product images and marketing copy that are approved for upload to the Qinghu service.

Risk: Generate actions can consume account credits.

Mitigation: Run the matching qhkit estimate command and get explicit user approval for the model, image count, quality, reference images, language, and estimated credits before submitting a generation job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-lazada-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to inspect qhkit options, estimate credits before generation, submit approved image-generation jobs, and return generated image URLs with actual credit usage.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
