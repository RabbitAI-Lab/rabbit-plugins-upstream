## Description:

Practical day-1 guide to building applications in Rust well, covering ownership, errors as values, traits, day-1 design choices, idioms, anti-patterns, crate selection, project setup, testing, performance, and release workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when starting, maintaining, testing, profiling, or releasing Rust applications and libraries. It helps agents provide practical Rust guidance, code patterns, shell commands, Cargo configuration, crate recommendations, and release-process advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional setup guidance includes installer commands and kache setup that can modify Cargo configuration or start a background daemon.

Mitigation: Review installer and kache commands before execution, run them in an appropriate developer environment, and confirm expected Cargo configuration changes.

Risk: Release and cache examples may involve GitHub, crates.io, or S3 credentials.

Mitigation: Use narrowly scoped credentials, prefer managed secret storage, and avoid pasting long-lived tokens into local shells or shared logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/rust-dev)
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/rust-dev)
- [Async Basics](references/async-basics.md)
- [Crate Shortlist](references/crate-shortlist.md)
- [Development Environment](references/dev-environment.md)
- [Error Handling](references/error-handling.md)
- [Ownership and Types](references/ownership-and-types.md)
- [Performance](references/performance.md)
- [Releasing and Distribution](references/releasing.md)
- [Testing](references/testing.md)
- [Traits and Generics](references/traits-and-generics.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses should be reviewed before executing installer, cache, CI, release, or credential-related commands.]

## Skill Version(s):

0.4.2 (source: frontmatter, release evidence, CHANGELOG released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
