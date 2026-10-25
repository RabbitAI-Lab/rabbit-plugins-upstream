## Description:

Cleans and analyzes local UTF-8 CSV or TSV files, producing exact decimal summaries, optional explicitly grouped totals, and formula-safe exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data analysts use the workbench to clean local CSV/TSV files and review duplicate, missing-value, decimal, and explicitly grouped amount summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default duplicate removal can remove legitimate repeated transactions.

Mitigation: Confirm the duplicate policy before processing; use the keep-duplicates option when repeated rows must remain.

Risk: Formula-safe export prefixes formula-shaped cells, including negative numbers, with apostrophes that may change spreadsheet display.

Mitigation: Review protected values in the exported CSV before relying on spreadsheet display or downstream processing.

## Reference(s):

- [MochiLab CSV Workbench on ClawHub](https://clawhub.ai/hznetnewpower/skills/mochi-csv-workbench)
- [MochiLab](https://mochilab.bz)

## Skill Output:

**Output Type(s):** [CSV files, JSON, Markdown, Analysis]

**Output Format:** [Cleaned CSV plus JSON and Markdown reports; exact decimal totals are represented as strings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source files; duplicate handling and amount grouping are policy-driven, and distinct currency labels are not combined.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
