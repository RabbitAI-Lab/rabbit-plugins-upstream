## Description:

Comprehensive best-practice guide for building, securing, testing, and shipping Tauri v2 desktop and mobile apps with a Rust core and web frontend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anjasta-tarigan](https://clawhub.ai/user/anjasta-tarigan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design, review, debug, test, and release Tauri v2 applications. It is especially relevant when working with IPC commands, capabilities and permissions, sidecars, plugins, window management, signing, updating, CI/CD, and Tauri-specific tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sidecar, updater, shell, filesystem, and CI/CD guidance can affect local system access, release integrity, or deployment secrets if applied too broadly.

Mitigation: Scope Tauri permissions tightly, keep signing keys and tokens in secret stores, and review capability files before shipping.

Risk: Tauri v2 APIs and plugin details can change across minor versions, especially for security-sensitive code paths.

Mitigation: Verify version-sensitive implementation details against current Tauri documentation before release or security-critical changes.

Risk: Configuration or code snippets may need adaptation to a specific app's windows, plugins, target platforms, and release process.

Mitigation: Review generated guidance in the target project context and cover IPC, capability, sidecar, updater, and E2E paths with appropriate tests.

## Reference(s):

- [Tauri2 Best Practice ClawHub skill page](https://clawhub.ai/anjasta-tarigan/skills/tauri2-best-practice)
- [IPC: Commands, Events, and Channels](artifact/references/ipc-commands.md)
- [Security: Capabilities, Permissions, Scopes, CSP](artifact/references/security-capabilities.md)
- [Plugin Development and Sidecars](artifact/references/plugins-sidecar.md)
- [State Management](artifact/references/state-management.md)
- [Bundling, Code Signing, Updater, CI/CD](artifact/references/bundling-updater-cicd.md)
- [Testing: Rust Unit Tests, Frontend Mocks, WebDriver E2E](artifact/references/testing.md)
- [Windows, Webviews and Multi-Window Management](artifact/references/windowing-multiwindow.md)
- [Tauri v2 Security](https://v2.tauri.app/security/)
- [Tauri v2 IPC](https://v2.tauri.app/concept/inter-process-communication/)
- [Tauri v2 State Management](https://v2.tauri.app/develop/state-management/)
- [Tauri v2 Testing](https://v2.tauri.app/develop/tests/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline Rust, TypeScript, JSON, YAML, and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend configuration diffs, test strategies, security checklists, and documentation links for Tauri v2 projects.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
