## Description: <br>
Sends text-to-speech voice messages to specified Telegram groups and topics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sanwecn](https://clawhub.ai/user/sanwecn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to send generated Chinese voice messages into Telegram groups or specific Telegram topics while keeping topic conversations organized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup documentation asks for Telegram administrator powers beyond basic voice-message delivery. <br>
Mitigation: Grant the bot only the minimum send-message and send-media permissions needed for the intended groups or topics unless a separate operational need requires more. <br>
Risk: Unsafe command execution paths can be exposed when message text or options come from untrusted users. <br>
Mitigation: Use this skill only with trusted inputs or shared access controls until command construction is rewritten to use safe argument passing. <br>
Risk: Voice message content, group identifiers, or topic metadata may expose private information. <br>
Mitigation: Do not send secrets, private data, or sensitive group metadata through this skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sanwecn/skills/telegram-voice-group) <br>
- [README](artifact/README.md) <br>
- [Feature documentation](artifact/FEATURES.md) <br>
- [Dependency guide](artifact/DEPENDENCIES.md) <br>
- [Telegram topics guide](artifact/TELEGRAM_TOPICS.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands, code] <br>
**Output Format:** [Markdown guidance with JavaScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates temporary audio files locally and sends Telegram voice messages when executed by an appropriately configured agent.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
