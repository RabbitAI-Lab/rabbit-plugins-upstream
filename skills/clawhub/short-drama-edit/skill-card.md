## Description:

将已生成的短剧镜头剪成成片，记录入出点、镜序、声音、字幕与交付规格。用于套剪、加字幕、统一响度、调整节奏或导出精修素材；需要补素材或修改故事时转回对应创作阶段。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧剪辑人员与创作者使用该技能，根据已生成且可读取的视频或静帧素材编写剪辑单、安排镜序与声音字幕，并渲染和检查成片。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a project-file overwrite risk.

Mitigation: Review the tool's access and workspace location before installation and use.

Risk: ClawScan reports unbounded media-processing risk.

Mitigation: Set resource limits and use a version-pinned Remotion command.

Risk: The security scan is partial: Skillspector inspected 23 of 30 components, and static analysis was partial for seven.

Mitigation: Treat the assessment as incomplete and review the remaining components before installation.

## Reference(s):

- [可用素材与接镜校正](references/generated-footage.md)
- [入出点与镜序](references/cut-craft.md)
- [声音、字幕与音乐](references/sound-and-subtitles.md)
- [静帧段](references/still-cuts.md)
- [交付与验收](references/delivery-verify.md)
- [Remotion 叠层说明](assets/remotion/README.md)
- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/short-drama-edit)

## Skill Output:

**Output Type(s):** [Markdown, Video files, Shell commands, Guidance]

**Output Format:** [Markdown 剪辑单、命令行指令与视频成片]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [剪辑单按逐镜 CUT 条目组织；需要已生成且可读取的素材。]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
