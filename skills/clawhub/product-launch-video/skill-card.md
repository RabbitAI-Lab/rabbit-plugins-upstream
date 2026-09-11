## Description:

Turn a product or marketing URL, pasted script, or brief into a product launch or promo video for SaaS promos, feature reveals, product demos, app launches, company launches, and site tours.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and marketing teams use this skill to orchestrate a HyperFrames workflow that captures product evidence, plans a storyboard and script, creates animated HTML frames, assembles audio and captions, and renders a launch video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to run unpinned remote tooling and can update global skills before the workflow continues.

Mitigation: Review before installing, use a sandboxed project workspace, prefer pinned or vetted HyperFrames CLI versions, and approve global skill updates only when the HyperFrames source is trusted.

Risk: User-influenced storyboard, frame, and audio metadata can flow into the render pipeline while the security summary reports unsafe path and HTML handling.

Mitigation: Do not feed untrusted STORYBOARD.md, frame.md, or audio_meta.json content into the pipeline until path containment and HTML/CSS escaping are fixed; review and scan project files before execution.

## Reference(s):

- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [Product-launch frame worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown plans and scripts, JSON metadata, shell commands, HTML/CSS/JavaScript frame compositions, and MP4 render artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a project workspace with storyboard, script, media metadata, frame files, assembled preview, snapshots, captions when available, and final video render.]

## Skill Version(s):

1.0.35 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
