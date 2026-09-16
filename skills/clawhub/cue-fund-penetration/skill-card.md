## Description:

用 Cue 穿透基金组合底层持仓，逐层分析股票、行业和风格暴露，检测重复配置与集中度风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External fund investors, fund advisors, wealth managers, and FOF researchers use this skill to run Cue-based penetration analysis of public A-share mutual fund portfolios. It helps identify overlapping top holdings, sector concentration, style exposure, and rebalancing considerations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends fund-analysis queries and API-key-authenticated requests to Cue's hosted service.

Mitigation: Install it only where hosted Cue processing is acceptable, keep API keys in configured secret locations, and avoid placing sensitive investor details in prompts.

Risk: The skill requires delivery of Cue share links and includes credit, referral, or payment guidance when credits are insufficient.

Mitigation: Review generated share links before distributing them and present credit or payment prompts as vendor account guidance, not neutral investment analysis.

Risk: Fund penetration analysis depends on public fund disclosures and can be delayed or incomplete.

Mitigation: Label report data cutoff dates, verify important findings against current public disclosures, and avoid treating results as real-time holdings or performance predictions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-fund-penetration)
- [Cue service](https://cuecue.cn)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [Cue health endpoint](https://cuecue.cn/api/health)
- [Cue playbook endpoint](https://cuecue.cn/api/playbook)
- [天天基金](https://fund.eastmoney.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown diagnostic report with optional shell command snippets and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a Cue original report link when available; output depends on public fund disclosure data and Cue service availability.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
