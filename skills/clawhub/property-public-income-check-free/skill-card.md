## Description:

A free local checker for residential community public-income ledgers that recomputes owner-share amounts, checks subtotals and totals, and flags duplicate, blank, invalid-rate, or negative entries with source line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External property managers, homeowners' committees, and audit reviewers use this skill before public disclosure or review to recalculate residential community public-income ledger rows and identify arithmetic or data-quality issues. It is intended for supplied ledger checks, not legal or audit opinions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill text includes a paid upgrade path and external payment/onboarding instructions outside the free local checker.

Mitigation: Use the free checker independently, and review any paid upgrade or onboarding flow separately before allowing an agent to start it.

Risk: The onboarding text includes an unpinned `npx ... @latest` installation command.

Mitigation: Do not run unpinned runtime installation commands unless the user explicitly requests it at that time and verifies the source and payment flow.

Risk: Ledger findings can be mistaken for legal, regulatory, or audit approval.

Mitigation: Treat outputs as arithmetic and data-quality checks against supplied rows; review contract terms, local rules, and audit requirements separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/property-public-income-check-free)
- [SkillPay storefront referenced by the skill](https://skillpay.alipay.com/public/tokendidi)
- [Purchase instructions referenced by the skill](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide referenced by the skill](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or text summaries with optional JSON result objects from local Node execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields instead of a conclusion.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
