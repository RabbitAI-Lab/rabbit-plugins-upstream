## Description: <br>
AudioPod helps agents use AudioPod AI's API for music generation, stem separation, text-to-speech, noise reduction, transcription, speaker separation, media extraction, wallet checks, and related audio-processing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rakesh1002](https://clawhub.ai/user/rakesh1002) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use AudioPod to generate or process audio through a third-party API, including music generation, stem separation, text-to-speech, speech transcription, denoising, diarization, and wallet or usage checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents to use an AudioPod API key for paid jobs, wallet checks, usage metadata, and provider-side job or voice management. <br>
Mitigation: Use a dedicated key, protect it as a secret, rotate it when needed, and check wallet balance or estimated cost before running expensive jobs. <br>
Risk: Audio and voice samples may be uploaded to a third-party service for processing, transcription, diarization, or voice cloning. <br>
Mitigation: Upload only media and voice samples the user has permission to process, and avoid sensitive recordings unless AudioPod's handling terms fit the use case. <br>
Risk: Voice cloning features can create consent and impersonation concerns. <br>
Mitigation: Create or use cloned voices only with clear permission from the speaker and for allowed purposes. <br>
Risk: The skill recommends installing third-party SDK packages before making API calls. <br>
Mitigation: Verify the SDK package source before installation, or use the documented raw HTTP requests when package provenance is uncertain. <br>


## Reference(s): <br>
- [AudioPod ClawHub Skill](https://clawhub.ai/rakesh1002/skills/audiopod) <br>
- [Stem Separation Reference](references/stems.md) <br>
- [Text to Speech Reference](references/tts.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python, JavaScript, cURL, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AUDIOPOD_API_KEY or an explicit API key; API calls may create provider-side jobs, upload media, and use wallet credits.] <br>

## Skill Version(s): <br>
1.2.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
