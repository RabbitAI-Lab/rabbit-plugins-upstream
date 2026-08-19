## Description:

Turn arbitrary text into a faceless explainer video with invented scene visuals such as typography, abstract graphics, diagrams, and data visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, educators, and developers use this skill to convert articles, notes, topics, or briefs into HyperFrames faceless explainer videos with storyboard, narration, design, frame, and render steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill updates HyperFrames skills without prompting before use.

Mitigation: Review the skill before installation and run it in an isolated workspace or container when working with untrusted inputs.

Risk: Generated video pages load GSAP from a third-party CDN.

Mitigation: Confirm that remote code loading is acceptable for the deployment environment before final rendering or distribution.

Risk: Generated projects may include HeyGen sign-in state, stored preferences, and generated media files.

Mitigation: Review sign-in status, stored preferences, and generated project files before final render.

## Reference(s):

- [Faceless Explainer Skill Page](https://clawhub.ai/heygen-com/skills/faceless-explainer)
- [Story Design](references/story-design.md)
- [Visual Design](references/visual-design.md)
- [Motion Language](references/motion-language.md)
- [Cut Catalog](references/cut-catalog.md)
- [Frame Worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands and generated HyperFrames project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces storyboard and script Markdown, audio metadata, HTML frame compositions, an index page, and final render commands or files.]

## Skill Version(s):

1.0.21 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
