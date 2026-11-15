## Description:

当用户需要做抖音账号诊断、抖音账号分析、抖音账号复盘、账号体检、播放低或不推流排查、近期作品表现整理和内容优化方向判断时使用。基于用户提供的抖音主页链接、分享文案或 sec_user_id，整理账号资料和近 30 天作品结果，输出可执行的账号分析报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and social media teams use this skill to review a Douyin account profile and recent public posts, then prepare an evidence-based performance report and low-risk content tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill repeatedly runs an automatically downloaded, unpinned CLI release; if compromised, it could access credentials or other files available to the user.

Mitigation: Confirm the package and release before use, and run it with access limited to the files and credentials needed for the request.

Risk: Account identifiers or share text may be sent to SocialDataX as part of a request.

Mitigation: Submit only the intended account information and omit unrelated or sensitive text.

Risk: The security scan was partial because some referenced paths were missing, so its results are incomplete.

Mitigation: Treat the scan as incomplete and review the full release contents before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-account-analysis-report)
- [SocialDataX API key access](https://socialdatax.com/ai?from=clawhub)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown account analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes returned account details, a recent post sample, engagement indicators, observed content patterns, evidence-based diagnosis, and a 30-day test plan; unavailable fields are identified rather than invented.]

## Skill Version(s):

0.1.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
