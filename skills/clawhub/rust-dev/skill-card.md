## Description:

Day-1 guide to building well in Rust - ownership, errors as values, String vs &str, Box/Rc/Arc, anyhow vs thiserror, and a crate shortlist (tokio, serde, axum, sqlx). Use when starting a Rust project, fighting the borrow checker, or picking crates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill when starting Rust CLI, service, or library projects, especially when making early decisions about ownership, error handling, async runtime use, crates, project structure, testing, performance, and release workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional setup guidance can install third-party tools globally or create persistent Cargo compiler-wrapper behavior.

Mitigation: Review setup steps before use, prefer pinned or independently verified installers, and avoid global compiler-wrapper setup unless it is trusted and needed.

Risk: Build-cache and release guidance can involve persistent daemons, Cargo configuration changes, S3 credentials, and privileged CI actions.

Mitigation: Know how to remove daemon and Cargo config changes, scope S3 credentials narrowly, and pin privileged CI actions to reviewed commit SHAs before copying workflows.

## Reference(s):

- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/rust-dev)
- [Async Basics](references/async-basics.md)
- [Crate Shortlist](references/crate-shortlist.md)
- [Development Environment](references/dev-environment.md)
- [Error Handling](references/error-handling.md)
- [Ownership and Types](references/ownership-and-types.md)
- [Performance](references/performance.md)
- [Project Shape: Past One Crate](references/project-shape.md)
- [Releasing and Distribution](references/releasing.md)
- [Testing](references/testing.md)
- [Traits and Generics](references/traits-and-generics.md)
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [Blessed.rs crate catalog](https://blessed.rs/crates)
- [Rustlings](https://github.com/rust-lang/rustlings)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose with Rust, TOML, YAML, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.5.1 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
