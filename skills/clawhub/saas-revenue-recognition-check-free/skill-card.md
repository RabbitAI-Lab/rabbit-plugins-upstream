## Description:

SaaS订阅收入确认表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations users can use this skill during monthly close, reconciliation, or review workflows to check SaaS subscription revenue-recognition tables for arithmetic, roll-forward, duplicate-row, blank-field, and negative-value issues. It reports only on table-level checks and does not provide accounting or audit assurance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake table-level arithmetic and reconciliation checks for full accounting or audit assurance.

Mitigation: Treat results as deterministic table checks only; review checks_not_run and consult an accountant for revenue-recognition judgments beyond table arithmetic.

Risk: The free release omits several checks that are listed as outside this package's executed scope.

Mitigation: Review the reported checks_not_run before relying on the output, especially for service-period mismatch, negative deferred-balance, and total-recognition issues.

Risk: Input that lacks required SaaS revenue-recognition table columns cannot support a finding.

Mitigation: Provide the table with required headers and review any insufficient-input response before making operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/saas-revenue-recognition-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, guidance]

**Output Format:** [Markdown instructions and command output; optional JSON result output from the local Node.js runner]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows when checks run; insufficient input returns missing requirements instead of a conclusion.]

## Skill Version(s):

1.0.42 (source: server-resolved release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
