## Description:

Creates brand-consistent Nano Banana Pro product photography assets for catalogs, ecommerce listings, hero images, lifestyle scenes, detail shots, bundles, color SKUs, and launch materials through AI Hive image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to plan product DNA, prepare prompt recipes, upload approved reference images, and generate consistent product-image sets with AI Hive. It supports catalog masters, premium hero visuals, lifestyle scale scenes, bundles, SKU variants, and multi-channel launch assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images are uploaded to AI Hive during generation.

Mitigation: Use only reference images that are approved for upload to AI Hive.

Risk: The AI Hive API key may be stored locally in ~/.ai-hive/config.json.

Mitigation: Treat the key as a paid-service credential, keep the file permissions restricted, and rotate the key if it may have been exposed.

Risk: Generated product imagery can misstate product shape, labels, materials, bundle contents, or platform claims if outputs are accepted without review.

Mitigation: Review generated assets against the approved SKU, packaging, claims, and current channel rules before publication.

## Reference(s):

- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-product-image)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash examples; generated image files are downloaded by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses approved reference images, prompt text, optional routing mode, batch size, model parameters, and output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
