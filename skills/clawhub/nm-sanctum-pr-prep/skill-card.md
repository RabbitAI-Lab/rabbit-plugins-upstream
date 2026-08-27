## Description:

Prepares pull requests by running quality gates, drafting descriptions, and validating tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to prepare pull requests by reviewing workspace state, running project quality gates, summarizing changes, documenting tests, and drafting a PR description.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quality-gate remediation may change repository files as part of normal PR preparation.

Mitigation: Use the skill from a clean git state and review formatter or lint fixes before committing.

Risk: The skill writes a PR description to a user-specified path.

Mitigation: Choose the output path deliberately and inspect the generated file before using it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-pr-prep)
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)
- [Pull Request Template Structure](modules/pr-template.md)
- [Quality Gates Pattern Reference](modules/quality-gates.md)
- [TodoWrite Patterns for Sanctum](modules/todowrite-patterns.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown PR description with inline shell command references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes the final PR description to the specified path and displays the path and contents for confirmation.]

## Skill Version(s):

1.9.19 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
