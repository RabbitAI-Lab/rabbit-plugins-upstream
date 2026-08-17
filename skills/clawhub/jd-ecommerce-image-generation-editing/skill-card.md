## Description:

为京东店铺生成和编辑商品主图、规格图、结构卖点图、场景图与京准通广告图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agent workflows use this skill to create and refine JD product main images, detail-page visuals, structure callouts, scene images, package-list images, and JD ad test images while preserving provided product facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or reference images and prompts are sent to AI Hive.

Mitigation: Use only approved product assets and avoid private files with --image or --file.

Risk: The AI Hive API key can be stored locally in ~/.ai-hive/config.json.

Mitigation: Review or remove the local config when access is no longer needed and keep the key protected.

Risk: Generated ecommerce images may add or distort product details, claims, prices, certifications, or SKU differences.

Mitigation: Review generated assets against supplied product facts and current JD category or advertising rules before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/jd-ecommerce-image-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands; generated image files and JSON task/status responses from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive image generation with optional reference images, batch generation, routing mode, output directory, and no-download controls.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
