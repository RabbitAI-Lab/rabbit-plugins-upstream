## Description:

Checks inventory provision schedules by recalculating row-level provision amounts, roll-forward balances, totals, duplicate rows, blank fields, and negative amounts, with findings tied back to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill during close, reconciliation, or inventory review to check whether an inventory provision schedule is internally consistent. It supports local review of the free declared checks and identifies missing inputs instead of fabricating conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged suspicious because it directs users toward an unpinned paid installation and purchase workflow outside the reviewed package.

Mitigation: Use only the reviewed free local checker unless the paid installation, external package, and separate payment/onboarding skill have been intentionally reviewed and authorized.

Risk: The free checker covers only its declared checks and does not evaluate net realizable value assumptions, inventory cost basis, tax treatment, approvals, disclosures, or the paid-tier checks.

Mitigation: Treat results as internal consistency checks and require finance review for omitted checks, source assumptions, and material accounting judgments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/inventory-provision-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Public paid-upgrade instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON command output, commonly summarized by the agent in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against supplied table text; reports insufficient input rather than asserting no issues when required material is missing.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
