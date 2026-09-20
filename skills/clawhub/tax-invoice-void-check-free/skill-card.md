## Description:

发票作废与红冲台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and tax operations users use this skill during monthly close, reconciliation, or inventory checks to review invoice void and reversal ledgers for arithmetic consistency, totals, duplicate invoice numbers, missing required fields, and negative amounts. It is a free local helper and does not determine tax compliance or filing correctness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the free-version output as a full tax or filing correctness review.

Mitigation: State that the skill is a local helper for the disclosed free checks and does not cover declaration-versus-ledger reconciliation or tax filing correctness.

Risk: The package discloses that several compliance-oriented checks are not included in the free version.

Mitigation: Review the listed checks not run on every output before relying on the result, especially when cross-month voiding, void-rate, missing reason, or declaration-reconciliation issues matter.

Risk: Documentation inconsistencies about included and excluded checks can confuse the output scope.

Mitigation: Use the security guidance and the runtime scope fields as the source of truth for which checks executed in a given run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tax-invoice-void-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON findings with cited source rows, executed checks, withheld checks, summary counts, and scope notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local ledger text input; reports insufficient input instead of drawing conclusions when required columns or rows are missing.]

## Skill Version(s):

1.0.53 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
