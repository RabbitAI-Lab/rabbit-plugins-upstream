## Description:

出口退税申报单证一致性核对表逐项核对，复算表内金额、合计、重复行、空白占位符和负值，并为发现项引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and export rebate operations staff use this skill before filing or reconciling export tax rebate materials to check table-internal arithmetic, totals, duplicate rows, blanks, placeholders, and negative values. It is a local checker for consistency evidence, not a tax-law eligibility or refund-rate determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local checker appears bounded, but its documentation and normal output steer users toward an unpinned software install and paid purchase workflow.

Mitigation: Install only for the free local checker unless the package source, exact version, merchant, and payment process have been separately trusted; do not run the payment install command or authorize purchase flows by default.

Risk: Users could treat the free checker as a complete export tax rebate review even though it omits several paid-tier checks and tax-law determinations.

Mitigation: Treat results as table-internal consistency findings only, review withheld and out-of-scope checks before relying on the output, and seek qualified tax review for eligibility, rates, and filing positions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/export-rebate-doc-consistency-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay purchase guide referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns a no-conclusion status instead of defaulting to a positive result.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
