## Description:

模具与工装摊销台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance and cost-accounting users can run local checks on mold and tooling amortization ledgers before monthly cost close. The skill recalculates stated amortization amounts, checks totals, flags duplicate or incomplete rows, and returns findings with source-line evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may misunderstand the skill as a complete accounting-policy review rather than an internal arithmetic and ledger-consistency check.

Mitigation: Review results as reconciliation evidence only, and separately validate capitalization policy, amortization method, useful life, residual value, and production assumptions.

Risk: Documentation contains inconsistent statements about anonymous usage statistics.

Mitigation: Confirm the current telemetry behavior before deployment, and use documented opt-out controls where required by policy.

Risk: Incomplete or malformed ledger input can lead to missing checks rather than a clean bill of health.

Mitigation: Provide a ledger with recognized headers and required amortization columns, and treat insufficient-input output as no conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/mold-amortization-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and JSON-capable checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; insufficient input returns missing requirements instead of a conclusion.]

## Skill Version(s):

1.0.49 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
