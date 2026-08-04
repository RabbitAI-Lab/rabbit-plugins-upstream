## Description: <br>
Hands-free voice assistant for OpenClaw on an ESP32-S3-BOX-3 - on-device wake word, switchable xAI Grok / ElevenLabs / FishAudio STT+TTS, no Home Assistant required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[darrenjrobinson](https://clawhub.ai/user/darrenjrobinson) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to configure an ESP32-S3-BOX-3 as a hands-free voice interface for OpenClaw, with Docker-based bridging, wake word capture, STT, and streamed TTS. It is intended for users who can manage LAN device configuration, API keys, and provider-specific speech services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Voice input and derived text may be sent to the selected STT/TTS provider and the configured OpenClaw endpoint. <br>
Mitigation: Confirm the selected providers and OpenClaw endpoint are acceptable for the intended data before installation. <br>
Risk: The configuration uses API keys and endpoint credentials in .env. <br>
Mitigation: Protect .env, avoid committing secrets, and rotate keys if they are exposed. <br>
Risk: The Docker bridge and device audio endpoint are intended for LAN use. <br>
Mitigation: Run the bridge only on a trusted LAN and avoid exposing the service publicly. <br>
Risk: Installation relies on running Docker Compose from the referenced GitHub repository. <br>
Mitigation: Review or pin the repository before running the compose workflow. <br>


## Reference(s): <br>
- [GitHub: darrenjrobinson/voice-esp32-openclaw](https://github.com/darrenjrobinson/voice-esp32-openclaw) <br>
- [ESPHome wake-word voice assistants](https://github.com/esphome/wake-word-voice-assistants) <br>
- [Going Direct - ESP32 Voice for OpenClaw](https://blog.darrenjrobinson.com/going-direct-esp32-voice-for-openclaw/) <br>
- [Hardware Voice Assistant for OpenClaw](https://blog.darrenjrobinson.com/hardware-voice-assistant-for-openclaw/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with setup steps, inline shell commands, and environment-variable configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Docker, git, an OpenClaw endpoint, ESP32 host details, and provider API keys matching the selected STT/TTS services.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
