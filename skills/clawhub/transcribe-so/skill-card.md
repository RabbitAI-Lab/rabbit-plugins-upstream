## Description:

Transcribe audio and video with the transcribe.so CLI. Turns YouTube videos, podcasts (Apple Podcasts, Spotify, SoundCloud, Vimeo, Twitch, Loom), direct media URLs, and local audio or video files into speaker-labelled transcripts with timestamped segments, chapters, sections, cited Q&A, and subtitle files (SRT, VTT, karaoke VTT). Use when the user wants a transcript, show notes, chapters, subtitles, quotes, or answers grounded in a recording. 52 languages and dialects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shsunmoonlee](https://clawhub.ai/user/shsunmoonlee)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agents use this skill to run transcribe.so CLI workflows for converting media URLs or local audio/video files into transcripts, chapters, show notes, cited Q&A, and subtitle files. It is useful when transcription work needs price quoting, upload handling, polling, budget limits, or repeatable batch processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected recordings, media URLs, and user questions are sent to transcribe.so for processing.

Mitigation: Use the skill only for media that may be shared with transcribe.so, avoid sensitive private recordings unless permitted, and review the service privacy policy before use.

Risk: Paid transcription jobs can spend account balance.

Mitigation: Run quote before create, show pricing for non-trivial jobs, and use explicit --max-usd budgets for run workflows.

Risk: API keys can expose account access or spending authority if stored in shared files.

Mitigation: Keep TRANSCRIBE_API_KEY in an environment variable or secret store, and do not hard-code real keys in shared configs.

Risk: Deletion and retry operations can remove data or charge again.

Mitigation: Require explicit user confirmation before commands that need --yes, and explain that delete is irreversible and retry re-charges from scratch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shsunmoonlee/skills/transcribe-so)
- [transcribe.so agent landing page](https://transcribe.so/agent)
- [transcribe.so developer docs](https://transcribe.so/developers/docs)
- [transcribe.so OpenAPI reference](https://transcribe.so/openapi.json)
- [transcribe.so MCP server card](https://transcribe.so/.well-known/mcp/server-card.json)
- [transcribe-so npm package](https://www.npmjs.com/package/transcribe-so)
- [Local upload flow example](examples/upload-flow.md)
- [Batch transcription example](examples/batch-transcribe.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce or retrieve transcripts, chapters, cited Q&A, subtitles, JSON command output, and batch-processing configurations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
