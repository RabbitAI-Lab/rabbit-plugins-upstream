## Description:

帮助作者按连续章节块分析长篇网络小说，整理章节摘要、剧情因果、节奏、角色、设定与文风，并支持续跑和按需补全已有成果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

面向创作长篇网文的作者：用于拆解小说开篇与逐章内容，梳理故事线、因果、读者情绪、节奏、人物关系和设定，并生成可续跑的分析报告与文风档案。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can update a separate topic-planning document without confirming that it is the intended target.

Mitigation: Instruct the agent to skip topic-decision updates unless you select the file and approve the change.

## Reference(s):

- [Stage 0–1：概要初稿与黄金三章](artifact/references/stage1-golden-chapters.md)
- [Stage 2：逐章提取](artifact/references/stage2-extraction.md)
- [Stage 3：剧情与节奏](artifact/references/stage3-plot-rhythm.md)
- [Stage 4：角色、设定与关系](artifact/references/stage4-characters-settings.md)
- [Stage 5：主报告](artifact/references/stage5-report.md)
- [Stage 6：文风档案](artifact/references/style-profile-generator.md)
- [阶段合成输入与事实保真](artifact/references/synthesis-inputs.md)
- [续跑、提交与恢复说明](artifact/references/pipeline-ops.md)
- [原文变化与索引重建](artifact/references/index-rebuild.md)
- [灵感库流程](artifact/references/inspiration-library.md)
- [作者可见的报告与回复规范](artifact/references/author-facing.md)
- [收尾检查](artifact/references/final-checks.md)
- [ClawHub skill release page](https://clawhub.ai/worldwonderer/skills/story-long-analyze)
- [Project link listed in skill metadata (not server-resolved provenance)](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, CSV, Files]

**Output Format:** [中文 Markdown 报告与分析文件；章节索引为 CSV，关系图可使用 Mermaid，图片格式可选。]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [支持分阶段续跑和复用已有分析成果；可生成章节索引、分析缓存及可选人物关系图。]

## Skill Version(s):

1.1.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
