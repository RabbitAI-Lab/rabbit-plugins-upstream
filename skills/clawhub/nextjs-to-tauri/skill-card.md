## Description:

Guides developers in wrapping a client-side Next.js 16 static export as a Tauri 2 desktop app, with optional desktop integrations and cross-platform release automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to adapt a client-side Next.js 16 static export into a Tauri 2 desktop app while preserving web behavior. It provides optional native integrations and a cross-platform build and release workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marks this release suspicious because install and update guidance uses unpinned tools and elevated CI commands, while scanner coverage is incomplete; it found no clear malicious intent.

Mitigation: Inspect the referenced files before installation, review and pin tool versions and CI permissions and commands, and wait for fuller scan coverage.

## Reference(s):

- [Skill homepage](https://github.com/rockbenben/aishort-skills/tree/main/skills/nextjs-to-tauri)
- [Tauri Content Security Policy documentation](https://v2.tauri.app/security/csp/)
- [Tauri EGL issue](https://github.com/tauri-apps/tauri/issues/9394)
- [AppImage compatibility case](https://github.com/espressif/idf-im-ui/issues/755)
- [Host library preload implementation example](https://github.com/refactoringhq/tolaria/commit/8c286a4856637d662f05428f679faa4aee607c66)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code blocks for TypeScript, Rust, YAML, JSON, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adaptable templates and optional integrations for the target project.]

## Skill Version(s):

1.1.16 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
