## Description:

Use when saving a magnet link, URL, or share link into PikPak, or checking the status of a specific task by exact ID; it is not a persistent batch job system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

External PikPak users use this skill to submit magnet or URL tasks, inspect a specific task by exact ID, and selectively restore approved files from share links while confirming the account and destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The wrong account, files, destination, or overwrite behavior could be selected.

Mitigation: Use a trusted PikPak CLI and confirm the account, selected files, destination, and overwrite behavior before acting.

Risk: An uncertain task-creation result could lead to duplicate submissions or a task being misidentified.

Mitigation: Keep the exact task ID, stop on unknown outcomes, and reconcile manually rather than retrying creation or guessing from task lists.

Risk: Documented CLI guidance may not match current live service behavior.

Mitigation: Confirm behavior before acting; live service behavior was not verified.

## Reference(s):

- [PikPak Help Center: Connected Apps Speed Limit](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [PikPak Help Center: Connected Apps Transfer Quota](https://mypikpak.com/zh-CN/help-center/transfer_quota/connected_apps_quota)
- [Rclone PikPak task-handling design reference](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/backend/pikpak/helper.go#L186-L215)
- [GitHub CLI login-flow design reference](https://github.com/cli/cli/blob/3d7967df5a94052b0554898ffa02526f0f90b8c9/pkg/cmd/auth/shared/login_flow.go#L204-L210)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with PikPak CLI commands and JSON task-status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No persistent task ledger or background queue; task inspection is local and does not access the network or credentials.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
