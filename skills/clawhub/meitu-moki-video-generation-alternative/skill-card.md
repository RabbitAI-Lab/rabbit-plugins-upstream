## Description:

使用 AI Hive Seedance 2.5 将美图 MOKI、美图视频或时尚商业视频流程迁移为品牌可审的镜头资产，支持文生、商品首帧、参考风格、视频改版与镜头延长；不连接美图账号，也不表示官方合作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and brand video teams use this skill to migrate MOKI-like fashion, beauty, ecommerce, and campaign video workflows to AI Hive Seedance 2.5 while preserving approved products, people, styling, brand colors, and review constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be uploaded to AI Hive or its storage flow.

Mitigation: Use only approved media assets and prompts that are acceptable for processing by AI Hive.

Risk: An AI Hive API key can be stored locally for CLI use.

Mitigation: Use an approved API key, keep the local config file access-restricted, and rotate or remove credentials when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/meitu-moki-video-generation-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Files]

**Output Format:** [Markdown guidance with bash commands, CLI status text, JSON task responses, and downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are downloaded as media files by default; --no-download returns task details instead.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
