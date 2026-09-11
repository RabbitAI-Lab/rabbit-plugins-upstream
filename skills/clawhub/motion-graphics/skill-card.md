## Description:

Creates short, design-led, unnarrated motion graphics such as kinetic typography, stat reveals, charts, logo stings, lower thirds, animated maps, article or tweet highlights, webpage animations, and asset-fusion shots that render to MP4 or transparent overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, designers, and developers use this skill to turn supplied text, data, brand assets, URLs, articles, tweets, maps, or images into short HyperFrames motion graphics. It is suited for social clips, data callouts, overlays, brand stings, UI highlights, and concise visual explanations that do not need narration or multi-scene video production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run HyperFrames package tooling, update global skills, fetch registry blocks, contact external providers, and use a networked headless browser.

Mitigation: Install and run it in a restricted workspace or container, review commands before execution, prefer pinned or vendored dependencies, and avoid exposing sensitive environment variables.

Risk: Search, media sourcing, page capture, and optional Gemini-based image localization can send user content or asset descriptions to external services.

Mitigation: Do not use external search or Gemini auto-location on confidential material without explicit approval; use local or user-supplied assets and the non-API grid localization path when needed.

Risk: Map baking depends on third-party tile/CDN endpoints and can produce incomplete or noncompliant outputs if availability, attribution, or terms are not checked.

Mitigation: Validate map parameters and generated outputs, preserve required map attribution in published work, and re-check provider terms before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/motion-graphics)
- [Builder contract](artifact/references/builder-contract.md)
- [Motion vocabulary](artifact/references/motion-vocabulary.md)
- [Shot-plan IR](artifact/references/shot-plan-ir.md)
- [Locate protocol](artifact/grounding/PROTOCOL.md)
- [Catalog map](artifact/catalog-map.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance, JSON shot plans, HTML/CSS/JavaScript compositions, shell commands, project-local assets, proof snapshots, and MP4/WebM/MOV renders.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow creates project-local HyperFrames artifacts and renders only after explicit approval; transparent overlay outputs use WebM or MOV.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
