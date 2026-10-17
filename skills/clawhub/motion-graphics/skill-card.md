## Description:

Creates short, design-led motion graphics such as kinetic typography, animated charts, maps, and overlays, with user approval before rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan, build, preview, and render short, unnarrated motion graphics from supplied content or sourced assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can execute current external tooling and update related skills.

Mitigation: Review and pin the tooling version before running it; approve skill updates explicitly.

Risk: Asset sourcing and rendering can use network-backed services.

Mitigation: Use only assets approved for external processing and review sources before rendering.

Risk: Optional cloud image localization may send images to Gemini when an API key is available.

Mitigation: Avoid the cloud detector path for private or sensitive images; use the local alternative.

## Reference(s):

- [Motion Graphics on ClawHub](https://clawhub.ai/heygen-com/skills/motion-graphics)
- [Motion Vocabulary](artifact/references/motion-vocabulary.md)
- [Shot Plan](artifact/references/shot-plan-ir.md)
- [Builder Contract](artifact/references/builder-contract.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance, Files]

**Output Format:** [HTML/JavaScript composition and rendered video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Renders MP4 or a transparent WebM/MOV overlay after user approval.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
