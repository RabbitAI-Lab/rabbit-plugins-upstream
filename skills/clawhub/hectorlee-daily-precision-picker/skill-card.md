## Description:

Filters a candidate pool of China A-share stocks through volume-price, fundamental-risk, fund-flow, sector, pattern-quality, and history signals to produce tiered daily screening results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to screen China A-share candidate pools and generate a tiered watchlist report for further human review. The output is a market-screening signal and not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unvalidated stock-code inputs may be used to build local shell commands.

Mitigation: Use only trusted candidate pools, pool files, and upstream signal files; review stock-code values before execution.

Risk: The skill runs local shell/npx commands to fetch stock data.

Mitigation: Install and run it only in an environment where local command execution and the referenced stock-data tooling are acceptable.

Risk: Screening output can be mistaken for investment advice.

Mitigation: Treat results as screening signals for human review and preserve the skill's investment-advice disclaimer.

## Reference(s):

- [Research Findings](artifact/references/research_findings.md)
- [ClawHub Skill Page](https://clawhub.ai/xiyanjun/skills/hectorlee-daily-precision-picker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown-style terminal report with tables, scores, status messages, and risk guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run local shell commands for stock data and can degrade output when upstream data is unavailable.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata; artifact manifest/frontmatter reports 2.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
