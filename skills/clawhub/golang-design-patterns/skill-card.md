## Description:

Provides idiomatic Go design-pattern guidance for constructors, error flow, resource management, resilience, architecture, dependency injection, data handling, and streaming.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and apply idiomatic Go patterns for API construction, initialization, error handling, resource lifecycle, resilience, data streaming, dependency injection, and architecture reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated guidance or code changes can introduce incorrect Go behavior, over-abstraction, or project-specific regressions.

Mitigation: Review proposed changes, inspect diffs, and run the project's Go tests and lint checks before merging.

Risk: The skill can edit Go files and run Go, golangci-lint, and git commands when invoked by a capable host agent.

Mitigation: Use the skill in a controlled workspace, review command output, and apply normal code review before accepting changes.

Risk: Architecture recommendations can be too heavy for small Go projects when project size and team preference are unclear.

Mitigation: Confirm the preferred architecture style and favor the smallest pattern that satisfies the requirement.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-design-patterns)
- [Project Homepage](https://github.com/samber/cc-skills-golang)
- [Architecture Patterns](references/architecture.md)
- [Clean Architecture in Go](references/clean-architecture.md)
- [Data Handling Patterns](references/data-handling.md)
- [Domain-Driven Design (DDD) in Go](references/ddd.md)
- [Hexagonal Architecture (Ports & Adapters) in Go](references/hexagonal-architecture.md)
- [Resource Management Patterns](references/resource-management.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with Go code snippets and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit Go files and run Go, golangci-lint, and git commands when the host agent grants those tools; the skill declares operation on **/*.go paths and requires the go binary.]

## Skill Version(s):

1.2.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
