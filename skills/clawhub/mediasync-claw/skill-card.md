## Description: <br>
MediaSync-Claw lets an OpenClaw agent list local MP4 videos and return playback links through a Flask media server with FRP/WebRTC remote access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yu-libin](https://clawhub.ai/user/yu-libin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users use this skill to expose a local MP4 folder to an agent action that lists media and returns playable links for chat-driven playback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish a local media server without authentication and expose local files over the public internet. <br>
Mitigation: Use only a dedicated videos folder containing non-sensitive files, and do not run the skill with access to private data. <br>
Risk: The skill uses a third-party FRP relay for public access to the local service. <br>
Mitigation: Install only when public relay access is intentional, and prefer a version with explicit tunnel opt-in, authentication, strict origin checks, and path allowlisting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yu-libin/skills/mediasync-claw) <br>
- [Publisher profile](https://clawhub.ai/user/yu-libin) <br>
- [FRP v0.65.0 release](https://github.com/fatedier/frp/releases/tag/v0.65.0) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls] <br>
**Output Format:** [JSON API response containing Markdown-formatted text and playback links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Lists MP4 files from the skill's local videos directory and returns public playback links.] <br>

## Skill Version(s): <br>
0.1.7 (source: server release metadata; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
