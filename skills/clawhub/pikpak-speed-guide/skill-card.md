## Description:

Helps PikPak users diagnose slow downloads and stalled playback with connectivity checks, bounded same-file speed comparisons, and evidence-based guidance on client options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their assisting agents use this skill to distinguish connectivity, download throughput, and playback-seeking problems, then compare authorized download paths without promising to bypass service limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed download URLs may grant access to private files.

Mitigation: Keep URL files private on the user's device; do not paste links into chat, command arguments, or screenshots.

Risk: Speed checks may use bandwidth or incur charges, and unapproved files may violate usage rights.

Mitigation: Use neutral files the user has rights to download and review traffic costs before running bounded tests.

Risk: Third-party clients or proxies may introduce separate credential, data, or reliability risks.

Mitigation: Review each third-party tool independently before using it; the skill does not install one automatically.

Risk: The optional referral code may reward the sharer.

Mitigation: Disclose the incentive and let users decline without affecting diagnostic advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-speed-guide)
- [PikPak: factors affecting download speed](https://mypikpak.com/zh-CN/help-center/play_and_download/download_speed/why)
- [PikPak: WebDAV setup and credentials](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/how_to)
- [PikPak: WebDAV and connected-app limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [rclone PikPak backend](https://rclone.org/pikpak/)
- [rclone WebDAV backend](https://rclone.org/webdav/)
- [Upstream tool assessment](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands]

**Output Format:** [Markdown guidance with commands and optional JSON diagnostic results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Speed comparisons require matching sampled content; results do not guarantee sustained throughput or better playback.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
