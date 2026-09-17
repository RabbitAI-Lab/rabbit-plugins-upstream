## Description:

A free deterministic checker for Chinese food delivery platform monthly statements, covering commission, merchant-borne delivery fees, activity subsidies, merchant net payout, total-row reconciliation, duplicate rows, and missing fields with source-line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External restaurant operators and finance staff use this skill after receiving monthly Meituan, Ele.me, or Douyin Takeout settlement statements to recalculate platform commissions, merchant-borne delivery fees, subsidies, merchant net payout, and totals before accepting settlement. The free edition reports only the implemented arithmetic and table-quality checks, and it withholds advanced dispute attribution and appeal wording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags under-disclosed paid-upgrade, dependency-install, and purchase-flow instructions.

Mitigation: Use the local free checker first; do not run the documented npx payment or onboarding command, install dependencies, or authorize payment unless the provider, package, payment flow, and host platform rules have been separately verified.

Risk: The free edition omits advanced checks such as dispute attribution, appeal wording, abnormal-rate checks, negative net payout checks, and order-count checks.

Mitigation: Treat a clean result as limited to the five implemented arithmetic and table-quality checks; do not use it as proof that contract rates, order-level reconciliation, refunds, cancellations, or special settlement cases are correct.

Risk: The checker depends on recognizable tabular headers and text or JSON input, and it does not read .xlsx files or fetch statements from platform backends.

Mitigation: Export or copy a header row and statement rows as tab-delimited text or JSON; when the tool reports insufficient input, treat that as no conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/takeout-commission-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or structured JSON from a local Node.js checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing requirements instead of a conclusion.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
