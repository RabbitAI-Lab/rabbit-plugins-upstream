## Description:

为快手电商、快手小店、直播间和磁力金牛生成与编辑以真实演示、主播口碑、工厂实拍和带货场景为核心的视频素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

快手电商商家、运营人员和内容制作人员 use this skill to plan AI Hive video generation and editing workflows for product demos, livestream previews, factory-source proof content, and paid promotion variants. It emphasizes visible evidence, authorized source material, and avoiding unsupported claims about endorsements, prices, sales, inventory, origin, or platform backing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, videos, audio, and prompts are sent to AI Hive.

Mitigation: Use only authorized product, factory, presenter, and customer media, and avoid uploading private or confidential materials.

Risk: AI Hive API usage may consume billable credits.

Mitigation: Confirm prompts, media, model settings, and task status before rerunning jobs; query existing tasks after timeouts to avoid duplicate generation.

Risk: The init flow may store an AI Hive API key locally in ~/.ai-hive/config.json.

Mitigation: Initialize only on trusted machines, keep the config file private, and rotate the key if it may have been exposed.

Risk: Generated ecommerce videos can create misleading claims if prompts invent endorsements, origin, production capacity, discounts, sales, or platform backing.

Mitigation: Ground claims in merchant-approved materials and review output against current Kuaishou ecommerce and ad policies before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/kuaishou-ecommerce-video-generation-editing)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and local configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompts and command workflows that may upload user-selected media to AI Hive and download generated video results.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
