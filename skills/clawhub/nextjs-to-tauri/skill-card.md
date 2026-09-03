## Description:

Packages client-side Next.js 16 App Router apps as Tauri 2 desktop apps with static export, auto-update, tray integration, and CI build templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to convert static-export-compatible Next.js App Router applications into Tauri desktop releases. It helps add desktop shell files, frontend desktop integration, auto-update configuration, tray behavior, and GitHub Actions packaging guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed auto-update configuration can download update payloads and depends on a private signing key.

Mitigation: Store the Tauri signing private key only as a GitHub secret, keep it out of git, and remove updater blocks when background update downloads are not intended.

Risk: The generated desktop app may contact GitHub release endpoints for update checks.

Mitigation: Confirm the release endpoint and update policy before enabling updater artifacts for a production release.

Risk: The Windows bundle template can silently bootstrap WebView2 and the opener permission allows external links to leave the app.

Mitigation: Confirm that silent WebView2 installation and broad external-link opening are acceptable for the target users and narrow or remove permissions when they are not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rockbenben/skills/nextjs-to-tauri)
- [Tauri file templates](tauri-files.md)
- [Frontend integration templates](frontend-integration.md)
- [Desktop build workflow template](desktop-build.yml)
- [Tauri Linux EGL issue](https://github.com/tauri-apps/tauri/issues/9394)
- [WebKitGTK EGL failure example](https://github.com/espressif/idf-im-ui/issues/755)
- [Tolaria libwayland AppImage fix](https://github.com/refactoringhq/tolaria/commit/8c286a4856637d662f05428f679faa4aee607c66)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code blocks, configuration templates, workflow YAML, Rust, TypeScript, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node tooling and assumes a static-export-compatible Next.js App Router application; generated release/update settings should be reviewed before shipping.]

## Skill Version(s):

1.1.6 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
