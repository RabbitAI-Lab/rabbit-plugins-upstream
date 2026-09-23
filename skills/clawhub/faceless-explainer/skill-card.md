## Description:

Turns articles, notes, topics, or briefs into faceless explainer videos with invented scene visuals such as typography, diagrams, abstract graphics, and data visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, educators, and agents use this skill to convert source text into a HyperFrames explainer-video workflow, including a brief, storyboard, script, frame compositions, captions, audio metadata, preview checks, and final render steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can run mutable external HyperFrames tooling and update installed skills globally.

Mitigation: Use a pinned or locally reviewed HyperFrames version, review update prompts before approval, and run the workflow in a controlled workspace.

Risk: The workflow can store source brief text and generated project files in the video project.

Mitigation: Avoid pasting secrets or sensitive private material, and review generated project contents before sharing or publishing.

Risk: When signed in, TTS and BGM steps can use a HeyGen login and associated media services.

Mitigation: Check authentication status before audio generation, use approved credentials, or choose offline/local fallback paths when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/faceless-explainer)
- [Faceless explainer workflow](artifact/SKILL.md)
- [Story design](artifact/references/story-design.md)
- [Visual design](artifact/references/visual-design.md)
- [Motion language](artifact/references/motion-language.md)
- [Cut catalog](artifact/references/cut-catalog.md)
- [Frame worker delta](artifact/sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown plans and scripts, JSON configuration, HTML frame code, shell commands, and rendered video project files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces HyperFrames project artifacts and final MP4 render steps when executed in a prepared project.]

## Skill Version(s):

1.0.34 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
