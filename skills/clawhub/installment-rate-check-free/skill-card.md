## Description:

分期方案核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operators use this skill to check installment worksheets for nominal fee, payment, annualized rate, IRR, total-row, duplicate, and missing-field inconsistencies. Findings cite source line numbers, and insufficient materials result in no conclusion rather than a default judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional paid-upgrade path runs unpinned remote npm code and follows newly installed skill instructions.

Mitigation: Use the free local checker independently; before any paid upgrade, verify the package source, version, publisher, and payment flow, and require the user to confirm wallet authorization or payment.

Risk: Worksheet checks can be incomplete when required table headers or values are missing.

Mitigation: Review the input worksheet before execution and treat insufficient-input responses as no conclusion, not as evidence that the installment plan is correct.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/installment-rate-check-free)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON findings with source line numbers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js; no network, registration, API key, or payment is required for the free checker.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
