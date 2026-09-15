## Description:

Checks FX settlement worksheets by recomputing book-base amounts, settlement amounts, FX gain or loss, received amounts, totals, duplicate document IDs, and blank fields, with source line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations users can use this skill to check copied or JSON-wrapped FX settlement worksheet text for arithmetic mismatches, reversed FX gain or loss signs, inconsistent received amounts, incorrect totals, duplicate document IDs, and missing fields. It is intended for local worksheet checks and does not provide accounting policy, tax, hedging, period-end remeasurement, or spreadsheet-file parsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation includes an optional paid upgrade flow that uses an unpinned `npx ...@latest` install command and may initiate a purchase workflow.

Mitigation: Use the free local checker independently from the paid upgrade path, and only run upgrade commands or authorize payment after verifying the SkillPay source, package version, merchant details, and local execution risk.

Risk: The checker is limited to the free local checks and does not evaluate accounting policy, tax treatment, hedging, period-end remeasurement, non-positive rates or amounts, or XLSX and bank receipt files.

Mitigation: Provide tabular text with the required headers, review omitted checks before relying on results, and escalate policy, tax, hedging, or unsupported file-format questions to the appropriate reviewer or tool.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/fx-settlement-check-free)
- [Optional paid upgrade shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON findings with worksheet line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires tabular text with recognized FX settlement headers; does not read XLSX or bank receipt files directly.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
