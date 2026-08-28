## Description:

HyperFrames routes agent requests to create, edit, animate, render, inspect, validate, preview, publish, or batch-render HTML-based video compositions and related workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and video teams use HyperFrames to turn briefs, URLs, PRs, Figma inputs, existing footage, music, or Remotion source into routed video projects and to manage existing HyperFrames projects through inspection, validation, preview, render, publish, and batch-render operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow setup and rendering can run HyperFrames npx commands.

Mitigation: Review proposed commands and run them in a trusted project workspace before allowing execution.

Risk: Site capture, user media, PRs, and Figma inputs may contain sensitive or third-party content.

Mitigation: Confirm source permissions and redact sensitive material before capture, generation, or render.

Risk: Project upgrades and publishing can change package pins or expose finished videos publicly.

Mitigation: Require explicit approval for upgrades and publishing, then validate the project after any upgrade.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes)
- [Publisher profile](https://clawhub.ai/user/heygen-com)
- [HyperFrames entry point](artifact/SKILL.md)
- [Intent layer](artifact/references/intent-interview.md)
- [Capability menu](artifact/references/capability-menu.md)
- [Pitch round](artifact/references/pitch-round.md)
- [Skill installation and freshness](artifact/references/skill-lifecycle.md)
- [Route: embedded-captions](artifact/references/routes/embedded-captions.md)
- [Route: faceless-explainer](artifact/references/routes/faceless-explainer.md)
- [Route: general-video](artifact/references/routes/general-video.md)
- [Route: motion-graphics](artifact/references/routes/motion-graphics.md)
- [Route: music-to-video](artifact/references/routes/music-to-video.md)
- [Route: pr-to-video](artifact/references/routes/pr-to-video.md)
- [Route: product-launch-video](artifact/references/routes/product-launch-video.md)
- [Route: remotion-to-hyperframes](artifact/references/routes/remotion-to-hyperframes.md)
- [Route: slideshow](artifact/references/routes/slideshow.md)
- [Route: talking-head-recut](artifact/references/routes/talking-head-recut.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and project file instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes work to HyperFrames workflows and domain skills; may produce or modify project briefs, HTML compositions, configuration, media references, and render commands.]

## Skill Version(s):

1.0.24 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
