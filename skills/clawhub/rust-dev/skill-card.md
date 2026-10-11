## Description:

Guides developers through Rust ownership, error handling, project setup, and choosing crates for new applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers use this skill to start Rust projects, navigate borrowing and errors, select crates, and set up testing, CI, and releases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Piping a downloaded Rust installer directly to a shell can execute unreviewed code.

Mitigation: Review official rustup installation instructions and the script before running it.

Risk: Enabling the optional build-cache daemon may modify local build behavior.

Mitigation: Try kache dry-run and no-service options before enabling its daemon.

Risk: CI and remote-cache examples use S3, GitHub, or crates.io credentials.

Mitigation: Keep tokens in protected secrets, minimize their scope, and avoid exposing them in logs.

## Reference(s):

- [Ownership and Types](references/ownership-and-types.md)
- [Error Handling](references/error-handling.md)
- [Crate Shortlist](references/crate-shortlist.md)
- [Development Environment](references/dev-environment.md)
- [Releasing and Distribution](references/releasing.md)
- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Publisher-listed project homepage](https://github.com/tenequm/skills/tree/main/skills/rust-dev)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Rust, TOML, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples are optional and should be reviewed before execution.]

## Skill Version(s):

0.8.0 (source: server release metadata, skill metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
