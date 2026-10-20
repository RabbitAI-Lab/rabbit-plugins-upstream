## Description:

Use Telegram to submit links to PikPak and check transfer tasks and root-directory listings, with authorized chats and explicit approval for deployment and outbound messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

External users can authorize the bot to submit PikPak links and query transfer tasks or recent root-directory entries from Telegram. Developers can use the included setup and recovery guidance to configure it without granting access to unapproved chats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized users could submit links or view bot replies, especially in group chats.

Mitigation: Authorize deployment explicitly, restrict both allowed chats and group senders, and prefer private chats for sensitive filenames or query results.

Risk: Bot credentials or persistent account state could be exposed or used with the wrong account.

Mitigation: Keep the token and state directory private, use a non-sensitive account-scope alias, and do not reuse state across PikPak accounts.

Risk: A custom Telegram API endpoint or PikPak executable could redirect credentials or actions to an untrusted service.

Mitigation: Use a trusted PikPak executable and retain the default Telegram endpoint unless you control the replacement.

Risk: A submission with an uncertain outcome could be duplicated if resent, and live compatibility and recovery remain unverified.

Mitigation: Check uncertain submissions manually before resending; treat live compatibility and recovery tests as pending rather than proven.

## Reference(s):

- [Upstream design evidence (reference, not release provenance)](artifact/references/upstream-design.md)
- [Telegram Bot API: getUpdates](https://core.telegram.org/bots/api#getupdates)
- [Telegram Bot API: Message](https://core.telegram.org/bots/api#message)
- [PikPak connected-app quota guidance](https://mypikpak.com/zh-CN/help-center/transfer_quota/connected_apps_quota)
- [PikPak connected-app speed limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [PikPak CLI help](https://mypikpak.com/en-US/help-center/connected_apps/pikpak_cli)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration instructions]

**Output Format:** [Text responses and Markdown setup or recovery instructions with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report task status or recent root-directory entries; /ls is limited to the most recent 10 entries.]

## Skill Version(s):

1.0.9 (source: server-resolved target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
