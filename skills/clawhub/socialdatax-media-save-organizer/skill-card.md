## Description:

用户提供社媒内容链接或媒体直链和输出目录时，保存支持平台的图片、视频或音频，并整理来源链接、本地文件路径及成功失败清单。支持小红书、抖音、快手、微博、X / Twitter 和 Bilibili，使用 SocialDataX 现有命令。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users provide social-media content or direct-media links and a local output folder to save supported images, videos, or audio. The skill organizes the saved files with source links, local paths, and per-item success or failure details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookups share selected links and attribution tags with SocialDataX and may consume paid credits.

Mitigation: Submit only links you intend to share and check credit usage before online lookups.

Risk: The SocialDataX API key is sensitive, and saved media may contain private or sensitive content.

Mitigation: Keep the API key private and choose an appropriate output folder.

Risk: The external CLI is invoked through a mutable @latest package version.

Mitigation: Consider using a reviewed fixed CLI version; the executable is not bundled with this skill.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/socialdatax-media-save-organizer)
- [SocialDataX AI and API Key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Files, Markdown, Text]

**Output Format:** [Saved image, video, or audio files with a Markdown or text checklist of sources, local paths, media types, and results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes user-selected links and saves files only to the specified output folder; reports missing or failed items without inventing paths or results.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
