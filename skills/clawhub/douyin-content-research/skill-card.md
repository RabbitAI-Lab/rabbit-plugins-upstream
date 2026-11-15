## Description:

当用户需要做抖音内容研究、抖音选题、热点观察、竞品内容对比、趋势判断或素材整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营人员、品牌调研人员和创作者可用它查看抖音热榜、搜索内容样本并比较竞品或趋势。它整理排名和热度信号、标题、作者、链接或内容 ID，并提供可继续研究的角度。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The changing, unpinned CLI package could access credentials available in its execution environment; the scan found no confirmed malicious behavior.

Mitigation: Review and pin the CLI version before installation, and only run it in an environment whose available credentials you are comfortable exposing to that CLI.

Risk: Search terms are sent to SocialDataX, and the scan reports no privacy disclosure for that data flow.

Mitigation: Avoid sensitive search terms and review SocialDataX's privacy information before use.

Risk: The scan was partial because several local references could not be resolved, leaving evidence about those references incomplete.

Mitigation: Review the referenced materials and the pinned package before installation.

## Reference(s):

- [SocialDataX AI and API key information](https://socialdatax.com/ai?from=clawhub)
- [抖音内容研究 on ClawHub](https://clawhub.ai/devinchen2014/skills/douyin-content-research)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Markdown research summaries based on JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include trend rankings, content samples, authors, links or IDs, available metrics, and follow-up angles.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
