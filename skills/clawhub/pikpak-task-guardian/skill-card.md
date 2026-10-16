## Description:

Monitors PikPak cloud download tasks, retries eligible failures, notifies on completion, and provides a daily status report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents use this skill to check cloud download progress, retry failed tasks when a source is registered, receive completion notifications, and review daily activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring monitoring can remove and recreate failed cloud tasks.

Mitigation: Review task sources and enable background retries only when intended; prefer one-shot monitoring otherwise.

Risk: Untrusted task names can trigger AppleScript injection in macOS notifications.

Mitigation: Do not run the current macOS notification path against untrusted task names until its AppleScript construction is fixed.

Risk: A user-selected PikPak executable may run during monitoring and retries.

Mitigation: Keep the PikPak executable path under your control and review the skill before installation.

## Reference(s):

- [PikPak Task Guardian on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-task-guardian)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown instructions and plain-text status reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Completion notifications on macOS; status messages in logs on other platforms.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
