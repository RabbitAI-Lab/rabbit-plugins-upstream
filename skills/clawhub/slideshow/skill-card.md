## Description:

Author a HyperFrames slideshow for presentations, pitch decks, or interactive decks with discrete slides, fragment reveals, branching, hotspot navigation, presenter mode, speaker notes, and source-page conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to turn explicit slideshow requests, or confirmed deck and page-conversion requests, into runnable HyperFrames decks with slide manifests, presenter notes, navigation, branches, and validation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable unpinned HyperFrames commands can update reviewed skill material or add live catalog code to a project.

Mitigation: Use a pinned local HyperFrames version, review skill updates before accepting them, and inspect catalog components before adding them to a deck.

Risk: Presenter notes may contain sensitive information on shared machines.

Mitigation: Avoid sensitive notes on shared devices unless localStorage can be cleared after use.

Risk: Optional third-party browser modules may be unsuitable for public or sensitive presentations.

Mitigation: Vendor optional browser modules before using the deck in public or sensitive settings.

## Reference(s):

- [Standalone HyperFrames Slideshow Harness](artifact/references/standalone-harness.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTML, JSON, CSS, JavaScript, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces runnable HyperFrames slideshow deck guidance rather than a rendered MP4.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
