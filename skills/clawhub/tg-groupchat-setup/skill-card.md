## Description: <br>
Configure a MoltBot agent to participate in a Telegram group chat by patching the gateway allowlist, mention patterns, and sender permissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arekqq](https://clawhub.ai/user/arekqq) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and MoltBot operators use this skill to set up a Telegram group so an agent responds only when mentioned and only from allowed senders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup reads a Telegram bot token while detecting bot identity. <br>
Mitigation: Protect the token from logs and screenshots, and avoid sharing command output that could expose credentials. <br>
Risk: The skill applies persistent gateway configuration changes for Telegram group access and sender permissions. <br>
Mitigation: Review the group ID, allowed users, mention patterns, and patch contents before applying the configuration. <br>
Risk: Turning Telegram privacy mode off allows the bot to receive group messages even when responses are mention-gated. <br>
Mitigation: Confirm that group participants understand the privacy mode behavior before enabling the setup. <br>


## Reference(s): <br>
- [Telegram Bot Privacy Mode](references/telegram-privacy-mode.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/arekqq/skills/tg-groupchat-setup) <br>
- [Publisher Profile](https://clawhub.ai/user/arekqq) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces gateway configuration guidance and confirmation text; no generated files are part of the skill output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
