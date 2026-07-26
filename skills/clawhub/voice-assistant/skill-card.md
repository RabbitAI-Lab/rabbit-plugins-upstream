## Description: <br>
Real-time voice assistant for OpenClaw that streams microphone audio through configurable STT providers, sends transcripts to an OpenClaw agent, and speaks responses with configurable TTS providers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[charantejmandali18](https://clawhub.ai/user/charantejmandali18) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to run a local browser-based voice interface that captures speech, sends transcripts to an OpenClaw gateway, and plays synthesized spoken responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive live audio, transcripts, and chat content through external STT and TTS providers and an OpenClaw gateway. <br>
Mitigation: Use only approved provider accounts and gateways, avoid sensitive speech unless those services are acceptable for the use case, and add a clear privacy notice before broad use. <br>
Risk: The local server exposes a voice WebSocket and health endpoint on the configured host with weak local access controls. <br>
Mitigation: Run the server only on a trusted machine and network, restrict binding or network exposure, and add WebSocket origin and authentication controls before wider deployment. <br>
Risk: The browser transcript renderer inserts transcript text into HTML. <br>
Mitigation: Render transcript content as text rather than HTML before using the skill with untrusted assistant output or user speech. <br>
Risk: The artifact references copying a .env.example file, but the release artifact does not include one. <br>
Mitigation: Provide a complete .env.example or equivalent setup documentation covering gateway, STT, TTS, and API key variables. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/charantejmandali18/skills/voice-assistant) <br>
- [Publisher profile](https://clawhub.ai/user/charantejmandali18) <br>
- [Local voice UI](http://localhost:7860) <br>
- [OpenClaw gateway endpoint](http://localhost:4141/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and environment variable configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides setup of a local FastAPI and WebSocket voice server that streams audio, transcripts, and spoken responses.] <br>

## Skill Version(s): <br>
0.1.0 (source: release metadata, _meta.json, and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
