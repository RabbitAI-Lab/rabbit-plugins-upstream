## Description:

Guides Rust developers through ownership, error handling, project setup, and choosing crates for new applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers use this reference when starting Rust projects, addressing ownership and type errors, selecting crates, and configuring Cargo tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copied installation or Docker commands may change the developer's system.

Mitigation: Review commands, particularly the rustup installer, before running them in the intended environment.

Risk: Build-cache setup may persist data or rewrite and clean target directories.

Mitigation: Check kache initialization and S3/OCI cache settings against local retention and access policies.

Risk: Release workflows can expose credentials when copied without review.

Mitigation: Review release-token configuration and use organization-approved secret handling.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tenequm/skills/rust-dev)
- [Project homepage (listed in skill metadata)](https://github.com/tenequm/skills/tree/main/skills/rust-dev)
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Ownership and Types](references/ownership-and-types.md)
- [Error Handling](references/error-handling.md)
- [Crate Shortlist](references/crate-shortlist.md)
- [Development Environment](references/dev-environment.md)
- [Testing](references/testing.md)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Rust, TOML, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance and examples require review before use.]

## Skill Version(s):

0.8.0 (source: release metadata, SKILL.md metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
