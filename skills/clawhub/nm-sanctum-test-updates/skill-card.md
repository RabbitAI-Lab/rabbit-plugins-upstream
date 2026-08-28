## Description:

Updates, generates, and validates tests using git-workspace context and TDD/BDD methodology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to discover test gaps, generate TDD/BDD test scaffolding, update existing tests, and validate test quality after code or execution-markdown changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect code and modify or create test files while applying broad test-generation or test-maintenance workflows.

Mitigation: Use it from a clean git state or disposable branch, review diffs before merging, and run the affected test suite after changes.

Risk: The skill may run test tooling, coverage checks, or mutation testing that can be slow or have side effects in the target workspace.

Mitigation: Run validation in a controlled environment and target specific paths for large or sensitive repositories.

Risk: The artifact references an external Night Market plugin for the full experience.

Mitigation: Vet the external plugin separately before installing or enabling its agents, hooks, or commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-test-updates)
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include test-gap reports, BDD/TDD scaffolding, quality recommendations, and validation commands.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
