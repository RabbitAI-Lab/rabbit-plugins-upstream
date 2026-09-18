## Description:

研发费用归集表逐项核对，执行逐行复算、合计勾稽、重复与空缺检测，并为每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Businesses with R&D spending can use this skill during quarterly prepayment and annual settlement workflows to check R&D expense collection worksheets. It helps users recalculate row totals, total rows, unified other-expense caps, duplicate projects, and blank or placeholder fields from local worksheet text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation and default output steer users toward an external AI-assisted install and purchase flow using mutable remote code.

Mitigation: Install only for the free local worksheet checker unless the user separately trusts and reviews the external payment and onboarding system.

Risk: The skill is a free subset and withholds several checks that may matter for R&D super-deduction review.

Mitigation: Treat results as limited to the executed checks and review withheld and out-of-scope checks before relying on the output.

Risk: The checker does not issue tax opinions or determine whether expenses qualify as R&D activities.

Mitigation: Use the findings as worksheet arithmetic and consistency checks, then have qualified personnel assess tax eligibility and applicable deduction ratios.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/rd-expense-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Plain text or JSON findings with source line numbers, summary totals, executed checks, withheld checks, and missing-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against supplied worksheet text; material-insufficient cases return missing fields instead of a conclusion.]

## Skill Version(s):

1.0.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
