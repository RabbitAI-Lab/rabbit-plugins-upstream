## Description:

Capture and automate macOS UI with the Peekaboo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill to capture, inspect, and automate macOS application UI with Peekaboo, including screenshots, element targeting, input actions, app/window/menu control, and JSON-scripted workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Peekaboo can view the screen, control input, use the clipboard, and manage apps after macOS Screen Recording and Accessibility permissions are granted.

Mitigation: Install only when those permissions are acceptable, avoid using it around passwords, tokens, private documents, or sensitive clipboard contents unless required, and scope automation to the task.

Risk: Automation commands or scripts can expose real credentials if they hardcode or type sensitive values.

Mitigation: Do not hardcode real credentials in Peekaboo commands or .peekaboo.json scripts; use appropriate runtime secret handling or test accounts when credentials are needed.

## Reference(s):

- [Peekaboo homepage](https://peekaboo.boo)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/peekaboo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON-oriented CLI usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [macOS only; requires the peekaboo binary plus Screen Recording and Accessibility permissions.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
