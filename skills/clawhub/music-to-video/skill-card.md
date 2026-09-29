## Description:

Turns a music track into a beat-synced lyric video, slideshow, or kinetic promo using optional user-supplied visuals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to make music-led videos from an audio track or a mood brief, with optional images or clips synchronized to the music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running unpinned video tooling may update globally installed skills.

Mitigation: Use a sandboxed project and review any skill-update request before proceeding.

Risk: Autonomous mode can weaken approval checkpoints before rendering.

Mitigation: Review the storyboard before building, and avoid autonomous mode on first use.

Risk: Generated videos may contain strobes or full-screen flashes.

Mitigation: Inspect the rendered output for flashing effects before sharing.

Risk: The workflow installs audio packages and processes local media.

Mitigation: Run it in an isolated project with media you are authorized to use.

## Reference(s):

- [Music to Video release on ClawHub](https://clawhub.ai/heygen-com/skills/music-to-video)
- [Storyboard format](artifact/references/storyboard-format.md)
- [Template catalog](artifact/references/template-catalog.md)

## Skill Output:

**Output Type(s):** [Video files, Markdown, JSON, Code]

**Output Format:** [MP4 video with a Markdown storyboard, JSON audio map, and HTML compositions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video pacing follows the music; user media is optional.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
