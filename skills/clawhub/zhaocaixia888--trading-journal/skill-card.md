## Description:

Record and manage futures/stock trades with standardized templates, calculate P&L, analyze performance, search entries, and export journals in Markdown or CSV.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaocaixia888](https://clawhub.ai/user/zhaocaixia888)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to maintain local trading journals, calculate realized P&L, summarize trading performance, search notes, and export records for review or spreadsheet analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Journal date handling can allow unsafe file paths.

Mitigation: Validate journal dates as strict YYYY-MM-DD values before reading, writing, updating, or deleting journal files.

Risk: CSV exports can contain unsafe spreadsheet formulas from trade notes or imported trade data.

Mitigation: Sanitize CSV cells before opening exports in spreadsheet software and treat external trade data as untrusted.

Risk: Trading journal outputs may be mistaken for financial advice or complete performance assurance.

Mitigation: Use the reports as record-keeping and analysis aids, and independently review calculations and trading decisions.

## Reference(s):

- [Trading Journal Skill Page](https://clawhub.ai/zhaocaixia888/skills/trading-journal)
- [Analysis Metrics Reference](references/analysis_metrics.md)
- [Trade Templates Reference](references/trade_templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, CSV, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local journal files are used for record keeping and exports.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
