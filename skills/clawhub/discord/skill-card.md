## Description: <br>
Use when you need to control Discord from Clawdbot via the discord tool: send messages, react, post or upload stickers, upload emojis, run polls, manage threads/pins/search, fetch permissions or member/role/channel info, or handle moderation actions in Discord DMs or channels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent interact with Discord through a configured bot, including messages, reactions, polls, threads, pins, search, server information, role changes, and moderation actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can post, edit, delete, search, and read Discord messages, which may expose sensitive channel content or change public server state. <br>
Mitigation: Install it only for trusted bots and servers, limit enabled action groups, restrict bot permissions to intended channels, and require confirmation before posting, deleting, editing, or searching sensitive channels. <br>
Risk: Role and moderation actions can affect users and server administration. <br>
Mitigation: Keep role and moderation action groups disabled unless they are explicitly needed, and require clear confirmation before changing roles, timing out, kicking, or banning users. <br>
Risk: Media upload actions can send local file paths or remote media into Discord. <br>
Mitigation: Confirm the exact file or URL before upload, restrict access to intended local paths, and disable emoji, sticker, or message uploads when they are not needed. <br>


## Reference(s): <br>
- [Discord skill page](https://clawhub.ai/steipete/skills/discord) <br>
- [Publisher profile](https://clawhub.ai/user/steipete) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, API Calls, Configuration] <br>
**Output Format:** [Markdown guidance with JSON action examples and Discord message text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Discord tool action payloads and user-facing message guidance; some action groups can be disabled with discord.actions.* configuration.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
