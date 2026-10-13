## Description:

Guides agents in building and validating renderable HyperFrames video compositions with timed clips, sub-compositions, media, and deterministic animation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to help an agent author HTML video compositions, structure timelines and media, and check projects before rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned CLI package may use a version that was not reviewed.

Mitigation: Use a trusted pinned HyperFrames version or a lockfile-managed local CLI before executing commands.

Risk: A background preview server may remain running after review.

Mitigation: Stop the background preview server when finished.

## Reference(s):

- [HyperFrames Core skill release](https://clawhub.ai/heygen-com/skills/hyperframes-core)
- [Minimal composition](references/minimal-composition.md)
- [Composition patterns](references/composition-patterns.md)
- [Data attributes](references/data-attributes.md)
- [Tracks and clips](references/tracks-and-clips.md)
- [Determinism rules](references/determinism-rules.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with HTML, CSS, JavaScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Composition structure and validation guidance; rendering requires separate user approval.]

## Skill Version(s):

1.0.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
