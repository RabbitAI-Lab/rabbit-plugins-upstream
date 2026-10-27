## Description:

分析中文长篇网文平台的榜单与新书样本，帮助作者识别题材趋势和可写的选题方向。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

网文作者和内容策划者用它汇总起点、番茄、晋江、七猫及刺猬猫的榜单样本，比较题材热度、发现新书信号，并结合写作条件选择题材。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running scrapers through a browser session could expose unrelated signed-in pages to the scraping workflow.

Mitigation: Use a dedicated browser profile without unrelated sensitive sessions.

Risk: Scraping writes ranking data and reports into the workspace and may collect incomplete rankings.

Mitigation: Use a dedicated output folder and check collection coverage before relying on topic recommendations.

## Reference(s):

- [Skill metadata link (not verified import provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [起点榜单采集与分析](references/platform-qidian.md)
- [番茄榜单采集与分析](references/platform-fanqie.md)
- [晋江榜单采集与分析](references/platform-jjwxc.md)
- [七猫榜单采集与分析](references/platform-qimao.md)
- [刺猬猫榜单采集与分析](references/platform-ciweimao.md)
- [选题决策指南](references/topic-decision.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown reports, Topic recommendations]

**Output Format:** [Markdown and local Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish observed ranking data from historical topic hypotheses and note missing samples.]

## Skill Version(s):

1.1.23 (source: ClawHub release metadata; skill frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
