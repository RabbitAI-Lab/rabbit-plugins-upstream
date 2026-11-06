## Description:

把长篇小说与连载网文整理成可追溯的章节索引、剧情分析和短剧分集候选。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

创作者用它判断原著是否适合改编，并整理章节功能、剧情单元、人物设定及分集候选，供后续改编规划使用。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An existing generated file in the analysis output folder may be replaced.

Mitigation: Use a dedicated analysis folder and check existing outputs before writing.

Risk: Index verification can miss source edits that preserve line counts.

Mitigation: Rebuild the chapter index after every source edit.

Risk: The optional companion skill has not been reviewed as part of this release.

Mitigation: Review it separately before installation.

## Reference(s):

- [长篇原著分析（ClawHub）](https://clawhub.ai/worldwonderer/skills/short-drama-novel-analyze)
- [改编价值快评](artifact/references/adaptation-triage.md)
- [章节提取](artifact/references/chapter-extraction.md)
- [聚合与实体](artifact/references/aggregation-and-entities.md)
- [改编价值与分集候选](artifact/references/adaptation-value.md)
- [阶段契约](artifact/references/stage-contract.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, JSONL]

**Output Format:** [Markdown analysis reports, a JSON chapter index, and JSONL episode candidates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only source analysis with traceable locators; does not write scripts or decide the adaptation plan.]

## Skill Version(s):

1.0.28 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
