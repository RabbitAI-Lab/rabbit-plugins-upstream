## Description:

Guides developers in packaging a client-side Next.js static export as an offline Windows Electron app without requiring WebView2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to turn client-side Next.js static exports into self-contained Windows desktop apps for offline or intranet computers without WebView2. It provides Electron source templates, packaging steps, tests, and CI release guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A copied CI release template may use unsuitable release permissions or action versions for the destination repository.

Mitigation: Review release permissions, dependency versions, and action versions before enabling the workflow.

Risk: The generated app writes local settings and may remain active in the Windows tray after its window closes.

Mitigation: Inform users about the settings file and provide a clear tray Quit action.

## Reference(s):

- [Project homepage (listed in skill metadata)](https://github.com/rockbenben/aishort-skills/tree/main/skills/nextjs-to-electron)
- [ClawHub skill listing](https://clawhub.ai/rockbenben/skills/nextjs-to-electron)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Windows packaging and CI release templates; the resulting app may save local settings and remain in the tray until quit.]

## Skill Version(s):

1.1.6 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
