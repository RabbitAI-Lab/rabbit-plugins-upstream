## Description: <br>
Generate and send video messages with a lip-syncing VRM avatar when a user asks for a video message, avatar video, video reply, or TTS delivered as video instead of audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thewulf7](https://clawhub.ai/user/thewulf7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and OpenClaw operators use this skill to generate lip-synced avatar video messages from text or audio and send them as video notes through the configured messaging tool. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send generated avatar videos through the configured messaging tool. <br>
Mitigation: Require explicit user confirmation before sending video messages. <br>
Risk: The documented cleanup pattern may delete more temporary video files than the current run created. <br>
Mitigation: Delete only the exact video file generated for the current run. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thewulf7/skills/avatar-video-messages) <br>
- [Publisher profile](https://clawhub.ai/user/thewulf7) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent to create an MP4 avatar video, send it as a video note, and return NO_REPLY after sending.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
