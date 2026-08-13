## Description:

Generates in-depth A-share equity investment reports with company profiles, business breakdowns, financial forecasts, SOTP valuation, investment rationale, trading plans, multidimensional analysis, risk notes, and summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiu-chuan](https://clawhub.ai/user/jiu-chuan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to generate structured A-share company investment report drafts from one or more company names. The reports are intended for research support and include source-sensitive financial assumptions, valuation discussion, trading-plan tables, and a disclaimer that they are not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on brief company-name prompts and generate financial analysis with ratings, target prices, and trading plans.

Mitigation: Confirm the user requested an investment report, preserve the report disclaimer, and require user review before treating any generated content as decision support.

Risk: Generated reports depend on current market data, institution forecasts, and web search results that can be incomplete, stale, or inconsistent.

Mitigation: Cite sources in the report, compare multiple sources for material claims, and have the user verify dates, prices, forecasts, and valuation assumptions.

Risk: The skill writes Markdown files to the workspace, using the root directory when no target folder is specified.

Mitigation: Confirm the output location for batch jobs and review generated filenames before relying on or sharing the files.

## Reference(s):

- [Report template](artifact/references/template.md)
- [ClawHub skill page](https://clawhub.ai/jiu-chuan/skills/investment-report)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report filenames follow the pattern {primary business}_{company short name}_investment report.md; batch requests may produce multiple Markdown files.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
