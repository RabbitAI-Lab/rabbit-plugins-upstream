## Description:

用户提供社媒内容链接或媒体直链和输出目录时，保存支持平台的图片、视频或音频，并整理来源链接、本地文件路径及成功失败清单。支持小红书、抖音、快手、微博、X / Twitter 和 Bilibili，使用 SocialDataX 现有命令。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要整理社交媒体素材的用户：根据用户提供的内容链接或媒体直链，将支持平台的图片、视频或音频保存到指定目录，并提供来源与处理结果清单。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an unpinned @latest CLI that may change without review and could access credentials or files; the security scan was partial because two local references were unresolved.

Mitigation: Review and install an exact package version with integrity checks, and inspect the unresolved references before use. Enter API keys only through the protected local prompt or the deployment platform's secret mechanism.

## Reference(s):

- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release](https://clawhub.ai/devinchen2014/skills/socialdatax-media-save-organizer)

## Skill Output:

**Output Type(s):** [Files, Markdown]

**Output Format:** [Saved image, video, or audio files with a Markdown source and result inventory]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The inventory records each item's source, local path, media type, and save result, including failures.]

## Skill Version(s):

1.0.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
