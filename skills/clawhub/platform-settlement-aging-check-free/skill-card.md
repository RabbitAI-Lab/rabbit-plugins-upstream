## Description:

Checks platform settlement and in-transit funds reconciliation tables for row arithmetic, total cross-checks, duplicates, blanks, and negative values, with each finding tied to source material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, treasury, and operations users can run this skill during monthly e-commerce settlement reconciliation to check platform settlement aging and in-transit funds tables. It helps identify arithmetic mismatches, total-row issues, duplicate rows, blanks or placeholders, and negative values while leaving platform policy and accounting judgment to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool is Chinese-language and targets financial reconciliation tables, so users may misunderstand findings if they are not comfortable with the language or accounting context.

Mitigation: Use it with finance staff who can review the source rows and reconcile any flagged items against platform statements and internal accounting policy.

Risk: The free version intentionally omits several advanced checks, including aging-limit, over-settlement, negative in-transit balance, frozen-ratio, and cross-period duplicate-settlement checks.

Mitigation: Treat clean free-tier output as limited to the executed checks and review the listed non-executed checks separately when they matter to the close process.

Risk: Help text mentions anonymous usage statistics even though the inspected security evidence says table data is not sent over the network and that the statistics behavior is not implemented in inspected code.

Mitigation: Review the release package before deployment and confirm network behavior in the installed version if usage telemetry is a policy concern.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/platform-settlement-aging-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON findings with cited source rows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local table checks for the free tier and reports missing required material instead of making unsupported conclusions.]

## Skill Version(s):

1.0.47 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
