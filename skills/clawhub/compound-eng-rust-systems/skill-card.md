## Description:

Provides Rust patterns for CLI tools, backend services, and application code, including Cargo workspaces, axum/tokio services, async concurrency, and tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design, implement, test, and maintain Rust CLI tools, web services, and libraries with practical guidance on Cargo, async execution, and production readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Permissive CORS in example services could expose production APIs to untrusted origins.

Mitigation: Replace permissive CORS with an explicit list of trusted origins before deployment.

Risk: Example tracing may log user identifiers, secrets, tokens, or other personal data.

Mitigation: Remove sensitive fields from traces and review logging configuration before deploying.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-rust-systems)
- [Toolchain and interfaces](references/toolchain-and-interfaces.md)
- [Ownership and execution](references/ownership-and-execution.md)
- [Applications and testing](references/applications-and-testing.md)
- [Axum HTTP services](references/axum-service.md)
- [Observability for Rust services](references/observability.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Rust, shell, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review generated examples before use in production.]

## Skill Version(s):

5.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
