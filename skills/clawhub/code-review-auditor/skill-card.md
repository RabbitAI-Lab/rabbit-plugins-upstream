## Description:

Review codebases for bugs, security issues, architecture/SOLID problems, code smells, justified design-pattern opportunities, anti-patterns, performance, observability, testability, hotspots, and planned refactors without changing code during analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cbbathaglini](https://clawhub.ai/user/cbbathaglini)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to perform evidence-led code reviews across security, reliability, architecture, performance, tests, observability, hotspots, and refactoring plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes generated review artifacts into the reviewed project.

Mitigation: Inspect files under review/<timestamp>/ before committing or sharing them.

Risk: Fix and refactor modes can change source code after a plan or explicit implementation request.

Mitigation: Use analysis modes for review-only work, and run fix/refactor modes only after approving the refactoring plan or explicitly requesting implementation.

Risk: Review findings and suggested changes may be incomplete or mistaken.

Mitigation: Validate important findings against the codebase, tests, configuration, and runtime contracts before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cbbathaglini/skills/code-review-auditor)
- [Publisher profile](https://clawhub.ai/user/cbbathaglini)
- [Review process](references/review-process.md)
- [Refactor planning](references/refactor-planning.md)
- [Reporting examples](references/reporting-examples.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Code, Shell commands, Configuration]

**Output Format:** [Markdown review package with JSON metadata and score files; code, shell commands, and configuration may be proposed or produced in approved fix/refactor modes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates timestamped local review folders under review/<timestamp>/ in the project being reviewed.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
