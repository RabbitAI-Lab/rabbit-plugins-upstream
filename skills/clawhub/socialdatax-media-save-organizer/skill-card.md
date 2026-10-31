## Description:

用户提供社媒内容链接或媒体直链和输出目录时，保存支持平台的图片、视频或音频，并整理来源链接、本地文件路径及成功失败清单。支持小红书、抖音、快手、微博、X / Twitter 和 Bilibili，使用 SocialDataX 现有命令。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

For users who provide specific supported social media posts or direct media links and a local output folder. The agent resolves supported posts, saves selected images, video, or audio, and reports source links, local paths, and failed items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookups send supplied links to SocialDataX using the configured API key and may consume service credits.

Mitigation: Use the key only with links the user intends to look up, and be mindful that online requests may consume credits.

Risk: The documented read-only limits are instructions rather than a technical sandbox, and the CLI dependency may change when run using its latest tag.

Mitigation: Use a reviewed exact CLI version and restrict its access to unrelated files and credentials.

## Reference(s):

- [SocialDataX API key and skill information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-media-save-organizer)

## Skill Output:

**Output Type(s):** [Files, Text, Guidance]

**Output Format:** [Saved media files and a concise text or Markdown list of sources, local paths, and results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media is saved in the user-selected output folder; failures and missing media are reported.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
