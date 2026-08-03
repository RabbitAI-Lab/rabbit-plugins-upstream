## Description: <br>
Applies a WorkBuddy desktop visual skin with animated or static backgrounds, glass-style UI changes, a calendar strip, and a sound-enabled counter through runtime injection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kuzen-so](https://clawhub.ai/user/kuzen-so) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Users and developers customizing a local WorkBuddy desktop app use this skill to apply, pause, and adjust a visual skin with Node.js commands. It is intended for local desktop theming and related configuration, not for changing WorkBuddy's underlying app package. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run WorkBuddy with a local debugging port. <br>
Mitigation: Install only when that local debugging posture is intentional, and pause or restart WorkBuddy when the skin is no longer needed. <br>
Risk: Automatic mode can add a persistent background LaunchAgent. <br>
Mitigation: Use automatic mode only when persistent reinjection is desired, and keep the uninstall-auto script available before enabling it. <br>
Risk: The launcher-flag install path can modify the WorkBuddy app launcher. <br>
Mitigation: Use the launcher modification only after confirming the reversal path, including the uninstall-flag script. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kuzen-so/skills/workbuddy-skin-chiikawa) <br>
- [Publisher profile](https://clawhub.ai/user/kuzen-so) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, file paths, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to start WorkBuddy with a local CDP debugging port and optionally install a macOS LaunchAgent for automatic reinjection.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
