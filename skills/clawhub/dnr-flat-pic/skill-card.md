## Description:

Transform reference photographs and visually dense images into sparse, recognizable, high-saturation flat-vector-style illustrations through semantic compression rather than literal tracing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[createlafont](https://clawhub.ai/user/createlafont)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative operators use this skill to convert supplied reference images into simplified flat-color illustration outputs while preserving recognizable composition and identity anchors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may remove text, logos, UI elements, or watermarks from visual outputs.

Mitigation: Use appropriate source images and review generated outputs for rights, identity, and representation concerns before reuse.

Risk: Users may request editable SVG or true vector artwork even though the skill's normal image-generation output is not an editable vector file.

Mitigation: Disclose the limitation and use an SVG-capable workflow when editable vector output is required.

## Reference(s):

- [DnR FlatPic ClawHub listing](https://clawhub.ai/createlafont/skills/dnr-flat-pic)
- [Aspect-Ratio Adaptation and Square Icon Conversion](references/aspect-ratio-adaptation.md)
- [Calibration Examples and Failure Modes](references/examples-and-failures.md)
- [Canonical Rendering Contract](references/generation-spec.md)
- [Human-Perceived Semantic Complexity and Budget](references/semantic-complexity.md)

## Skill Output:

**Output Type(s):** [guidance, image artifacts]

**Output Format:** [Generated flat-vector-style image artifact, typically PNG, with minimal text unless the user asks for analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses supplied reference images; defaults to semantic complexity 6 out of 10 or lower, fixed-HSB solid fills, crisp boundaries, and no gradients or light-halo effects.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
