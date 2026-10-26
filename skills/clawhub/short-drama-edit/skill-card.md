## Description:

将已生成的短剧镜头剪成成片，记录入出点、镜序、声音、字幕与交付规格。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧剪辑师和制作团队可用它按分镜整理已生成的镜头素材，调整节奏、保留完整台词、添加字幕与声音，并导出和核验成片。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File-writing flaws may overwrite unintended files.

Mitigation: Work from a disposable project copy with backups, use trusted edit lists, and keep Remotion in a dedicated workspace. Avoid untrusted projects until output containment is fixed.

Risk: Media checks may exhaust memory.

Mitigation: Until decode limits are fixed, run media processing with memory and time limits.

## Reference(s):

- [短剧剪辑与成片 on ClawHub](https://clawhub.ai/worldwonderer/skills/short-drama-edit)
- [Publisher profile: worldwonderer](https://clawhub.ai/user/worldwonderer)

## Skill Output:

**Output Type(s):** [Video, Markdown, Text, Shell commands, Guidance]

**Output Format:** [Rendered episode video with text-based edit and verification reports]

**Output Parameters:** [Project assets, episode, edit list, subtitle and audio cues, and delivery settings]

**Other Properties Related to Output:** [Can retain intermediate render files; verification reports measurable checks without changing the rendered video.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
