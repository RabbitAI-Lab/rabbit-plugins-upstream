## Description:

Turns arbitrary text such as an article, notes, a topic, or a brief into a faceless explainer video with invented per-scene visuals such as typography, abstract graphics, diagrams, and data visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn source text into a HyperFrames faceless explainer workflow, including a durable brief, storyboard, script, audio metadata, frame compositions, captions, transitions, and a final rendered video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable remote tooling may change behavior during installation or workflow execution.

Mitigation: Review before installing, prefer pinned HyperFrames tooling, and approve updates only when the exact source being fetched is trusted.

Risk: File-path handling may write outside the intended project when project files such as STORYBOARD.md or audio_meta.json are untrusted.

Mitigation: Run the skill only in a sandbox or disposable project and avoid untrusted project files until path containment is fixed.

Risk: The workflow may use HeyGen or local audio tooling and save project briefs and preferences for later reuse.

Mitigation: Use only appropriate project content, review saved preferences and generated files, and remove sensitive material before reuse or sharing.

## Reference(s):

- [Faceless Explainer ClawHub skill page](https://clawhub.ai/heygen-com/skills/faceless-explainer)
- [Story design](artifact/references/story-design.md)
- [Visual design](artifact/references/visual-design.md)
- [Motion language](artifact/references/motion-language.md)
- [Cut catalog](artifact/references/cut-catalog.md)
- [Frame worker](artifact/sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project artifacts such as BRIEF.md, STORYBOARD.md, SCRIPT.md, audio_meta.json, HTML frame compositions, captions, transition updates, index.html, and renders/video.mp4 when the workflow is executed.]

## Skill Version(s):

1.0.30 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
