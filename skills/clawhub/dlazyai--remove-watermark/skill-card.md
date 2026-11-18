## Description:

Removes watermarks, text, logos, and promotional graphics from images, then reconstructs the covered areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and e-commerce content creators use it to prepare clean product images by removing overlays and rebuilding the hidden background.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious and reports that images may be sent to external services; its analysis was partial.

Mitigation: Avoid using sensitive images unless you understand and accept the external processing, and do not treat the partial scan as proof that all bundled content is safe.

Risk: Reconstruction may infer obscured content and slightly change other parts of the image.

Mitigation: Review the result, especially obscured product details, before using or publishing it.

Risk: Removing another party's copyright watermark or a required brand or legal mark can enable misuse or remove important information.

Mitigation: Use only images you are authorized to edit, and do not remove statutory, safety, or certification marks.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Model flags reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [Related fission-pattern workflow](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/fission-pattern/skill.md)
- [Related clothing-grass-planting workflow](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/clothing-grass-planting/skill.md)

## Skill Output:

**Output Type(s):** [Image files]

**Output Format:** [JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reconstructed areas are model-inferred and may alter covered details or slightly change the surrounding image.]

## Skill Version(s):

1.0.33 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
