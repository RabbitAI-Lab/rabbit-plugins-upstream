## Description:

Checks government subsidy and deferred-income reconciliation tables by recalculating line items, testing totals, detecting duplicates and blanks, and citing source rows for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this free local checker during monthly or annual close to test government subsidy and deferred-income reconciliation tables for arithmetic, roll-forward, duplicate-row, blank-field, and negative-amount issues. It supports review of provided table data but does not make accounting judgments about subsidy classification, recognition timing, tax treatment, or external source documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence security summary says the local checker appears offline but the skill directs users toward installing external payment tooling and initiating a paid-skill purchase.

Mitigation: Use the free checker locally; do not let an agent run the external installer, load new skill instructions, or initiate payment until the package, source, merchant, and purchase terms have been independently verified.

Risk: The free artifact intentionally omits several checks and does not decide subsidy classification, recognition timing, tax treatment, or source-document compliance.

Mitigation: Treat results as table-reconciliation assistance only, review the listed checks not run, and use qualified accounting review for accounting judgments or complete coverage.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/gov-subsidy-deferred-income-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid-version purchase information](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Human-readable report or JSON emitted by a local Node.js checker.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing-field guidance instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
