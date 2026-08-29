## Description:

Transforms flat-lay garment photos into ghost-mannequin product images with realistic volume while preserving garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and agents use this skill to turn clear single-garment flat-lay photos into ghost-mannequin product images. It provides prompt guidance and runnable commands for volume, garment fidelity, aspect ratio, quality level, provider selection, and local output saving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected garment images are sent to dLazy or another configured cloud image provider.

Mitigation: Confirm the provider and data-sharing posture are acceptable before use, and avoid sending sensitive or restricted product imagery.

Risk: Untrusted image URLs could expose internal resources or pull unintended content into a provider request.

Mitigation: Use local image files or trusted HTTPS image URLs, and avoid internal or untrusted URLs as image references.

Risk: Generated assets are written to local paths selected by the user or default output paths.

Mitigation: Choose an explicit --save path and review generated files before publishing or reusing them.

Risk: Shared brand.yaml values can affect production visual identity and model reference behavior.

Mitigation: Review brand.yaml content, especially model descriptions and reference paths, before using it for production branding.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI Reference](artifact/references/provider-cli.md)
- [gpt-image-2 Model Flags](artifact/references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown with bash command examples and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompt templates and commands that send selected garment images to a configured image provider and save generated image files locally.]

## Skill Version(s):

1.0.1 (source: evidence.release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
