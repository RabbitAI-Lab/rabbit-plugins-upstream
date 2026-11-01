## Description:

Video Analyzer analyzes video and audio to produce timestamped transcripts, scene and speaker summaries, cross-modal insights, and editing outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, editors, and analysts use the skill to turn videos, podcasts, and recordings into timestamped transcripts, scene and speaker summaries, and editable highlights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online media downloads may have weakened security when certificate verification is disabled.

Mitigation: Restore certificate verification before downloading online media; for offline use, preinstall models and pass --no-update-check.

Risk: Persistent pip mirror settings can affect other projects.

Mitigation: Use an isolated Python environment and avoid persistent pip mirror changes.

Risk: Subtitle text may be handled by the configured translation router.

Mitigation: Keep translation disabled unless the router is trusted and its handling of subtitle text is understood.

## Reference(s):

- [Video Analyzer on ClawHub](https://clawhub.ai/fyniujin/skills/video-analyzer-local)

## Skill Output:

**Output Type(s):** [Analysis, HTML reports, JSON data, Markdown reports, Subtitle files, Editing timelines, Edited video clips]

**Output Format:** [HTML, JSON, Markdown, SRT/VTT/ASS subtitles, EDL timelines, and video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Timestamped transcripts and scene or speaker annotations; optional translated subtitles and media exports.]

## Skill Version(s):

4.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
