## Description:

Turn a product or marketing URL, pasted script, or brief into a product launch / promo video -- SaaS promos, feature reveals, product demos, app and company launches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to turn a product URL, script, or marketing brief into a HyperFrames product launch or promotional video with captured assets, storyboard/script planning, frame construction, audio, captions, and final rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow instructs the agent to perform a silent networked self-update before use.

Mitigation: Require explicit approval for updates, or remove/override the self-update step and use reviewed, pinned skill versions.

Risk: The workflow uses network capture, existing media/API credentials, and external services to produce video assets.

Mitigation: Run it only with trusted inputs and appropriately scoped credentials, and review captured or generated assets before publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [Story Design](references/story-design.md)
- [Visual Design](references/visual-design.md)
- [Motion Language](references/motion-language.md)
- [Cut Catalog](references/cut-catalog.md)
- [Frame Worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON/configuration files, HTML frame compositions, and rendered video artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a staged HyperFrames project with BRIEF.md, STORYBOARD.md, SCRIPT.md when narration is needed, frame HTML, index.html, optional audio/caption metadata, and renders/video.mp4.]

## Skill Version(s):

1.0.26 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
