## Description:

Author a HyperFrames slideshow: a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching, hotspot navigation, and built-in presenter mode with speaker notes; also converts an existing page into a deck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content authors use this skill to create runnable HyperFrames slideshow decks with slide navigation, fragments, branching, speaker notes, presenter mode, and validation guidance. It can also guide conversion of an existing page into a deck while preserving source-page interaction, motion, media behavior, and visual design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to run live unpinned npx hyperframes commands, including a skill self-update.

Mitigation: Install only from a trusted HyperFrames package source, pin the HyperFrames CLI version where possible, avoid automatic skill updates unless intended, and review generated package.json scripts before reuse.

Risk: A slideshow can be incorrectly rendered as a single MP4, which may silently truncate the deck to the first composition.

Mitigation: Use HyperFrames presenter mode for the live deck and per-slide snapshots for still output; surface the MP4 limitation when users ask for a linear video export.

## Reference(s):

- [Standalone HyperFrames Slideshow Harness](references/standalone-harness.md)
- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/slideshow)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTML, JSON, JavaScript, CSS, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for a navigable live deck and per-slide snapshots, not a linear MP4.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
