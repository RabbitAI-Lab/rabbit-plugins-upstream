## Description:

Rust patterns for CLI tools, backend services, and general application code, including Cargo workspaces, axum/tokio services, clap CLIs, async concurrency, and Rust tooling configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for Rust application work across CLI tools, backend services, libraries, Cargo workspaces, async Tokio code, testing, observability, CI, and production-readiness reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Rust changes may alter dependencies, CI, configuration, environment handling, service authentication, database access, or external HTTP behavior.

Mitigation: Review generated changes before applying them, with extra attention to dependency additions, CI edits, config and environment handling, and service code touching databases, authentication, or external clients.

Risk: Guidance may propose production service patterns that need project-specific validation before deployment.

Mitigation: Run the repository's Rust formatting, linting, testing, license, advisory, and deployment-readiness checks before merging or releasing generated changes.

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

**Output Format:** [Markdown with inline code and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

4.4.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
