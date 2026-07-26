## Description: <br>
Generate music from text prompts using ElevenLabs Eleven Music API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawdbotborges](https://clawhub.ai/user/clawdbotborges) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to generate songs, soundtracks, jingles, lullabies, and other music from text prompts through ElevenLabs. It supports instrumental generation, AI-generated lyrics and vocals, configurable track length, and custom MP3 output paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts are sent to ElevenLabs and require an ElevenLabs API key. <br>
Mitigation: Use a revocable API key and install the skill only when sending prompts to ElevenLabs is acceptable. <br>
Risk: The script writes generated MP3 output to the configured output path. <br>
Mitigation: Choose output paths carefully and prefer a temporary or dedicated directory when testing. <br>
Risk: The music API is a paid API-backed service. <br>
Mitigation: Confirm the ElevenLabs plan and expected usage costs before generating longer tracks or repeated outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clawdbotborges/skills/elevenlabs-music) <br>
- [ElevenLabs pricing](https://elevenlabs.io/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and a local MP3 file path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ELEVENLABS_API_KEY, uv, and a paid ElevenLabs plan; generated music is written to /tmp/music.mp3 by default or to a user-specified output path.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
