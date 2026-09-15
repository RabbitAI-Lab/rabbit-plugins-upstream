## Description:

Author a HyperFrames slideshow - a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching, hotspot navigation, and built-in presenter mode with speaker notes; also converts an existing page into a deck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to create runnable HyperFrames slideshow decks with slide navigation, fragments, branches, hotspots, presenter mode, speaker notes, and source-page conversion while preserving relevant interactive behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users or agents to run mutable, unpinned npm commands, including a skill updater.

Mitigation: Review skill updates before use and prefer pinning hyperframes to a reviewed version or using a lockfile-backed local install.

Risk: Standalone harness examples may be risky if deployed publicly without hardening message origins or dependency loading.

Mitigation: Avoid public deployment of standalone harness examples until message origins are tightened and CDN dependencies are vendored or otherwise reviewed.

## Reference(s):

- [Standalone HyperFrames Slideshow Harness](references/standalone-harness.md)
- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/slideshow)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, JSON, JavaScript, CSS, and shell command examples for runnable HyperFrames slideshow projects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces navigable deck assets and presenter-mode handoff guidance rather than a rendered MP4.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
