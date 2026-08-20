## Description:

为快手电商、快手小店、直播间和磁力金牛生成与编辑商品卡、主播同框、源头工厂、直播贴片及广告图片。Use this skill for 快手电商图片、快手小店商品图、直播带货图片、老铁种草、主播推荐、源头好货、磁力金牛测图、工厂实拍和商品详情；支持 AI Hive 参考图生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agent users use this skill to generate or edit Kuaishou product cards, host-and-product images, factory/source proof images, livestream product overlays, and Magnet Jinniu test creatives. The workflow emphasizes authorized reference materials, accurate product and host representation, and leaving prices, sales claims, platform labels, and promotional text for approved downstream editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an AI Hive API key and can store configuration locally.

Mitigation: Keep the AI Hive config file private, prefer scoped credentials where available, and rotate the key if it is exposed.

Risk: Reference product, host, or factory images are uploaded to the AI Hive service.

Mitigation: Upload only authorized media needed for the task and avoid passing sensitive unrelated files as references.

Risk: Generated ecommerce creatives can misstate prices, sales volume, certifications, factory scale, or platform claims.

Mitigation: Use approved reference material, keep restricted commercial claims out of prompts, and review outputs against current Kuaishou ecommerce and Magnet Jinniu rules before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/kuaishou-ecommerce-image-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown guidance with bash commands; runtime commands submit AI Hive image tasks, print JSON task data when requested, and download generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key, optional reference image uploads, batch size and model parameters, routing options, task polling, and local result downloads.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
