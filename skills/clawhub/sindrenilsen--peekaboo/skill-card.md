## Description:

Capture and automate macOS UI with the Peekaboo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sindrenilsen](https://clawhub.ai/user/sindrenilsen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-focused users use Peekaboo to inspect macOS UI, capture screenshots or video, and issue targeted input, window, menu, and system commands for desktop workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a mutable third-party Homebrew tap and a CLI that can control the macOS desktop.

Mitigation: Install only from a trusted Peekaboo tap, review updates before use, and grant permissions only on systems where that control is acceptable.

Risk: Screen Recording access can capture secrets, private content, or regulated data visible on the desktop.

Mitigation: Run captures against clearly scoped windows or apps, avoid sensitive screens, and handle generated screenshots or captures as sensitive artifacts.

Risk: Accessibility automation can click, type, paste, or manage windows in ways that affect local applications.

Mitigation: Use read-only commands such as list, permissions, and see before taking action, constrain targets with app/window selectors or element IDs, and revoke permissions when no longer needed.

## Reference(s):

- [Peekaboo homepage](https://peekaboo.boo)
- [ClawHub skill page](https://clawhub.ai/sindrenilsen/skills/peekaboo)
- [ClawHub publisher profile](https://clawhub.ai/user/sindrenilsen)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target macOS and may rely on Peekaboo JSON output, screenshot paths, window selectors, or UI element IDs.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
