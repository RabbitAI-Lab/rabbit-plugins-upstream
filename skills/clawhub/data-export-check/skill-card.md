## Description:

Data Export Check is a zero-dependency local checklist that pre-screens five data export compliance obligations and reports PASS or FAIL, with optional JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance teams, and agent operators use this skill to run a local pre-screen before moving data to overseas SaaS, cloud, or receiving-party workflows. It helps identify missing checklist obligations such as data classification, separate consent, PIA retention, standard contract or security assessment, and audit trail retention.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable remote install sources may change after this release was reviewed.

Mitigation: Review or pin the exact repository commit or package version before installing, and avoid one-command global installs unless the upstream source is trusted.

Risk: Checklist output can be mistaken for complete legal advice.

Mitigation: Use the result as a preliminary screen only and route key data export decisions to qualified human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/data-export-check)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [CLI text or JSON checklist output with exit codes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit codes indicate PASS (0), FAIL (1), or usage error (2).]

## Skill Version(s):

1.0.0 (source: release metadata; SKILL.md states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
