## Description:

Creates short, design-led, unnarrated motion graphics such as kinetic typography, stat count-ups, data-viz hits, logo stings, lower thirds, animated maps, web/news/tweet treatments, and asset-fusion shots, rendering to MP4 or a transparent overlay.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, content teams, and developers use this skill to turn a concise brief or supplied content into a short motion graphic. It can plan the shot, source or prepare assets when needed, compose a HyperFrames animation, run visual checks, and render only after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run mutable HyperFrames update or install commands through npx.

Mitigation: Use a sandboxed workspace, pin or pre-vet the HyperFrames CLI, and separately approve any global skill updates before installation.

Risk: Image localization can upload full images to Gemini when a Gemini or Google API key is present.

Mitigation: Unset GEMINI_API_KEY and GOOGLE_API_KEY when image upload is not intended, or explicitly approve image processing before using that path.

Risk: Webpage, news, tweet, and map workflows may perform networked processing of supplied or searched content.

Mitigation: Avoid sensitive content in networked workflows and review sourced assets before rendering or publishing the result.

Risk: Generated motion graphics may contain layout, timing, or readability issues if verification is skipped.

Mitigation: Run lint, check, and proof snapshots, inspect the contact sheet, and require explicit user approval before rendering.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/motion-graphics)
- [shot-plan-ir.md](references/shot-plan-ir.md)
- [builder-contract.md](references/builder-contract.md)
- [motion-vocabulary.md](references/motion-vocabulary.md)
- [grounding protocol](grounding/PROTOCOL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance, JSON shot plans, HTML/GSAP composition code, shell commands, proof snapshots, and rendered video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create project-local assets, HyperFrames configuration, contact-sheet snapshots, MP4 renders, or transparent WebM/MOV overlays.]

## Skill Version(s):

1.0.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
