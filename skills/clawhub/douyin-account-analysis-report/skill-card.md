## Description:

当用户需要做抖音账号诊断、抖音账号分析、抖音账号复盘、账号体检、播放低或不推流排查、近期作品表现整理和内容优化方向判断时使用。基于用户提供的抖音主页链接、分享文案或 sec_user_id，整理账号资料和近 30 天作品结果，输出可执行的账号分析报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向抖音创作者及运营人员，整理公开账号资料与近期作品表现，生成用于复盘和内容优化的账号诊断报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account lookup inputs are sent to SocialDataX and API requests may incur charges.

Mitigation: Use only an intended public profile link or identifier, omit unrelated private text, and proceed only if you trust SocialDataX and accept its API charges.

Risk: Installing the latest package can introduce changes after review.

Mitigation: Prefer a reviewed, pinned package version over @latest.

Risk: A limited sample or missing public metrics can lead to incomplete account conclusions.

Mitigation: Base findings on returned fields and the sampled posts, identify missing metrics, and avoid claims about unreturned views, exposure, or recommendation behavior.

## Reference(s):

- [SocialDataX skill and API key information](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX billing](https://socialdatax.com/dashboard/billing)
- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/douyin-account-analysis-report)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Markdown account analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes account details and a recent-post sample with evidence-based observations and a 30-day test plan; identifies missing metrics and does not infer them.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
