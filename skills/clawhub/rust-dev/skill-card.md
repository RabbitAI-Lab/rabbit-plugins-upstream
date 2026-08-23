## Description:

Practical day-1 guide to building applications in Rust well, covering ownership, errors as values, traits, common day-1 decisions, idioms, anti-patterns, crate choices, Cargo setup, testing, profiling, and releasing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill when starting or maintaining Rust applications, especially when they need practical guidance on ownership, borrowing, error handling, async work, crate selection, Cargo configuration, testing, performance work, and release workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a rustup install command that executes a downloaded shell script.

Mitigation: Review the command and install source before running it; execute setup commands only in an environment where toolchain changes are acceptable.

Risk: Optional kache, build-cache, S3 remote cache, and release workflow setup can modify local or CI development environments.

Mitigation: Enable these integrations deliberately, confirm credentials and cache scope, and verify the build with cache wrappers disabled when diagnosing unexpected failures.

Risk: Release automation guidance may involve publishing steps, personal access tokens, S3 credentials, and irreversible registry releases.

Mitigation: Use least-privilege credentials, review workflow permissions, build artifacts before publishing, and apply release automation only to repositories where rollback and recovery procedures are understood.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/rust-dev)
- [Metadata Homepage](https://github.com/tenequm/skills/tree/main/skills/rust-dev)
- [Async Basics](references/async-basics.md)
- [Crate Shortlist](references/crate-shortlist.md)
- [Development Environment](references/dev-environment.md)
- [Error Handling](references/error-handling.md)
- [Ownership and Types](references/ownership-and-types.md)
- [Performance](references/performance.md)
- [Releasing and Distribution](references/releasing.md)
- [Testing](references/testing.md)
- [Traits and Generics](references/traits-and-generics.md)
- [The Rust Book](https://doc.rust-lang.org/book/)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [Blessed.rs Crate Catalog](https://blessed.rs/crates)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline Rust, TOML, YAML, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is source-backed by the bundled Rust development references and may include commands or configuration snippets for the user to review before execution.]

## Skill Version(s):

0.4.3 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
