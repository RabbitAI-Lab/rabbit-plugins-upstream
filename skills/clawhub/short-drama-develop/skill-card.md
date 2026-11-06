## Description:

帮助创作者把短剧或漫剧点子、长篇小说及系列材料发展为改编方案、故事引擎和分集地图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

面向短剧与漫剧创作者，用于梳理创作方向、开发系列故事机制，并把小说或既有材料整理为开发简报和分集规划。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An in-place manuscript edit that preserves file length can escape index verification.

Mitigation: Rebuild the manuscript index after edits before relying on saved episode locations.

Risk: Project files may be written to an unintended location if output paths are not checked.

Mitigation: Use a dedicated project folder and inspect output paths before running commands.

Risk: Companion skills have separate security coverage.

Mitigation: Review each companion skill separately before installing it.

## Reference(s):

- [ClawHub release: 短剧开发 1.0.30](https://clawhub.ai/worldwonderer/skills/short-drama-develop)
- [Publisher profile: worldwonderer](https://clawhub.ai/user/worldwonderer)
- [多集整稿接入与断点续跑](artifact/references/multi-episode-intake.md)
- [分集设计](artifact/references/episode-design.md)
- [故事工艺](artifact/references/story-craft.md)
- [阶段契约](artifact/references/stage-contract.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, JSONL, Guidance]

**Output Format:** [中文文本、Markdown 开发文档，以及 JSON 和 JSONL 项目文件]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [交付内容依项目材料与阶段而定；本技能不撰写场景动作或对白，也不生成媒体。]

## Skill Version(s):

1.0.30 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
