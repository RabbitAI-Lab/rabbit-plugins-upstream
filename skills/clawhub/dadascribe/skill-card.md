## Description:

Transcribe audio and video with the DaDaScribe AI service from YouTube URLs, direct links, or local files, with support for 100+ languages, speaker diarization, translation to up to 5 languages, and .txt plus .srt outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fablau](https://clawhub.ai/user/fablau)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to submit audio or video sources to DaDaScribe for transcription, subtitle generation, translation, and speaker-labeled transcript workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio, video, source links, speaker names, and language options are sent to DaDaScribe for processing.

Mitigation: Use the skill only when DaDaScribe's privacy and retention terms are acceptable for the recording, and avoid confidential recordings unless those terms meet the user's requirements.

Risk: API keys could be exposed if hard-coded or logged.

Mitigation: Keep the DaDaScribe API key in an environment variable such as DADASCRIBE_API_KEY and never store or log the full key.

Risk: Optional package installation from GitHub can introduce supply-chain risk.

Mitigation: Prefer the documented HTTP API or a pinned and verified package installation before using the optional GitHub pip command.

## Reference(s):

- [DaDaScribe skill page](https://clawhub.ai/fablau/skills/dadascribe)
- [DaDaScribe API documentation](https://api.dadascribe.com/docs)
- [DaDaScribe OpenAPI specification](https://api.dadascribe.com/openapi.json)
- [DaDaScribe API key page](https://www.dadascribe.com/account/api.php)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with API examples, JSON payloads, Python code, shell commands, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce transcript and subtitle files through DaDaScribe API calls, including .txt and .srt outputs.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
