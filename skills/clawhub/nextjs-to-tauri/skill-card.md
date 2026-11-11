## Description:

Use when packaging a Next.js 16 App Router static export as a Tauri 2 desktop app, with tray, auto-update and a GitHub Actions release. Triggers on 打包成桌面应用 / Next.js 转 Tauri / Tauri 桌面应用 / package a Next.js app as a desktop app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and engineers use this skill to package a client-side Next.js 16 App Router static export as a Tauri 2 desktop app, with optional tray behavior, auto-updates, and cross-platform GitHub Actions releases. It is intended for apps that do not require server-side rendering or a live Node server at runtime.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation guidance includes an unpinned `@latest` dependency command, and one referenced file was only partially inspected.

Mitigation: Review the referenced content and confirm the dependency version before running installation steps.

Risk: Exposure of the updater signing private key could let others sign updates trusted by app clients.

Mitigation: Keep the private key out of version control, store it only as a repository secret, and rotate it if exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/rockbenben/skills/nextjs-to-tauri)
- [Skill homepage](https://github.com/rockbenben/aishort-skills/tree/main/skills/nextjs-to-tauri)
- [Tauri configuration and Rust templates](tauri-files.md)
- [Frontend integration examples](frontend-integration.md)
- [GitHub Actions desktop build workflow](desktop-build.yml)
- [Tauri Linux rendering issue #9394](https://github.com/tauri-apps/tauri/issues/9394)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration, Shell commands]

**Output Format:** [Markdown with code blocks and project configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes project-file templates for adaptation.]

## Skill Version(s):

1.1.10 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
