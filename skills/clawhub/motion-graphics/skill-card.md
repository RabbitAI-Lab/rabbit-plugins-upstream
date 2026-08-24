## Description:

Creates short, design-led, unnarrated motion graphics such as kinetic typography, stat count-ups, charts, logo reveals, lower-thirds, animated maps, social/news/webpage overlays, and asset-fusion shots that render to MP4 or transparent overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to plan, source assets for, build, verify, and render short HyperFrames motion graphics from supplied content or search-resolved assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Networked asset sourcing and the optional Gemini-backed locate path may send images or prompts to external services when ambient credentials are present.

Mitigation: Use supplied or local assets for sensitive material, avoid or unset Gemini credentials when external image handling is not acceptable, and review the generated asset ledger before rendering.

Risk: Map baking uses headless Chrome without its normal sandbox while loading third-party map and CDN resources.

Mitigation: Run map baking in a contained environment, verify third-party resource availability and terms before release, and use the baked local output for deterministic rendering.

Risk: The security verdict requires review before deployment.

Mitigation: Review and scan the skill before deployment, with particular attention to networked asset sourcing, browser execution, and handling of sensitive input media.

## Reference(s):

- [Shot-plan IR](references/shot-plan-ir.md)
- [Builder Contract](references/builder-contract.md)
- [Motion Vocabulary](references/motion-vocabulary.md)
- [Asset Source Phase Guide](phases/source/guide.md)
- [Grounding Protocol](grounding/PROTOCOL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, JSON shot plans, HTML/CSS/JavaScript compositions, shell commands, proof snapshots, and MP4/WebM/MOV render files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-local artifacts are written under videos/<project-name>; rendering follows lint, check, and snapshot gates and requires explicit user approval.]

## Skill Version(s):

1.0.15 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
