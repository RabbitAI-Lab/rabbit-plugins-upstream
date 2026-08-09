## Description: <br>
Provides text-to-speech, sound effects, music generation, voice management, and quota checks through the ElevenLabs API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to generate speech, dialogue, sound effects, and music; manage ElevenLabs voices; and check quota or usage from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Voice cloning can upload local voice samples and may create clones without sufficient consent or privacy review. <br>
Mitigation: Only clone voices owned by the user or covered by explicit permission, and review the voice cloning workflow before installation or use. <br>
Risk: Text prompts and audio samples are sent to ElevenLabs API endpoints and may include confidential or sensitive content. <br>
Mitigation: Avoid sending confidential text or sensitive audio unless the data handling terms are acceptable for the use case. <br>
Risk: Broad sample directories can accidentally include unrelated local audio files for voice cloning. <br>
Mitigation: Keep voice sample directories narrow and dedicated, using the documented voiceclone-samples directory or a carefully scoped custom sample directory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gasgangrene/skills/elevenlabs) <br>
- [Publisher profile](https://clawhub.ai/user/gasgangrene) <br>
- [Setup instructions](artifact/SETUP.md) <br>
- [ElevenLabs](https://elevenlabs.io) <br>
- [ElevenLabs Music API reference](https://elevenlabs.io/docs/api-reference/music/compose) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown guidance with shell commands; scripts can produce audio files and JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ELEVENLABS_API_KEY, Python requests, and optional ffmpeg or afplay depending on workflow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.3.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
