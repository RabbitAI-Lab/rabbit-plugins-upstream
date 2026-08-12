## Description:

Desktop Autopilot helps an AI agent operate desktop GUIs through visual element matching, OCR text location, intelligent waits, workflow orchestration, recording/playback, DPI adaptation, and multi-monitor support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-focused agent builders use this skill to create GUI workflows for form filling, data entry, app-to-app transfer, UI regression testing, and repetitive desktop tasks where visual checks are safer than fixed coordinates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control the GUI and capture screen content, which may expose sensitive applications or regulated data.

Mitigation: Use it only for explicit desktop automation tasks and avoid credentials or regulated data unless the environment, logs, and screenshots are controlled.

Risk: Logs, recordings, and snapshots may persist sensitive desktop content.

Mitigation: Periodically clear or disable persistent logs, recordings, and snapshots, and restrict access to their storage locations.

Risk: Automated clicks, typing, and app-to-app copying can affect the wrong window or perform unintended actions.

Mitigation: Enable confirmation and failsafe behavior, use visual checks before actions, and review workflows before running them on important systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/desktop-autopilot)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dependency setup, desktop automation steps, workflow examples, and safety guidance for GUI actions.]

## Skill Version(s):

1.0.1 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
