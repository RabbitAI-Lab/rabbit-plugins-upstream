## Description: <br>
Transform any text into emotionally expressive audio with ambient soundscapes using ElevenLabs v3 audio tags and Sound Effects API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ashutosh887](https://clawhub.ai/user/ashutosh887) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, content creators, writers, and developers use MoodCast to turn supplied text into expressive narrated audio, optional ambient soundscapes, and previewable enhanced text with mood and voice controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Provided text, voice settings, and ambient prompts are sent to ElevenLabs using the user's API key. <br>
Mitigation: Avoid using the skill on secrets, regulated data, or confidential material unless organizational policy permits sending that data to ElevenLabs. <br>
Risk: The script may install the ElevenLabs Python dependency automatically if it is missing. <br>
Mitigation: Pre-install and pin the ElevenLabs dependency in the target environment before running the skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ashutosh887/skills/moodcast) <br>
- [Publisher Profile](https://clawhub.ai/user/ashutosh887) <br>
- [Project Homepage](https://github.com/ashutosh887/moodcast) <br>
- [ElevenLabs](https://elevenlabs.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, files, shell commands, configuration, guidance] <br>
**Output Format:** [Enhanced text, command-line status text, and generated MP3 audio files or local playback.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ELEVENLABS_API_KEY; optional voice, mood, model, output format, ambient prompt, ambient duration, and output path settings.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
