## Description:

将已生成的短剧镜头剪成成片，记录入出点、镜序、声音、字幕与交付规格。用于套剪、加字幕、统一响度、调整节奏或导出精修素材；需要补素材或修改故事时转回对应创作阶段。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧剪辑人员和创作者用它把已生成的视频镜头或静帧、配音素材整理成剪辑单并渲染成片，核对字幕、声音与交付规格。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remotion setup may overwrite unrelated files.

Mitigation: Back up the project and use a dedicated, disposable Remotion workspace with no unrelated files or symlinks.

Risk: Media checks and frame rendering can consume excessive memory.

Mitigation: Limit media size and processing resources; use the default FFmpeg route when screen-text overlays are unnecessary.

## Reference(s):

- [生成素材的可用区间](references/generated-footage.md)
- [入出点与镜序](references/cut-craft.md)
- [声音、字幕与音乐](references/sound-and-subtitles.md)
- [静帧段](references/still-cuts.md)
- [交付与验收](references/delivery-verify.md)
- [剪辑阶段契约](references/stage-contract.md)
- [Remotion 叠层](assets/remotion/README.md)
- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/short-drama-edit)

## Skill Output:

**Output Type(s):** [Markdown, Video files, Verification reports]

**Output Format:** [剪辑单 Markdown、MP4 成片和可测项目的文字验收报告]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [需要现有且可读的视频或静帧素材；Remotion 可用于画面文字和可选字幕排版。]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
