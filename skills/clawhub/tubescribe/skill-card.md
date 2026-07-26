## Description: <br>
TubeScribe summarizes and transcribes YouTube videos into speaker-aware documents with key quotes, linked timestamps, viewer-comment analysis, and optional local audio summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[matusvojtek](https://clawhub.ai/user/matusvojtek) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees, external users, and developers use TubeScribe to turn YouTube videos with captions into local documents and optional audio summaries for review, note-taking, and reuse. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A YouTube URL can start background processing that fetches public YouTube data, writes local files, and invokes local tools. <br>
Mitigation: Review the skill before deployment and consider requiring explicit user confirmation before processing each URL. <br>
Risk: Transcript and comment text may pass through the user's agent model environment during summarization. <br>
Mitigation: Avoid private or sensitive videos and process only content appropriate for the configured agent environment. <br>
Risk: The optional setup flow can download local tools or models. <br>
Mitigation: Review setup.py before accepting optional downloads and install only the dependencies needed for the intended deployment. <br>


## Reference(s): <br>
- [TubeScribe ClawHub skill page](https://clawhub.ai/matusvojtek/skills/tubescribe) <br>
- [Kokoro TTS reference](https://github.com/hexgrad/kokoro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown documents, DOCX or HTML exports, and MP3 or WAV audio files with inline shell commands for processing.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a YouTube URL and writes outputs to the configured local TubeScribe folder.] <br>

## Skill Version(s): <br>
1.1.8 (source: server release metadata and CHANGELOG, released 2026-02-10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
