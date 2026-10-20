## Description:

Helps authors build navigable HyperFrames slideshow decks with slide transitions, fragment reveals, branching, hotspots, presenter mode, and speaker notes, including conversions from existing pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to author or convert presentations into interactive, browser-based HyperFrames decks with navigation and presenter notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live, unpinned CLI commands can execute changing external code or update the skill unexpectedly.

Mitigation: Review commands before running, pin the HyperFrames CLI or use a lockfile-backed install, and update the skill only through a trusted channel.

Risk: Remote runtime assets can change or become unavailable for sensitive decks.

Mitigation: Vendor or integrity-pin runtime assets such as Three.js.

## Reference(s):

- [Slideshow release on ClawHub](https://clawhub.ai/heygen-com/skills/slideshow)
- [Standalone slideshow harness](references/standalone-harness.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [HTML and JSON deck files with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A navigable deck with optional fragments, branching, and presenter notes; not a single rendered MP4.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
