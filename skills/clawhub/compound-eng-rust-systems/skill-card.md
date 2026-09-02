## Description:

Rust patterns for CLI tools, backend services, and general application code covering Cargo workspaces, axum/tokio services, clap CLIs, async concurrency, and Rust tooling configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for Rust project implementation and review across CLIs, HTTP services, workspaces, async concurrency, observability, CI, and production resilience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rust service guidance copied directly into production may expose internal database or anyhow error details to clients.

Mitigation: Review the Axum error-handling snippet before use and replace internal errors with generic client-facing responses while logging details server-side.

Risk: Agent-authored Rust recommendations may be incomplete or misapplied for a specific repository.

Mitigation: Review proposed changes, run the project's Rust test and lint gates, and scan the skill before deployment.

## Reference(s):

- [Axum HTTP Services](references/axum-service.md)
- [Build Profiles](references/build-profiles.md)
- [Rust CI Pipeline](references/ci-pipeline.md)
- [Rust CLI Tools](references/cli-tools.md)
- [Macro Hygiene and OS Boundaries](references/macros-and-os-boundaries.md)
- [Observability for Rust Services](references/observability.md)
- [Hot-Path Performance](references/performance.md)
- [Production Resilience](references/production-resilience.md)
- [Rustdoc Discipline](references/rustdoc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable install behavior; outputs are agent-authored Rust development guidance.]

## Skill Version(s):

4.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
