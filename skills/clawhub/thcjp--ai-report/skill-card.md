## Description:

AI财报分析 helps agents analyze financial report data, generate structured reports, summarize F-score-style indicators, and surface risk warnings from user-provided financial inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and finance teams use this skill to analyze financial statement data, generate reports, evaluate portfolio or transaction risk, and export structured results. It is best suited to user-reviewed financial analysis workflows rather than fully autonomous investment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad execution and financial-data handling authority while its scope is inconsistent.

Mitigation: Review the skill before installation and require explicit confirmation before package installs, command execution, API calls, monitoring, or exports.

Risk: Financial inputs may include sensitive portfolios, private statements, or API-backed account data.

Mitigation: Use only financial data suitable for processing through the agent and avoid connecting sensitive portfolios or private statements until the publisher narrows the privacy scope.

Risk: Financial analysis, risk ratings, and investment-related outputs can be incomplete or misleading.

Mitigation: Require human review before relying on generated analysis for financial decisions or external reporting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-report)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured JSON examples and inline shell or Python commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk ratings, financial analysis summaries, export guidance, troubleshooting steps, and implementation commands for agent workflows.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
