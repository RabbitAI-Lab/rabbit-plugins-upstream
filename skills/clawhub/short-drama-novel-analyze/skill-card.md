## Description:

将长篇小说、连载网文和多集散稿整理为可追溯的章节索引、剧情分析与分集候选，供创作者评估短剧改编。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

面向编剧、改编策划和内容创作者，帮助他们判断长篇作品是否适合改编，并整理章节功能、剧情单元、人物设定和分集候选。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks this release suspicious with medium confidence, citing a reported mismatch between claimed content-hash checks and implemented indexing behavior; part of the scan was incomplete.

Mitigation: Review the indexing behavior and resolve the incomplete scan before installation; if installed, account for the index not detecting source changes.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/short-drama-novel-analyze)
- [Chapter extraction](references/chapter-extraction.md)
- [Adaptation triage](references/adaptation-triage.md)
- [Story aggregation and entities](references/aggregation-and-entities.md)
- [Adaptation value and episode candidates](references/adaptation-value.md)
- [Stage contract](references/stage-contract.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown analysis documents, JSON chapter indexes, and JSONL episode candidates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are tied to source spans; adaptation assessments and episode candidates remain proposals for creator review.]

## Skill Version(s):

1.0.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
