## Description:

Removes watermarks, text, logos, promotional badges, coupon strips, decorative frames, and stickers from an uploaded image and reconstructs the covered areas for cleaner product or marketing assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to clean watermarks, promotional text, price badges, coupon strips, logos, stickers, and decorative frames from product or marketing images before reuse or downstream image generation. It reconstructs covered areas with a hosted image-editing model, so results require human review when accuracy, rights, or pixel fidelity matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts are uploaded to dLazy for cloud processing.

Mitigation: Do not submit confidential, regulated, rights-sensitive, or third-party-owned material unless the user has permission and the processing is acceptable for the environment.

Risk: The skill depends on a hosted API and the dLazy CLI supply chain.

Mitigation: Review the pinned CLI or source before use in strict environments, keep API keys managed by the user, and rotate or revoke keys when access changes.

Risk: Watermark, logo, or text removal can be misused to obscure ownership, branding, or required labels.

Mitigation: Use only on images the user owns or is authorized to edit, and do not remove legal, safety, certification, ingredient, or required brand markings.

Risk: Reconstructed regions are inferred rather than pixel-exact repairs.

Mitigation: Review outputs manually for accuracy and use professional editing tools when exact preservation of original pixels is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy service homepage](https://dlazy.com)
- [dLazy CLI source reference](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces dLazy CLI invocations and prompts; generated image URLs or saved image files are returned by the external service.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
