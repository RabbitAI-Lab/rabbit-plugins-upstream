## Description:

Creates short, design-led, unnarrated motion graphics such as kinetic typography, data-viz hits, logo reveals, overlays, maps, social/news/webpage animations, and asset-fusion shots that render to MP4 or transparent overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to produce short motion-graphic video assets, including typography, charts, logo stings, overlays, maps, web/news/tweet animations, and image-based asset-fusion shots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs the agent to silently update installed skills before use, which can change agent behavior without user approval.

Mitigation: Require explicit approval for skill or dependency updates, pin the reviewed version, and rescan before routine use.

Risk: The workflow may run HyperFrames commands, search or capture external content, copy selected assets into local video projects, and optionally send images to Gemini when that path is enabled.

Mitigation: Use approved content sources, review asset provenance before rendering, and leave optional image-provider keys unset unless that data flow is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/motion-graphics)
- [Builder contract](artifact/references/builder-contract.md)
- [Motion vocabulary](artifact/references/motion-vocabulary.md)
- [Shot-plan IR](artifact/references/shot-plan-ir.md)
- [Asset localization protocol](artifact/grounding/PROTOCOL.md)
- [Director to catalog block map](artifact/catalog-map.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown instructions with JSON plans, HTML/GSAP composition code, shell commands, project files, snapshots, and rendered media outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project-local HyperFrames assets and can render MP4, WebM, or MOV after explicit user approval.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
