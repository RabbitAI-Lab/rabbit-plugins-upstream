## Description:

现金盘点表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Cashiers, store managers, finance staff, and operations teams use this skill to check cash-count tables for arithmetic mismatches, total-row errors, duplicate shifts, missing values, and mismatch between variance signs and variance labels. It is intended as a local table-checking aid and does not determine fraud, audit conclusions, or legal responsibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional upgrade instructions delegate to a payment and installation flow that may run unpinned remote code and initiate a purchase.

Mitigation: Use the free checker only for local cash-count verification unless you have separately verified the SkillPay flow, package version, and purchase terms, and personally approve any wallet or payment step.

Risk: The free release intentionally omits some checks, including threshold-based variance checks, negative cash checks, and strict variance-type value validation.

Mitigation: Treat results as the stated arithmetic and completeness checks only; review the withheld checks before relying on the output for operational decisions.

Risk: Cash-count discrepancies can be misread as proof of cause, fraud, audit conclusions, or legal responsibility.

Mitigation: Use the findings as line-cited table review guidance and route material discrepancies through normal finance, audit, or compliance review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cash-count-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Plain text or JSON findings with source line numbers, summary totals, executed checks, withheld checks, and guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; accepts a JSON input file or pasted cash-count table text.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
