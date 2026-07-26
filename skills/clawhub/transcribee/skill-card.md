## Description: <br>
Transcribee transcribes YouTube, Instagram, TikTok, and local audio or video files with speaker diarization and organizes the resulting transcripts into a local knowledge library. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itsfabioroma](https://clawhub.ai/user/itsfabioroma) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to transcribe online videos, podcasts, interviews, or local media into speaker-labeled transcripts for later LLM analysis and personal knowledge management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media, transcripts, and transcript-derived classification data are sent to cloud AI services. <br>
Mitigation: Use the skill only with media that is acceptable to process through ElevenLabs and Anthropic, and avoid sensitive local recordings unless that processing is approved. <br>
Risk: Transcript files and metadata are stored in ~/Documents/transcripts. <br>
Mitigation: Review local storage and retention expectations before use, and remove or relocate generated transcripts when they contain sensitive content. <br>
Risk: AI-selected category names influence local output paths. <br>
Mitigation: Validate generated category names as a single safe path segment, reject path traversal or nested paths, and confirm writes remain contained under ~/Documents/transcripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itsfabioroma/skills/transcribee) <br>
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) <br>
- [FFmpeg](https://ffmpeg.org/) <br>
- [ElevenLabs](https://elevenlabs.io/) <br>
- [Anthropic](https://anthropic.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Plain text transcripts and JSON metadata written to local files, with CLI progress output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes under ~/Documents/transcripts/{category}/{title-date}/; optional --raw adds word-level transcript JSON.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata; artifact package.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
