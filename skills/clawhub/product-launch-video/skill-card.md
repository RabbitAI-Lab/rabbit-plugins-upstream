## Description:

Turns a product or marketing URL, pasted script, or brief into a HyperFrames product launch or promo video for SaaS promos, feature reveals, demos, app launches, and website showcases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, founders, and developers use this skill to turn a commercial product URL, pasted script, or brief into a launch video workflow with captured brand assets, storyboard/script, HTML frame compositions, audio/captions, and a rendered MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill silently updates installed HyperFrames skills globally before use.

Mitigation: Install and run it only where that update behavior is acceptable, and review the workflow before execution in controlled environments.

Risk: Website capture, media generation, captioning, and audio may use signed-in HeyGen credentials or available vision/API keys.

Mitigation: Use collaborative mode, verify auth status and provider choices, and avoid supplying sensitive URLs or API keys when those services should not be used.

Risk: Existing BRIEF.md or STORYBOARD.md files can cause the workflow to resume without re-asking setup questions.

Mitigation: Review existing project files before resuming so stale assumptions do not drive the generated video.

## Reference(s):

- [ClawHub Product Launch Video Skill Page](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [Story Design](references/story-design.md)
- [Visual Design](references/visual-design.md)
- [Motion Language](references/motion-language.md)
- [Cut Catalog](references/cut-catalog.md)
- [Frame Worker Delta](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands plus generated HyperFrames project files, including HTML compositions, JSON metadata, caption artifacts, and MP4 video output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates work under videos/<project>; the final video target is renders/video.mp4 after lint, check, snapshot review, and approval gates.]

## Skill Version(s):

1.0.28 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
