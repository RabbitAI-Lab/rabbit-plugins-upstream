## Description:

Adds styled captions to a single-subject talking-head video, from readable subtitles to cinematic text behind the speaker and themed effects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to transcribe speech, choose a caption style, and render captions into a single-subject talking-head clip. Multi-shot footage should be split before processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may update globally installed skills.

Mitigation: Review or disable automatic global skill updates and confirm changes before running them.

Risk: Local rendering and transcription run external tools and may download models.

Mitigation: Install only if the local media pipeline and its ffmpeg, Node, Chromium/Puppeteer, uvx WhisperX, model-download, and HyperFrames dependencies are acceptable.

Risk: Automatic captions may misrepresent unclear or silent speech, and Theme mode changes the rendered plate effects.

Mitigation: Review the transcript and visual previews before rendering; choose Standard or Cinematic when footage should otherwise remain untouched.

## Reference(s):

- [Embedded Captions on ClawHub](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [Caption style catalog](artifact/CATALOG.md)
- [Caption grouping guidance](artifact/references/caption-grouping.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown instructions with shell commands and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local rendering produces a captioned video file.]

## Skill Version(s):

1.0.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
