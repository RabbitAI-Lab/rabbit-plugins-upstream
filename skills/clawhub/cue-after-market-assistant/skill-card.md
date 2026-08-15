## Description:

用 Cue 在 10 分钟内自动生成深度市场复盘报告，帮助用户理解市场涨跌逻辑、资金流向、持仓影响和次日关注信号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and individual investors use this skill after market close to generate a structured recap covering index moves, market drivers, capital flows, sector rotation, portfolio relevance, and next-day watch items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portfolio details, watchlists, or account-related text entered into the query may be sent to Cue's external service.

Mitigation: Avoid including sensitive personal holdings, proprietary watchlists, or account information unless the user is comfortable sharing that text with Cue.

Risk: Report quality and freshness depend on Cue service availability and the external data sources Cue uses.

Mitigation: Review source links in the generated report and rerun or use the documented manual fallback channels when Cue or a source is unavailable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/panting09266-ai/skills/cue-after-market-assistant)
- [Cue service](https://cuecue.cn)
- [Cue runner source referenced by skill](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror referenced by skill](https://gitee.com/sensedeal/cue-skills)
- [Cue API key page](https://cuecue.cn/api-key)
- [Example Cue report](https://cuecue.cn/share/e48Yoz--t14FjIHxaxxLz)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with shell command snippets and optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write reports to a user-selected Markdown path and optionally convert them to DOCX or PDF with pandoc.]

## Skill Version(s):

1.0.5 (source: server release metadata; SKILL.md frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
