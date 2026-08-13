## Description:

Author HyperFrames slideshow decks with discrete slides, fragment reveals, branching, hotspot navigation, presenter mode with speaker notes, and conversion support for existing pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design or marketing teams use this skill to create or convert HyperFrames slideshow projects with slide manifests, presenter notes, fragments, branches, hotspots, validation, and presenter-mode handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to silently run an external update command before doing slideshow work, which can change installed skills without explicit user approval.

Mitigation: Require any npx hyperframes skills update slideshow action to be explicit, user-approved, and preferably pinned or handled as a separate setup step.

Risk: Using a linear MP4 render workflow for a slideshow deck can produce a silently truncated output.

Mitigation: Use HyperFrames presenter mode for live decks and per-slide snapshots for still outputs; disclose that linear MP4 export is not the supported slideshow handoff.

## Reference(s):

- [Standalone HyperFrames Slideshow Harness](artifact/references/standalone-harness.md)
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/slideshow)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, JSON, CSS, JavaScript, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces runnable HyperFrames slideshow project guidance; decks are navigable presentations, not MP4 renders.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
