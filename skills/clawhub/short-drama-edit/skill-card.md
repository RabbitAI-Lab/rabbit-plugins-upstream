## Description:

将已有短剧镜头按分镜剪辑成片，并记录镜序、入出点、声音、字幕与交付要求。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者和剪辑人员使用已有镜头、关键帧与配音编排剪辑单，渲染并核验带字幕和声音的交付成片。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 特制 CUT ID 可能导致 MP4 写入预期输出目录之外。

Mitigation: 仅处理可信项目，或先将 CUT ID 限制为不含路径分隔符的文件名；核对输出位置与成片。

Risk: 可选 Remotion 叠层会在持久缓存工作区安装 npm 依赖。

Mitigation: 启用前检查依赖来源和安装环境，并在交付前审看生成内容。

## Reference(s):

- [ClawHub 技能发布页](https://clawhub.ai/worldwonderer/skills/short-drama-edit)
- [入出点与镜序](references/cut-craft.md)
- [声音、字幕与音乐](references/sound-and-subtitles.md)
- [交付与验收](references/delivery-verify.md)
- [Remotion 叠层说明](assets/remotion/README.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown 剪辑单、MP4 成片与核验报告]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [需要已有可读素材及 ffmpeg/ffprobe；可选的画面文字叠层需要安装 Remotion 依赖。]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
