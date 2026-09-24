## Description:

Computer Control (tarsx) lets an agent inspect and operate a desktop by taking screenshots, clicking, typing, pressing hotkeys, scrolling, launching apps, opening URLs, and running AppleScript through the bundled tarsx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[topgemstoken](https://clawhub.ai/user/topgemstoken)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agent operators use this skill when shell or browser tools cannot reach a GUI workflow, such as inspecting the screen, selecting windows by app name, filling desktop forms, and performing controlled desktop actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad live computer control, including screenshots, clicking, typing, launching apps, and URL opening.

Mitigation: Use it only with trusted agents and prompts, review proposed actions before execution, and confirm sensitive or destructive actions with the user.

Risk: The tarsx osa command can run arbitrary AppleScript on macOS.

Mitigation: Review AppleScript before running it, avoid credential and one-time-code entry, and rely on macOS Accessibility, Screen Recording, and Automation permissions as explicit control points.

Risk: Linux app launching accepts app names that can be risky if untrusted input is passed through.

Mitigation: Use known application names only and do not pass user-controlled shell fragments as app names.

## Reference(s):

- [Computer Control (tarsx) on ClawHub](https://clawhub.ai/topgemstoken/skills/computer-control)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline tarsx shell commands and optional JSON command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create screenshot PNG files and machine-readable JSON when --json is used.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
