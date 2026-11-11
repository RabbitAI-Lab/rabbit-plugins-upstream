## Description:

分析起点、番茄、晋江、七猫等平台的长篇网文榜单与新书数据，识别重复题材信号并形成扫榜报告和选题建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

面向长篇网文作者，用于查看多个阅读平台的排行榜和新书样本、归纳题材趋势，并把证据与作者条件整理成扫榜报告和选题建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan verdict is benign with medium confidence, but only 9 of 16 components were fully inspected.

Mitigation: Review the seven partially inspected scripts before installation or execution; treat the scan as incomplete.

Risk: Incomplete platform samples or mixing platform-specific ranking metrics can lead to misleading trend conclusions.

Mitigation: State which boards were unavailable, compare metrics only within each platform's published measure, and do not infer private author analytics.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/story-long-scan)
- [Topic decision guide](references/topic-decision.md)
- [Historical genre candidates](references/genre-trends.md)
- [Qidian platform guide](references/platform-qidian.md)
- [Fanqie platform guide](references/platform-fanqie.md)
- [Jinjiang platform guide](references/platform-jjwxc.md)
- [Qimao platform guide](references/platform-qimao.md)
- [Ciweimao platform guide](references/platform-ciweimao.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown scan reports and topic decision files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compares each platform using its own public ranking metrics; historical candidates are labeled as hypotheses when live samples are unavailable.]

## Skill Version(s):

1.1.27 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
