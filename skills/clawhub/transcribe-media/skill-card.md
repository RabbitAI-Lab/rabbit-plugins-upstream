## Description:

Fetches transcripts from YouTube videos, public podcast episodes, other public media links, and local audio or video files, preferring existing captions and using AudioFlow ASR only when needed with explicit approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[niuzb](https://clawhub.ai/user/niuzb)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to obtain transcripts from supported public media URLs or local media files, then optionally summarize, answer questions about, or extract information from the transcript.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local files or downloaded media may be uploaded to AudioFlow when remote ASR is needed.

Mitigation: Require explicit per-run approval before remote ASR and only approve uploads for media the user is allowed to send to AudioFlow.

Risk: An AudioFlow token may be stored locally for future use.

Mitigation: Prefer an existing AUDIOFLOW_TOKEN environment variable when available, avoid logging tokens, and use the skill's local credential handling for stored credentials.

Risk: The workflow may download and cache a managed yt-dlp release when no suitable local tool is available.

Mitigation: Ask for separate approval before tool download and use the pinned, SHA-256-verified release described by the skill.

## Reference(s):

- [Transcribe a Xiaoyuzhou Episode](references/xiaoyuzhou.md)
- [Transcribe Media on ClawHub](https://clawhub.ai/niuzb/skills/transcribe-media)
- [yt-dlp Installation](https://github.com/yt-dlp/yt-dlp/wiki/Installation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Plain transcript text or Markdown response; command output may be JSON containing transcript text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [For transcript-only requests, the skill returns the transcript verbatim and avoids adding summaries, edits, or unrelated explanation.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
