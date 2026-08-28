## Description:

Video Analyzer converts local media files or supported media URLs into timestamped transcripts, scene analysis, multimodal summaries, highlight selections, editing suggestions, and HTML, JSON, and Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, media analysts, and content teams use this skill to analyze video or audio inputs, generate transcripts and structured reports, and prepare editing artifacts such as subtitles, highlights, EDL timelines, and chapter slices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims local or offline processing, but security evidence says it may contact GitHub, model hosts, video platforms, and user-provided URLs.

Mitigation: Use --no-update-check in restricted environments, prefer local media files, and allow network access only when remote downloads or model retrieval are intended.

Risk: Remote downloads may include TLS checks disabled according to security evidence.

Mitigation: Avoid sensitive or internal URLs, use trusted media sources, and review downloaded content before processing or sharing generated outputs.

Risk: Downloaded or untrusted videos can be resource-intensive to process.

Mitigation: Set memory and priority controls such as --max-memory and --nice, and use reduced analysis modes such as --no-visual or --no-ocr for large or untrusted inputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fyniujin/skills/video-analyzer-local)
- [Artifact README](artifact/README.md)
- [Artifact Skill Definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Files, Shell commands]

**Output Format:** [HTML, JSON, Markdown, subtitles, EDL timelines, media clips, and generated command files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include report.html, data.json, script.md, scene thumbnails, subtitles, chapter clips, platform metadata, timeline files, and timestamped summaries.]

## Skill Version(s):

4.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
