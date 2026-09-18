## Description:

A free deterministic checker for piece-rate wage sheets that recomputes piece wages and payable piece wages, cross-checks totals, and flags duplicate rows, blanks, negative values, and quantity mismatches with source line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business users such as manufacturing, apparel, and electronics assembly payroll staff use this skill before payroll to check piece-rate wage tables for arithmetic and cross-footing errors. It helps identify mismatches in qualified quantity, process rate, piece wage, deductions, top-ups, payable wage, totals, duplicate rows, blanks, and negative values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid upgrade prompts can lead users toward remote payment tooling and a separate product installation.

Mitigation: Review the payment flow before use and do not run the paid-upgrade npx installer or authorize purchases unless the SkillPay and Alipay tooling are independently trusted.

Risk: The checker does not provide labor-law or payroll compliance advice.

Mitigation: Use its findings only for arithmetic and table-internal reconciliation, and route compensation policy or legal questions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/piece-rate-wage-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands, plus optional JSON results from the local checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields instead of conclusions.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
