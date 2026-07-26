## Description: <br>
Real-time WhatsApp voice message processing. Transcribe voice notes to text via Whisper, detect intent, execute handlers, and send responses. Use when building conversational voice interfaces for WhatsApp. Supports English and Hindi, customizable intents (weather, status, commands), automatic language detection, and streaming responses via TTS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[syedateebulislam](https://clawhub.ai/user/syedateebulislam) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and automation teams use this skill to build WhatsApp voice assistants that transcribe incoming voice notes, detect user intent, run configured handlers, and return text or voice responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The listener automatically processes private WhatsApp voice files and logs full transcripts. <br>
Mitigation: Run the listener only for trusted WhatsApp senders, remove or gate raw transcript logging, and protect or rotate logs. <br>
Risk: The transcription path uses a shell-string execSync call that is not safely scoped. <br>
Mitigation: Replace shell-string execution with argument-safe process spawning before enabling the skill in sensitive environments. <br>
Risk: Custom handlers can change devices, accounts, files, or public outputs if extended without controls. <br>
Mitigation: Add explicit confirmations and authorization checks before enabling handlers that perform side effects. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/syedateebulislam/skills/whatsapp-voice-chat-integration-open-source) <br>
- [API Reference](references/API.md) <br>
- [Setup Guide](references/SETUP.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown documentation with JavaScript, Python, shell, and JSON examples; runtime functions return JSON-compatible result objects.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes audio buffers or watched voice-message files and produces transcript, intent, language, response, sender, timestamp, and error fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
