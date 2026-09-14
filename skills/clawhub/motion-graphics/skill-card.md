## Description:

Creates short, design-led, unnarrated motion graphics such as kinetic typography, stat count-ups, charts, logo reveals, lower-thirds, animated maps, tweet or news cards, webpage highlights, and image-to-chart asset-fusion shots, usually rendered as MP4 or a transparent overlay.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, designers, marketers, and developers use this skill to direct an agent through planning, sourcing, building, verifying, and rendering short motion graphics for text, data, brand, map, social, article, webpage, and asset-fusion use cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives agents broad mutable code execution paths while planning, composing, checking, and rendering motion graphics.

Mitigation: Review the skill before installation, run it only in a constrained workspace without unrelated secrets, and pin or preinstall the HyperFrames CLI instead of relying on floating npx execution.

Risk: Asset sourcing or image generation can send user images to Gemini or other external providers.

Mitigation: Require explicit user consent before uploading images or using external providers, and use local or search-only fallbacks when consent or credentials are unavailable.

Risk: The workflow can perform global skill updates during normal use.

Mitigation: Avoid global skill updates during routine runs unless the user explicitly approves the update.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/motion-graphics)
- [Builder contract](artifact/references/builder-contract.md)
- [Motion vocabulary](artifact/references/motion-vocabulary.md)
- [Shot-plan IR](artifact/references/shot-plan-ir.md)
- [Locate protocol](artifact/grounding/PROTOCOL.md)
- [Source phase guide](artifact/phases/source/guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON shot plans, HTML/GSAP composition code, shell commands, project-local assets, proof snapshots, and rendered MP4 or transparent overlay files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rendering is user-gated; external image, search, and generation providers are optional and may be unavailable.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
