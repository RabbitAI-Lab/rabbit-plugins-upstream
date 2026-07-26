## Description: <br>
Telegram Bot API operations for forum management, including creating, editing, archiving, and configuring Telegram forum topics with OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brennerspear](https://clawhub.ai/user/brennerspear) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage Telegram forum topics through the Telegram Bot API and keep related OpenClaw topic configuration and sessions aligned with those changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can manage Telegram forum topics and modify persistent OpenClaw Telegram configuration. <br>
Mitigation: Use a minimally privileged bot token, verify topic and group identifiers before execution, and review every configuration patch before applying it. <br>
Risk: New topic configuration can leave all skills available by default. <br>
Mitigation: Use an explicit skills allowlist for each topic when the topic does not require full agent capability. <br>
Risk: Bot tokens and Telegram identifiers may be exposed through command history, logs, or chat transcripts. <br>
Mitigation: Avoid pasting secrets into shared channels, redact tokens from logs, and rotate any token that may have been exposed. <br>


## Reference(s): <br>
- [Forum Topic Emoji IDs](references/emoji-ids.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/brennerspear/skills/telegram-ops) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline bash commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Telegram Bot API command examples, topic icon references, and OpenClaw configuration patch guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
