## Description:

Turns a product or marketing URL, pasted script, or brief into a product launch or promotional video workflow for SaaS promos, feature reveals, demos, app launches, company launches, and site showcases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing teams use this skill to orchestrate HyperFrames projects that capture product source material, plan a launch story, generate storyboard and script assets, design timed visual frames, and assemble a promotional video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned remote CLI execution and global skill refreshes can change workflow behavior or run unexpected code.

Mitigation: Review the skill before installation, prefer a reviewed or pinned HyperFrames version, and run it in a contained project workspace.

Risk: The workflow may use available media or provider credentials while creating video assets.

Mitigation: Expose only the credentials needed for the video project and avoid sharing unrelated credentials with the workspace.

## Reference(s):

- [Product Launch Video on ClawHub](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [Story Design](artifact/references/story-design.md)
- [Visual Design](artifact/references/visual-design.md)
- [Motion Language](artifact/references/motion-language.md)
- [Cut Catalog](artifact/references/cut-catalog.md)
- [Frame Worker Delta](artifact/sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, project configuration, storyboard/script files, HTML frame code, JSON metadata, and rendered media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a HyperFrames project workflow that can culminate in a rendered product launch video.]

## Skill Version(s):

1.0.43 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
