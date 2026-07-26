## Description: <br>
Generate short sound effects via ElevenLabs SFX (text-to-sound) for clips like applause, canned laughter, whooshes, ambience, or short stingers, with optional WhatsApp-friendly OGG/Opus conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[javicasper](https://clawhub.ai/user/javicasper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to generate short sound-effect audio files from text prompts through ElevenLabs, then attach or convert the resulting media for downstream use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sound-effect prompts are sent to ElevenLabs and may contain sensitive or confidential details. <br>
Mitigation: Avoid including secrets, private data, or confidential context in prompts sent to the external service. <br>
Risk: Using the ElevenLabs API can affect account quota or billing. <br>
Mitigation: Use an appropriate API key and monitor quota or billing before generating repeated or long clips. <br>
Risk: The script writes generated audio directly to the output path provided by the caller. <br>
Mitigation: Choose output paths deliberately and review the destination before running the command. <br>


## Reference(s): <br>
- [Sound FX on ClawHub](https://clawhub.ai/javicasper/skills/sound-fx) <br>
- [ElevenLabs sound generation API endpoint](https://api.elevenlabs.io/v1/sound-generation) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration guidance] <br>
**Output Format:** [MP3 audio file path with a MEDIA line, plus optional OGG/Opus conversion guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an ElevenLabs API key; prompts are sent to ElevenLabs and the script writes to the caller-provided output path.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
