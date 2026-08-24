## Description:

为拼多多店铺生成和编辑商品主图视频、批量 SKU 演示、工厂素材重制、多多搜索与场景广告视频，并通过 Seedance 多模式和 AI Hive API 提交、轮询、下载生成结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and developers use this skill to create, adapt, and batch-track Pinduoduo product videos across SPU masters, SKU variants, factory footage, search ads, scene ads, and package demonstrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key and can store it in ~/.ai-hive/config.json.

Mitigation: Treat the config file as a credential file, keep restrictive file permissions, and prefer environment or CLI-provided credentials in shared environments.

Risk: Product images, videos, or audio files explicitly passed to the tool are uploaded to AI Hive for generation or editing.

Mitigation: Upload only media that is approved for AI Hive processing and avoid passing confidential or unlicensed product assets.

Risk: Batch video generation can incur costs and may create misleading ecommerce claims if prompts include unverified prices, sales, certifications, or capabilities.

Mitigation: Review costs before batch runs and keep platform labels, pricing, sales claims, certifications, and unverified performance claims out of generated prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/pinduoduo-ecommerce-video-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples, JSON task responses, and downloaded media files from AI Hive tasks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is submitted through AI Hive, polled by task ID, and downloaded to the configured output directory unless no-download mode is used.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
