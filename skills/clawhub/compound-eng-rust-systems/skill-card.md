## Description:

Rust patterns for CLI tools, backend services, and general application code; use when working with Rust, Cargo workspaces, axum/tokio services, clap CLIs, async concurrency, or configuring clippy, rustfmt, cargo-nextest, or Cargo.toml.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to produce and review Rust CLIs, Axum/Tokio services, libraries, Cargo workspace configuration, async code, tests, observability, and production resilience patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Axum service examples may carry forward permissive CORS into production code.

Mitigation: Review generated Axum service code and replace permissive CORS with an explicit allowlist of trusted origins, methods, and headers before production use.

## Reference(s):

- [Applications and Testing](references/applications-and-testing.md)
- [Axum HTTP Services](references/axum-service.md)
- [Build Profiles](references/build-profiles.md)
- [Rust CI Pipeline](references/ci-pipeline.md)
- [Rust CLI Tools](references/cli-tools.md)
- [Macro Hygiene and OS Boundaries](references/macros-and-os-boundaries.md)
- [Observability for Rust Services](references/observability.md)
- [Ownership and Execution](references/ownership-and-execution.md)
- [Hot-Path Performance](references/performance.md)
- [Production Resilience](references/production-resilience.md)
- [Rustdoc Discipline](references/rustdoc.md)
- [Toolchain and Public Interfaces](references/toolchain-and-interfaces.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline Rust, TOML, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project structure, Cargo configuration, Rust examples, validation commands, and review guidance.]

## Skill Version(s):

4.5.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
