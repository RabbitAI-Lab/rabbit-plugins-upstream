## Description:

用于小红书热榜选题、小红书热点选题、小红书热榜分析、小红书热点分析和趋势选题参考。先看当前小红书热榜，再结合相关热门笔记样本，把热榜信号整理成可执行选题，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and social media analysts use this skill to review current Xiaohongshu hot searches and relevant public note samples, then develop timely topic ideas, title hooks, and content angles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX, and calls may use paid credits.

Mitigation: Avoid confidential inputs and set sensible result limits.

Risk: An exposed API key could be misused.

Mitigation: Store the key in a secret store or an untracked local configuration.

Risk: Package updates may change behavior.

Mitigation: Prefer an exact, reviewed CLI version.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-hot-topic-selection)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the current hot list and returned public note samples; results may not cover the whole platform and do not guarantee reach or engagement.]

## Skill Version(s):

0.1.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
