## Description:

用户提供社媒内容链接或媒体直链和输出目录时，保存支持平台的图片、视频或音频，并整理来源链接、本地文件路径及成功失败清单。支持小红书、抖音、快手、微博、X / Twitter 和 Bilibili，使用 SocialDataX 现有命令。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向希望整理社媒素材的用户。Agent 根据用户给出的链接和输出目录保存支持平台的媒体，并提供来源链接、本地路径及成功或失败清单。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online resolution sends supplied links or share text to SocialDataX.

Mitigation: Avoid submitting sensitive or credential-bearing links.

Risk: The external npm package implementation and future releases are outside this review.

Mitigation: Prefer a reviewed, fixed CLI version and restrict its access to necessary files and credentials.

## Reference(s):


## Skill Output:

**Output Type(s):** [Files, Markdown, Text]

**Output Format:** [图片、视频或音频文件，以及来源链接和保存结果清单]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [按用户指定目录保存素材，并逐项记录来源、本地路径及成功或失败原因。]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
