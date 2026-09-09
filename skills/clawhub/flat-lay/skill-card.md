## Description:

Turns flat-lay garment photos and pose references into on-model e-commerce product images while preserving garment color, texture, print, and fit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, merchandisers, and creative operators use this skill to generate catalog-ready model photos from flat-lay garment images and pose references. It supports single garments, separated top and bottom looks, and optional fixed-model references for consistent SKU imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted image paths, URLs, or brand files may cause unintended files or remote resources to be read and sent to an image-generation provider.

Mitigation: Use local image files you selected yourself, avoid internal or sensitive URLs, review brand configuration before use, and run --dry-run before paid generation.

Risk: Provider endpoint and environment-variable configuration can route API keys and generation inputs to unintended services.

Mitigation: Set provider credentials only for services you trust, avoid ARK_BASE_URL unless the endpoint is intentional and trusted, and rotate exposed keys if configuration is uncertain.

Risk: Generated on-model images may alter garment details, anatomy, faces, or commercial context in ways that are not immediately obvious.

Mitigation: Quality-check outputs for color, texture, logo placement, anatomy, and identity consistency before publishing, and do not use the skill to imply unauthorized personal endorsement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/flat-lay)
- [gpt-image-2 parameter list](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generated JPEG image files when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses image-generation provider credentials and may save generated assets to a local output path.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
