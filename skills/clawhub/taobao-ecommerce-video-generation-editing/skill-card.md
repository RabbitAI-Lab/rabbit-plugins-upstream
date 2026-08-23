## Description:

为淘宝、天猫商品页、店铺首页、上新与推广生成和编辑商品视频，支持文生、图生、参考生成、现有视频重制与 AI Hive 自动下载。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, operators, and developers use this skill to plan, generate, edit, upload, poll, and download ecommerce product videos for Taobao, Tmall, product pages, live-commerce previews, SKU displays, and paid promotion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, videos, or audio may be uploaded to AI Hive during generation or editing.

Mitigation: Use this skill only with product assets that the user is comfortable sending to AI Hive, and avoid confidential media unless the account and data handling terms permit it.

Risk: The skill stores or reads an AI Hive API key locally or from the environment.

Mitigation: Prefer environment-based secrets or a controlled local config, keep the config file permissions restricted, and rotate the key if it may have been exposed.

Risk: Generated ecommerce videos may contain inaccurate product details, unsupported claims, pricing, promotions, or platform marks.

Mitigation: Verify product structure, SKU, claims, price, certification, promotion text, and current Taobao or Tmall publishing rules before release.

Risk: Automatic downloads may write generated media to the default output directory.

Mitigation: Use --no-download for task-only workflows or set --output-dir to a controlled directory when generated files need to be reviewed first.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/taobao-ecommerce-video-generation-editing)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API key and account page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, JSON, Files]

**Output Format:** [Markdown guidance with bash commands; CLI operations can return JSON task data and downloaded media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires requests, an AI_HIVE_API_KEY or local AI Hive config, and user-selected media for upload when using image, video, audio, or frame references.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
