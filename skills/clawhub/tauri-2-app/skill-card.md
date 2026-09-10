## Description:

Scaffold a new Tauri 2 desktop app with a Rust backend and TypeScript/React frontend, or add Tauri command and Rust module slices using the skill's documented architecture and templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create Tauri 2 desktop app scaffolds and to add typed backend command or module slices to an existing Tauri project. It emphasizes a thin frontend, modular Rust backend, platform abstractions, encrypted secret handling, updater setup, and cross-platform CI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated desktop apps may have under-scoped file and WebView security controls.

Mitigation: Before production use, replace null CSP values with an explicit Content Security Policy and review all WebView-facing permissions.

Risk: Generated storage code can become unsafe if untrusted filenames are passed into file persistence helpers.

Mitigation: Use fixed internal storage filenames or validate filenames before they reach storage helpers.

Risk: Tauri plugin permissions may grant more capability than a specific window needs.

Mitigation: Grant only the exact plugin permissions required for each window and prune unused default permissions.

Risk: Updater, installer, and native open-command behavior can affect production security posture.

Mitigation: Review updater endpoints and signing keys, installer settings, and native open-command flows before shipping.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dennisrongo/skills/tauri-2-app)
- [Good Patterns](references/good-patterns.md)
- [Anti-patterns](references/anti-patterns.md)
- [Canonical Folder Layout](references/folder-layout.md)
- [Tauri Configuration Template](references/templates/tauri-conf.md)
- [Capabilities Template](references/templates/capabilities.md)
- [Encrypted Secrets Template](references/templates/encryption-mod.md)
- [Cross-platform CI Template](references/templates/ci-workflow.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with generated project files, code snippets, shell commands, and configuration templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a full Tauri app scaffold or focused command/module additions depending on the user's requested mode.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
