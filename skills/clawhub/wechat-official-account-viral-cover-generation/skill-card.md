## Description:

使用 Nano Banana Pro 为微信公众号文章制作主封面、分享卡片和系列视觉，让标题承诺、文章核心论点和裁切安全区保持一致。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External content operators, editors, and developers use this skill to generate and edit WeChat Official Account cover images, share cards, and recurring column visuals from article themes and authorized reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Article prompts and optional reference images are sent to AI Hive.

Mitigation: Use only authorized, non-sensitive prompts and images that are suitable for processing by AI Hive.

Risk: The helper stores an AI Hive API key locally.

Mitigation: Protect the local key, prefer environment-based secret handling where appropriate, and avoid sharing generated config files.

Risk: Generated covers may misrepresent people, brands, events, data, or article claims.

Mitigation: Review generated covers before publishing and verify that people, brands, events, data, and title promises are backed by authorized source material.

Risk: WeChat cover dimensions and crop behavior can change.

Mitigation: Preview the main cover, share card, and history-feed crop in the current WeChat publishing interface before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/wechat-official-account-viral-cover-generation)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and generated image files downloaded by the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed Nano Banana Pro image model through AI Hive; generated images are downloaded to the configured output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
