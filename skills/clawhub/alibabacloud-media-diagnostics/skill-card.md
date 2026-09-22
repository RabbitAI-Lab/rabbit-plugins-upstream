## Description:

Diagnoses playback and streaming problems in user-provided media files and URLs, including container, codec, HLS/TS integrity, bitrate/frame-rate, audio-video sync, and live latency issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, media engineers, and support teams use this skill to inspect a user-confirmed local media file, playlist, or stream URL and receive read-only diagnostics plus suggested next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may read the specific media file, playlist, or media URL supplied for diagnosis, including HLS segment URLs referenced by a supplied playlist.

Mitigation: Confirm the exact target before analysis and probe only the user-provided file or URL and its referenced HLS segments.

Risk: Suggested ffmpeg or RTMP repair examples could write files or push streams if executed later.

Mitigation: Treat repair commands as manual examples and require explicit confirmation, destination review, and a separate user instruction before running them.

## Reference(s):

- [Media Diagnostics Knowledge Base](references/knowledge-base.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown diagnosis with structured script JSON used for routing and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostic reports; repair commands are suggestions only and require separate user confirmation before execution.]

## Skill Version(s):

0.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
