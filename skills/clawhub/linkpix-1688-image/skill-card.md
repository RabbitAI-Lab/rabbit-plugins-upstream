## Description:

Helps 1688 wholesalers, factories, and B2B operators use LinkPix/qhkit to generate product main images, carousel sets, detail-page images, campaign posters, white-background industrial images, parameter diagrams, detail breakdowns, multi-SKU compositions, and watermark-protected images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External B2B ecommerce operators use this skill to prepare 1688-ready product imagery and marketing visuals from product photos and copy. The skill guides an agent through qhkit installation, model option lookup, cost estimation, confirmation, generation, polling, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires qhkit installation or upgrade on the host.

Mitigation: Review package installation commands before use and run the skill in an environment where host-level changes are acceptable.

Risk: The skill requires an API key for Qinghu/qhkit access.

Mitigation: Prefer a platform secret manager or environment variable instead of pasting the key directly into chat.

Risk: Product images may be uploaded to the service and generation consumes credits after confirmation.

Mitigation: Confirm the reference images, selected model or template, image count, quality, and estimated credits before running generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-1688-image)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and credit usage after user confirmation.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
