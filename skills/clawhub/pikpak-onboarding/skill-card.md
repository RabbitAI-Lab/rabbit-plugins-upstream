## Description:

Guides users through PikPak CLI setup, account registration, referral choices, and verification of a first cloud-download task, without unattended signup or automatic recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

External PikPak users use this skill for guided CLI setup, account registration with an explicit referral choice, and checking the first authorized magnet or share-link cloud task. It provides instructions and command previews rather than unattended account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A referral may reward the guide's publisher, and an omitted referral option may inherit an installer-recorded code.

Mitigation: Disclose the referral before registration, obtain an explicit accept-or-decline choice, and use the explicit empty option when declined.

Risk: Cloud tasks affect the user's account and can consume connected-app transfer quota.

Mitigation: Authorize only the user's own account and confirm the destination and quota impact before creating a task.

Risk: A CLI's logged-in state does not establish account identity.

Mitigation: Confirm the account is the user's and authorized before account queries or task actions; do not treat logged-in status as identity verification.

## Reference(s):

- [PikPak CLI installation](https://mypikpak.com/cli)
- [PikPak CLI registration policy](https://mypikpak.com/en-US/help-center/connected_apps/pikpak_cli/register_account)
- [PikPak connected-app speed limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [PikPak connected-app transfer quota](https://mypikpak.com/zh-CN/help-center/transfer_quota/connected_apps_quota)
- [GitHub CLI login flow design reference](https://github.com/cli/cli/blob/3d7967df5a94052b0554898ffa02526f0f90b8c9/pkg/cmd/auth/shared/login_flow.go#L204-L210)
- [rclone PikPak task handling design reference](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/backend/pikpak/helper.go#L186-L215)
- [Upstream design notes](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON command-plan output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interactive, user-confirmed steps; the registration helper previews commands and does not execute them.]

## Skill Version(s):

1.0.9 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
