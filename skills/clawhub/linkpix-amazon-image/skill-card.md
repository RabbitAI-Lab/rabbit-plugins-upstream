## Description:

Helps Amazon sellers and cross-border ecommerce teams use LinkPix/Qinghu AI through qhkit to prepare Amazon product images, main-image sets, detail-page images, comparison graphics, selling-point graphics, multilingual images, and campaign posters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, Amazon sellers, designers, and marketing teams use this skill to configure and submit product-image generation tasks for Amazon listing visuals through qhkit and the Qinghu/LinkPix service. It is intended for workflows that need platform-aware product photos, detail pages, activity images, multilingual assets, and generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the third-party qhkit npm CLI and a Qinghu/LinkPix API key.

Mitigation: Install qhkit from the documented package source, configure credentials intentionally, and confirm the service account and environment before use.

Risk: Referenced product images are uploaded to an external service for generation.

Mitigation: Use only images that are approved for external processing and avoid submitting confidential, restricted, or rights-unclear product assets.

Risk: Generate actions can consume paid credits.

Mitigation: Run an estimate when supported and require explicit user approval of model, image count, quality, language, reference images, and expected credits before submitting generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-amazon-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead the agent to request user confirmation before paid generation, invoke qhkit actions, upload referenced product images, and return generated image URLs with credit usage.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
