## Description:

Checks department budget execution tables locally by recalculating line items, totals, duplicate rows, blank fields, and negative amounts, with findings tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and accounting operations staff use this skill during monthly close, reconciliation, or inventory-style checks to verify department budget execution tables. It helps identify arithmetic mismatches, total-line discrepancies, duplicate department-subject rows, blank placeholders, and negative amount entries without sending materials over the network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill promotes an optional unpinned payment and onboarding command for a separate paid version.

Mitigation: Do not let an agent run the npx payment or onboarding command, install the paid workflow, or initiate a purchase unless the package, vendor instructions, and payment flow have been separately verified in a restricted environment.

Risk: The free version intentionally omits some budget-execution checks, so its output can be mistaken for a complete audit.

Mitigation: Review the listed executed and withheld checks before relying on results, and use a separate review path for out-of-scope checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/department-budget-execution-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional full-version purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Console text or JSON from a local Node.js runner]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include source row references; insufficient input returns missing requirements instead of a conclusion.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
