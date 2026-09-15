## Description:

用 Cue 在 10 分钟内自动生成深度市场复盘报告，帮助用户理解当天市场涨跌逻辑、资金流向、持仓影响和次日关注信号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and individual investors use this skill after market close to request a structured Cue-generated recap of A-share market moves, capital flows, sector activity, holding relevance, and next-day watch items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send market questions, holdings, or watchlist details to cuecue.cn.

Mitigation: Avoid entering sensitive account details and review what will be sent before running the Cue request.

Risk: The skill relies on an external Cue runner and Cue service that are not included in the artifact for full review.

Mitigation: Review and install the external runner only from the referenced source, and confirm Cue service health before use.

Risk: The artifact promotes Cue links, recurring scheduled use, and credit, referral, or payment paths.

Mitigation: Confirm any scheduled task, payment, referral, or recurring-use setup with the user before enabling it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-after-market-assistant)
- [Cue platform](https://cuecue.cn/)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with source links and optional shell commands for running Cue and converting output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces market recap content through Cue and may include a Cue share link plus a local Markdown report path.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
