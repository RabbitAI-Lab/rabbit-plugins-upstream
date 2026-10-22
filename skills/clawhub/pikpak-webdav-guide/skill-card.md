## Description:

Guides users through enabling PikPak WebDAV, configuring supported clients, and checking access, permissions, and quota limits without promising faster speeds or bypassing service restrictions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users configure WebDAV in media players, file managers, or rclone and perform cautious access checks. The guide distinguishes WebDAV from native PikPak integrations and explains membership, credential permissions, and transfer-quota limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dedicated WebDAV credentials can modify files, not just read them.

Mitigation: Enter credentials only in a trusted local client, never share them in chat, and revoke exposed credentials through the official account page.

Risk: The optional account-status check invokes a local CLI with the operator's environment.

Mitigation: Use it only after deliberate authorization for an account the user controls, and trust the selected CLI executable and environment.

Risk: The metadata checker cannot establish WebDAV connectivity or available transfer quota.

Mitigation: Verify connectivity separately with an authorized client and check transfer quota in the official account page.

## Reference(s):

- [PikPak WebDAV setup](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/how_to)
- [PikPak WebDAV speed limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [rclone WebDAV configuration](https://rclone.org/webdav/)
- [rclone mount documentation](https://rclone.org/commands/rclone_mount/)
- [upstream-design.md](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, Code, JSON]

**Output Format:** [Markdown guidance with shell examples and optional JSON metadata reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes user-controlled setup and read-only checks; does not verify live WebDAV connectivity or transfer quota.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
