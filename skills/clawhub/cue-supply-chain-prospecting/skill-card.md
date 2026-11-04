## Description:

用 Cue 沿核心企业客户/供应商/招投标关系链，挖掘产业链上下游可拓展名单——给出每家切入点和可能的金融需求，助力对公客户经理精准拓客。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向对公客户经理及企业拓展团队，从一家具体的核心企业出发，整理其客户、供应商和招投标关系，并形成带有拓展切入点、潜在金融需求和优先级的名单。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup asks the user to share a Cue API key through chat.

Mitigation: Configure the key locally instead, and rotate any key already shared.

Risk: Execution depends on an external runner and Cue service whose behavior was unavailable in this package; queries consume credits.

Mitigation: Review and pin the runner before execution, and check credit use when deciding whether to run a query.

Risk: Promotional follow-ups are described as mandatory in some low-credit flows.

Mitigation: Keep promotional follow-ups optional and retain control over cancellation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-supply-chain-prospecting)
- [Cue platform](https://cuecue.cn)
- [企查查](https://www.qcc.com)
- [天眼查](https://www.tianyancha.com)
- [东方财富行业数据](https://data.eastmoney.com)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Structured Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company relationship map, prospect list, outreach entry points, potential financing needs, priority tiers, and source links; accuracy and freshness depend on Cue and its data sources.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
