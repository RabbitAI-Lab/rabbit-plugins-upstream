## Description:

Guides agents in implementing dependency injection in Go with uber-go/dig, including containers, Provide and Invoke, dig.In and dig.Out, named values, value groups, optional dependencies, scopes, Decorate, and graph validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to wire Go applications with uber-go/dig, refactor dependency graphs, validate constructors, and avoid service-locator patterns. It is most useful when a codebase imports go.uber.org/dig or is adopting reflection-based dependency injection at the composition root.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated dependency-injection changes can alter application startup behavior or hide missing providers until invocation.

Mitigation: Review proposed wiring changes, keep the container at the composition root, and validate the production graph in tests with dig.DryRun(true).

Risk: Adopting go.uber.org/dig may add or update a third-party Go module in the target project.

Mitigation: Review go.mod changes, confirm the selected module version and license, and run normal Go tests and vulnerability checks before release.

## Reference(s):

- [pkg.go.dev: go.uber.org/dig](https://pkg.go.dev/go.uber.org/dig)
- [uber-go/dig GitHub repository](https://github.com/uber-go/dig)
- [cc-skills-golang homepage](https://github.com/samber/cc-skills-golang)
- [Advanced uber-go/dig reference](references/advanced.md)
- [uber-go/dig recipes](references/recipes.md)
- [Testing with uber-go/dig](references/testing.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with Go code snippets and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces implementation guidance for agent-authored Go code changes; review generated dependency wiring before applying.]

## Skill Version(s):

1.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
