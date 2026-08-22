## Description:

Turn a product or marketing URL, pasted script, or brief into a product launch or promo video for SaaS promos, feature reveals, product demos, app launches, company launches, site tours, and website showcases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, product, and creative teams use this skill to plan and build launch or promotional videos from a product URL, script, or brief. It captures brand and product material, drafts storyboard and narration, builds HyperFrames frame compositions, and renders an MP4 after review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may send script, storyboard, or audio requests to HeyGen or other configured providers.

Mitigation: Use offline or local provider options for confidential launches and review provider configuration before running audio or media steps.

Risk: The workflow captures product pages and stores project state, captured assets, and remembered preferences under videos/<project>.

Mitigation: Review input material before capture, avoid confidential product pages unless approved, and inspect generated project files before sharing.

Risk: The HyperFrames skill update behavior may refresh related installed skills globally.

Mitigation: Confirm updates before running the workflow and review the installed skill set when global skill changes matter.

## Reference(s):

- [Story design - product launch video](artifact/references/story-design.md)
- [Visual design - product-launch per-frame shot method](artifact/references/visual-design.md)
- [Motion language - move vocabulary and seek-safe core](artifact/references/motion-language.md)
- [Cut catalog - within-frame seams](artifact/references/cut-catalog.md)
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/product-launch-video)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown workflow guidance with inline shell commands and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces HyperFrames project artifacts including briefs, capture files, storyboard and script markdown, frame HTML, caption and audio metadata, contact sheets, and MP4 renders.]

## Skill Version(s):

1.0.31 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
