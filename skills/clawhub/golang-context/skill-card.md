## Description:

Idiomatic context.Context usage in Golang: propagation through API boundaries, cancellation, timeouts and deadlines, request-scoped values, and context.WithoutCancel for background work outliving requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill when designing, reviewing, or debugging Go code that propagates context.Context across HTTP handlers, service layers, databases, external APIs, and goroutines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents that edit Go files or run Go, golangci-lint, and git commands.

Mitigation: Review proposed edits and commands before applying them in important repositories.

Risk: Incorrect context propagation advice can change cancellation, timeout, or background-work behavior in Go services.

Mitigation: Validate changes with focused tests for request cancellation, timeout expiry, and context value propagation.

## Reference(s):

- [Cancellation, Timeouts & Deadlines](references/cancellation.md)
- [Context in HTTP Servers & Service Calls](references/http-services.md)
- [Context Values & Cross-Service Tracing](references/values-tracing.md)
- [cc-skills-golang homepage](https://github.com/samber/cc-skills-golang)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown guidance with Go code examples and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go tooling when applying lint, build, or test checks.]

## Skill Version(s):

1.3.0 (source: skill metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
