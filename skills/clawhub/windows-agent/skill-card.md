## Description:

Windows Agent lets an agent inspect and control a local Windows desktop through PowerShell scripts for screenshots, window control, mouse and keyboard input, UI Automation, clipboard handling, waits, and process management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunsettide](https://clawhub.ai/user/sunsettide)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill when they want an agent to observe a Windows desktop, manipulate windows, click or type into UI, wait for UI state, read accessible text, manage clipboard contents, and inspect or manage local processes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can see screen contents and read accessible UI text across the local Windows desktop.

Mitigation: Install only when desktop control is intended, avoid sensitive windows unless explicitly needed, and clean up saved screenshots after use.

Risk: The skill can click, type, alter clipboard contents, close windows, and manage processes.

Mitigation: Review actions before clicks, text entry, clipboard writes, window closes, or process kills, and confirm destructive or irreversible operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sunsettide/skills/windows-agent)
- [SKILL.md](SKILL.md)
- [PREREQUISITES.md](PREREQUISITES.md)
- [CHANGELOG.md](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with PowerShell command examples; scripts emit plain text status, file paths such as IMAGE_READY, and screenshot image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-only execution; requires a logged-in desktop session and PowerShell 7.]

## Skill Version(s):

0.0.1 (source: release metadata and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
