## Description:

Rust Best Practice provides a comprehensive Rust engineering reference covering idioms, ownership, error handling, API design, async, performance, unsafe code, testing, tooling, web and CLI work, project structure, and supply-chain security.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anjasta-tarigan](https://clawhub.ai/user/anjasta-tarigan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing, reviewing, debugging, or designing Rust code and Rust project workflows. It helps agents provide idiomatic guidance across Rust language features, common frameworks, quality practices, and supply-chain security.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may cause the skill to load frequently for Rust-related conversations and increase context usage.

Mitigation: Review activation wording and reference loading behavior before deployment where context efficiency matters.

Risk: The skill provides extensive engineering guidance that could be applied incorrectly if used without review.

Mitigation: Review generated recommendations against project requirements, tests, and authoritative Rust documentation before applying changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anjasta-tarigan/skills/rust-best-practice)
- [Idiomatic Style, Naming, and Control Flow](references/01-idiomatic-style-and-naming.md)
- [Ownership, Borrowing, and Lifetimes](references/02-ownership-borrowing-lifetimes.md)
- [Error Handling](references/03-error-handling.md)
- [Traits, Generics, and Type Design](references/04-traits-generics-and-type-design.md)
- [Concurrency and Async](references/05-concurrency-and-async.md)
- [Performance and Memory](references/06-performance-and-memory.md)
- [Unsafe Rust](references/07-unsafe-rust.md)
- [Testing and Quality Assurance](references/08-testing-and-quality.md)
- [Tooling, Cargo, and CI](references/09-tooling-cargo-and-ci.md)
- [Web Backend and Networking](references/10-web-backend-and-networking.md)
- [CLI and Systems Tools](references/11-cli-and-systems-tools.md)
- [Project Structure, Workspaces, and Dependencies](references/12-project-structure-workspaces-and-dependencies.md)
- [Security and Supply-Chain](references/13-security-and-supply-chain.md)
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [The Cargo Book](https://doc.rust-lang.org/cargo/)
- [Clippy documentation](https://doc.rust-lang.org/clippy/)
- [RustSec Advisory Database](https://rustsec.org/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code examples and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May load a broad Rust reference set frequently when Rust-related terms appear.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
