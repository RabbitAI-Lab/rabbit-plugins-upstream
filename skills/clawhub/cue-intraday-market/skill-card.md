## Description:

用 Cue 做大盘盘中分析——聚合早盘核心行情，穿透指数表象识别市场真实情绪与资金流向，定位逆势主线与风险雷区，输出盘中观察评论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Traders, analysts, and market observers use this skill to request an intraday market overview through Cue, focusing on early-session conditions, sentiment, capital flows, active themes, risk areas, and a linked Markdown report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Cue's external service and a separately installed runner that the security evidence says should be reviewed.

Mitigation: Review and pin the runner before deployment, and install only from the cited source you have approved.

Risk: Market-analysis prompts and the Cue API key are sent to cuecue.cn during normal operation.

Mitigation: Use only with data appropriate for Cue, store the API key securely, and avoid exposing it in shared logs, screenshots, or shell history.

Risk: When credits are insufficient, the skill directs the agent to present referral and payment options.

Mitigation: Treat payment or referral text as user-facing commercial messaging and present it clearly without retrying or changing the query to bypass the credit failure.

Risk: The report's quality and freshness depend on Cue service availability and external market data sources.

Mitigation: Run the documented health checks before use and keep source links in the delivered report so users can verify time-sensitive claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-intraday-market)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [Cue runner source referenced by artifact](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror referenced by artifact](https://gitee.com/sensedeal/cue-skills)
- [Cue service health endpoint](https://cuecue.cn/api/health)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown market-analysis report with source links, Cue share URL, local report path, and setup or diagnostic shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key, the external Cue runner, and access to cuecue.cn; normal runs may take 2-15 minutes.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
