## Description:

Analyzes local or downloaded video and audio to produce transcripts, scene timelines, summaries, and optional editing assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, editors, and developers use this skill to turn media into timestamped transcripts, scene analyses, and summaries, and to prepare subtitles or edited clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims offline processing but can make outbound requests for updates, models, and remote media.

Mitigation: For sensitive media, use local files with --no-update-check and review network activity before downloading models.

Risk: Remote download options may bypass certificate verification.

Mitigation: Disable certificate-bypass options before using remote URLs or platform downloads.

Risk: Processing reads local media, writes reports, caches, and models, and runs media or download subprocesses.

Mitigation: Review the skill before installation and run it only with appropriate file permissions and trusted inputs.

## Reference(s):

- [Video Analyzer on ClawHub](https://clawhub.ai/fyniujin/skills/video-analyzer-local)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, Media files]

**Output Format:** [Timestamped reports, transcripts, subtitles, and optional edited video or image assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scene thumbnails, subtitle files, and editing timelines.]

## Skill Version(s):

4.5.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
