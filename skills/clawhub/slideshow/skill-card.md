## Description:

Guides agents to author HyperFrames slideshow decks with discrete slides, fragment reveals, branching, hotspot navigation, speaker notes, and presenter mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to build interactive presentation and pitch decks or convert existing pages into navigable HyperFrames slideshows with presenter notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned npx HyperFrames commands can execute changing remote package code.

Mitigation: Pin or lock the HyperFrames dependency before running commands, and review generated package scripts that invoke npx.

Risk: Rendering a multi-slide deck as one MP4 can silently include only its first slide.

Mitigation: Present the navigable deck or export individual slide stills; disclose that a complete linear MP4 is not supported.

## Reference(s):

- [ClawHub slideshow release](https://clawhub.ai/heygen-com/skills/slideshow)
- [Standalone HyperFrames Slideshow Harness](references/standalone-harness.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [HTML, CSS, JavaScript, and JSON deck files with Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a navigable slideshow deck, not a rendered MP4.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
