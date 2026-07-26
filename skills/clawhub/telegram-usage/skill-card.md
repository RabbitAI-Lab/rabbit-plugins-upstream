## Description: <br>
Displays session usage statistics including quota, reset timing, token usage, and context usage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[c-drew](https://clawhub.ai/user/c-drew) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Clawdbot users and operators use this skill from Telegram or the CLI to check current API quota, reset timing, token usage, and context usage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Invoking the skill can expose usage metadata such as provider, token counts, context usage, reset timing, and a truncated session ID in the Telegram chat where it runs. <br>
Mitigation: Use it only in Telegram chats where that operational metadata is acceptable to disclose. <br>
Risk: The skill depends on the local Clawdbot installation and the clawdbot command available in PATH. <br>
Mitigation: Install only where the local Clawdbot installation and PATH-resolved command are trusted. <br>


## Reference(s): <br>
- [Telegram Usage Stats ClawHub page](https://clawhub.ai/c-drew/skills/telegram-usage) <br>
- [Clawdbot skills documentation](https://docs.clawd.bot/tools/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration] <br>
**Output Format:** [Telegram-safe text or HTML-formatted message, with optional JSON output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a trusted local Clawdbot installation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
