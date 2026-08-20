## Description:

Uses Nano Banana 2 through AI Hive to retouch product catalog photos consistently while preserving SKU facts such as color, structure, labels, accessories, and disclosed defects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, catalog operators, and content production teams use this skill to prepare consistent e-commerce product photos from user-selected source images. It supports catalog retouching workflows for jewelry, apparel, appliances, furniture, and packaging while requiring QC against the original SKU facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images are sent to AI Hive for processing.

Mitigation: Use the skill only for images approved for AI Hive processing, and avoid uploading confidential or restricted product imagery unless that transfer is acceptable.

Risk: Generated retouches may accidentally alter SKU facts such as labels, logos, colors, quantities, visible defects, or product structure.

Mitigation: Compare each output against the original product image and reject any result that changes SKU facts or removes defects that must remain disclosed.

Risk: The helper may store an AI Hive API key locally.

Mitigation: Store credentials with restricted file permissions or use an environment variable, and rotate the key if local exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-product-retouch)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Image files]

**Output Format:** [Markdown guidance with bash commands; the helper can return JSON task details and download generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key and at least one user-selected product image; uses the fixed public_model_nano_banana_2 image model.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
