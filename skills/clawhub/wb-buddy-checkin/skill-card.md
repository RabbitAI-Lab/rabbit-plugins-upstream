## Description:

Automates WorkBuddy Buddy Gas Station daily check-ins on Windows, using either authenticated API calls or calibrated GUI clicks with screenshot-based verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

Employees or individual WorkBuddy users use this skill to claim daily Buddy Gas Station points through a Windows agent. The API check-in path is preferred, with calibrated GUI automation available as a fallback when local login state or API access is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read a local WorkBuddy/CodeBuddy login token and send authenticated requests to copilot.tencent.com.

Mitigation: Use API mode only when the user accepts token access; otherwise prefer the GUI-only path or require an explicit prompt before API execution.

Risk: The skill can control the mouse and save screenshots or state files in the skill directory.

Mitigation: Run after coordinate calibration, avoid active user sessions when possible, and review generated screenshots and state files after execution.

Risk: The update recovery flow can create a temporary Windows scheduled task.

Mitigation: Require explicit approval before scheduled-task recovery and verify the task is removed after the check-in flow completes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/wb-buddy-checkin)
- [Coordinate calibration guide](references/calibration.md)
- [WorkBuddy service host](https://copilot.tencent.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash command blocks; scripts may emit local PNG and JSON state files when run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Windows exit codes to report success, failure, missing WorkBuddy window, or update recovery state.]

## Skill Version(s):

0.1.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
