## Description:

Watch and analyze video URLs or files using Gemini native agentic video understanding for summaries, timestamped answers, transcripts, and visual reconstruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bill492](https://clawhub.ai/user/bill492)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect authorized video URLs or local video files, ask focused questions, and produce summaries, timestamped answers, transcripts, or visual descriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos and prompts are sent to Google Gemini for cloud analysis.

Mitigation: Confirm user authorization before cloud processing and check applicable Gemini account or data terms before using sensitive material.

Risk: Signed URLs or credential-bearing links can expose secrets through command history, logs, or downloader requests.

Mitigation: Use authorized local files for sensitive sources and keep credentials in managed environment configuration.

Risk: The downloader accepts broad HTTP(S) video sources and is not a network isolation boundary for untrusted jobs.

Mitigation: Do not expose it as a public fetch service unless host-level egress controls cover redirects, extractors, manifests, segments, and child processes.

Risk: Cache, history, retained downloads, and output files can preserve video-derived content.

Mitigation: Use retention flags only when intentional, store outputs in authorized locations, and verify purge completion before claiming deletion.

## Reference(s):

- [Data flow and retention](references/privacy.md)
- [ClawHub skill page](https://clawhub.ai/bill492/skills/video-understanding)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown responses with optional JSON or text analysis output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include summaries, timestamped answers, transcripts, visual descriptions, and download-only media outputs when explicitly requested.]

## Skill Version(s):

2.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
