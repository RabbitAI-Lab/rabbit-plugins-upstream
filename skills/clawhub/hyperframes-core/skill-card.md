## Description:

Guides developers in building and validating renderable HyperFrames HTML video compositions with timed clips, tracks, sub-compositions, media, and deterministic animation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to author or edit a single HyperFrames composition and check its timing, media, and render behavior before producing video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running unpinned HyperFrames CLI commands may execute an untrusted installation.

Mitigation: Run HyperFrames from a trusted, pinned local dependency or lockfile instead of copying unpinned npx commands.

Risk: Preview mode may leave a background server running.

Mitigation: Stop the preview server after review.

## Reference(s):

- [HyperFrames Core on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-core)
- [Minimal composition](references/minimal-composition.md)
- [Composition patterns](references/composition-patterns.md)
- [Data attributes](references/data-attributes.md)
- [Tracks and clips](references/tracks-and-clips.md)
- [Sub-compositions](references/sub-compositions.md)
- [Variables and media](references/variables-and-media.md)
- [Determinism rules](references/determinism-rules.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with HTML and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides composition and validation guidance; rendering requires user approval.]

## Skill Version(s):

1.0.37 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
