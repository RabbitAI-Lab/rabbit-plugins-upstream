## Description:

Faceless Explainer turns arbitrary text into a HyperFrames explainer video with invented scene visuals such as typography, abstract graphics, diagrams, and data visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn articles, notes, topics, or briefs into faceless explainer videos in HyperFrames. It is intended for topic explainers, concept breakdowns, how-tos, and listicles where the visuals are invented rather than captured from a website or product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may update the global HyperFrames skill set through npx/GitHub-based skill update behavior.

Mitigation: Review and approve update behavior before installation or execution, and run the skill only in an environment where global skill-set changes are acceptable.

Risk: Audio workflows may use HeyGen credentials when the user is signed in.

Mitigation: Check authentication status before setup continues, confirm whether to use signed-in or offline providers, and avoid running with credentials in untrusted workspaces.

Risk: Generated HTML previews or renders may contact jsDelivr to load GSAP.

Mitigation: Preview and render only where public CDN access is allowed, or review generated HTML and provide an approved local dependency path before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/faceless-explainer)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker delta](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, video files]

**Output Format:** [Markdown guidance with shell commands, generated project files, HTML frame code, and rendered video artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a HyperFrames project under videos/<project> and typically renders to renders/video.mp4]

## Skill Version(s):

1.0.26 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
