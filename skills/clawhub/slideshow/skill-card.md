## Description:

Build a HyperFrames slideshow to present live - slides, fragment reveals, branching hotspots and presenter mode with speaker notes, served by `hyperframes present` - or turn an existing page into one. Use when the person wants a deck or presentation rather than a rendered video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and presentation creators use this skill to build or adapt a HyperFrames project into a live slideshow with slide navigation, reveals, branching hotspots, and presenter notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The HyperFrames CLI can send account-linked usage reporting, and external CLI, player bundles, CDN code, and parent plugin rules are outside the supplied security review.

Mitigation: Set the CLI telemetry opt-out before first use when account-linked reporting is unwanted. Use a reviewed, locked CLI version, and use local Three.js assets for private or offline presentations.

## Reference(s):

- [ClawHub slideshow release](https://clawhub.ai/heygen-com/skills/slideshow)
- [Standalone HyperFrames Slideshow Harness](artifact/references/standalone-harness.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Guidance]

**Output Format:** [HyperFrames HTML composition and slideshow JSON, with shell commands and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a runnable slideshow project and presenter setup instructions.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
