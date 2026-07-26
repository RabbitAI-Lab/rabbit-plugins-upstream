## Description: <br>
Give OpenClaw full access to a user-owned Telegram session so it can automate workflows and manage chats through local or hosted CRM paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seichris](https://clawhub.ai/user/seichris) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when they want an agent to work with Telegram through an explicit user-owned login instead of the narrower Telegram Bot API. It supports hosted Chiho.ai CRM workflows and a self-hosted tgchats runtime for local Telegram session access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may gain broad visibility into Telegram chats available to the logged-in account. <br>
Mitigation: Install only when account-level Telegram access is intended, and prefer a dedicated Telegram account for clearer workflow boundaries. <br>
Risk: Chiho tokens and Telegram API credentials can grant sensitive account or session access if exposed. <br>
Mitigation: Protect tokens and credentials like passwords, avoid placing them in URLs or shared logs, and revoke tokens or log out sessions when access is no longer needed. <br>
Risk: Write-capable Telegram workflows can send messages from the connected account. <br>
Mitigation: Enable message sending only for approved write-capable workflows and require explicit user approval before sending. <br>


## Reference(s): <br>
- [Telegram Full Access on ClawHub](https://clawhub.ai/seichris/skills/telegram-full-access) <br>
- [telegram-for-ai-agents on GitHub](https://github.com/chihoai/telegram-for-ai-agents) <br>
- [Local tgchats runtime skill](https://github.com/chihoai/telegram-for-ai-agents/blob/main/skills/tgchats-local/SKILL.md) <br>
- [Telegram workflow catalog](https://github.com/chihoai/telegram-for-ai-agents/blob/main/docs/SKILL_CATALOG.md) <br>
- [Chiho.ai signup](https://chiho.ai/signup) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference optional environment variables TELEGRAM_API_ID, TELEGRAM_API_HASH, and DATABASE_URL depending on the runtime path.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
