## Description:

Rust patterns for CLI tools, backend services, and general application code, including Cargo workspaces, axum/tokio services, clap CLIs, async concurrency, clippy, rustfmt, cargo-nextest, and Cargo.toml.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when implementing or reviewing Rust CLI tools, backend services, libraries, Cargo workspaces, async Tokio code, and production-facing Rust project configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Axum middleware can be unsafe if CORS, authentication, rate limits, or middleware order are copied without review.

Mitigation: Review middleware order and policy choices before production use, and test auth, CORS, timeout, and rate-limit behavior in the target service.

Risk: CI examples can introduce supply-chain exposure when third-party GitHub Actions are referenced by mutable versions.

Mitigation: Pin third-party GitHub Actions to reviewed commit SHAs and keep Rust security checks such as cargo audit or cargo deny in required CI.

Risk: The skill provides general Rust systems guidance that may not match every codebase's runtime constraints or public API commitments.

Mitigation: Run the target project's normal Rust verification commands, including formatting, clippy, tests, and production dependency checks before merging generated changes.

## Reference(s):

- [SKILL.md](SKILL.md)
- [SPEC.md](SPEC.md)
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

**Output Format:** [Markdown guidance with inline Rust, TOML, shell, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces guidance and examples for an agent to adapt; generated code and commands require project-specific review before use.]

## Skill Version(s):

4.5.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
