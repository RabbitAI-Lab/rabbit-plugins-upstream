## Description:

Guides users through account-free connectivity checks and bounded, integrity-checked comparisons of authorized PikPak downloads without promising to bypass speed limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and support agents can distinguish connectivity from download performance, compare authorized file paths using limited matching samples, and select a client or WebDAV path based on observed results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed download links can expose access credentials.

Mitigation: Keep links in private local files; do not paste them into chat, commands, or screenshots.

Risk: Small, direct-connection samples may misrepresent sustained downloads or existing proxy performance and incur data charges.

Mitigation: Compare the same authorized file under controlled conditions, confirm the traffic budget, and report proxy and sample limitations.

Risk: A third-party proxy may mishandle authentication, file ranges, or cached data.

Mitigation: Review its version, credential handling, range correctness, and cache isolation before use; do not deploy it automatically.

## Reference(s):

- [PikPak download-speed guidance](https://mypikpak.com/zh-CN/help-center/play_and_download/download_speed/why)
- [PikPak WebDAV setup and permissions](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/how_to)
- [PikPak WebDAV connected-app limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [rclone PikPak backend](https://rclone.org/pikpak/)
- [rclone WebDAV backend](https://rclone.org/webdav/)
- [Upstream design and limitations](references/upstream-design.md)
- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-speed-guide)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Analysis]

**Output Format:** [Markdown guidance with shell commands and optional JSON diagnostic results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports observations and bounded sample comparisons; a speedup ratio is given only when samples pass integrity checks.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
