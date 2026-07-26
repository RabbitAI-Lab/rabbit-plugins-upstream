## Description: <br>
Transcribe audio via OpenAI Audio Transcriptions API (Whisper). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to transcribe local audio files through OpenAI's audio transcription API and save the transcript as text or JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected audio files are sent to OpenAI for transcription. <br>
Mitigation: Install and use only when sending the chosen audio to OpenAI is acceptable, and avoid confidential, regulated, or unauthorized third-party recordings. <br>
Risk: Transcript output is written locally and may overwrite an important file if the output path is chosen poorly. <br>
Mitigation: Choose output paths deliberately and review the destination before running the transcription command. <br>


## Reference(s): <br>
- [OpenAI Speech to Text Guide](https://platform.openai.com/docs/guides/speech-to-text) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Text or JSON transcript file path emitted by a shell command] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and OPENAI_API_KEY; writes the transcript to the requested output path or a default sibling .txt/.json file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
