## Description:

Helps an agent inspect and control common macOS system functions, including system status, processes, volume, brightness, network settings, power actions, screenshots, clipboard, Finder, and System Settings shortcuts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlutwuwei](https://clawhub.ai/user/dlutwuwei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and macOS users use this skill when they want an agent to propose or run command-line steps for checking system state, adjusting settings, managing processes, and performing common Finder, screenshot, clipboard, network, and power operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to run powerful local macOS system commands.

Mitigation: Review requested actions before execution and only install the skill when macOS system control is intended.

Risk: Shutdown, restart, process killing, and empty-trash commands can interrupt work or remove data.

Mitigation: Require explicit user confirmation and verify the target process, file location, or power action before running these commands.

Risk: Screenshot and clipboard commands may expose sensitive local information.

Mitigation: Confirm user intent before capturing screens or reading clipboard contents, and avoid sharing captured content beyond the current task.

Risk: Network commands can change Wi-Fi state or contact an external public-IP service.

Mitigation: Confirm network changes before execution and tell the user before running commands that contact external services such as ifconfig.me.

## Reference(s):

- [ClawHub skill page: mac-system-control](https://clawhub.ai/dlutwuwei/skills/mac-system-control)
- [ClawHub publisher profile: dlutwuwei](https://clawhub.ai/user/dlutwuwei)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include macOS command proposals, command output summaries, and confirmation prompts for sensitive actions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
