## Description:

Track deductible expenses year-round with IRS category matching, receipt logging, tax-savings estimates, audit-risk flags, and Schedule C, Schedule A, or CSV exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to track deductible expenses, mileage, and home-office deductions throughout the year, then generate tax-preparation summaries and exports for review by the user or a tax professional.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores sensitive tax and expense records in a local JSON file at ~/.tax_docs.json.

Mitigation: Keep the file backed up and protected, and avoid using the skill on shared accounts unless filesystem permissions are appropriate.

Risk: Expense records can be removed immediately with the delete command.

Mitigation: Review record identifiers before deleting and keep backups of ~/.tax_docs.json before cleanup or tax-filing workflows.

Risk: Tax categorization, savings estimates, and audit-risk flags are general guidance and may not match a user's filing situation.

Mitigation: Review exports and high-risk deductions with a qualified tax professional before filing.

## Reference(s):

- [IRS Deduction Categories Reference](references/irs-categories.md)
- [Audit Risk Factors](references/audit-risk.md)
- [Server-resolved GitHub source](https://github.com/voronindenis5/tax-doc-collector)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/tax-doc-collector)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and local text or CSV export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores tax and expense records locally in ~/.tax_docs.json.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
