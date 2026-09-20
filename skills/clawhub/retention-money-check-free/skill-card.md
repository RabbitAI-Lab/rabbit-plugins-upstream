## Description:

A Chinese-language, local Node.js checker that recomputes construction retention-money ledger rows, validates totals, flags duplicate or incomplete entries, and cites the source ledger line for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Construction project accountants, cost staff, and owner-side finance teams use this skill to check copied retention-money ledger text during periodic settlement, final settlement reconciliation, and warranty-expiry refund review. It provides arithmetic and formatting assistance, not a complete financial audit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free version does not check overdue refunds, contract-rate legality, deduction reasonableness, early refunds, or interest and financing impacts.

Mitigation: Treat results as arithmetic and formatting assistance, review the listed omitted checks, and verify contracts and source documents before making financial decisions.

Risk: The checker is designed for Chinese-language copied ledger text and may not cover unsupported file formats or incomplete table headers.

Mitigation: Use tab-delimited ledger text with the required headers, review missing-input messages, and compare every cited source line against the original ledger.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/retention-money-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [Artifact SKILL.md](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable Chinese text or JSON containing scope, findings, summary, omitted checks, and source line references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local ledger text input; material-insufficient cases return missing-field guidance instead of conclusions.]

## Skill Version(s):

1.0.49 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
