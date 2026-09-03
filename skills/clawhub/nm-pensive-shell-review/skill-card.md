## Description:

Audits shell scripts for correctness, portability, and common pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review shell scripts used in CI/CD pipelines, hooks, wrappers, and build automation for exit-code handling, portability, safety, and maintainability issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad shell and CI-related triggers may activate the skill during adjacent repository discussions.

Mitigation: Confirm the task is actually a shell script review before applying the skill's findings or recommendations.

Risk: Suggested verification and formatting commands may affect repository files if run without checking scope.

Mitigation: Review command targets and flags before running formatters, fix commands, or repository-wide checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-shell-review)
- [ClawHub publisher profile](https://clawhub.ai/user/athola)
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)
- [Exit code patterns](artifact/modules/exit-codes.md)
- [Shell portability](artifact/modules/portability.md)
- [Shell safety patterns](artifact/modules/safety-patterns.md)
- [Shell structure patterns](artifact/modules/structure-patterns.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes file and line references for findings when available, plus an approve, approve with actions, or block recommendation.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
