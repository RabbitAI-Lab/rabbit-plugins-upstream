## Description:

为微信小店、视频号、社群和私域运营生成与编辑商品演示、直播预热、店主讲解、朋友圈视频及复购内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, ecommerce operators, and agent users use this skill to create WeChat Shop and Channels ecommerce video prompts and to run AI Hive video generation for product demos, host explanations, group-buying clips, live-stream previews, and repeat-purchase content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to AI Hive for generation.

Mitigation: Use only media you are authorized to upload and avoid sensitive local files or private customer material unless it has been approved for that service.

Risk: Running init stores an AI Hive API key on the local machine.

Mitigation: Prefer environment variables for shared systems, keep the local config file private, and rotate the API key if it may have been exposed.

Risk: Generated outputs are saved to a local downloads directory by default.

Mitigation: Set an explicit output directory when generated ecommerce media requires controlled storage, review, or retention handling.

Risk: Ecommerce video content can become misleading if it invents prices, reviews, scarcity, sales counts, or customer stories.

Mitigation: Follow the skill's acceptance guidance: keep product and service facts accurate, add prices and rules manually, and avoid unauthorized customer or order information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/wechat-shop-ecommerce-video-generation-editing)
- [AI Hive API service endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands; CLI commands can submit AI Hive video tasks, print JSON task responses, and download generated media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs are saved under ~/Downloads/AiHive by default unless an output directory is supplied.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
