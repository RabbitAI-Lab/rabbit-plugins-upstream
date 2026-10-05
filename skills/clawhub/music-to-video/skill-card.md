## Description:

Turns music into a beat-synced lyric video, slideshow, or kinetic promo, with optional user-supplied images and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a music track or mood brief into a beat-synced video, with optional images or video clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Networked HyperFrames commands can run an unpinned package and update globally installed skills.

Mitigation: Use a constrained workspace, review update prompts, and pin or pre-vet HyperFrames where possible.

Risk: Music and video assets may be sensitive, and the workflow creates project files under videos/<project>.

Mitigation: Avoid sensitive media and review the project directory and outputs before sharing.

Risk: Some video templates can produce intense flashing or strobe visuals.

Mitigation: Inspect previews and replace or soften flashing effects before release.

## Reference(s):

- [Music to Video on ClawHub](https://clawhub.ai/heygen-com/skills/music-to-video)
- [Frame skeleton](references/frame-skeleton.md)
- [Storyboard format](references/storyboard-format.md)
- [Template catalog](references/template-catalog.md)

## Skill Output:

**Output Type(s):** [Video, Markdown, Code, JSON]

**Output Format:** [MP4 video with storyboard Markdown, HTML compositions, and audio-map JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video pacing follows the music; supplied images and videos are optional.]

## Skill Version(s):

1.0.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
