## Description: <br>
Monitor iMessage/SMS conversations and auto-respond based on configurable rules, AI prompts, and rate-limiting conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koba42corp](https://clawhub.ai/user/koba42corp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to configure and operate a macOS iMessage/SMS auto-responder for selected contacts, with AI-generated replies, rate limits, time windows, keyword triggers, and status/history management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read private message history and send conversation context to an AI provider. <br>
Mitigation: Use it only for non-sensitive conversations, restrict the watch list to specific contacts, and be transparent with contacts when appropriate. <br>
Risk: The skill can send iMessage/SMS replies automatically on the user's behalf. <br>
Mitigation: Configure nonzero delays, daily reply caps, time windows, and narrow keyword triggers, and review response history regularly. <br>
Risk: Telegram and natural-language management expose an unsafe command path. <br>
Mitigation: Avoid untrusted Telegram or natural-language management input until command construction is fixed, and limit management access to trusted users. <br>
Risk: Plaintext logs and reused API keys can increase exposure if the host account or files are accessed. <br>
Mitigation: Use a dedicated API key, protect logs and configuration files, rotate credentials if exposed, and avoid using the skill for sensitive conversations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/koba42corp/skills/autoresponder) <br>
- [imsg CLI](https://imsg.to) <br>
- [OpenAI](https://openai.com) <br>
- [OpenAI API keys](https://platform.openai.com/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command snippets and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include auto-responder status, contact management guidance, configuration changes, test-response previews, and reminders to restart the watcher after relevant changes.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
