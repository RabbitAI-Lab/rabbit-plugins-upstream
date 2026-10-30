## Description:

Use when building, debugging, or releasing a WPF app on .NET, including tray behavior, single-file publishing, DPI, startup, and release CI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build, debug, and release WPF desktop utilities on .NET. It provides project setup choices, symptom-based troubleshooting, development checks, and GitHub Actions release guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Desktop recovery advice may lead users to stop dwm.exe without understanding the wider display impact.

Mitigation: Review recovery steps first, prefer recovery limited to the affected application, and require explicit confirmation with a display-impact warning before stopping dwm.exe. Test overlays and input hooks in an isolated Windows session.

## Reference(s):

- [WPF Desktop skill page](https://clawhub.ai/rockbenben/skills/wpf-desktop)
- [Project setup guide](artifact/project-setup.md)
- [Troubleshooting pitfalls](artifact/pitfalls.md)
- [Development switches and checks](artifact/dev-switches.md)
- [GitHub Actions release guide](artifact/github-actions.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with code examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Version-sensitive recommendations; verify current releases before use.]

## Skill Version(s):

1.1.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
