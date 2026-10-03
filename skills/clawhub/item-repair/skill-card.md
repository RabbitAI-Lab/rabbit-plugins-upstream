## Description:

Retouches product photos for listings by smoothing incidental wrinkles, balancing lighting, and cleaning backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to prepare product photos for listings, removing incidental creases and improving lighting and backgrounds without changing the product itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts may be sent to an external AI provider for processing.

Mitigation: Use only images approved for cloud processing, confirm the selected provider, and inspect requests with --dry-run before generating.

Risk: Retouching can inadvertently alter product details or conceal defects in listing images.

Mitigation: Compare outputs against the source and reject changes to construction, color, hardware, intentional folds, or actual damage.

## Reference(s):

- [Item Repair release on ClawHub](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Text or Markdown instructions and commands; saved product images when generation is run]

**Output Parameters:** [1D for agent responses; image files for generated assets]

**Other Properties Related to Output:** [Supports one to four product views and optional local output paths.]

## Skill Version(s):

1.0.16 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
