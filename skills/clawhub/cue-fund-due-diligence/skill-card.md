## Description:

用 Cue 一键给一只基金做全维度深度体检，覆盖基金经理画像、业绩归因、风格一致性、风险指标、费率与规模，帮助用户判断历史业绩更可能来自能力还是市场环境。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External fund investors, advisors, and fund researchers use this skill to request Cue-powered due diligence reports for Chinese public equity mutual funds. It supports fund selection, holding diagnosis, fund manager assessment, and replacement-fund comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fund queries and the Cue API key may be sent to cuecue.cn for external processing.

Mitigation: Install and use the skill only when external Cue processing is acceptable, and keep API keys out of shared transcripts and logged shell histories where possible.

Risk: Generated due diligence reports are third-party financial analysis and may contain outdated, incomplete, or misleading conclusions.

Mitigation: Verify important claims against fund disclosures and other reliable sources before making investment decisions.

Risk: Health-check commands can expose operational details or credentials in shared shells or heavily logged environments.

Mitigation: Run diagnostics in a private shell and avoid pasting raw command output that includes secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-fund-due-diligence)
- [ClawHub publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue platform](https://cuecue.cn)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [Eastmoney Fund](https://fund.eastmoney.com)
- [Morningstar China](https://www.morningstar.cn)
- [Howbuy Fund](https://www.howbuy.com)
- [ChinaFOF](https://www.chinafof.com)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance, Configuration]

**Output Format:** [Markdown report with inline shell commands and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports should include the Cue source report link when available and should not invent report links.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
