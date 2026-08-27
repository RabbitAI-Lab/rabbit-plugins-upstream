## Description:

Use when controlling Android from OpenClaw via ADB, wireless debugging, Termux, intents, UI automation, app launching, screenshots, logging, and safe message actions with verification and recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw operators use this skill to control Android devices through ADB, wireless debugging, Termux, intents, and UI automation while checking device state and verifying each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ADB and wireless debugging can provide broad control over an Android device.

Mitigation: Limit ADB and wireless debugging to trusted devices, verify authorization before commands, and use the minimum action needed for the task.

Risk: Real messages, app installation or removal, file deletion, account data, screenshots, logs, and security settings can affect privacy or device state.

Mitigation: Review these actions before execution, confirm the target and intent, and verify the result after completion.

Risk: UI automation or intents may act on the wrong app, screen, recipient, or element if state is assumed.

Mitigation: Inspect the current device state, prefer verified package names and semantic UI selectors, and re-check state after each action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/android-control)
- [README](README.md)
- [Skill homepage](https://github.com/pmuhammadagus-byte/openclaw-settings)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose ADB, Termux, intent, UI inspection, and verification steps for Android control tasks.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
