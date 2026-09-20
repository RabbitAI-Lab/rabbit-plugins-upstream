## Description:

物业费计算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Property managers and business operations staff use this skill to check property-fee billing tables and late-fee calculations before sending monthly invoices or collection notices. It recalculates line items, totals, duplicate records, and blanks from user-provided tabular text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billing tables may contain customer, tenant, or unit-level financial information.

Mitigation: Provide only the rows and columns needed for the calculation, consistent with the security guidance.

Risk: The runner text mentions anonymous usage statistics, while security evidence says no network code was found in this version.

Mitigation: Confirm the telemetry messaging during release review and document the expected local-only behavior for operators.

Risk: The free edition omits range checks and contract or legal judgment, so a clean arithmetic result may still miss out-of-scope issues.

Mitigation: Treat output as arithmetic reconciliation only and review contract terms, legal limits, and withheld checks separately.

Risk: Incomplete or unrecognized table input can prevent a conclusion.

Mitigation: Require complete tabular input with recognizable headers before relying on the findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/property-fee-check-free)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable console text or JSON result payload]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields instead of conclusions.]

## Skill Version(s):

1.0.26 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
