## Description:

Rust patterns for CLI tools, backend services, general application code, Cargo workspaces, axum/tokio services, clap CLIs, async concurrency, and Rust tooling configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement and review Rust CLIs, backend services, libraries, Cargo workspaces, async execution, observability, testing, and production readiness checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review identified a permissive CORS default in an Axum service template.

Mitigation: Review generated or edited Axum service code before production use and replace permissive CORS with explicit trusted origins, methods, and headers.

## Reference(s):

- [Applications and testing](references/applications-and-testing.md)
- [Axum HTTP Services](references/axum-service.md)
- [Build Profiles](references/build-profiles.md)
- [Rust CI Pipeline](references/ci-pipeline.md)
- [Rust CLI Tools](references/cli-tools.md)
- [Macro Hygiene and OS Boundaries](references/macros-and-os-boundaries.md)
- [Observability for Rust Services](references/observability.md)
- [Ownership and execution](references/ownership-and-execution.md)
- [Hot-Path Performance](references/performance.md)
- [Production Resilience](references/production-resilience.md)
- [Rustdoc Discipline](references/rustdoc.md)
- [Toolchain and public interfaces](references/toolchain-and-interfaces.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

4.5.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
