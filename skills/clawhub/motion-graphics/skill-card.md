## Description:

Motion Graphics creates short, design-led, unnarrated motion graphics such as kinetic typography, data-viz hits, logo reveals, overlays, animated maps, source-driven article or tweet animations, webpage/UI animation, and asset-fusion shots, rendering to MP4 or transparent overlay.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to plan, source, build, verify, and render short motion graphics in a HyperFrames project. It is suited for compact brand, social, data, map, UI, news, tweet, and asset-fusion animations where motion carries the message.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable network tooling and skill updates can change behavior between reviews.

Mitigation: Use a pinned or locally vetted HyperFrames CLI and review any skill updates before relying on them.

Risk: Image localization or asset processing may send images to Google when a detector key such as `GEMINI_API_KEY` is available.

Mitigation: Do not process sensitive or private images with those keys enabled unless that data sharing is acceptable.

Risk: Map baking and preview servers execute local tooling that may touch network or workspace resources.

Mitigation: Run these steps in a constrained workspace or container and review outputs before rendering.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/motion-graphics)
- [Shot Plan IR](artifact/references/shot-plan-ir.md)
- [Builder Contract](artifact/references/builder-contract.md)
- [Motion Vocabulary](artifact/references/motion-vocabulary.md)
- [Asset Sourcing Guide](artifact/phases/source/guide.md)
- [Locate Protocol](artifact/grounding/PROTOCOL.md)
- [Director to Catalog Block Map](artifact/catalog-map.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files]

**Output Format:** [Markdown instructions with bash commands plus project files such as JSON shot plans, HTML/CSS/JavaScript compositions, asset ledgers, snapshots, and MP4/WebM/MOV renders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces deterministic HyperFrames compositions with proof snapshots before user-approved rendering; transparent overlay export is supported.]

## Skill Version(s):

1.0.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
