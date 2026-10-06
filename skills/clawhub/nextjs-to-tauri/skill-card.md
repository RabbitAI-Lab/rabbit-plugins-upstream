## Description:

Helps developers package a statically exported Next.js 16 App Router application as a Tauri 2 desktop app with optional auto-update, tray integration, and cross-platform builds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to turn client-side Next.js apps that support static export into Windows, macOS, and Linux desktop packages, with guidance for frontend integration, updates, and CI releases. It does not cover apps that require a live Node.js server at runtime.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying the templates changes the app's frontend, Tauri configuration, and release workflow.

Mitigation: Review the proposed file changes and build behavior before merging or shipping.

Risk: Automatic updates can pull releases from an incorrectly configured endpoint or expose signing material if secrets are mishandled.

Mitigation: Verify the updater endpoint and release process, keep the signing private key in protected CI secrets, and omit auto-update if unnecessary.

Risk: The Windows installer template can silently install WebView2.

Mitigation: Review the silent bootstrapper setting and choose an installation mode appropriate for users before distribution.

## Reference(s):

- [Project homepage (listed in skill metadata)](https://github.com/rockbenben/aishort-skills/tree/main/skills/nextjs-to-tauri)
- [ClawHub skill listing](https://clawhub.ai/rockbenben/skills/nextjs-to-tauri)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown with code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapt templates and placeholders to the target application before use.]

## Skill Version(s):

1.1.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
