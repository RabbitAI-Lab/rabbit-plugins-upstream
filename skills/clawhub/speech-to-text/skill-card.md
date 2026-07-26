## Description: <br>
Transcribe audio to text with Whisper models via inference.sh CLI, including transcription, translation, multi-language support, and timestamps for meetings, subtitles, podcast transcripts, and voice notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and other ClawHub users use this skill to run inference.sh Whisper transcription workflows for meetings, podcasts, subtitles, voice notes, interviews, accessibility, and translation to English. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio may be sent to an external transcription service. <br>
Mitigation: Do not submit confidential, regulated, or private recordings unless the service's data handling terms are acceptable for the use case. <br>
Risk: The quick-start install path runs a remote CLI installer. <br>
Mitigation: Prefer the manual or checksum-verified CLI installation path when possible. <br>


## Reference(s): <br>
- [Speech To Text on ClawHub](https://clawhub.ai/okaris/skills/speech-to-text) <br>
- [inference.sh](https://inference.sh) <br>
- [Running Apps](https://inference.sh/docs/apps/running) <br>
- [Audio Transcription Example](https://inference.sh/docs/examples/audio-transcription) <br>
- [Apps Overview](https://inference.sh/docs/apps/overview) <br>
- [CLI Checksums](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON input/output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The transcription service returns JSON with text, optional timestamped segments, and detected language.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
