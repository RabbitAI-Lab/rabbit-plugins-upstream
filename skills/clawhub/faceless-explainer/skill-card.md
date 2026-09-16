## Description:

Turns articles, notes, topics, or briefs into faceless explainer videos with invented typography, abstract graphics, diagrams, and data visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video teams use this skill to convert source text into a HyperFrames faceless explainer video, including brief setup, storyboard and script drafting, visual direction, frame generation, captions, transitions, checks, and final MP4 rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The normal workflow can run mutable external tooling, update global skills, and execute npm-resolved code.

Mitigation: Use a sandboxed workspace, avoid sensitive directories, and prefer a pinned and reviewed HyperFrames version before preview or render.

Risk: Local file-handling issues could affect files outside the intended project.

Mitigation: Run the skill only from an isolated project directory and review STORYBOARD.md and audio_meta.json paths before preview or render.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/faceless-explainer)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker delta](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated HyperFrames project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project artifacts such as BRIEF.md, STORYBOARD.md, SCRIPT.md, frame HTML, captions, index.html, and renders/video.mp4 when executed.]

## Skill Version(s):

1.0.31 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
