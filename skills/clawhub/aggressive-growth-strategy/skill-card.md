## Description:

Aggressive Growth Strategy helps agents screen small-cap growth stocks, analyze individual equities, judge market season, and draft staged entry and exit plans using documented market-data workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenxyzcyxpp](https://clawhub.ai/user/chenxyzcyxpp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to produce informational stock screens, equity analysis reports, market posture assessments, and trading-plan guidance for an aggressive growth investing framework. It is intended to support reviewable analysis, not automated trading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run local Python scripts, install market-data packages if dependencies are missing, and make network requests to financial-data providers.

Mitigation: Review scripts and dependency changes before execution, and run the skill in an environment where outbound data-provider access is expected.

Risk: Stock ratings and buy or sell plans may be treated as investment advice or may be misleading if source data is stale, unavailable, or incorrect.

Mitigation: Treat outputs as informational analysis only, verify financial data against authoritative sources, and require human review before financial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenxyzcyxpp/skills/aggressive-growth-strategy)
- [Screening criteria](references/screening_criteria.md)
- [Stock analysis report template](templates/stock_analysis_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON script output, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are informational and depend on external financial-data providers.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
