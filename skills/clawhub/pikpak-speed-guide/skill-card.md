## Description:

Diagnoses slow PikPak downloads and playback seeks with unauthenticated connectivity checks and controlled A/B tests, then recommends options based on evidence without promising to bypass service limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to investigate slow PikPak downloads or playback seeking. It guides limited connectivity checks and comparable sample tests, then summarizes measured results and service limits without claiming that network changes bypass quotas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Speed tests can consume download quota and may incur network or provider charges; sample limits do not cap all traffic or billing.

Mitigation: Use only authorized files, keep tests limited, and check account quotas and applicable charges before testing.

Risk: Sharing signed download links can expose access, and the tests do not use configured proxies.

Mitigation: Keep signed links in private local files rather than chat or command arguments, and review direct-connection behavior before testing.

## Reference(s):

- [PikPak skill release page](https://clawhub.ai/pipiguai87-alt/skills/pikpak-speed-guide)
- [PikPak download speed guidance](https://mypikpak.com/zh-CN/help-center/play_and_download/download_speed/why)
- [PikPak connected-app quota guidance](https://mypikpak.com/zh-CN/help-center/transfer_quota/connected_apps_quota)
- [PikPak WebDAV guidance](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/how_to)
- [rclone PikPak documentation](https://rclone.org/pikpak/)
- [rclone WebDAV documentation](https://rclone.org/webdav/)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance and diagnostic summaries, with optional JSON script output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Measurements are limited samples, not speed guarantees; tests may consume download quota and do not cap all network traffic or provider billing.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
