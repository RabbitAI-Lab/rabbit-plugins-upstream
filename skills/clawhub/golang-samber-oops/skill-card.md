## Description:

Structured error handling in Golang with samber/oops — error builders, stack traces, error codes, error context, error wrapping, error attributes, user-facing vs developer messages, panic recovery, and logger integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when adopting or maintaining Go code that uses github.com/samber/oops for structured errors, panic recovery, public messages, and logging integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated error-handling examples may attach personal data, request or response details, sensitive headers, or raw payloads to errors that are later logged or exported.

Mitigation: Review generated error attributes before use; prefer opaque identifiers, avoid emails and raw bodies, and sanitize payloads before they are stored in error context or sent to logs or APM systems.

Risk: Verbose stack traces and source fragments can expose internal implementation details in external error tracking systems.

Mitigation: Configure stack trace depth and source fragment behavior deliberately before deployment, and confirm exported error output matches the service's data handling policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-samber-oops)
- [Skill homepage](https://github.com/samber/cc-skills-golang)
- [github.com/samber/oops](https://github.com/samber/oops)
- [pkg.go.dev/github.com/samber/oops](https://pkg.go.dev/github.com/samber/oops)
- [samber/oops Advanced Patterns](references/advanced.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go code examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go tooling when validating generated examples or diagnostics.]

## Skill Version(s):

1.2.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
