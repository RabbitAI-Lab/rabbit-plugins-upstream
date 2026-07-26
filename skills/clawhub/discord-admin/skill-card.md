## Description: <br>
Complete A-Z Discord server administration. Channel/role/member management, AutoMod, webhooks, templates, audit logs, scheduled events, threads, and full server control via CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thebigbrainchad](https://clawhub.ai/user/thebigbrainchad) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Discord server administrators and automation-focused developers can use this skill to generate or run CLI workflows for managing channels, roles, members, messages, AutoMod rules, webhooks, invites, audit logs, events, and other server settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad Discord server-changing power. <br>
Mitigation: Use a dedicated least-privilege bot limited to the intended guild and grant only the permissions required for the planned task. <br>
Risk: Discord bot tokens can be exposed through command-line arguments, logs, or shared shell history. <br>
Mitigation: Provide tokens through a protected environment variable or secret manager, avoid passing tokens on the command line, and keep tokens out of logs. <br>
Risk: Delete, ban, kick, webhook, role, guild-setting, and bulk commands can cause disruptive or irreversible server changes. <br>
Mitigation: Manually review each high-impact command before execution and test automation on a limited or non-production guild when possible. <br>


## Reference(s): <br>
- [Discord API v10](https://discord.com/api/v10) <br>
- [ClawHub skill page](https://clawhub.ai/thebigbrainchad/skills/discord-admin) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown with bash command examples and shell scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, a Discord bot token, and the intended Discord guild or resource IDs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
