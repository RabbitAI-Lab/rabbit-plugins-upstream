## Description: <br>
A Discord voice-channel AI conversation skill that lets an agent join and leave voice channels and use local speech recognition and speech synthesis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to add a Discord voice assistant to personal or small-team voice channels, with local Whisper speech recognition and Kokoro text-to-speech for offline voice interaction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Voice-channel audio may be recorded and transcribed. <br>
Mitigation: Use the skill only in Discord channels where participants know audio may be recorded and transcribed. <br>
Risk: Open access in shared Discord servers can allow unintended users to trigger the assistant. <br>
Mitigation: Configure allowedUsers for shared servers instead of leaving access open. <br>
Risk: A Discord bot token or voice transcripts may be exposed through environment handling, logs, or screenshots. <br>
Mitigation: Keep DISCORD_TOKEN in a private environment variable or secret manager, and avoid sharing logs or screenshots that expose credentials or transcripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/discord-voice-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Discord voice commands and local setup commands when the host agent has tool-use and exec capability.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
