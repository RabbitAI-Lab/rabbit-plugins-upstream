## Description:

Turns arbitrary text such as an article, notes, topic, or brief into a faceless explainer video with invented scene visuals such as typography, abstract graphics, diagrams, and data visualization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, educators, and developers use this skill to convert source text into a narrated faceless HyperFrames explainer video. The workflow plans the teaching story, creates storyboard and script files, designs invented visuals, builds HTML frame compositions, and renders a final video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs the agent to silently refresh HyperFrames skills from GitHub before normal use.

Mitigation: Review or disable the silent update step before deployment, and pin trusted versions when operating in controlled environments.

Risk: User-provided source text and generated project files may contain sensitive content.

Mitigation: Avoid providing secrets or sensitive source material unless storage in the generated project directory is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/faceless-explainer)
- [Publisher profile](https://clawhub.ai/user/heygen-com)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker delta](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with shell commands plus generated project files, HTML frame code, JSON metadata, captions, audio metadata, and video render outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a HyperFrames project under videos/<project>/ with storyboard, script, frame compositions, index page, and renders/video.mp4 when the workflow completes.]

## Skill Version(s):

1.0.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
