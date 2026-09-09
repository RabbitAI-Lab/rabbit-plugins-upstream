## Description:

用 Cue 查询和分析上市公司股权激励计划，覆盖公开披露的 A 股上市公司激励方案要素、实施效果和同行对比。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

上市公司董秘、HR、投资者、分析师和咨询顾问 use this skill to research public-company equity incentive plans, compare peers, and assess incentive-plan competitiveness and reasonableness. It is intended for publicly disclosed listed-company data, not private-company grants or personal option records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends company research queries and a Cue API key to Cue's external service.

Mitigation: Use it only when sending those queries to cuecue.cn is acceptable, and manage the Cue API key according to your organization's credential handling rules.

Risk: The skill depends on a separate Cue runner installation outside the reviewed Markdown artifact.

Mitigation: Verify the runner source and installation before use, and review runner updates separately from this skill card.

Risk: Outputs depend on Cue service availability and external public data sources.

Mitigation: Run the documented health checks before time-sensitive research and review source links in the generated report.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/cue-equity-incentive)
- [Cue API Key](https://cuecue.cn/hub/api-key)
- [Cue Example Report](https://cuecue.cn/share/TIxQDFYs)
- [Cue Runner Source](https://github.com/sensedeal/cue-skills)
- [Cue Runner Gitee Mirror](https://gitee.com/sensedeal/cue-skills)
- [CNINFO](https://www.cninfo.com.cn)
- [Eastmoney Equity Incentive Data](https://data.eastmoney.com)
- [SEC EDGAR](https://www.sec.gov/edgar)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with source links and optional conversion commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports cover company incentive overview, historical plan elements, implementation effects, peer comparison, competitiveness assessment, and source links.]

## Skill Version(s):

1.1.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
