## Description:

Removes watermarks, text, logos, badges, promotional frames, and similar overlays from images by generating image-editing prompts and commands that reconstruct the covered areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce operators use this skill to prepare cleaner product images or upstream inputs by removing visible text, watermarks, badges, coupon bars, and decorative frames. It is best suited for images where the removed areas can be plausibly reconstructed and the result can be reviewed before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input images may be uploaded to cloud image-generation providers for processing.

Mitigation: Use the dry-run flow first, choose the provider deliberately, and avoid copyrighted, confidential, regulated, or personal images unless the user has permission and accepts the provider's handling of uploaded media.

Risk: Removed regions are reconstructed by a model and may not preserve the original pixels, perspective, texture, or product details exactly.

Mitigation: Review saved outputs before use, especially where overlays cover product details; use professional image-editing tools when strict pixel fidelity is required.

Risk: The workflow could be misused to remove copyright watermarks, brand identifiers, or required legal markings.

Mitigation: Use only on images the user is authorized to edit, and do not use it to misrepresent ownership, product origin, certifications, warnings, ingredients, or other required labels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [gpt-image-2 model flags](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a cloud image-editing workflow; saved outputs should be reviewed because reconstructed regions are model-generated.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
