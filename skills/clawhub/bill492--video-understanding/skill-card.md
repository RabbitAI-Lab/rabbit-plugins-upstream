## Description:

Watch and analyze video URLs or files using Gemini native agentic video understanding for summaries, timestamped answers, transcripts, and visual reconstruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bill492](https://clawhub.ai/user/bill492)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to analyze authorized video URLs or local video files, producing summaries, focused timestamped answers, transcripts, and visual descriptions while preserving uncertainty and audience boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch arbitrary HTTP(S) video sources from the host network.

Mitigation: Use it only with trusted video sources, or deploy it where network egress blocks internal, metadata, loopback, private, and redirected destinations.

Risk: Video content and prompts are sent to Google Gemini using local credentials.

Mitigation: Confirm user authorization before cloud processing and avoid confidential recordings or signed URLs unless the user and organization explicitly approve that processing.

Risk: Cache, history, download, and output options can retain video-derived content or remote upload handles.

Mitigation: Use retention flags only when intended, store outputs in authorized locations, and use purge workflows to remove retained handles and local records when required.

## Reference(s):

- [Data flow and retention](references/privacy.md)
- [ClawHub skill page](https://clawhub.ai/bill492/skills/video-understanding)
- [Publisher profile](https://clawhub.ai/user/bill492)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; the analysis script can return formatted text, raw JSON, or optional output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video analysis may include summaries, timestamped answers, transcripts, visual descriptions, speaker labels, estimated duration, and explicit uncertainty.]

## Skill Version(s):

2.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
