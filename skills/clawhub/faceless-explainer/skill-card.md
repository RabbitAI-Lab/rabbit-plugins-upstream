## Description:

Turn arbitrary text into a faceless explainer video by planning a teaching story and building invented per-scene visuals such as typography, abstract graphics, diagrams, and data visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to convert articles, notes, topics, or briefs into HyperFrames faceless explainer videos with storyboards, narration/audio metadata, frame compositions, captions, transitions, and a final render path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to run mutable npm and GitHub-sourced HyperFrames/media tooling.

Mitigation: Install only when that tooling is trusted for the workspace, review commands before execution, and keep user approval gates for setup, storyboard, and final render.

Risk: Project-boundary and generated-HTML safety gaps may affect resumed projects or untrusted storyboard, frame, token, and font inputs.

Mitigation: Review existing BRIEF.md, STORYBOARD.md, frame.md, and tokens.json before resuming; avoid untrusted font names and storyboard files until path containment and HTML escaping issues are fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/faceless-explainer)
- [story-design.md](references/story-design.md)
- [visual-design.md](references/visual-design.md)
- [motion-language.md](references/motion-language.md)
- [cut-catalog.md](references/cut-catalog.md)
- [frame-worker.md](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces HyperFrames project artifacts such as BRIEF.md, STORYBOARD.md, SCRIPT.md, audio_meta.json, HTML frame compositions, captions, transitions, index.html, and renders/video.mp4.]

## Skill Version(s):

1.0.28 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
