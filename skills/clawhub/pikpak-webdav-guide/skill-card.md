## Description:

Guides users through enabling PikPak WebDAV, connecting trusted clients, and checking access while explaining credential permissions and service limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak account holders and developers use this guide to enable official WebDAV access and connect media players or rclone to their own files. An optional local check reports account metadata without claiming to verify WebDAV connectivity or transfer quota.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WebDAV credentials can manage files, and sharing them may expose the account.

Mitigation: Configure dedicated credentials only in trusted local clients; never share passwords or tokens in chat, and revoke exposed credentials.

Risk: Account metadata or successful login could be mistaken for verified WebDAV eligibility or available transfer quota.

Mitigation: Confirm membership, WebDAV activation, and actual quotas in the official account page; treat the optional check as metadata-only.

Risk: The optional account check runs a local PikPak executable and inherits its environment.

Mitigation: Run it only for your own account with explicit authorization and trusted script, executable, PATH, and PIKPAK_BIN settings.

Risk: The disclosed referral code may financially benefit its sharer.

Mitigation: Treat the referral as optional and decline it if preferred.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-webdav-guide)
- [PikPak WebDAV setup](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/how_to)
- [PikPak connected-app limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [rclone WebDAV configuration](https://rclone.org/webdav/)
- [Upstream design and verification boundaries](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local check produces text or JSON account-metadata hints; it does not verify WebDAV access or transfer quota.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
