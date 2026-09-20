## Description:

仓储费结算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Business operators and finance teams use this skill to check warehouse fee settlement tables for arithmetic mismatches, total-row errors, duplicate customer or batch entries, and blank placeholders. It is intended for worksheet checking, not for contract interpretation, legal advice, or rate-compliance decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic worksheet findings as contract, legal, or rate-compliance advice.

Mitigation: Use the output as a reproducible arithmetic check and have qualified staff verify contract terms, free-storage periods, rates, and legal conclusions.

Risk: Documentation is inconsistent about anonymous usage statistics.

Mitigation: Review the release behavior before deployment and run in a network-restricted environment if anonymous telemetry would be unacceptable.

Risk: The free edition omits some validation checks, including negative rate, non-positive quantity, day-range, and overdue-day consistency checks.

Mitigation: Treat the included findings as limited to the stated free checks and run separate controls for omitted validations before relying on settlement results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/warehouse-fee-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON containing checks, findings, summaries, missing-input guidance, and cited source line numbers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs deterministic local checks over pasted text or JSON input; sample mode demonstrates the expected worksheet structure.]

## Skill Version(s):

1.0.29 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
