## Description:

将已生成的短剧镜头剪成成片，记录入出点、镜序、声音、字幕与交付规格。用于套剪、加字幕、统一响度、调整节奏或导出精修素材；需要补素材或修改故事时转回对应创作阶段。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

面向制作短剧的创作者与剪辑人员，将已生成的镜头按分镜整理成片。用户记录镜头取舍、入出点、声音和字幕，并检查、渲染和验收交付视频。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan 将此版本评为 suspicious，报告文件覆盖、输出路径、资源使用及未声明工具能力方面的风险；仅部分组件经过完整检查。

Mitigation: 扫描建议不要安装；如需评估，先审阅源码和扫描结果，并在可丢弃的项目副本上操作，保留输入备份并限制渲染并发。

## Reference(s):

- [入出点与镜序](references/cut-craft.md)
- [生成素材与接镜](references/generated-footage.md)
- [声音、字幕与音乐](references/sound-and-subtitles.md)
- [静帧段](references/still-cuts.md)
- [交付与验收](references/delivery-verify.md)
- [剪辑阶段契约](references/stage-contract.md)

## Skill Output:

**Output Type(s):** [Markdown, Video files, Shell commands, Guidance]

**Output Format:** [Markdown 剪辑单、命令行操作说明和导出成片]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [需要项目内已有且可读取的镜头素材；视频处理依赖 ffmpeg 和 ffprobe。]

## Skill Version(s):

1.0.17 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
