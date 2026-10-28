## Description:

帮助用户在开盘前了解隔夜全球事件对 A 股的潜在影响，并整理今日值得关注的方向与风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向关注中国 A 股的个人投资者，用于生成盘前简报，梳理隔夜事件、可能受影响的行业方向和风险。报告基于公开信息推断，不构成投资建议。

### Deployment Geography for Use:

China (A-share market)

## Known Risks and Mitigations:

Risk: The workflow uses a Cue API key and an external runner; mishandling either could expose credentials or run unreviewed code.

Mitigation: Configure the key outside chat with directory permissions 0700 and file permissions 0600, review and pin the runner before execution, and keep sandbox protections enabled.

Risk: Recurring reports consume Cue credits.

Mitigation: Enable recurring reports only when wanted and account for their credit use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-pre-market-strategy)
- [Cue API Key setup](https://cuecue.cn/api-key?src=clawhub-pre-market-strategy)
- [Cue billing](https://cuecue.cn/pay)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown pre-market report with source links, plus setup and troubleshooting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize public information and include potential sector impacts and risk notes; they do not provide real-time quotes or buy/sell points.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
