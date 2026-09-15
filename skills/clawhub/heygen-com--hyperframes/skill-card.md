## Description:

HyperFrames routes agents through video, animation, motion-graphics, slideshow, and Remotion-to-HyperFrames workflows, including creation, editing, previewing, rendering, publishing, and batch rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agent operators use HyperFrames to route briefs, URLs, PRs, Figma inputs, footage, music, or existing project files into HyperFrames video and deck workflows. The skill helps agents capture intent, select the owning workflow, update required tools, produce project artifacts, and verify or render the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can update CLI packages and workflow skills during use, which may change local project behavior.

Mitigation: Run it in a constrained project workspace and review package or skill changes before accepting them.

Risk: Untrusted STORYBOARD.md content is associated with a local Markdown file-inclusion weakness in blueprint path handling.

Mitigation: Avoid untrusted STORYBOARD.md files until the blueprint path handling is fixed, and review generated frame packets before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/hyperframes)
- [Brief Contract](references/brief-contract.md)
- [Capability Menu](references/capability-menu.md)
- [Intent Interview](references/intent-interview.md)
- [Production Loop](references/production-loop.md)
- [Review Loop](references/review-loop.md)
- [Skill Lifecycle](references/skill-lifecycle.md)
- [Storyboard Format](references/storyboard-format.md)
- [Embedded Captions Route](references/routes/embedded-captions.md)
- [Faceless Explainer Route](references/routes/faceless-explainer.md)
- [General Video Route](references/routes/general-video.md)
- [Motion Graphics Route](references/routes/motion-graphics.md)
- [Music-to-Video Route](references/routes/music-to-video.md)
- [PR-to-Video Route](references/routes/pr-to-video.md)
- [Product Launch Video Route](references/routes/product-launch-video.md)
- [Remotion-to-HyperFrames Route](references/routes/remotion-to-hyperframes.md)
- [Slideshow Route](references/routes/slideshow.md)
- [Talking Head Recut Route](references/routes/talking-head-recut.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, generated project files, and HTML or JavaScript composition code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update BRIEF.md, STORYBOARD.md, frame specifications, composition HTML, media metadata, render outputs, and publish links depending on the selected workflow.]

## Skill Version(s):

1.0.27 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
