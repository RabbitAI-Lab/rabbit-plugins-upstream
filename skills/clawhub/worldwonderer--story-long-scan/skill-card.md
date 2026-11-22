## Description:

长篇网文扫榜。分析起点、番茄、晋江、七猫等平台排行榜与新书数据，提炼市场趋势与热门题材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

面向长篇网文作者与编辑，用于采集并比较中文网文平台的榜单，发现反复出现的题材信号，并形成带依据和验证建议的选题报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some scripts were not fully inspected, leaving uncertainty about their behavior.

Mitigation: Review the affected scripts and decide whether their behavior is acceptable before running them.

Risk: Detected environment and network capabilities have an undeclared tool scope.

Mitigation: Confirm what environment and network access is needed and limit execution to that scope.

## Reference(s):

- [起点采集与分析指南](artifact/references/platform-qidian.md)
- [番茄采集与分析指南](artifact/references/platform-fanqie.md)
- [晋江采集与分析指南](artifact/references/platform-jjwxc.md)
- [七猫采集与分析指南](artifact/references/platform-qimao.md)
- [刺猬猫采集与分析指南](artifact/references/platform-ciweimao.md)
- [题材候选参考](artifact/references/genre-trends.md)
- [选题决策指南](artifact/references/topic-decision.md)
- [刺猬猫排行榜](https://www.ciweimao.com/rank-index)
- [番茄作品页面](https://fanqienovel.com/page/{bookId})

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [中文 Markdown 扫榜报告与选题决策文件，附结构化榜单数据]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [结论基于所采集的公开榜单样本；各平台热度口径分别解读，不推断未提供的作者后台指标。]

## Skill Version(s):

1.1.30 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
