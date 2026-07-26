## Description: <br>
Hands-free voice assistant for OpenClaw on an ESP32-S3-BOX-3 with on-device wake word, switchable xAI Grok or ElevenLabs STT/TTS, and no Home Assistant requirement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[darrenjrobinson](https://clawhub.ai/user/darrenjrobinson) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure an ESP32-S3-BOX-3 as a hands-free voice interface for an OpenClaw chat endpoint, using Docker, LAN device access, and selected STT/TTS providers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spoken requests may be routed through configured STT/TTS providers and the OpenClaw endpoint. <br>
Mitigation: Use only providers and endpoints whose privacy and retention policies are acceptable for the deployment. <br>
Risk: API keys are required for selected providers and may be stored in the local .env file. <br>
Mitigation: Keep .env local, avoid committing or sharing it, and rotate keys if exposure is suspected. <br>
Risk: The bridge relies on LAN access to the ESP32 device and serves reply audio over a local HTTP port. <br>
Mitigation: Run the bridge only on a trusted LAN and configure BRIDGE_ADVERTISE_HOST and exposed ports deliberately. <br>
Risk: Local usage metrics may be retained in out/metrics.jsonl. <br>
Mitigation: Review or purge the metrics file according to the user's local retention requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/darrenjrobinson/skills/esp32-voice-assistant) <br>
- [Project repository](https://github.com/darrenjrobinson/voice-esp32-openclaw) <br>
- [Going Direct - ESP32 Voice for OpenClaw](https://blog.darrenjrobinson.com/going-direct-esp32-voice-for-openclaw/) <br>
- [Hardware Voice Assistant for OpenClaw](https://blog.darrenjrobinson.com/hardware-voice-assistant-for-openclaw/) <br>
- [ESPHome wake-word voice assistants](https://github.com/esphome/wake-word-voice-assistants) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with setup steps, configuration tables, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes required environment variables, Docker commands, troubleshooting guidance, and provider selection notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
