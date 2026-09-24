## Description:

Helps agents control Android devices from OpenClaw using ADB, wireless debugging, Termux, intents, UI automation, app launching, screenshots, logging, and verified recovery workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to let an agent inspect Android device state, select an appropriate control method, execute permitted Android actions, and verify the result. It is aimed at ADB, Termux, intents, app control, UI automation, screenshots, logging, and safe message-preparation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Android automation can affect the wrong device, app, or screen state if the environment is assumed instead of checked.

Mitigation: Verify ADB availability, authorization, target device, current app state, and command result before proceeding to the next action.

Risk: ADB and wireless debugging can expose device control when authorized for untrusted devices or hosts.

Mitigation: Keep device debugging authorized only for trusted devices and hosts, and disconnect or revoke access when it is no longer needed.

Risk: Message sending, app install or uninstall, data deletion, security changes, and screenshots of sensitive screens can create privacy or user-impacting harm.

Mitigation: Require clear user confirmation for sensitive or destructive actions, use the minimum necessary action, and avoid capturing or logging private data unless required for the task.

## Reference(s):

- [ClawHub Android Control Skill](https://clawhub.ai/pmuhammadagus-byte/skills/android-control)
- [Project Homepage](https://github.com/pmuhammadagus-byte/openclaw-settings)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes verification, minimal action, and confirmation boundaries for sensitive or destructive Android actions.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
