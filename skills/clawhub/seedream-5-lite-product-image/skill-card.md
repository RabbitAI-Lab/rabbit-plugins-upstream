## Description:

使用 Seedream 5.0 Lite 通过 AI Hive 生成产品摄影、商品主图、场景图、细节图、包装清单和 SKU 系列，并帮助保持商品结构与品牌事实准确。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and product-content teams use this skill to generate product photography, ecommerce main images, detail shots, usage scenes, packing list images, and consistent SKU image sets from product references through AI Hive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key.

Mitigation: Use a scoped key where available, avoid sharing the key, and store it only in the documented environment variable or protected local config.

Risk: Product and reference media may be uploaded to AI Hive or its object storage.

Mitigation: Use only media that is intended for that service and avoid private files or unreleased product assets unless the upload is approved.

Risk: The bundled helper code exposes broader AI Hive commands than the product-image workflow.

Mitigation: Review commands before execution and limit routine use to the documented Seedream product-image generation flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-product-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and local image files from AI Hive task downloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key, can upload product or reference media, and defaults downloads to ~/Downloads/AiHive.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
