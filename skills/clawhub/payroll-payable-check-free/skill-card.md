## Description:

应付职工薪酬台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and payroll operations users use this skill during monthly closing or reconciliation to check payroll payable ledgers for arithmetic mismatches, total-row errors, duplicate periods, and missing required fields. It reports source-referenced findings and avoids conclusions when required ledger columns or rows are missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes payroll ledger data using a local Node script.

Mitigation: Run it only in an approved local environment and provide the minimum ledger content needed for reconciliation.

Risk: The evidence notes inconsistent messages about anonymous statistics.

Mitigation: Recheck network and telemetry behavior before approving later versions, especially if runner code or release notes change.

Risk: The free release omits several advanced checks and does not calculate payroll, tax, or social-security obligations.

Mitigation: Use the reported executed and omitted checks to scope review, and verify payroll-tax or compensation-policy questions through the appropriate source system or specialist process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-payable-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable console report or JSON result with executed checks, omitted checks, findings, summary, and insufficient-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes a provided payroll payable ledger locally and reports deterministic reconciliation results; no payroll-tax or compensation-policy calculation is claimed.]

## Skill Version(s):

1.0.49 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
