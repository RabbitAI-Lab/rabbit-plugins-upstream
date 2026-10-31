## Description:

Transcribes local audio and video, then prepares transcripts for focused summaries, meeting notes, analysis, and optional subtitle or offline HTML output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bjbook](https://clawhub.ai/user/bjbook)

### License/Terms of Use:

MIT-0

## Use Case:

People working with recordings can use the skill to transcribe local audio or video, then prepare a focused summary, meeting notes, analysis, or subtitles. They can reuse cached transcripts to create summaries from different angles and optionally render a summary as offline HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transcript text is sent to the current model provider during summarization.

Mitigation: Use recordings whose transcript you are comfortable sharing with that provider.

Risk: Cached transcripts remain on disk until removed.

Mitigation: Delete cached transcripts when they are no longer needed.

Risk: HTML summaries may contain links.

Mitigation: Review links in HTML summaries before following them.

Risk: The workflow installs dependencies for local transcription.

Mitigation: Install dependencies from trusted sources.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bjbook/skills/zhz-transcript-summarize)
- [Project Homepage](http://openclaw.bjbook.net/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Subtitle files, HTML]

**Output Format:** [Transcript text and JSON; summary and preparation files in Markdown; optional SRT/VTT subtitles and standalone HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output language, summary focus, audience, format, length, glossary corrections, timeline, and optional subtitle export can be configured.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
