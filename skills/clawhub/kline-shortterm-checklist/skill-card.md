## Description:

K线超短线选股 helps agents screen A-share short-term trading candidates, check 96-principle buy and hold discipline, evaluate bottom K-line patterns, and generate structured screening reports from public market data plus required human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handm-735](https://clawhub.ai/user/handm-735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to screen A-share watchlists or individual stock codes against short-term technical-analysis rules, then produce a disciplined pre-trade or holding review. It is intended as a research and review aid, not investment advice or an automated trading system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may overinterpret stock-screening reports as investment advice.

Mitigation: Treat outputs as research aids only; require human review, risk tolerance checks, position sizing, and stop-loss discipline before any real trading decision.

Risk: The scripts fetch public market data from Chinese finance sites and write output files in the current directory.

Mitigation: Run the skill in an expected workspace, review generated files before relying on them, and confirm network data sources are acceptable for the deployment environment.

Risk: Future versions may add automated trading or brokerage/API account access.

Mitigation: Review future releases carefully before upgrade and do not provide brokerage credentials unless the added behavior has been audited and approved.

Risk: Some checks, including major shareholder reduction and negative announcement review, are not automated in the current artifact.

Mitigation: Require manual review of relevant announcements and company disclosures before treating a candidate as cleared.

## Reference(s):

- [K线短线选股检查清单](references/checklist.md)
- [K线形态规则](references/kline_patterns.md)
- [ClawHub Skill Page](https://clawhub.ai/handm-735/skills/kline-shortterm-checklist)
- [Tencent Finance](https://finance.qq.com/)
- [Sina Finance](https://finance.sina.com.cn/)
- [Eastmoney Quote](https://quote.eastmoney.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance, JSON screening data, and fixed-layout HTML dashboard reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write candidates.json, kline_data.json, and a dated HTML screening report in the current directory.]

## Skill Version(s):

1.0.3 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
