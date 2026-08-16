## Description:

HyperFrames routes requests to create, edit, animate, inspect, validate, render, publish, or batch-render videos, animations, motion graphics, slideshows, captioned clips, Remotion migrations, and HTML-based HyperFrames compositions from inputs such as URLs, pull requests, Figma designs, briefs, footage, or music.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and teams use this skill as the HyperFrames entry point for video and motion work, including routing fresh briefs, resuming projects, selecting workflow skills, and producing checked compositions or renders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Website capture, media reuse, brand assets, and published links can expose or reuse source material in ways the user did not intend.

Mitigation: Confirm source pages, media, brand assets, and final publish links are safe to expose or reuse before capture or publish.

Risk: The skill installs or updates related HyperFrames workflow skills and can run render-affecting CLI commands.

Mitigation: Install only when HyperFrames should manage the project, review and scan the skill before deployment, and surface update or validation failures instead of proceeding from memory.

Risk: Incorrect routing or generated video guidance could produce misleading captions, edits, product narratives, or code-change explanations.

Mitigation: Review the selected route, confirmed brief, storyboard or preview, and final render before external use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes)
- [HyperFrames entry point](artifact/SKILL.md)
- [Intent interview](artifact/references/intent-interview.md)
- [Capability menu](artifact/references/capability-menu.md)
- [Skill lifecycle](artifact/references/skill-lifecycle.md)
- [Route briefs](artifact/references/route-briefs.md)
- [Workflow catalog](artifact/references/workflow-catalog.md)
- [Route: embedded captions](artifact/references/routes/embedded-captions.md)
- [Route: faceless explainer](artifact/references/routes/faceless-explainer.md)
- [Route: general video](artifact/references/routes/general-video.md)
- [Route: motion graphics](artifact/references/routes/motion-graphics.md)
- [Route: music to video](artifact/references/routes/music-to-video.md)
- [Route: pull request to video](artifact/references/routes/pr-to-video.md)
- [Route: product launch video](artifact/references/routes/product-launch-video.md)
- [Route: Remotion to HyperFrames](artifact/references/routes/remotion-to-hyperframes.md)
- [Route: slideshow](artifact/references/routes/slideshow.md)
- [Route: talking head recut](artifact/references/routes/talking-head-recut.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and project file instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update HyperFrames project files, briefs, HTML compositions, media assets, render outputs, and public publish links depending on the selected workflow.]

## Skill Version(s):

1.0.22 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
