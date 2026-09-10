## Description:

用 Cue 一键对公募基金做全维度深度尽调，包括基金经理画像、业绩归因、风格一致性、风险指标、费率与规模分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Fund investors, wealth advisors, and FOF researchers use this skill to run Cue-based due diligence on public A-share equity mutual funds before selection, diagnosis, manager comparison, or replacement screening decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fund research prompts are sent to Cue/cuecue.cn and related data providers.

Mitigation: Do not include private account numbers, credentials, nonpublic client information, or other sensitive data in queries.

Risk: Cue credentials and resumable session state are stored locally.

Mitigation: Protect ~/.cue/config.json as a secret-bearing file and manage ~/.cue/session/task according to local data-retention policy.

Risk: Fund due-diligence results can be stale, incomplete, or unsuitable as future performance predictions.

Mitigation: Review the report's data cutoff date, compare against current public fund disclosures, and avoid treating the analysis as timing or guaranteed-return advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-fund-due-diligence)
- [ClawHub publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue](https://cuecue.cn)
- [Cue API key](https://cuecue.cn/hub/api-key)
- [天天基金](https://fund.eastmoney.com)
- [晨星中国](https://www.morningstar.cn)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown due-diligence reports with command examples and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cue reports should preserve source results and data cutoff dates; full due-diligence runs may take 2-15 minutes and require a Cue API key.]

## Skill Version(s):

1.0.7 (source: server release evidence, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
