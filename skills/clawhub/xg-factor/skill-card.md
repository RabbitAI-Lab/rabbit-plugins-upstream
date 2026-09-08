## Description:

小果量化因子库 is a Python quantitative factor calculation system that integrates 300+ technical indicators, Alpha factors, and trading signals for single-security analysis and full-market factor generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[li152](https://clawhub.ai/user/li152)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, quantitative researchers, and strategy analysts use this skill to compute technical indicators, Alpha factors, trading signals, and risk/return metrics from local market-data files for research, screening, and backtesting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflows read local market-data files and can write generated factor outputs to local data directories.

Mitigation: Confirm target data paths and output directories before executing copied examples, especially batch or force recalculation workflows.

Risk: Formula-conversion guidance may turn source formula text into runnable Python.

Mitigation: Review converted code and only execute formulas from trusted sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/li152/skills/xg-factor)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Python examples, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of Pandas DataFrame, Excel, JSON, and Parquet factor outputs when the user executes the described local workflows.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
