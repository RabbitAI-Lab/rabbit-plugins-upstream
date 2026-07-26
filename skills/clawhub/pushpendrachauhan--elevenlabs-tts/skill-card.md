## Description: <br>
Generates an ElevenLabs voiceover MP3 for a short-form video job and rewrites input.json subtitles with measured word-level timings from the timestamped response. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pushpendrachauhan](https://clawhub.ai/user/pushpendrachauhan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video pipeline agents use this skill to synthesize voiceover audio for a job folder and replace predicted subtitle timings with measured timings from ElevenLabs alignment data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the job's TTS script to ElevenLabs using the configured API key. <br>
Mitigation: Use only with scripts that are approved for the ElevenLabs service and provide the API key through the ELEVENLABS_API_KEY environment variable. <br>
Risk: The skill intentionally rewrites input.json subtitles, replacing predicted timings. <br>
Mitigation: Keep an original copy of input.json when the pre-run subtitle timings must be preserved. <br>
Risk: Voice selection depends on ELEVENLABS_VOICE_ID or a per-channel voices.json configuration. <br>
Mitigation: Confirm the configured voice mapping before running the voiceover stage. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pushpendrachauhan/skills/elevenlabs-tts) <br>
- [Publisher profile](https://clawhub.ai/user/pushpendrachauhan) <br>
- [ElevenLabs timestamped text-to-speech endpoint](https://api.elevenlabs.io/v1/text-to-speech/$VOICE_ID/with-timestamps) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with bash, jq, and Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs ElevenLabs API calls, saves audio/voiceover.mp3 and audio/voiceover_timings.json, and mutates input.json subtitles with measured timings.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
