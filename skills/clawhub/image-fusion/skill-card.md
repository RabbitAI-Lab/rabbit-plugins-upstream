## Description:

多单品搭配融图 Image Fusion helps agents turn up to 8 product images into one full outfit image on a single model while preserving each item's color, material, pattern, and details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce teams and agents use this skill to prepare prompts and generation commands that combine multiple apparel and accessory reference images into consistent outfit product photography. It is intended for catalog and storefront image production workflows, with user review of generated results before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand YAML files can cause unintended local files to be included in provider uploads.

Mitigation: Use only trusted brand YAML files, review referenced image paths before execution, and use dry-run mode to inspect the final image list before paid cloud calls.

Risk: The security evidence flags the YAML parser as needing stronger rejection of prototype-related keys.

Mitigation: Avoid third-party brand files until the parser rejects __proto__, constructor, and prototype keys and confirms uploaded files explicitly.

Risk: Generated model imagery may be misused for unauthorized likeness or endorsement claims.

Mitigation: Use only authorized model references and review outputs for consent, likeness, watermark, and platform compliance before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider CLI Reference](references/provider-cli.md)
- [seedream-5.0 Model Flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, image files, guidance]

**Output Format:** [Markdown guidance with bash command examples, optional JSON dry-run output, and saved image files when generation commands are executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports provider selection, brand YAML configuration, local or URL image inputs, dry-run cost inspection, batch generation, and saved output paths.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
