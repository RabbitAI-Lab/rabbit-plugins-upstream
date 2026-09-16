## Description:

用 Cue 对个股做短线走势与技术面分析，从量价关系、资金流向、趋势结构入手，计算波动率与最大回撤，产出可复核的走势分析底稿，辅助判断短线的买卖节奏和关键价位。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run Cue-backed short-term technical analysis for individual stocks. It produces a structured report covering price-volume behavior, fund flows, trend structure, volatility, drawdown, support and resistance levels, risks, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends stock-analysis queries to Cue and depends on Cue and external market data sources.

Mitigation: Review the Cue API key requirement before installation, disclose third-party service use to users, and verify market information against independent sources before trading.

Risk: The skill can add Cue share links and present referral or payment instructions when credits run out.

Mitigation: Keep credit, referral, and subscription prompts explicit and optional, and do not let them replace requested analysis or clear error handling.

Risk: Generated technical analysis may be incorrect, stale, or too decisive for trading decisions.

Mitigation: Treat outputs as informational research, preserve source links, and require independent review before making trading decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-technical-analysis)
- [ClawHub publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with source links and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key and a target stock query; completed reports should include the Cue share link when available.]

## Skill Version(s):

1.1.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
