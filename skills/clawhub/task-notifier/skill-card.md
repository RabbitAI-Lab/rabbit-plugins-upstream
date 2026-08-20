## Description:

Task Notifier provides documentation and operating guidance for installing, configuring, verifying, and uninstalling an OpenClaw desktop notification runtime plugin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wdgame](https://clawhub.ai/user/wdgame)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to set up desktop notifications when OpenClaw agents or subagents finish user-initiated work. It also guides verification, troubleshooting, filtering, and rollback for the Task Notifier runtime plugin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The runtime plugin is persistent and can observe OpenClaw lifecycle hook context across agents.

Mitigation: Install only after explicit user consent and acceptance of the documented unsafe-install warning.

Risk: The runtime plugin runs local OS notification commands and reads the active foreground window title for suppression.

Mitigation: Review the security notice before installation, run the doctor after setup, and adjust the active-window match configuration if suppression behaves incorrectly.

Risk: The runtime plugin writes small per-run state files under active workspaces.

Mitigation: Use the documented disable, uninstall, gateway restart, and stale-state cleanup commands when rolling back.

## Reference(s):

- [Task Notifier ClawHub Page](https://clawhub.ai/wdgame/skills/task-notifier)
- [Task Notifier Reference README](references/README.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with bash command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes install, verification, configuration, diagnostic, and rollback guidance.]

## Skill Version(s):

1.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
