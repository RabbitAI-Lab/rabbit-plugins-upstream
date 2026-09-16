## Description:

A free, local overtime pay worksheet checker that recomputes hourly wage conversion, statutory overtime multipliers, line totals, aggregate totals, duplicate people, and blank fields, with each finding citing the source line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

HR and finance users use this skill before monthly payroll to check overtime pay worksheets for arithmetic consistency, missing fields, duplicate people, and total-line discrepancies. It reports missing required inputs instead of making a conclusion when the worksheet cannot be checked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a paid-upgrade path that uses unpinned external tooling and purchase instructions.

Mitigation: Use the free local checker only unless the user deliberately chooses the paid path; verify the vendor, package version, payment terms, and wallet confirmation before any paid install.

Risk: The free edition does not perform every overtime-pay compliance check described by the artifact.

Mitigation: Treat results as checks for the explicitly executed arithmetic and worksheet-consistency items, and review withheld checks separately when full compliance coverage is needed.

Risk: A passing worksheet check can be mistaken for approval of attendance records, overtime authorization, or legal conclusions.

Mitigation: Use the output as an arithmetic and consistency review only; HR, payroll, or legal reviewers should verify source data, approvals, and applicable policy before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/overtime-pay-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable text or JSON findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, source line, message, advice, executed checks, withheld checks, and insufficient-input details.]

## Skill Version(s):

1.0.14 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
