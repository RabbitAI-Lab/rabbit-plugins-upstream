## Description:

逐项核对租金收缴与欠租台账的表内算术、合计勾稽、重复行、空缺项和负值，并为每条结论提供原文行号与出处。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashiering, property management, and asset management teams use this skill during monthly closing, reconciliation, or ledger review to recalculate rent collection and arrears ledgers before reporting or follow-up. It is intended for table-level consistency checks, not accounting, tax, contract, or legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic ledger findings as accounting, tax, contract, or legal advice.

Mitigation: Use the skill only for the listed ledger arithmetic and consistency checks, and route accounting, tax, contract, or legal interpretations to qualified reviewers.

Risk: The free version omits listed checks, so absence of findings is not a complete rent ledger audit.

Mitigation: Review the reported checks_not_run and out-of-scope items before relying on the result for monthly close, collections, or reporting.

Risk: Insufficient, malformed, or headerless ledger text can prevent checks or narrow the result.

Mitigation: Provide the rent ledger with recognizable headers and review missing-field guidance whenever the skill returns insufficient_input.

Risk: Help text mentions anonymous usage statistics even though no such network code was present in the inspected files.

Mitigation: Review network behavior before deployment if telemetry disclosure is material, and validate that deployed artifacts match the inspected release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/rent-collection-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or pretty-printed JSON with scope, findings, summary, omitted checks, and insufficient-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided ledger text; insufficient or unrecognized input returns missing requirements instead of a consistency conclusion.]

## Skill Version(s):

1.0.42 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
