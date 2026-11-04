## Description:

将已生成的短剧镜头剪成成片，记录入出点、镜序、声音、字幕与交付规格。用于套剪、加字幕、统一响度、调整节奏或导出精修素材；需要补素材或修改故事时转回对应创作阶段。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

短剧创作者和剪辑人员使用此技能，把已生成的视频或静帧素材按分镜整理成片，记录剪辑取舍、字幕与声音处理，并检查交付指标。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crafted cut lists or an unsafe workspace choice can cause unintended file overwrites.

Mitigation: Work from a backup in an isolated project and fresh dedicated Remotion workspace; require safe CUT filenames, keep output paths inside the project, prevent symlink overwrites, and apply media resource limits.

## Reference(s):

- [入出点与镜序](artifact/references/cut-craft.md)
- [生成素材的可用带与接镜](artifact/references/generated-footage.md)
- [静帧段](artifact/references/still-cuts.md)
- [声音、字幕与音乐](artifact/references/sound-and-subtitles.md)
- [交付与验收](artifact/references/delivery-verify.md)
- [Remotion 叠层](artifact/assets/remotion/README.md)
- [Skill release on ClawHub](https://clawhub.ai/worldwonderer/skills/short-drama-edit)

## Skill Output:

**Output Type(s):** [Video files, Markdown, Analysis, Shell commands]

**Output Format:** [Rendered video files, a Markdown editing sheet, and a verification report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires readable source footage; rendering and measurement use ffmpeg and ffprobe.]

## Skill Version(s):

1.0.14 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
