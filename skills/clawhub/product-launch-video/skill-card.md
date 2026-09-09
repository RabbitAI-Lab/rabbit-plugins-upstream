## Description:

Turns a product or marketing URL, pasted script, or brief into a product launch or promo video workflow for SaaS promos, feature reveals, product demos, app launches, and site showcases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, creators, and developers use this skill to capture product source material, plan a launch story, build HyperFrames scenes, add audio/captions, validate the assembled result, and render a promo video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow asks the agent to run mutable global skill updates and unpinned npx HyperFrames commands.

Mitigation: Use a pinned, locally installed HyperFrames version where possible and review update behavior before running the workflow in a shared environment.

Risk: Generated caption or timing HTML can carry script-injection risk when fed untrusted transcript or timing metadata.

Mitigation: Avoid untrusted transcript and timing inputs until caption serialization is hardened, and review captured sites, generated captions, and preview output before rendering or sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON metadata, HTML frame code, media project files, and rendered video output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces HyperFrames project artifacts such as BRIEF.md, STORYBOARD.md, SCRIPT.md, frame.md, audio_meta.json, HTML frame compositions, index.html, contact sheets, and renders/video.mp4.]

## Skill Version(s):

1.0.33 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
