## Description:

租赁负债摊销表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during monthly close, reconciliation, or review to check lease liability amortization tables for row-level arithmetic, totals, duplicate periods, blanks, and negative amounts. It is intended as a deterministic arithmetic review, not a full lease-accounting validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free version does not perform all lease-accounting checks, including interest-to-discount-rate validation.

Mitigation: Treat results as a deterministic review of the listed checks only, and separately review omitted checks before relying on the table for full accounting conclusions.

Risk: Insufficient or malformed input can prevent a conclusion.

Mitigation: Provide the amortization table with the required columns and review any insufficient-input response instead of treating it as a clean result.

Risk: The skill does not determine lease classification, payment completeness, lease modifications, or business terms.

Mitigation: Have qualified finance or accounting reviewers validate contract terms, discount-rate assumptions, and out-of-scope lease events outside the tool.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/lease-liability-check-free)
- [Skill instructions](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance or JSON findings from a local Node.js checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic arithmetic checks; free version omits the listed advanced lease-accounting checks.]

## Skill Version(s):

1.0.35 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
