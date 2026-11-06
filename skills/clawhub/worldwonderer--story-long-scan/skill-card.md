## Description:

分析起点、番茄、晋江、七猫等平台的长篇网文排行榜与新书数据，提炼市场趋势和热门题材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

面向网文作者，汇总长篇平台榜单与新书样本，帮助识别重复出现的题材趋势，并结合作者条件形成选题建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-based collection uses the active Chrome profile and its site logins.

Mitigation: Use a dedicated Chrome profile containing only the logins needed for the selected platforms, and review the browser-cdp setup before use.

Risk: Reruns can replace sections in saved local reports.

Mitigation: Review the existing report and confirm the saved results after each rerun.

Risk: Live website behavior and external browser tooling were not verified during static inspection.

Mitigation: Check collection quality and confirm the selected platform pages load as expected before relying on report conclusions.

## Reference(s):

- [起点平台参考](references/platform-qidian.md)
- [番茄平台参考](references/platform-fanqie.md)
- [晋江平台参考](references/platform-jjwxc.md)
- [七猫平台参考](references/platform-qimao.md)
- [刺猬猫平台参考](references/platform-ciweimao.md)
- [选题决策指南](references/topic-decision.md)
- [历史题材候选](references/genre-trends.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Files]

**Output Format:** [Markdown scan reports and topic recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports and topic decisions are saved locally; repeated scans may replace report sections.]

## Skill Version(s):

1.1.25 (source: target release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
