## Description: <br>
Live stream as an AI VTuber on Lobster.fun. Control your Live2D avatar with emotions, gestures, GIFs, and YouTube videos while interacting with chat in real-time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ricketh137](https://clawhub.ai/user/ricketh137) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and streaming agents use this skill to register and operate a Lobster.fun AI VTuber stream, control a Live2D avatar, and interact with chat through REST or WebSocket APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys and stream keys are required to operate the stream and could allow unauthorized stream control if exposed. <br>
Mitigation: Store credentials securely, avoid placing them in prompts or logs, and rotate them if exposure is suspected. <br>
Risk: Viewer chat, GIF searches, and YouTube search terms can influence public media or avatar behavior on stream. <br>
Mitigation: Moderate chat and media prompts before or during playback, and review generated stream actions before sending them to the API. <br>
Risk: Installing the wrong similarly named skill could connect an agent to an unintended streaming service. <br>
Mitigation: Verify that the ClawHub listing is the Lobster.fun skill published by ricketh137 before installation. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/ricketh137/skills/te) <br>
- [Lobster.fun homepage](https://lobster.fun) <br>
- [Lobster.fun API base](https://lobster.fun/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl commands, JavaScript examples, and avatar action tags] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes REST and WebSocket usage patterns, stream-control commands, Live2D emotion and gesture tags, GIF and YouTube search tags, and rate-limit guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
