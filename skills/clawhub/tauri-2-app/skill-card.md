## Description:

Scaffold or extend Tauri 2 desktop apps with a Rust backend, TypeScript or React frontend, modular commands, secure storage patterns, Tauri capabilities, updater wiring, and cross-platform CI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create a new Tauri 2 desktop app or add Rust command and module slices to an existing Tauri app while preserving secure, modular project conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may contact package registries and run npm or cargo commands while scaffolding or verifying a project.

Mitigation: Review the requested operations before installation or execution in restricted environments.

Risk: Generated Tauri security defaults such as CSP, capability permissions, updater keys, bundle identifiers, and endpoints may need project-specific review.

Mitigation: After generation, review the Tauri CSP, remove unused capabilities and plugins, and confirm updater keys, bundle identifiers, and endpoints belong to the project.

## Reference(s):

- [Tauri 2 App Scaffolder](SKILL.md)
- [Good Patterns](references/good-patterns.md)
- [Anti-patterns](references/anti-patterns.md)
- [Tauri 2 App - Canonical Folder Layout](references/folder-layout.md)
- [Tauri Configuration Template](references/templates/tauri-conf.md)
- [Cargo Manifest Template](references/templates/cargo-toml.md)
- [Capabilities Template](references/templates/capabilities.md)
- [Frontend Config Templates](references/templates/vite-and-tsconfig.md)
- [Typed Tauri Command Hook Template](references/templates/use-tauri-command.md)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with code snippets and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify Tauri project files and run npm or cargo verification commands.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
