## Description:

Structured logging extensions for Golang using samber/slog-**** packages for multi-handler pipelines, log sampling, attribute formatting, HTTP middleware, and backend routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when designing or maintaining Go structured logging pipelines with samber/slog packages. It helps configure sampling, formatting, routing, HTTP middleware logging, backend sinks, and graceful shutdown patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTTP request or response body logging can expose sensitive data.

Mitigation: Keep body logging disabled by default; enable it only for narrow debugging with redaction, size limits, route allowlists, and exclusions for authentication, payment, and PII-bearing endpoints.

Risk: Buffered backend handlers can lose log records during shutdown.

Mitigation: Use the documented graceful shutdown or flush calls for batch-oriented handlers before the process exits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-samber-slog)
- [cc-skills-golang repository](https://github.com/samber/cc-skills-golang)
- [slog-multi](https://github.com/samber/slog-multi)
- [slog-sampling](https://github.com/samber/slog-sampling)
- [slog-formatter](https://github.com/samber/slog-formatter)
- [Pipeline Patterns](references/pipeline-patterns.md)
- [Sampling Strategies](references/sampling-strategies.md)
- [HTTP Middlewares](references/http-middlewares.md)
- [Backend Handlers](references/backend-handlers.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go code examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference Go tooling and package documentation for version, symbol, import, and vulnerability checks.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
