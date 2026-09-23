## Description:

Finance Radar helps agents analyze stocks and cryptocurrencies using Yahoo Finance data, including financial analysis, valuation modeling, and automated report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to request stock or cryptocurrency analysis, valuation modeling, finance summaries, and automated report-style outputs from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad read, write, and command execution authority while describing automation beyond finance analysis.

Mitigation: Install only in a controlled finance-analysis workflow, limit workspace access, and require explicit user confirmation before file changes, shell commands, or API calls.

Risk: Financial analysis outputs may be incomplete, stale, or unsuitable for investment decisions without review.

Mitigation: Treat outputs as decision support, verify market data and assumptions against trusted sources, and require qualified human review before acting on financial recommendations.

Risk: The skill may use API keys or external services during finance workflows.

Mitigation: Provide only the minimum required credentials, keep secrets out of source control and logs, and rotate credentials if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/finance-radar)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-shaped results and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request ticker symbols, processing mode, retry count, and skipped steps; outputs may include analysis reports, configuration notes, and execution logs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
