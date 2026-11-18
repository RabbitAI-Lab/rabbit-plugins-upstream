## Description:

分析长篇网络小说的章节事实、剧情因果、情绪节奏、角色设定与文风，并支持复用或续跑既有分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

作者和小说编辑可用它逐章拆解长篇网文，整理故事结构、情绪节奏、人物关系与可迁移的写作机制，并复用或续跑已有分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with medium confidence, citing edits to a separate topic-selection document without clear authorization, broad triggers, and undeclared tool scope.

Mitigation: Before installing or running, review requested file changes and available tools; approve only intended edits and keep actions within the requested analysis.

Risk: Skillspector marked its analysis partial because several local path-like references could not be resolved, so available evidence does not establish that the skill is safe.

Mitigation: Review the skill and resolve referenced paths before use; treat unavailable files as unverified.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/story-long-analyze)
- [剧情与节奏分析](artifact/references/stage3-plot-rhythm.md)
- [角色与设定分析](artifact/references/stage4-characters-settings.md)
- [主报告](artifact/references/stage5-report.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown files, CSV data, Relationship diagrams, Writing guidance]

**Output Format:** [Markdown reports, CSV chapter indexes, and relationship diagrams]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Staged chapter analysis; can reuse existing analysis files and resume incomplete stages.]

## Skill Version(s):

1.1.43 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
