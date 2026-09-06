## Description:

Removes watermarks, text, logos, badges, promotional frames, and similar overlays from images, then reconstructs the covered image areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare cleaner product or source images by removing visible text, watermarks, badges, coupons, logos, and decorative overlays before downstream image generation or editing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be used to remove copyright watermarks, platform marks, brand identifiers, legal warnings, certifications, ingredient labels, or other required text.

Mitigation: Use only on images the user owns or is authorized to edit, and do not use it to remove ownership marks, required disclosures, legal labels, or safety-critical markings.

Risk: Image content is sent to cloud providers during editing.

Mitigation: Avoid confidential, sensitive, or regulated images unless the selected provider's data handling terms are acceptable.

Risk: Covered areas are reconstructed by an image model and may not preserve original pixels, perspective, product details, or textures exactly.

Mitigation: Review outputs manually, use batch outputs when helpful, and use professional image-editing tools when pixel-level fidelity is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Parameter Reference](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline bash commands and image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces edited image files through cloud image-editing providers; reconstructed regions are model-inferred and require visual review.]

## Skill Version(s):

1.0.5 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
