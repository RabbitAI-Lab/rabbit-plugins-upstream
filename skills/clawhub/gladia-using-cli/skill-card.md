## Description: <br>
Terminal transcription of audio files and URLs with the Gladia CLI (gladia speech-to-text). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gladiaio](https://clawhub.ai/user/gladiaio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run Gladia CLI transcription for local audio files, http(s) URLs, or YouTube URLs, then answer follow-up questions grounded in the captured transcript. It is intended for shell-based, one-off transcription workflows rather than application integration or live audio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Transcribing local files sends audio content to Gladia's service. <br>
Mitigation: Confirm the audio can be shared with Gladia before transcription and avoid processing sensitive files without user approval. <br>
Risk: Using gladia auth set stores the API key locally. <br>
Mitigation: Prefer GLADIA_API_KEY or a per-command key when persistent local credentials are not desired. <br>
Risk: Follow-up answers can become misleading if they rely on details absent from the transcript output. <br>
Mitigation: Ground answers only in captured output and rerun transcription with JSON or diarization flags when timestamps or speakers are required. <br>


## Reference(s): <br>
- [CLI vs SDK Routing Guide](artifact/references/cli-vs-sdk.md) <br>
- [Gladia CLI repository](https://github.com/gladiaio/gladia-cli/) <br>
- [Pre-recorded quickstart](https://docs.gladia.io/chapters/pre-recorded-stt/quickstart) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides command selection for Gladia CLI transcription; command output may be text, JSON, SRT, or VTT depending on flags.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
