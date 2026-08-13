## Description:

用 Cue 对上市公司最新财报做深度分析，从核心数据变动、业务驱动因子、利润含金量、产业链话语权与典型财务信号，产出一份带可回查出处的业绩点评。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Equity research analysts and investment researchers use this skill to quickly turn a public company's latest financial report into a structured earnings review with source links. It supports post-earnings digestion, fundamentals tracking, peer comparison, and draft research materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party Cue API, so company queries and authenticated requests are sent to cuecue.cn.

Mitigation: Use the skill only where sending those queries to Cue is acceptable, and avoid including confidential investment or client information unless approved.

Risk: The skill relies on runner code from the referenced sensedeal/cue-skills source.

Mitigation: Verify the repository source and review installer or runner code before executing it in a trusted environment.

Risk: The skill writes report files to a local output path.

Mitigation: Confirm the requested output path before running the command and review generated reports before sharing them.

Risk: Report quality and timeliness depend on Cue service availability and the external financial data sources used by Cue.

Mitigation: Keep source links in the report and verify material investment conclusions against primary filings or trusted market data before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-earnings-analysis)
- [Cue service](https://cuecue.cn)
- [Cue sample earnings report](https://cuecue.cn/share/FKeQR7E8)
- [Runner source mentioned by the skill](https://github.com/sensedeal/cue-skills)
- [Runner source mirror mentioned by the skill](https://gitee.com/sensedeal/cue-skills)
- [CNINFO filing source](https://www.cninfo.com.cn)
- [Eastmoney financial data](https://data.eastmoney.com)
- [SEC EDGAR filings](https://www.sec.gov/edgar)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown report with source links, plus shell commands and configuration guidance for running Cue and converting reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report can be written to a local Markdown file and optionally converted to Word or PDF with pandoc.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
