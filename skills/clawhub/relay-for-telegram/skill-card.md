## Description: <br>
Relay for Telegram lets an agent search, retrieve, summarize, and extract action items from a user's synced Telegram message history through Relay's API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[relayintel](https://clawhub.ai/user/relayintel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent answer Telegram-related questions, search synced chats, summarize conversations, and extract action items after the user configures RELAY_API_KEY. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad access to private synced Telegram message history. <br>
Mitigation: Install only if you trust Relay to sync and store that history, keep RELAY_API_KEY private, and review message-derived outputs before relying on them. <br>
Risk: Model invocation is enabled, so an agent may access Telegram data when it decides a request is Telegram-related. <br>
Mitigation: Consider disabling model invocation, requiring explicit skill use, or removing RELAY_API_KEY when Telegram access should not be available. <br>
Risk: The artifact documents billing and referral actions even though the security summary notes the skill is not purely read-only. <br>
Mitigation: Require explicit user confirmation before any billing or referral workflow and prefer read-only search, chat, and message retrieval operations. <br>


## Reference(s): <br>
- [Relay for Telegram on ClawHub](https://clawhub.ai/relayintel/skills/relay-for-telegram) <br>
- [Relay homepage](https://relayfortelegram.com) <br>
- [Relay API base URL](https://relayfortelegram.com/api/v1) <br>
- [Relay skill source](https://relayfortelegram.com/skill.md) <br>
- [Relay agent reference](https://relayfortelegram.com/agents.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with REST API examples and optional JSON summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires RELAY_API_KEY; API access is rate-limited and limited to synced Telegram data.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release metadata; artifact frontmatter says 2.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
