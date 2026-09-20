## Description:

车辆保险与保费摊销核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and operations staff use this skill during monthly close or reconciliation to check vehicle insurance premium amortization tables. It recalculates line items, checks totals, detects duplicate or blank placeholder entries, and cites source rows for each finding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation contains inconsistent wording about no-network operation and anonymous statistics, which can confuse users who require strict offline execution.

Mitigation: Review the runner and documentation before deployment; clarify or remove the anonymous-statistics wording if strict no-network assurances are required.

Risk: The checker intentionally covers only the free-tier checks and withholds additional checks listed in the artifact.

Mitigation: Tell users that results cover only the executed checks and should not be treated as a complete insurance, accounting, or contract review.

Risk: The tool returns no conclusion when source table data is insufficient or lacks recognizable headers.

Mitigation: Require users to provide the vehicle insurance amortization table with headers and review missing-input messages before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/vehicle-insurance-amortization-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON findings from a local Node.js checker, with cited source rows and status details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided vehicle insurance amortization table data; returns no conclusion when input is insufficient.]

## Skill Version(s):

1.0.44 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
