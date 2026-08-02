## Description: <br>
Agentvibes Voice Skill helps agents run text-to-speech workflows with Piper TTS, macOS Say, Windows SAPI, and Soprano, including voice selection, previews, speech effects, speed control, background music, and language-learning playback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, automation builders, content creators, and language learners use this skill to let agents configure and run text-to-speech workflows for voice announcements, narration, previews, effects, and bilingual playback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run local audio commands, write generated audio/cache files, and download voice models on first use. <br>
Mitigation: Review proposed commands before execution, use a trusted workspace, and verify pip packages and downloaded voice models come from trusted sources. <br>
Risk: Selected providers may require API keys or similar credentials. <br>
Mitigation: Provide credentials only through environment variables and avoid embedding secrets in prompts, files, or logs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/agentvibes-voice-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline commands and structured JSON-style results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run local audio commands, write generated audio or cache files, and download voice models on first use.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
