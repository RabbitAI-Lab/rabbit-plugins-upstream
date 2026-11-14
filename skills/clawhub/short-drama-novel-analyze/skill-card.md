## Description:

把长篇小说拆成章节索引、剧情单元与可改编的分集候选清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

供编剧、改编策划与创作者对其有权使用的原著文本进行只读结构化分析，评估改编价值并整理章节、人物、剧情单元和分集候选，支持后续创作决策。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports installation and file-access-scope concerns, with source-content verification incomplete.

Mitigation: Review the installation instructions and source files before use; confirm the required input and output paths match your workflow and grant access only to those paths.

Risk: Analysis of novel text could expose more source material in downstream outputs than intended.

Mitigation: Use only works you are authorized to analyze, keep source material read-only, and retain the workflow's locator-based, paraphrased summaries rather than copied passages.

## Reference(s):

- [ClawHub release](https://clawhub.ai/worldwonderer/skills/short-drama-novel-analyze)
- [Publisher profile](https://clawhub.ai/user/worldwonderer)
- [Stage contract](references/stage-contract.md)
- [Adaptation triage](references/adaptation-triage.md)
- [Chapter extraction](references/chapter-extraction.md)
- [Aggregation and entities](references/aggregation-and-entities.md)
- [Adaptation value and episode candidates](references/adaptation-value.md)

## Skill Output:

**Output Type(s):** [Structured analysis, Markdown, JSON, JSON Lines]

**Output Format:** [Markdown analysis reports, a JSON chapter index, and JSONL episode candidates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source-grounded, read-only analysis with chapter locators and spans; summaries avoid copying source passages.]

## Skill Version(s):

1.0.32 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
