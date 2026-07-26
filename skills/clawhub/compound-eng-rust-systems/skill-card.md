## Description: <br>
Rust patterns for CLI tools, backend services, and general application code covering Cargo workspaces, axum/tokio services, clap CLIs, async concurrency, and Rust tooling configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill for Rust application work, including CLIs, axum/tokio services, Cargo workspaces, async concurrency, testing, observability, performance tuning, and CI configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Production web-service examples may be copied with broad CORS behavior or client-facing error detail that is inappropriate for a deployment. <br>
Mitigation: Review CORS allowlists, client error messages, authentication, and secret redaction before using the examples in production. <br>
Risk: Cargo, CI, and build-profile snippets can change build behavior, dependency checks, or release artifacts when applied. <br>
Mitigation: Apply snippets in a reviewed branch and run the repository's format, lint, test, and dependency checks before release. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-rust-systems) <br>
- [SPEC.md](SPEC.md) <br>
- [Axum HTTP Services](references/axum-service.md) <br>
- [Build Profiles](references/build-profiles.md) <br>
- [Rust CI Pipeline](references/ci-pipeline.md) <br>
- [Rust CLI Tools](references/cli-tools.md) <br>
- [Observability for Rust Services](references/observability.md) <br>
- [Hot-Path Performance](references/performance.md) <br>
- [Production Resilience](references/production-resilience.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Rust, TOML, YAML, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No automatic execution; outputs are recommendations and snippets for agent-assisted Rust development.] <br>

## Skill Version(s): <br>
4.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
