## Description: <br>
Transcribes user-selected audio files or media URLs with Speech is Cheap automatic speech-to-text, including optional diarization, word timestamps, audio labels, language selection, and subtitle formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ilyakam](https://clawhub.ai/user/ilyakam) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to submit audio URLs or local media files to Speech is Cheap for transcription and to check transcription job status. It is suited to automated speech-to-text workflows that need JSON, SRT, VTT, or WebVTT output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected audio files or media URLs are sent to a third-party transcription API. <br>
Mitigation: Use the skill only for recordings you are permitted to process, and avoid confidential, regulated, or third-party recordings unless Speech is Cheap privacy and retention terms are acceptable. <br>
Risk: A missing or misconfigured API key prevents transcription requests from running. <br>
Mitigation: Configure SIC_API_KEY before use and restrict the credential to environments authorized to send data to Speech is Cheap. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ilyakam/skills/asr) <br>
- [Speech is Cheap](https://speechischeap.com) <br>
- [Speech is Cheap API Documentation](https://docs.speechischeap.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; command results are JSON or subtitle text depending on requested output format] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SIC_API_KEY and sends selected audio files or media URLs to the Speech is Cheap API.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata, artifact manifest, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
