## Description:

用 Cue 分析热门赛道与 A 股上市 ETF，涵盖赛道全景、ETF 对比、持仓穿透和估值水位。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

个人 ETF 投资者、理财经理和投顾使用此技能比较 A 股上市的行业与主题 ETF，查看持仓、估值和赛道风险，辅助研究决策；不提供具体买卖时点建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs externally maintained Cue runner code that may change between uses.

Mitigation: Review the runner before execution and pin a reviewed revision instead of automatically pulling updates.

Risk: Health checks can read the Cue API key from local configuration or the environment, despite the skill's claim that the agent cannot view it.

Mitigation: Inspect key-handling commands before running them, restrict access to the key, and never expose it in logs or chat.

Risk: Research prompts are sent to cuecue.cn, and session and report files are stored locally.

Mitigation: Avoid confidential queries, review the service's data-handling terms, and protect local session and report files.

Risk: ETF analysis depends on public data availability and the Cue service and may be incomplete or out of date.

Mitigation: Check material figures against current fund and index disclosures before making investment decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/panting09266-ai/skills/cue-sector-etf)
- [Cue research service](https://cuecue.cn)
- [Cue runner referenced by the skill](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown research report with ETF comparison tables and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a Cue report link and local Markdown copy when a report is available; limited to A-share-listed ETFs.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata; bundled SKILL.md says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
