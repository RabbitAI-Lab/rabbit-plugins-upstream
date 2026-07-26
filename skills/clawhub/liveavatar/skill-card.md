## Description: <br>
Talk face-to-face with your OpenClaw agent using a real-time video avatar powered by LiveAvatar. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ennno](https://clawhub.ai/user/ennno) <br>

### License/Terms of Use: <br>


## Use Case: <br>
OpenClaw users use this skill to start a browser-based LiveAvatar interface for voice and video conversations with their local OpenClaw agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spoken input may include sensitive conversation data that is transcribed by LiveAvatar and then sent to the OpenClaw agent flow. <br>
Mitigation: Use the skill only when that voice data flow is acceptable, and avoid speaking secrets or confidential information during sessions. <br>
Risk: The skill launches the openclaw-liveavatar npm package and depends on a LiveAvatar API key. <br>
Mitigation: Install and run it only when you trust LiveAvatar and the npm package, keep the API key out of prompts and logs, and rotate the key if it is exposed. <br>


## Reference(s): <br>
- [LiveAvatar](https://liveavatar.com) <br>
- [LiveAvatar app](https://app.liveavatar.com) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [LiveAvatar skill on ClawHub](https://clawhub.ai/ennno/skills/liveavatar) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LiveAvatar API key, Node.js/npm, a modern browser with microphone access, and a running OpenClaw Gateway.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
