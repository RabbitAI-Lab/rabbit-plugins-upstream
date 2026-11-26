## Description:

分析知乎盐言、七猫、黑岩和点众等平台的热门短篇数据，提炼题材趋势与可验证的选题方向。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

面向短篇小说作者与编辑，汇总平台榜单样本、分析题材与读者情绪趋势，并形成注明样本范围和可信度的扫榜报告及选题匹配建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is benign with medium confidence, but some script contents were only partially interpreted and the tool scope is undeclared.

Mitigation: Review the scripts and requested access before installation, taking the scan's stated uncertainty into account.

Risk: Ranking and engagement figures reflect attention within a platform's metric and do not establish story quality; incomplete or historical samples can mislead trend conclusions.

Mitigation: State the platform, metric, date, sample coverage, and confidence in each report, and label historical-only conclusions as candidates pending a current re-scan.

## Reference(s):

- [点众平台采集说明](artifact/references/platform-dianzhong.md)
- [黑岩平台采集说明](artifact/references/platform-heiyan.md)
- [作者提供榜单的整理格式](artifact/references/manual-rank-input.md)
- [历史市场数据说明](artifact/references/real-market-data.md)
- [选题匹配方法](artifact/references/topic-match.md)
- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/story-short-scan)
- [Source URL listed in skill metadata (not server-resolved provenance)](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Chinese Markdown scan reports, comparison tables, and topic suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports identify the sample date, platform coverage, confidence, and suggested re-scan date; historical data is labeled as unverified candidate guidance.]

## Skill Version(s):

1.1.27 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
