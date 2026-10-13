## Description:

Top-level Windows computer-use skill with a bundled standalone runtime that bootstraps itself without any local Claude installation, private native modules, or extracted app assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wimi321](https://clawhub.ai/user/wimi321)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to build and run a Windows-only MCP server that gives an agent screenshot, mouse, keyboard, app launch, window/display mapping, and clipboard capabilities through a bundled standalone runtime.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local MCP client can control the active Windows desktop, including mouse, keyboard, app launch, screenshots, and clipboard access.

Mitigation: Install only on a trusted local Windows host, close sensitive windows before use, and review requested actions before granting desktop access.

Risk: Screenshots can expose anything visible on the selected monitor because the runtime reports no native screenshot filtering.

Mitigation: Use a dedicated workspace or monitor, avoid displaying sensitive information, and rely on MCP-layer action gating where available.

Risk: The security evidence reports desktop, screenshot, clipboard, and system-key access without a real user approval prompt.

Mitigation: Prefer a release that adds explicit user approval for each app and clipboard or system-key flag before broad deployment.

Risk: Runtime behavior has not been end-to-end validated on a real Windows machine according to the bundled validation notes.

Mitigation: Validate GUI control, screenshot capture, UAC and elevated-window behavior, secure desktop transitions, and multi-monitor DPI behavior before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wimi321/skills/computer-use-windows)
- [Project repository](https://github.com/wimi321/windows-computer-use-skill)
- [Bundled project README](artifact/project/README.md)
- [Example MCP configuration](artifact/project/examples/mcp-config.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with shell commands and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-only runtime; first launch may create a Python virtual environment and install public Python dependencies.]

## Skill Version(s):

0.1.1 (source: SKILL.md frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
