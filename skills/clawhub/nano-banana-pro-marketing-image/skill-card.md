## Description:

使用 Nano Banana Pro 和 AI Hive 生成一致的品牌 Campaign 营销图片，从主 KV 扩展到社交内容、品牌故事、联名活动、本地化市场和多尺寸素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, designers, and agents use this skill to define reusable campaign visual codes and generate consistent Nano Banana Pro marketing image assets through AI Hive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow stores an AI Hive API key in a local configuration file.

Mitigation: Use the documented initialization path or environment variable, restrict local config file permissions, and avoid sharing the configured machine or file.

Risk: Reference images and media selected by the user are uploaded to AI Hive.

Mitigation: Upload only the marketing assets required for the campaign and avoid private or unrelated files.

Risk: Generated marketing images can drift from approved product, brand, authorization, or localization constraints.

Mitigation: Review generated assets against the skill's consistency checklist before publishing, including product fidelity, authorized collaboration assets, and localized-market claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-marketing-image)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with bash command examples and generated image task output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference images, batch generation, aspect ratio parameters, routing mode, and output directory selection.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
