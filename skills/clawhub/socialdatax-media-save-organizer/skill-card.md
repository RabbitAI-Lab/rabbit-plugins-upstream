## Description:

用户提供社媒内容链接或媒体直链和输出目录时，保存支持平台的图片、视频或音频，并整理来源链接、本地文件路径及成功失败清单。支持小红书、抖音、快手、微博、X / Twitter 和 Bilibili，使用 SocialDataX 现有命令。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users provide selected social media post links or direct media links and an output folder to save supported images, videos, or audio, then receive a source and results list with local paths and any failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookups send selected post links or identifiers to SocialDataX and may consume API credits.

Mitigation: Confirm the link list before lookup, use only the links requested by the user, and keep the API key in the client’s supported secret storage.

Risk: Direct media downloads contact the media host, and the skill relies on an external CLI implementation.

Mitigation: Use a reviewed, pinned CLI version where practical and restrict file access to the user-selected output folder.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-media-save-organizer)
- [SocialDataX AI and API key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Files, Text, Markdown]

**Output Format:** [Saved image, video, or audio files with a source and results list of links, local paths, types, and outcomes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes only user-selected links; reports failures and missing media alongside successful saves.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
