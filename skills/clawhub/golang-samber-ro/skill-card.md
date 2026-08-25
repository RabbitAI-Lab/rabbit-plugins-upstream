## Description:

Guides agents working in Go projects to use samber/ro for reactive streams, event-driven pipelines, hot and cold observables, subjects, operators, plugins, and context-aware error handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when a Go codebase imports or is adopting github.com/samber/ro, or when designing asynchronous event-driven pipelines, real-time processing, and stream composition. It helps choose operators and subjects, write typed pipeline code, handle retries, cancellation, observability, and avoid using ro for finite slice transforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested Go code edits or reactive pipeline designs may introduce incorrect stream behavior, missed errors, or lifecycle leaks.

Mitigation: Review generated changes, keep full observer error handling and cancellation paths, and run the project's Go tests and lint checks.

Risk: When active, the skill may propose or run scoped Go, git, godig, gopls, LSP, or related repository tooling.

Mitigation: Review shell commands before execution and keep tooling scoped to the target repository.

Risk: The skill is not exhaustive documentation for samber/ro APIs or package status.

Mitigation: Check the official samber/ro documentation, pkg.go.dev, and repository references when exact APIs, versions, or vulnerability status matter.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-samber-ro)
- [Publisher Profile](https://clawhub.ai/user/samber)
- [ClawHub Metadata Homepage](https://github.com/samber/cc-skills-golang)
- [samber/ro GitHub Repository](https://github.com/samber/ro)
- [samber/ro Documentation](https://ro.samber.dev)
- [pkg.go.dev github.com/samber/ro](https://pkg.go.dev/github.com/samber/ro)
- [ReactiveX](https://reactivex.io/)
- [Operators Guide](references/operators-guide.md)
- [Reactive Patterns](references/patterns.md)
- [Plugin Ecosystem](references/plugin-ecosystem.md)
- [Subjects Guide](references/subjects-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include suggested Go code edits, package commands, tests, linting, and repository-scoped tooling guidance.]

## Skill Version(s):

1.2.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
