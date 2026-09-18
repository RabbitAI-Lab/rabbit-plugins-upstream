## Description:

坏账准备计提表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during month-end closing, reconciliation, inventory checks, and audit preparation to check bad-debt provision tables for arithmetic consistency, total reconciliation, duplicates, and missing key fields. The free version runs a defined local subset of checks and reports when input is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary flags that the free local checker also steers users and agents toward an external paid install and purchase workflow that is not needed for the free check.

Mitigation: Use the bundled local checker directly for the free workflow; separately verify any installer package, payment flow, merchant or product IDs, requested permissions, and rollback steps before allowing an agent to initiate paid installation steps.

Risk: The checker intentionally omits several checks that are reserved for a separate full version, so results may not cover all bad-debt provision review needs.

Mitigation: Review the reported checks_not_run and checks_out_of_scope fields before relying on the output, and perform omitted accounting-policy or expected-credit-loss checks through another reviewed process.

Risk: Input that is missing required headers or usable rows does not produce an accounting conclusion.

Mitigation: Provide the complete bad-debt provision table with customer, aging bucket, receivable balance, provision rate, and provision amount columns; treat insufficient_input output as a request for more evidence, not as a pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bad-debt-provision-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [analysis, json, markdown, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON containing executed checks, omitted checks, findings, summary, scope, and source-line references when findings are present.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard-library code; accepts pasted table text or a JSON input file with a text field.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
