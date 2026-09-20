## Description:

收款手续费核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations users use this skill to check copied payment-fee worksheet text for fee recalculation errors, total-row mismatches, duplicate channels, and blank or placeholder fields. The skill reports findings with source line references and declines to conclude when required worksheet fields are missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact text states both that checks do not need networking and that a run may perform anonymous usage statistics, creating privacy ambiguity for sensitive finance workflows.

Mitigation: Review the telemetry wording before deployment and avoid giving unrelated or highly sensitive finance files unless the local checker is intended to read them.

Risk: The free release intentionally omits several checks, including fee-rate range checks, negative fixed-fee checks, settlement bounds checks, and threshold-based difference checks.

Mitigation: Treat clean output as confirmation only for the listed executed checks and review withheld or out-of-scope conditions separately.

Risk: The skill cannot evaluate incomplete or unrecognized worksheet inputs and will not infer missing values.

Mitigation: Provide worksheet text with headers for channel, transaction amount, rate, fixed fee, expected fee, billed fee, settlement amount, and difference.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payment-fee-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Console text or JSON containing worksheet findings, summaries, executed checks, skipped checks, and source line references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided worksheet text or JSON input with recognizable payment-fee columns.]

## Skill Version(s):

1.0.31 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
