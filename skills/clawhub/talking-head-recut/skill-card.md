## Description:

Adds transcript-timed graphic overlays to an existing talking-head video while preserving the underlying clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and creators use this skill to add designed titles, quotes, data callouts, and other timed graphics to an existing interview, podcast, or talking-head clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running or updating an unpinned external HyperFrames CLI can change the code the agent executes.

Mitigation: Review or pin the HyperFrames version before use, and confirm skill updates before running them.

Risk: Extracted audio and transcripts may remain in the project work directory.

Mitigation: Avoid sensitive videos unless local storage of their audio and transcripts is acceptable.

## Reference(s):

- [Talking Head Recut on ClawHub](https://clawhub.ai/heygen-com/skills/talking-head-recut)
- [Visual design reference library](references/DESIGN_INDEX.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with HTML and JSON files, plus a rendered MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a storyboard, transcript, graphic-card HTML, a composition, and a rendered video.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
