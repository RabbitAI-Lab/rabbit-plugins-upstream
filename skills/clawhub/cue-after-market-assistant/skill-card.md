## Description:

用 Cue 在 10 分钟内自动生成深度市场复盘报告，穿透涨跌逻辑与资金流向，帮助用户快速理解当天市场、持仓影响和次日关注信号，并可指定板块深挖主线。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and personal investors use this skill after the A-share market close to generate structured recap reports, review capital flows and sector drivers, understand possible holdings impact, and prepare next-day watch points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external Cue runner that can change outside the reviewed skill package.

Mitigation: Review the runner source and current update before use, and do not install it in environments where unpinned remote code is not acceptable.

Risk: Generated Cue share links may expose financial context to anyone who receives the link.

Mitigation: Avoid including confidential holdings or client information, omit the share link when the user requests it, and forward links only to trusted recipients.

Risk: Market recap output depends on Cue service availability and external financial data source timing.

Mitigation: Treat reports as informational, check cited sources and data timestamps, and verify material claims before making investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-after-market-assistant)
- [Cue platform](https://cuecue.cn/)
- [Cue API key management](https://cuecue.cn/hub/api-key)
- [Cue runner source referenced by the skill](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror referenced by the skill](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown market recap report with shell command snippets and optional Cue share link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report may be saved locally as Markdown and can be converted to Word or PDF when pandoc is available.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
