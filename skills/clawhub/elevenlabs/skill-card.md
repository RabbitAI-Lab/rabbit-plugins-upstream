## Description: <br>
Text-to-speech, sound effects, music generation, voice management, and quota checks via the ElevenLabs API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creators use this skill to generate speech, dialogue, sound effects, and music, manage ElevenLabs voices, and inspect quota or usage from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, dialogue text, and generated audio requests are sent to ElevenLabs using the user's API key. <br>
Mitigation: Review content before generation and avoid sending confidential or regulated text unless the ElevenLabs account and terms are approved for that use. <br>
Risk: Voice-cloning samples may contain sensitive biometric or personal data. <br>
Mitigation: Clone voices only with clear authorization from the speaker and store samples in the intended local sample directory. <br>
Risk: API keys and quota usage are sensitive operational data. <br>
Mitigation: Keep ELEVENLABS_API_KEY in environment or local state files outside shared commits, and use the quota tool to monitor usage. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/odrobnik/skills/elevenlabs) <br>
- [ElevenLabs](https://elevenlabs.io) <br>
- [ElevenLabs Music API Documentation](https://elevenlabs.io/docs/api-reference/music/compose) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text, Files] <br>
**Output Format:** [Markdown guidance with shell commands; generated artifacts may be audio files, text summaries, or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an ElevenLabs API key and may consume paid API quota when commands are executed.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
