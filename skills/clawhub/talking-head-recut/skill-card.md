## Description:

Packages an existing talking-head, interview, or podcast video with timed designed graphic overlays such as kinetic titles, lower-thirds, data callouts, quotes, side panels, and picture-in-picture cards while the original clip plays underneath.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators, marketing teams, and agents use this skill to turn an existing spoken-video clip into a packaged MP4 with transcript-timed graphic cards. It is suited to adding designed on-screen graphics rather than plain subtitles or from-scratch video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow runs local media-processing commands and may use npx to obtain or update HyperFrames tooling if approved.

Mitigation: Use videos that are appropriate for local processing, approve tool updates deliberately, and review the generated project directory before sharing the final MP4.

Risk: Transcript-derived cards or visual summaries may misstate what the speaker said if transcription or card selection is wrong.

Mitigation: Review and correct transcript text, card timing, and generated overlays before rendering or publishing the video.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/talking-head-recut)
- [Attribution notice](artifact/NOTICE.md)
- [Visual design reference index](artifact/references/DESIGN_INDEX.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON storyboards, HTML/CSS card code, and render instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed by an agent, the workflow can produce local project files such as metadata.json, transcript.json, storyboard.json, card HTML, public/index.html, and output.mp4.]

## Skill Version(s):

1.0.9 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
