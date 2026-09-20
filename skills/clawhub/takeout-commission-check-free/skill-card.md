## Description:

Checks Chinese food-delivery platform monthly statements by recalculating commission, merchant-borne delivery fees, activity subsidies, merchant net payout, totals, duplicates, and missing fields with line-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External restaurant operators, accounting staff, and advisors use this skill after receiving monthly Meituan, Ele.me, or Douyin takeout statements to check arithmetic consistency before settlement. It highlights recalculation mismatches, total-row discrepancies, duplicate rows, and missing required fields without making contract-rate, legal, or platform-policy determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic findings as proof of a contract, platform-policy, or legal violation.

Mitigation: Present results as recalculations of the supplied statement only and review contract terms, platform rules, and legal positions separately.

Risk: Insufficient or malformed billing text can prevent checks or create misleading expectations about coverage.

Mitigation: Require a recognizable table with headers and line items; when required fields are missing, return missing-input guidance rather than a clean result.

Risk: The artifact help text advertises a --no-stats option that the security guidance says is not implemented.

Mitigation: Do not rely on or document that flag as a control; use the server security finding that the inspected package shows no telemetry code to disable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/takeout-commission-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable text or JSON report with line-cited findings, summary counts, executed checks, omitted checks, and missing-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns arithmetic checks only; it does not validate contracts, platform policies, legal claims, or special settlement rules.]

## Skill Version(s):

1.0.38 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
