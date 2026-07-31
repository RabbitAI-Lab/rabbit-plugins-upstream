## Description: <br>
Rust patterns for CLI tools, backend services, and general application code covering Cargo workspaces, axum/tokio services, clap CLIs, async concurrency, clippy, rustfmt, cargo-nextest, and Cargo.toml. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill for Rust application work, including CLI tools, backend services, Cargo workspace structure, async concurrency, documentation, observability, CI, resilience, and production readiness practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary reports one confirmed bug in an axum error-handling example that can expose internal database or anyhow error details to clients. <br>
Mitigation: Before production use, log internal errors server-side and return a generic client-facing message for internal server error responses. <br>
Risk: Rust guidance can be copied into production services without adapting validation, secret redaction, timeout, retry, and backpressure settings to the target system. <br>
Mitigation: Review generated or modified code against the bundled production-resilience and observability guidance before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-rust-systems) <br>
- [ia-rust-systems specification](SPEC.md) <br>
- [Axum HTTP Services](references/axum-service.md) <br>
- [Build Profiles](references/build-profiles.md) <br>
- [Rust CI Pipeline](references/ci-pipeline.md) <br>
- [Rust CLI Tools](references/cli-tools.md) <br>
- [Observability for Rust Services](references/observability.md) <br>
- [Hot-Path Performance](references/performance.md) <br>
- [Production Resilience](references/production-resilience.md) <br>
- [Rustdoc Discipline](references/rustdoc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with Rust, TOML, YAML, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing implementation guidance; it does not execute code or handle credentials.] <br>

## Skill Version(s): <br>
4.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
