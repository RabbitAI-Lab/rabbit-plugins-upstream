## Description:

Enables an agent to control a Windows desktop through a bundled standalone computer-use runtime and MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chimeraone1](https://clawhub.ai/user/chimeraone1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to take screenshots and interact with Windows applications through mouse, keyboard, window, and clipboard controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The runtime automatically grants requested app, clipboard, and system-key permissions despite prompts suggesting user approval is required.

Mitigation: Do not rely on its permission prompts; use only in a contained, trusted Windows session.

Risk: Live desktop access can expose sensitive windows and clipboard contents.

Mitigation: Keep sensitive windows closed and avoid sensitive clipboard contents while the skill is active.

## Reference(s):

- [Windows Computer-Use Skill on ClawHub](https://clawhub.ai/chimeraone1/skills/computer-use-windows)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Images]

**Output Format:** [Markdown instructions and MCP tool results, including screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-only; desktop actions and screenshots require a trusted local session.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
