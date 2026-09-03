## Description:

Helps developers package a client-side Next.js static export as a Windows Electron app for offline or intranet environments without WebView2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to convert a static-export Next.js App Router project into a self-contained Windows Electron desktop application, including packaging, test, and CI guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated project packaging files, Electron dependencies, and CI or release workflow configuration can affect published desktop artifacts.

Mitigation: Review package changes, electron-builder settings, GitHub Actions permissions, and release upload steps before publishing artifacts.

Risk: The playbook targets current 64-bit Windows 10 or newer and is out of scope for 32-bit or pre-Windows 10 targets.

Mitigation: Verify target machine bitness and Windows build number before committing to an Electron desktop build.

Risk: Headless execution cannot fully verify desktop GUI behavior, offline operation, tray behavior, or localized navigation.

Mitigation: Run the packaged app on a real Windows machine, ideally in the same offline or WebView2-less environment expected in deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rockbenben/skills/nextjs-to-electron)
- [electron-files.md](electron-files.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The guidance targets Windows Electron packaging for static Next.js exports and includes human GUI verification steps.]

## Skill Version(s):

1.1.5 (source: evidence.json release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
