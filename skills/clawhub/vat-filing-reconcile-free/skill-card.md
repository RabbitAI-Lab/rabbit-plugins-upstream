## Description:

增值税申报与账载开票对照表逐项核对，执行逐行复算、合计勾稽、重复与空缺检测，并让每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance staff, cashiers, and external business users can use this skill during monthly closing, reconciliation, or VAT filing checks to compare book revenue, VAT filing values, and invoice-system values. It reports arithmetic differences, total-row mismatches, duplicate months, blanks, and insufficient input with source-line evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes VAT reconciliation data in a local Node script.

Mitigation: Run it only in an environment where local processing of the supplied VAT table is acceptable, and review inputs before execution.

Risk: Runner help text mentions anonymous usage statistics and a --no-stats option, but security evidence says no such network code or option is implemented.

Mitigation: Treat those statistics and opt-out statements as publisher-documentation issues until the implementation is confirmed or corrected.

Risk: The free edition omits several checks and does not determine whether tax treatment is legally correct.

Mitigation: Use the output as a reconciliation aid, verify omitted checks separately, and consult qualified tax advice for tax-law judgments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/vat-filing-reconcile-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or pretty-printed JSON containing reconciliation results, missing-input messages, executed checks, and withheld checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs over user-provided VAT reconciliation table text or JSON; reports insufficient input instead of fabricating conclusions.]

## Skill Version(s):

1.0.43 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
