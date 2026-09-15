## Description:

仓储费与超期费核对（免费）在本地逐行复算仓储费、超期费、应结合计和合计行，并标出重复、空缺及带原文行号的核对结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance, operations, and warehouse reconciliation users can use this skill to check warehouse fee settlement tables for arithmetic mismatches, totals, duplicate customer or batch entries, and blank placeholders. The free release is scoped to the checks declared by its local checker and does not replace contract, rate, or legal review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags an agent-ready, unpinned external payment and installation workflow in the documentation.

Mitigation: Do not run the SkillPay installer, install the paid onboarding skill, or authorize a purchase unless the package, source, payment page, merchant, and newly installed skill have been independently verified.

Risk: The free checker intentionally omits listed paid-tier validations, so a successful run is not a complete warehouse-fee audit.

Mitigation: Treat results as limited to the free checks and separately review withheld validations, contract terms, free-storage-period rules, rates, and legal questions.

Risk: Incomplete or unrecognized input could otherwise be mistaken for a clean reconciliation result.

Mitigation: Provide settlement-table headers and rows in the expected text or JSON format; the runner should return insufficient-input guidance instead of a conclusion when required material is missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/warehouse-fee-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay paid-upgrade shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing-material guidance rather than a no-issues conclusion.]

## Skill Version(s):

1.0.3 (source: evidence.json release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
