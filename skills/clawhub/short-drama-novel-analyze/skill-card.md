## Description:

把长篇小说、连载网文或多集散稿拆解为可追溯的章节索引、戏剧功能、改编价值评估与分集候选，供后续短剧开发使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

面向编剧与短剧开发者，用于从合法持有的长篇小说或连载文本中提取可追溯的剧情结构、人物与设定，并评估改编价值、整理分集候选。分析结果供创作者审阅和后续开发，不替创作者决定改编方案。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A previously built chapter index may no longer reflect edited source text; verification does not check source content hashes.

Mitigation: Rebuild the index whenever source files change and keep only the intended novel files in a dedicated analysis folder.

Risk: Installing the companion skill adds a separate component beyond this standalone analysis skill.

Mitigation: The companion is unnecessary for standalone use; review it separately before installing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/short-drama-novel-analyze)
- [改编价值与分集候选](references/adaptation-value.md)
- [逐章提取](references/chapter-extraction.md)
- [原著分析阶段契约](references/stage-contract.md)
- [Installation and companion skills](INSTALL.md)

## Skill Output:

**Output Type(s):** [JSON, JSONL, Markdown, Shell commands, Guidance]

**Output Format:** [Chapter indexes and episode candidates in JSON or JSONL, with structured analysis reports in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis files are scoped to source-analysis; original source material is read-only and should not be reproduced in long excerpts.]

## Skill Version(s):

1.0.27 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
