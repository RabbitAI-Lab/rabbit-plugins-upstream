## Description:

逐项核对应收对账表的客户余额、账龄分档、合计行、重复客户和空缺项，并让每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, warehouse, and operations staff use this skill during monthly closing, reconciliation, payroll, inventory, and collections workflows to check AR aging table arithmetic, totals, duplicate customers, and blanks with source-line evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags promotional output that steers users toward an external paid installation and purchase workflow.

Mitigation: Use the free checker only when comfortable with that output, and do not copy the paid-upgrade prompt or run `npx ...@latest` commands unless the package source, version, permissions, and payment flow are independently verified in a least-privileged environment.

Risk: The free edition does not run the full set of AR aging checks described for the paid edition.

Mitigation: Treat results as limited to the executed free checks and review the listed withheld and out-of-scope checks before relying on conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ar-aging-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown-style console text with optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; JSON mode is available with --json.]

## Skill Version(s):

1.0.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
