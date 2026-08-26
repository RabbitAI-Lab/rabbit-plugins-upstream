## Description:

Author HyperFrames slideshow decks with discrete slides, fragment reveals, branching, hotspot navigation, presenter mode with speaker notes, and source-page conversion support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create or convert HyperFrames slideshow projects into runnable presenter decks with navigation, speaker notes, fragments, branches, validation, and handoff guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask to run HyperFrames CLI commands, update related HyperFrames skills, start a local presenter server, or store presenter-note edits in the browser.

Mitigation: Confirm command execution with the user, review commands before running them, keep presenter servers local unless explicitly shared, and disclose that note edits are browser-local.

Risk: Rendering a slideshow as a single MP4 can silently truncate the deck because slides are authored as multiple top-level scene compositions.

Mitigation: Use the live presenter deck or per-slide snapshots for handoff, and state the current MP4 limitation when a linear video is requested.

Risk: Presenter media sync can be constrained by browser autoplay policy, especially for audience-window audio.

Mitigation: Mirror native media events, try muted audience playback first, and provide an audience unlock control when playback is blocked.

## Reference(s):

- [Standalone HyperFrames Slideshow Harness](references/standalone-harness.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, JSON, CSS, JavaScript, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a runnable HyperFrames slideshow deck rather than a rendered MP4; supported handoff is presenter mode or per-slide snapshots.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
