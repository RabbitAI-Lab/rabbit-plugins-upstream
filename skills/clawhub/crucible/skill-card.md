## Description:

Use when the user wants a full product delivery pipeline from PM to UX to development to testing, or when building from scratch with quality gates and built-in implement, review, and fix loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yvancheng](https://clawhub.ai/user/yvancheng)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Crucible to orchestrate structured product delivery, code review, testing, and acceptance workflows with staged self-review and gate checks. It is suited for new product builds, front-end/back-end contract alignment, code quality audits, and complex development tasks that benefit from role-based review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can make broad changes to project code, documentation, and tests when used for full delivery tasks.

Mitigation: Invoke it deliberately for substantial delivery work and review generated plans, diffs, tests, and gate reports before accepting changes.

Risk: The packaged command file references a hardcoded Windows Administrator skill path.

Mitigation: Check and adjust the installed command path before use, especially on non-Windows systems or installations under a different user profile.

## Reference(s):

- [Crucible Skill Page](https://clawhub.ai/yvancheng/skills/crucible)
- [Methodology Reference](skill/references/methodology.md)
- [Verification Reference](skill/references/verification.md)
- [Security Checklist](skill/references/security-checklist.md)
- [Tooling Reference](skill/references/tooling.md)
- [Lessons Reference](skill/references/lessons.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with file paths, review reports, code changes, shell commands, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify project documentation, tests, and source files when invoked for delivery workflows.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
