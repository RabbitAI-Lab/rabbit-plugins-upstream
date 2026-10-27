## Description:

Rust patterns for CLI tools, backend services, and general application code, for work with Rust, Cargo workspaces, axum/tokio services, clap CLIs, async concurrency, and Rust tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill when building or maintaining Rust command-line tools, web services, libraries, and Cargo workspaces. It provides practical patterns for APIs, async execution, safety, testing, and project tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo build and test commands execute project code.

Mitigation: Review the project and commands before running builds or tests.

Risk: Dependency changes and optional telemetry can affect the project and its environment.

Mitigation: Review dependency changes and configure optional telemetry for the intended environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-rust-systems)
- [Applications and testing](references/applications-and-testing.md)
- [Axum HTTP services](references/axum-service.md)
- [Build profiles](references/build-profiles.md)
- [Rust CI pipeline](references/ci-pipeline.md)
- [Rust CLI tools](references/cli-tools.md)
- [Macro hygiene and OS boundaries](references/macros-and-os-boundaries.md)
- [Observability for Rust services](references/observability.md)
- [Ownership and execution](references/ownership-and-execution.md)
- [Hot-path performance](references/performance.md)
- [Production resilience](references/production-resilience.md)
- [Rustdoc discipline](references/rustdoc.md)
- [Toolchain and public interfaces](references/toolchain-and-interfaces.md)
- [Cargo build rustflags documentation](https://doc.rust-lang.org/cargo/reference/config.html#buildrustflags)
- [Rust allocation error handler documentation](https://doc.rust-lang.org/std/alloc/fn.handle_alloc_error.html)
- [Tokio select macro documentation](https://docs.rs/tokio/latest/tokio/macro.select.html)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Rust code examples, Cargo configuration, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Context-sensitive guidance for Rust edition 2024 application code; excludes no_std and embedded Rust.]

## Skill Version(s):

5.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
