## Description:

Build a HyperFrames slideshow to present live - slides, fragment reveals, branching hotspots and presenter mode with speaker notes, served by `hyperframes present` - or turn an existing page into one. Use when the person wants a deck or presentation rather than a rendered video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to build and present live HyperFrames slide decks, add fragment reveals and branching interactions, and port existing pages into presentations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unreviewed or changing HyperFrames dependency can affect the generated deck.

Mitigation: Use a reviewed, pinned HyperFrames installation.

Risk: An optional graphics library served remotely can expose network requests or be unavailable for private and offline decks.

Mitigation: Consider serving the graphics library locally, especially for private or offline decks.

Risk: Presenter-note edits persist in browser storage.

Mitigation: Avoid entering sensitive notes when using a shared browser profile.

Risk: External packages and companion plugin rules are outside the available security review.

Mitigation: Review external dependencies and plugin execution rules before using plugin-based decks.

## Reference(s):

- [Standalone HyperFrames Slideshow Harness](references/standalone-harness.md)
- [ClawHub slideshow release](https://clawhub.ai/heygen-com/skills/slideshow)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Guidance]

**Output Format:** [HTML composition and JSON slideshow configuration with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project files for a live slideshow deck, including slide structure, navigation, and optional presenter notes and media.]

## Skill Version(s):

1.0.19 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
