## Description:

Turns a music track into a beat-synced lyric video, slideshow, or kinetic promo, with optional user-supplied media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to plan, assemble, and render music-led videos from a supplied or generated track, optionally incorporating images, footage, or lyrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned runtime commands may execute changed external code.

Mitigation: Prefer a pinned or local HyperFrames CLI and review commands before running them.

Risk: The update command can change globally installed HyperFrames skills.

Mitigation: Confirm with the user and review the update before applying it.

Risk: Authentication status output may contain information unsuitable for sharing.

Mitigation: Review authentication output before forwarding or publishing it.

Risk: Strobe-heavy video effects may be unsuitable for photosensitive viewers.

Mitigation: Avoid or clearly warn about strobe-heavy output for sensitive audiences.

## Reference(s):

- [ClawHub music-to-video release](https://clawhub.ai/heygen-com/skills/music-to-video)
- [Frame skeleton](references/frame-skeleton.md)
- [Storyboard format](references/storyboard-format.md)
- [Template catalog](references/template-catalog.md)
- [Asset treatments](references/montage.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Configuration, Shell commands]

**Output Format:** [Storyboard Markdown, HTML compositions, JSON configuration, and render commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [After review and rendering, delivers a beat-synced MP4 with audio.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
