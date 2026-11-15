## Description:

用于分析小红书热榜和相关热门笔记样本，并将趋势信号整理为可执行的选题建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者和社媒运营人员可用它查看当前小红书热榜、结合热门笔记样本分析趋势，并整理候选选题、标题钩子和内容角度。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security guidance flags CLI authentication setup, credential persistence, and an npx package reference as setup risks; the scan was partial, so its evidence is incomplete.

Mitigation: Confirm the package version being executed, use the documented private local credential flow, keep API keys out of chat and project files, and review the resolved package before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-hot-topic-selection)
- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance]

**Output Format:** [Markdown text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes current hot-list signals, topic candidates, note samples, title hooks, content angles, and next steps; conclusions are limited to the returned public results.]

## Skill Version(s):

0.1.15 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
