## Description:

Provides Rust patterns for CLI tools, backend services, Cargo workspaces, async concurrency, and application code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Rust developers use this skill to design and review CLI tools, Tokio/axum services, libraries, Cargo configuration, and tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic CORS settings in web-service examples may be unsafe for authenticated APIs.

Mitigation: Restrict allowed origins and methods to the application's needs before production use.

Risk: Copying example middleware order may produce unintended access or timeout behavior.

Mitigation: Review and test tower middleware ordering in the target service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-rust-systems)
- [Toolchain and interfaces](artifact/references/toolchain-and-interfaces.md)
- [Ownership and execution](artifact/references/ownership-and-execution.md)
- [Applications and testing](artifact/references/applications-and-testing.md)
- [Axum HTTP services](artifact/references/axum-service.md)
- [Production resilience](artifact/references/production-resilience.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Rust and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations and examples require adaptation and testing for the target project.]

## Skill Version(s):

5.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
