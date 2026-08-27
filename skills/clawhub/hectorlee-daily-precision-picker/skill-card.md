## Description:

每日精选1-3只股票的四层漏斗策略系统，从量价形态初筛池出发，依次通过量价二次过滤、基本面安全排雷、资金流向打分、板块与形态质量打分，最终输出精选/优选/关注池三层分级结果，选不出则空仓。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to screen China A-share stock candidates through a four-layer funnel that combines volume-price signals, fundamental risk filters, fund-flow scoring, and sector or pattern quality. The resulting tiers support market research workflows and should be treated as informational screening output, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found that helper code can construct shell commands from unvalidated stock-code inputs, creating local command-execution risk.

Mitigation: Run only on controlled candidate lists, validate stock codes such as sh/sz plus six digits before execution, and replace shell-command strings with fixed argument arrays.

Risk: The skill produces stock-screening output that may be mistaken for investment advice.

Mitigation: Present results as informational market-screening signals, include the skill's not-investment-advice disclaimer, and require human review before any trading decision.

Risk: External market, fund-flow, finance, and sector data may be unavailable or incomplete during screening.

Mitigation: Surface data-availability status in the report and downgrade or skip affected dimensions instead of treating missing data as a positive signal.

## Reference(s):

- [Research Findings](references/research_findings.md)
- [ClawHub Skill Page](https://clawhub.ai/xiyanjun/skills/hectorlee-daily-precision-picker)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports and optional structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces tiered stock-screening results with data-availability notes and operational guidance.]

## Skill Version(s):

2.2.1 (source: frontmatter, manifest, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
