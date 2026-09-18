## Description:

A local deterministic checker for accounts-payable provisional ledgers that recalculates provision amounts, reversals, invoice differences, balance roll-forwards, totals, duplicates, blanks, negative amounts, and invoice-status markers with source-line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounts-payable teams use this skill before period close to check provisional ledger arithmetic, totals, missing fields, duplicate document numbers, and invoice-status markers. It reports findings only when the supplied ledger has enough recognizable tabular evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes prompts and links for an external paid-version purchase and installation flow.

Mitigation: Use the free checker as a local ledger-analysis tool unless the user explicitly wants the paid flow; before any paid installation, separately review the installer source, exact package version, payment terms, and authorization steps.

Risk: Ledger conclusions depend on recognizable input columns and complete row data.

Mitigation: Provide the required ledger headers and source rows, preferably tab-separated; treat insufficient-input responses as no conclusion rather than as a clean result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ap-provisional-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable terminal text or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, source line, message, advice, execution scope, and checks not run.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
