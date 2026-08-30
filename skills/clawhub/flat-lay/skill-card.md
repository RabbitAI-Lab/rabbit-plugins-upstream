## Description:

Turns garment flat-lay and pose reference images into on-model ecommerce product photos while preserving garment style, color, material, texture, and fit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and developers use this skill to generate catalog-ready virtual try-on photos from garment and reference/model images, including single garments, coordinated outfits, and batch SKU workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided garment photos, reference/model images, and prompts are sent to configured cloud providers.

Mitigation: Use only images you have rights to process, avoid sensitive personal photos unless provider terms allow it, and review provider privacy terms before commercial use.

Risk: Generated virtual try-on images may alter appearance, fit, anatomy, colors, or garment details.

Mitigation: Review outputs for garment fidelity and acceptable model/reference use before publishing, and rerun with stricter prompt constraints when defects appear.

Risk: Image generation can consume provider credits and save generated outputs locally.

Mitigation: Use the dry-run and doctor options to verify provider configuration and estimated credits before paid generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/flat-lay)
- [dLazy](https://dlazy.com)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with bash commands and JSON-style command outputs; generated assets are saved as JPEG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-supplied garment and reference/model images; the flat-lay task defaults to 1024x1536 high-quality JPEG output.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
