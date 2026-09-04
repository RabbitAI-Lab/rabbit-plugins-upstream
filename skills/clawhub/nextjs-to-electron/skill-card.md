## Description:

Use when packaging a Next.js static export as a Windows Electron app, notably offline/intranet boxes with no WebView2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to convert client-side Next.js static exports into Windows Electron desktop apps for offline or intranet environments where WebView2 may be unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Electron and GitHub Actions templates may contain project-specific placeholders or release-upload behavior that is wrong for the target application.

Mitigation: Review appId, product names, release-upload steps, and packaging paths before applying the templates.

Risk: The generated desktop app stores locale and window state locally, which may be unexpected in tightly controlled environments.

Mitigation: Confirm the small local settings file is acceptable for the deployment environment and document its purpose for operators.

Risk: Close-to-tray behavior can make the app appear to stay open after the window is closed.

Mitigation: Review the tray quit path and close-to-hide behavior during Windows QA before release.

## Reference(s):

- [nextjs-to-electron on ClawHub](https://clawhub.ai/rockbenben/skills/nextjs-to-electron)
- [electron-files.md](artifact/electron-files.md)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JavaScript, JSON, YAML, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces implementation guidance and copy-paste templates for Electron main-process files, electron-builder configuration, tests, and GitHub Actions.]

## Skill Version(s):

1.1.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
