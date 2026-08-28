## Description:

Turn a product or marketing URL, pasted script, or brief into a product launch or promo video for SaaS promos, feature reveals, product demos, app launches, company launches, site tours, and website showcases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketing teams, and developers use this skill to turn product URLs, scripts, or launch briefs into structured HyperFrames projects and final promotional videos. It supports capture, brand extraction, storyboarding, narration or music metadata, frame assembly, preview checks, and MP4 rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may crawl a provided or confirmed product URL and use external media services.

Mitigation: Confirm the URL and desired access path before capture; choose offline or no-capture paths when external access is not desired.

Risk: Configured media credentials or API keys may be used for narration, music, sound effects, or optional vision-assisted asset descriptions.

Mitigation: Review authentication status and provider choices before media generation, and continue with local or silent paths when credentials should not be used.

Risk: Project state is saved under videos/<project> and may be reused when a project is resumed.

Mitigation: Review BRIEF.md and project files before resuming old work so stale briefs, preferences, or generated assets are not reused unintentionally.

Risk: Generated previews and renders load GSAP from a CDN.

Mitigation: Use the workflow only when CDN loading is acceptable for the target environment, or review generated HTML before distribution.

## Reference(s):

- [ClawHub product-launch-video skill page](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown plans and scripts, JSON metadata, HTML frame compositions, shell commands, project files, and an MP4 render.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saves project state under videos/<project>; generated previews and renders may load GSAP from a CDN.]

## Skill Version(s):

1.0.32 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
