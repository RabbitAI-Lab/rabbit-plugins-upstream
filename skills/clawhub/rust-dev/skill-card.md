## Description: <br>
Practical day-1 guidance for building Rust applications, covering ownership, error handling, traits and generics, async Rust, testing, performance, crate selection, and release workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when starting or maintaining Rust CLI tools, services, and libraries. It helps with Rust mental models, type and ownership choices, Cargo setup, testing, performance work, and release/distribution decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Suggested setup, cache, or release commands may install tools or change local and CI configuration. <br>
Mitigation: Review commands before running them, pin versions where practical, and test changes in a disposable project or branch first. <br>
Risk: Cache and release workflows may involve S3 credentials, personal access tokens, registry tokens, or other secrets. <br>
Mitigation: Use least-privilege credentials, keep secrets in approved secret stores, and inspect generated CI workflows before enabling publication. <br>
Risk: Broad Rust-development activation can surface guidance in many Rust-adjacent conversations. <br>
Mitigation: Confirm the intended task before applying project changes, especially when the user only mentions Rust concepts or tooling. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/rust-dev) <br>
- [Project Homepage](https://github.com/tenequm/skills/tree/main/skills/rust-dev) <br>
- [Ownership and Types](references/ownership-and-types.md) <br>
- [Error Handling](references/error-handling.md) <br>
- [Traits and Generics](references/traits-and-generics.md) <br>
- [Async Basics](references/async-basics.md) <br>
- [Crate Shortlist](references/crate-shortlist.md) <br>
- [Development Environment](references/dev-environment.md) <br>
- [Testing](references/testing.md) <br>
- [Performance](references/performance.md) <br>
- [Releasing and Distribution](references/releasing.md) <br>
- [The Rust Book](https://doc.rust-lang.org/book/) <br>
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/) <br>
- [Rustlings](https://github.com/rust-lang/rustlings) <br>
- [Blessed.rs Crate Catalog](https://blessed.rs/crates) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline Rust, TOML, YAML, and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Cargo commands, configuration snippets, CI examples, and release workflow guidance for review before use.] <br>

## Skill Version(s): <br>
0.4.1 (source: server release metadata, SKILL.md frontmatter, and changelog released 2026-07-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
