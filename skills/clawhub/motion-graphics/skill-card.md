## Description:

Creates short, design-led motion graphics such as kinetic typography, animated charts, maps, logos, and social overlays for video or transparent-overlay export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan, assemble, check, and render brief, unnarrated motion graphics from supplied content or sourced assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned HyperFrames commands may fetch and run remote tooling with local shell access.

Mitigation: Use a pinned, reviewed HyperFrames version before running commands.

Risk: Setup or freshness checks may update installed skills.

Mitigation: Review and approve skill-update prompts before allowing changes.

Risk: Asset searches may use network services, and image generation may send images to Google when a Gemini key is configured.

Mitigation: Review assets and external-service use; leave Gemini keys unset unless third-party image inference is intended.

## Reference(s):

- [ClawHub motion-graphics release](https://clawhub.ai/heygen-com/skills/motion-graphics)
- [Shot plan schema](references/shot-plan-ir.md)
- [Motion vocabulary](references/motion-vocabulary.md)
- [Builder contract](references/builder-contract.md)

## Skill Output:

**Output Type(s):** [Video, Code, Configuration, Guidance]

**Output Format:** [MP4 video or transparent overlay, with an HTML composition and JSON shot plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rendering requires explicit user approval after checks and proof snapshots.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
