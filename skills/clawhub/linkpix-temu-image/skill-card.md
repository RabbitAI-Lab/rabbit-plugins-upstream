## Description:

Helps Temu sellers create product image sets, detail images, and promotional graphics from product photos using the Qinghu AI image service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Temu sellers and their agents use the skill to turn product photos into marketplace image sets, detail-page graphics, and promotional posters. It guides model selection, cost estimation, generation, and delivery of image links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating the external qhkit CLI may change the user's environment.

Mitigation: Review the npm package and prefer a pinned version; avoid persistent PATH or profile changes unless needed.

Risk: Product images and an API key are used with an external paid service.

Mitigation: Confirm the service is acceptable for the images, protect the API key, check estimated credits, and obtain explicit approval before generating.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-temu-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Image links, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with generated image links and credit usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation requires product images, a service API key, and user approval of estimated credits.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
