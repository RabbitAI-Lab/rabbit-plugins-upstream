## Description:

Guides PikPak members through official WebDAV setup, client connection, and cautious read-only checks without promising faster transfers or quota bypasses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak account holders and media-library users use this skill to enable official WebDAV, configure Infuse, VidHub, or rclone, and check access without sharing credentials with an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WebDAV credentials can manage files, and disclosing them can expose account contents.

Mitigation: Create dedicated credentials on PikPak's official page, enter them only into trusted local clients, keep them out of chat, and revoke exposed credentials.

Risk: The optional checker can query account metadata through a local PikPak executable.

Mitigation: Run it only on a trusted machine with a trusted PikPak binary, and query an account only after its owner authorizes the check.

Risk: The disclosed optional referral code may reward the sharer.

Mitigation: Let users decline the referral without affecting setup guidance.

## Reference(s):

- [PikPak WebDAV Guide release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-webdav-guide)
- [PikPak official WebDAV setup](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/how_to)
- [PikPak connected-app transfer limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [rclone WebDAV configuration](https://rclone.org/webdav/)
- [rclone PikPak backend](https://rclone.org/pikpak/)
- [Upstream design and verification boundaries](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, JSON]

**Output Format:** [Markdown guidance and example commands; optional checker reports text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional checker reports membership metadata only; WebDAV access and transfer quotas remain unverified.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
