## Description:

为天猫旗舰店生成与编辑商品页视频、品牌故事、新品首发、详情演示、大促会场和会员内容，并通过 AI Hive/Seedance 模式提交视频生成、编辑和延长任务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, creative teams, and agency developers use this skill to prepare Tmall product-page, flagship-store, launch, promotion, and member-retention video workflows. It helps them structure prompts, submit AI Hive video jobs, poll task status, and download generated media for human review and post-production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an AI Hive API key and sends selected product images, videos, audio, and prompts to AI Hive or its upload storage.

Mitigation: Use a scoped API key, keep the local AI Hive config file restricted, and submit only media approved for that external service.

Risk: Generated Tmall marketing videos may include inaccurate product, promotional, certification, pricing, or platform-compliance details if those are delegated to generation.

Mitigation: Keep prices, discounts, certifications, platform marks, and complex Chinese copy in a human-reviewed post-production step, then check current Tmall product, campaign, and advertising rules before release.

Risk: Generated media downloads are written to a user-selected output directory.

Mitigation: Choose the output directory deliberately and review generated files before sharing or publishing them.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wubin1836/skills/tmall-ecommerce-video-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with bash commands, JSON task status, and downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submits AI Hive video generation jobs; downloads result media unless the user selects no-download behavior.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
