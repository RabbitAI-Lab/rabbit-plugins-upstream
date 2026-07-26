## Description: <br>
This skill helps agents convert text to speech, transcribe voice messages, list ElevenLabs voices, and support multilingual voice workflows using ElevenLabs AI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amreahmed](https://clawhub.ai/user/amreahmed) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agent users use this skill to generate spoken replies from text, transcribe incoming voice messages, and integrate ElevenLabs voice workflows into assistant or messaging experiences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text and audio supplied to the skill are sent to ElevenLabs for cloud processing. <br>
Mitigation: Use the skill only with content approved for external processing, and avoid confidential or regulated recordings unless policy permits it. <br>
Risk: The skill requires an ElevenLabs API key. <br>
Mitigation: Use a dedicated API key stored in environment variables or a protected .env file, and avoid sharing it in prompts, logs, or repository files. <br>
Risk: Generated speech is written to caller-selected output paths. <br>
Mitigation: Choose output filenames carefully and avoid paths that could overwrite important files. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/amreahmed/skills/elevenlabs-voice) <br>
- [ElevenLabs API Base](https://api.elevenlabs.io/v1) <br>
- [ElevenLabs Pricing](https://elevenlabs.io/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance, audio files] <br>
**Output Format:** [Markdown guidance with Python and shell examples; scripts return JSON-like status objects and write MP3 audio files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ELEVENLABS_API_KEY and sends selected text or audio to ElevenLabs for cloud processing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
