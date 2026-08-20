## Description:

Authors HyperFrames slideshows, including presentations, pitch decks, interactive decks, and page-to-deck conversions with discrete slides, fragment reveals, branching, hotspot navigation, and presenter mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and presentation authors use this skill to create runnable HyperFrames slideshow decks with navigation, presenter notes, fragments, branching, and handoff validation. It is also useful when converting an existing page into a deck while preserving visual design, media behavior, and interaction patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs the agent to silently run an automatic skill update before doing the user's task.

Mitigation: Change update behavior to an explicit, user-approved maintenance step with pinned provenance before routine use.

Risk: Rendering a slideshow deck as a single MP4 can silently produce a truncated export.

Mitigation: Use the supported presenter deck workflow or per-slide snapshots, and disclose the MP4 limitation when a user asks for linear video output.

Risk: Presenter-driven audience media playback can be blocked by browser autoplay policy.

Mitigation: Start remote audience playback muted when needed, provide an audience unlock control if playback is rejected, and verify media behavior in browser presentation mode.

## Reference(s):

- [Standalone HyperFrames Slideshow Harness](references/standalone-harness.md)
- [ClawHub slideshow skill page](https://clawhub.ai/heygen-com/skills/slideshow)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, JSON manifest snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces runnable HyperFrames slideshow decks, presenter handoff instructions, and validation steps; it warns that decks should not be rendered as a single MP4.]

## Skill Version(s):

1.0.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
