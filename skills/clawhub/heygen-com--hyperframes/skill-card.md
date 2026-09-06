## Description:

HyperFrames is an entry-point skill that routes agent requests to create, edit, animate, render, inspect, validate, preview, publish, or batch-render video, animation, motion graphics, slideshows, Remotion ports, and HyperFrames HTML compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and external users use this skill as the front door for HyperFrames video work: it resumes existing project state, interviews for fresh briefs, selects the appropriate workflow, and routes the agent toward video, motion graphic, slideshow, captioning, overlay, PR explainer, product promo, or Remotion migration tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable remote package and workflow-skill updates can change executable tooling and future agent instructions.

Mitigation: Review update behavior before installation, use a sandbox or controlled project environment, and require explicit review of package and skill updates when possible.

Risk: Automatic project CLI upgrades can change the pinned HyperFrames version used for render-affecting commands.

Mitigation: Run the documented check after upgrades, report old and new versions, and revert the package pin if validation fails.

Risk: Running the skill in a broad workspace could expose unrelated credentials or files to selected workflows.

Mitigation: Run it only in the intended project workspace and avoid exposing unrelated credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes)
- [Capability menu](references/capability-menu.md)
- [Intent layer](references/intent-interview.md)
- [Pitch round](references/pitch-round.md)
- [Skill installation and freshness](references/skill-lifecycle.md)
- [Route briefs](references/route-briefs.md)
- [Workflow catalog](references/workflow-catalog.md)
- [Route: embedded-captions](references/routes/embedded-captions.md)
- [Route: faceless-explainer](references/routes/faceless-explainer.md)
- [Route: general-video](references/routes/general-video.md)
- [Route: motion-graphics](references/routes/motion-graphics.md)
- [Route: music-to-video](references/routes/music-to-video.md)
- [Route: pr-to-video](references/routes/pr-to-video.md)
- [Route: product-launch-video](references/routes/product-launch-video.md)
- [Route: remotion-to-hyperframes](references/routes/remotion-to-hyperframes.md)
- [Route: slideshow](references/routes/slideshow.md)
- [Route: talking-head-recut](references/routes/talking-head-recut.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and project file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update HyperFrames briefs, HTML compositions, JSON configuration, media manifests, and render or publish commands through selected workflows.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
