## Description:

Creates short, design-led, unnarrated motion graphics such as kinetic typography, stat and chart hits, logo reveals, overlays, animated maps, news, tweet, webpage highlights, and asset-fusion shots rendered to MP4 or transparent overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to turn a short motion-graphics request into a planned, sourced, built, verified, and render-approved HyperFrames project. It is suited to external or internal agents creating concise visual explainers, social overlays, map animations, chart hits, and brand stings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner flagged silent global skill updates before use.

Mitigation: Review the update behavior before installation and run the skill in an isolated or pinned environment when reproducibility matters.

Risk: Asset sourcing, web capture, and image-generation paths can expose user images, URLs, page content, or prompts to external services.

Mitigation: Do not use confidential images, unreleased brand assets, authenticated pages, internal URLs, or sensitive prompts unless provider data-handling terms have been reviewed.

Risk: Ambient provider keys can enable external processing when a local-only workflow is expected.

Mitigation: Unset provider keys such as GEMINI_API_KEY and GOOGLE_API_KEY before use when external processing is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/motion-graphics)
- [Builder contract](references/builder-contract.md)
- [Motion vocabulary](references/motion-vocabulary.md)
- [Shot-plan IR](references/shot-plan-ir.md)
- [Grounding protocol](grounding/PROTOCOL.md)
- [Source phase guide](phases/source/guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON shot plans, HTML/GSAP composition code, shell commands, project files, and render handoff notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project-local HyperFrames artifacts; final video output may be MP4, WebM, or MOV transparent overlay after explicit render approval.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
