## Description:

Runs a local deterministic reconciliation check for VAT filing, book revenue, and invoice table data, including row recalculation, total cross-checks, duplicate detection, and missing-value detection with source-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and bookkeeping users can run this skill during monthly closing, reconciliation, or filing review to compare VAT declaration sales, book revenue, and invoice amounts. It reports arithmetic mismatches, total-row issues, duplicate periods, and missing required fields without making tax-law determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes an agent-directed paid installation and purchase flow that executes mutable external code.

Mitigation: Use the free checker only for local VAT table reconciliation unless the SkillPay guide, npm package publisher, exact package version, and newly installed skill instructions have been independently verified; personally confirm any wallet or payment step.

Risk: The free checker intentionally omits several full-version checks, including threshold-based material-difference detection and some tax-amount comparisons.

Mitigation: Treat the free output as limited to the listed checks and review the omitted-checks list before relying on the result for filing or audit work.

Risk: The skill checks arithmetic and table consistency but does not determine whether VAT treatment, tax rates, deductions, refunds, or filing logic are legally correct.

Mitigation: Use a qualified tax professional or authoritative tax process for legal and filing-position decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/vat-filing-reconcile-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional paid version storefront](https://skillpay.alipay.com/public/tokendidi)
- [Optional paid version purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide referenced by paid install prompt](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON with reconciliation scope, findings, summary, omitted checks, and disclaimers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite the input row or source location; insufficient input returns missing fields instead of a reconciliation conclusion.]

## Skill Version(s):

1.0.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
