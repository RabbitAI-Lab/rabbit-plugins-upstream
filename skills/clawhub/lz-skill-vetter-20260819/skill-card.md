## Description:

LZ Skill Vetter Pro audits OpenClaw skills across security, performance, and quality rules, producing human-readable or JSON findings for pre-install review and CI checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill before installing, publishing, or batch-checking OpenClaw and ClawHub skills to flag security, performance, and quality issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Safe-pattern exemption behavior can suppress risky lines from scanner reports, including hidden Markdown suppressions.

Mitigation: Review exemption behavior and inspect suspicious suppressions before relying on this scanner for installation decisions.

## Reference(s):

- [LZ Skill Vetter Pro on ClawHub](https://clawhub.ai/zuoyunlai/skills/lz-skill-vetter-20260819)
- [Audit Protocol](references/audit_protocol.md)
- [Output Format Reference](references/output_format.md)
- [Pattern Library Reference](references/patterns.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and optional text or JSON audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can emit CI-oriented exit codes for pass, warning, or fail outcomes.]

## Skill Version(s):

2.1.1 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
