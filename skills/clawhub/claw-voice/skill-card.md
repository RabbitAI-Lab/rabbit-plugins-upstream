## Description: <br>
ClawVoice connects an agent to a live voice session so it can send, receive, listen for, and bridge messages through a WebSocket client. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[niczy](https://clawhub.ai/user/niczy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to connect an OpenClaw agent to a local or trusted voice session, exchange transcribed user messages, and optionally bridge those messages into agent responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connecting to an untrusted WebSocket endpoint could expose voice-session content or allow unexpected messages into the agent session. <br>
Mitigation: Use only a trusted local voice server or trusted WebSocket endpoint. <br>
Risk: Bridge mode can send sensitive speech-derived text into an agent session and may run indefinitely by default. <br>
Mitigation: Avoid highly sensitive speech in bridge mode, prefer running sessions with --timeout, and stop the bridge when the voice session is over. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/niczy/skills/claw-voice) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON message examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled client can print single JSON responses, stream JSON lines, or bridge messages until a timeout or manual stop.] <br>

## Skill Version(s): <br>
0.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
