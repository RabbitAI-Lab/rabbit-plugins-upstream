## Description: <br>
Transcribes video or audio into local Whisper plain-text transcripts and SRT subtitle files, with optional guidance for transcript-informed video editing when a Sparki API key is intentionally configured. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[Symbolk](https://clawhub.ai/user/Symbolk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to transcribe local media files into text and subtitles for review, captioning, and downstream editing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented AI Edit workflow can upload private media and prompts to a third-party API. <br>
Mitigation: Use the skill for local Whisper transcription unless cloud editing is intentional, and confirm trust in the Sparki service before uploading private media. <br>
Risk: The documented SPARKI_API_KEY check can print the key value. <br>
Mitigation: Avoid commands that echo the full key; check only whether the variable is configured before using cloud editing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/Symbolk/video-to-text) <br>
- [Sparki homepage](https://sparki.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands; transcript output is plain text and SRT files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs on local media with ffmpeg and Whisper; writes .txt and .srt files next to the input file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
