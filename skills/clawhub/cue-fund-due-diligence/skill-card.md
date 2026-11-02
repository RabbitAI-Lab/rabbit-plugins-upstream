## Description:

用 Cue 一键给一只基金做全维度深度体检——基金经理画像、业绩归因、风格一致性、风险指标、费率与规模，告诉你"这只基金的历史业绩是靠运气还是靠能力"，买之前心里有底。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individual fund investors, financial advisers, and fund researchers use this skill to review public A-share equity funds, including manager history, performance attribution, style consistency, risk measures, holdings, fees, and fund size. It produces historical research to support a user's own review; it does not predict future returns or provide timing advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions ask users to paste a Cue API key into chat despite conflicting privacy assurances.

Mitigation: Configure the key locally in a protected configuration file or through CUE_API_KEY, and rotate any key already shared in chat.

Risk: Research queries are sent to Cue, and the skill asks agents to install or update an external runner before executing it.

Mitigation: Tell users that queries reach Cue, and review a fixed runner version before executing downloaded code.

## Reference(s):

- [Cue](https://cuecue.cn)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-fund-due-diligence)
- [Eastmoney Fund](https://fund.eastmoney.com)
- [Morningstar China](https://www.morningstar.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Configuration guidance, Shell commands]

**Output Format:** [Structured Markdown fund due diligence report with setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers public A-share equity funds; findings depend on available public data and Cue service status.]

## Skill Version(s):

1.0.12 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
