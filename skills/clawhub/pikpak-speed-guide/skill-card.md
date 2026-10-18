## Description:

Diagnoses slow PikPak downloads and playback seeking with account-free connectivity checks and bounded same-file speed comparisons, then guides users through evidence-based client and WebDAV options without promising to bypass service limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and support agents can check connectivity without account access, compare bounded samples of the same authorized file across download paths, and choose a client or WebDAV workflow based on measured results and service limits.

### Deployment Geography for Use:

Global (primarily Simplified Chinese documentation)

## Known Risks and Mitigations:

Risk: Signed download URLs in local input files may grant access to private content.

Mitigation: Keep URL files private and out of the repository, chat, command-line arguments, and screenshots; use only files the user is authorized to download.

Risk: Network tests can incur data charges, and sample sizes do not bound all network traffic or billing.

Mitigation: Review traffic costs first and use the documented bounded sample settings rather than treating them as a billing cap.

Risk: Direct measurements do not represent an existing proxy route or prove a general speed improvement.

Mitigation: Report the no-proxy route and compare matching samples under controlled conditions; validate playback separately.

Risk: The disclosed referral code may benefit its sharer.

Mitigation: Keep referral choice separate from diagnostic recommendations and allow users to decline it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-speed-guide)
- [PikPak download speed guidance](https://mypikpak.com/zh-CN/help-center/play_and_download/download_speed/why)
- [PikPak WebDAV setup and credentials](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/how_to)
- [PikPak WebDAV speed limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [rclone PikPak backend](https://rclone.org/pikpak/)
- [rclone WebDAV backend](https://rclone.org/webdav/)
- [Upstream design and source review](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with Python commands and optional JSON measurement results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Direct, no-proxy measurements; a speed comparison requires matching authorized file samples.]

## Skill Version(s):

1.0.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
