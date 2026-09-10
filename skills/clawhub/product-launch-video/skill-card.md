## Description:

Turn a product or marketing URL, pasted script, or brief into a product launch or promotional video for SaaS promos, feature reveals, product demos, app launches, company launches, and site tours.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing teams use this skill to turn product briefs, scripts, websites, or captured product material into HyperFrames launch videos with storyboard, script, design, audio, captions, frame compositions, and final MP4 render steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install and runtime steps can update related global skills or touch files outside the project if project files are manipulated.

Mitigation: Use a pinned HyperFrames version or isolated workspace, and review generated STORYBOARD.md paths before assembly.

Risk: Autonomous mode may be inappropriate for sensitive launches or unreleased marketing material.

Mitigation: Use the collaborative review gates for sensitive work and avoid autonomous mode when approval, provenance, or confidentiality matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code, Files]

**Output Format:** [Markdown workflow guidance with shell commands plus generated HyperFrames project files, HTML frame compositions, JSON metadata, captions, audio assets, and an MP4 render.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs gated workflow steps for setup, capture, storyboard approval, frame generation, verification, and final render.]

## Skill Version(s):

1.0.34 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
