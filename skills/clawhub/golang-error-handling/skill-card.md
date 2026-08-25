## Description:

Idiomatic Golang error handling -- creation, wrapping with %w, errors.Is/As, errors.Join, custom error types, sentinel errors, panic/recover, the single handling rule, structured logging with slog, HTTP request logging middleware, and samber/oops for production errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, review, and audit idiomatic Go error handling in codebases, including error creation, wrapping, inspection, logging, panic/recover boundaries, and production error context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and potentially edit Go files and run Go, golangci-lint, git, or agent-based audit workflows when asked.

Mitigation: Use it in repositories where that code access is appropriate, and review proposed edits and commands before applying them.

Risk: Parallel audit mode can inspect broad areas of a Go codebase.

Mitigation: Scope audits to intended paths and avoid running broad inspections in repositories containing code the agent should not access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-error-handling)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [Error Creation](references/error-creation.md)
- [Error Handling Patterns and Logging](references/error-handling.md)
- [Error Wrapping and Inspection](references/error-wrapping.md)
- [samber/oops](https://github.com/samber/oops)
- [samber/slog-http](https://github.com/samber/slog-http)
- [log/slog package](https://pkg.go.dev/log/slog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Go code examples and command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits, Go commands, golangci-lint checks, git inspection, and parallel audit findings when requested.]

## Skill Version(s):

1.3.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
