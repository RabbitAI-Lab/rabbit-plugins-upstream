## Description:

当用户需要做抖音账号诊断、抖音账号分析、抖音账号复盘、账号体检、播放低或不推流排查、近期作品表现整理和内容优化方向判断时使用。基于用户提供的抖音主页链接、分享文案或 sec_user_id，整理账号资料和近 30 天作品结果，输出可执行的账号分析报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

抖音创作者和运营人员可用它整理公开账号资料及近期作品表现，形成有证据支撑的账号复盘和内容测试建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account URLs or identifiers are sent to SocialDataX, and requests may consume credits.

Mitigation: Provide only the public account URL or identifier needed for the requested analysis, and review the returned scope before proceeding with additional requests.

Risk: The skill invokes downloaded CLI software, whose package implementation is outside the supplied instruction review.

Mitigation: Use a reviewed, fixed CLI version with limited local access. Store the API key in supported secret storage and keep it out of chat and version control.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Markdown, Text]

**Output Format:** [Markdown account analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account profile summary, recent-post sample, engagement comparisons, content and posting patterns, evidence-based findings, and a 30-day test plan; unavailable metrics are identified rather than inferred.]

## Skill Version(s):

0.1.5 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
