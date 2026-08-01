## Description: <br>
DaDaScribe transcribes audio and video from YouTube URLs, direct links, or local files, supports 100+ languages, speaker diarization and up to five translation targets, and returns text transcripts plus SRT subtitles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fablau](https://clawhub.ai/user/fablau) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to submit media to DaDaScribe for transcription, caption generation, speaker-labeled transcripts, and subtitle translation. It is suited for YouTube videos, podcasts, meetings, interviews, and direct audio or video files when the user has a DaDaScribe API key and permission to process the media. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio, video, source URLs, speaker labels, and requested translation settings are sent to DaDaScribe for processing. <br>
Mitigation: Confirm user consent and data-handling requirements before processing confidential, regulated, or third-party media. <br>
Risk: The skill requires a DaDaScribe API key and may use optional package installation paths. <br>
Mitigation: Load the API key from DADASCRIBE_API_KEY, never log or hard-code it, and prefer the documented HTTP API or review and pin any optional package before installation. <br>
Risk: Generated output links are unauthenticated and expire after one hour. <br>
Mitigation: Download results promptly, share output links only with intended recipients, and avoid relying on expired links for audit or archival needs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fablau/skills/dadascribe) <br>
- [DaDaScribe API Docs](https://api.dadascribe.com/docs) <br>
- [DaDaScribe OpenAPI Specification](https://api.dadascribe.com/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON, Python, and shell examples; API results are plain text transcripts and SRT subtitle files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DADASCRIBE_API_KEY for authenticated requests; supports batched source submissions, polling, and time-limited output downloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill API version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
