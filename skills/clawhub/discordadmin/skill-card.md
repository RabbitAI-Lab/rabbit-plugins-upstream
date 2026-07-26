## Description: <br>
Complete A-Z Discord server administration, including channel, role, member, AutoMod, webhook, template, audit log, scheduled event, thread, and full server control through a CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thebigbrainchad](https://clawhub.ai/user/thebigbrainchad) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and server administrators use this skill to manage Discord servers through shell commands that call the Discord API. It is intended for live server administration tasks such as moderation, channel and role management, message operations, webhooks, templates, audit logs, scheduled events, and bulk actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad live-server control over Discord administration actions. <br>
Mitigation: Install only when agent-led Discord administration is intended, and use a dedicated bot with the minimum permissions needed instead of Administrator where possible. <br>
Risk: Destructive or bulk actions such as delete, ban, prune, webhook, guild-edit, template, and bulk operations can affect production servers. <br>
Mitigation: Test on a non-production server first and require explicit human review before running destructive, bulk, or server-wide actions. <br>
Risk: Discord bot tokens can be exposed through command arguments, logs, shared terminals, or environment handling. <br>
Mitigation: Keep the token out of logs and shared terminals, avoid passing tokens with --token, and provide credentials through protected environment configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thebigbrainchad/skills/discordadmin) <br>
- [Publisher profile](https://clawhub.ai/user/thebigbrainchad) <br>
- [Discord API v10 endpoint](https://discord.com/api/v10) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command output from the Discord API] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Discord bot token and Discord permissions appropriate to the requested server action.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
