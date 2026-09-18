## Description:

逐项核对预付账款核销台账的逐行复算、合计勾稽、重复和空缺问题，并为结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance staff and operations users use this skill during month-end closing, reconciliation, or inventory checks to verify prepayment offset ledgers for arithmetic mismatches, total-row discrepancies, duplicates, and missing required fields. It is scoped to ledger-internal checks and does not decide commercial reasonableness, impairment, reclassification, foreign-currency treatment, or ERP and bank-statement ingestion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker points users toward an external paid install and purchase flow using mutable remote code.

Mitigation: Treat paid upgrade instructions as optional; do not run the @latest install command or initiate payment unless the source, package, and purchase flow are independently trusted and the user explicitly confirms wallet or payment actions.

Risk: The free version performs a limited subset of checks and may be mistaken for full audit or accounting coverage.

Mitigation: Review the reported checks_not_run and out-of-scope items before relying on the result, and handle accounting judgments or broader audit questions outside this skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/prepayment-offset-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown-style prose or JSON results from local Node commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines when available; insufficient input returns missing-field guidance instead of a ledger conclusion.]

## Skill Version(s):

1.0.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
