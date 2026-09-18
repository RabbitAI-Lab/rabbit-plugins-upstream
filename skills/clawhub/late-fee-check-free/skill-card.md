## Description:

A Chinese-language local Node.js skill that checks late-payment surcharge tables for row arithmetic, total reconciliation, duplicate rows, blank fields, and source-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during month-end close, reconciliation, or tax repayment review to locally check Chinese late-payment surcharge tables. It produces source-cited findings for arithmetic, date-difference, total, duplicate, and blank-field issues, while declining to conclude when required table material is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release steers users or agents toward an unpinned external SkillPay installer and purchase workflow for a paid version.

Mitigation: Do not run the SkillPay npx command, install onboarding payment tooling, or initiate a purchase unless the package version, source, and payment flow are separately verified and the user personally confirms any wallet or payment step.

Risk: The free checker intentionally omits documented paid-version checks, so a clean result does not cover every listed late-fee anomaly.

Mitigation: Treat results as limited to the free checks reported by the tool and review the checks_not_run and out-of-scope items before relying on the conclusion.

Risk: Tax late-fee calculations can depend on legal or tax-authority determinations outside the table arithmetic.

Mitigation: Use the skill for table reconciliation only and confirm obligation start dates, exemptions, refunds, disputes, and jurisdiction-specific treatment with authoritative tax guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/late-fee-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay storefront referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [Purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON emitted by a local Node.js command.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-supplied table text; reports insufficient input instead of fabricating conclusions.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
