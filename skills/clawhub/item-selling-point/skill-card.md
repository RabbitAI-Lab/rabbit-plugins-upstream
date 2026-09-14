## Description:

Generates conversion-focused ecommerce main product images with readable Chinese selling-point copy from a product image and concise feature or promotion inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agents use this skill to turn one product image plus concise feature and promotion points into a square or vertical main listing image with readable Chinese copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, generated outputs, or API keys may be sent to the selected external provider or an unsafe endpoint.

Mitigation: Use only trusted providers and HTTPS endpoints, avoid setting ARK_BASE_URL unless it is controlled and trusted, and use separate revocable API keys.

Risk: The helper can fetch arbitrary image URLs without safety limits.

Mitigation: Use local files or trusted image URLs, avoid running in network environments with access to internal services or cloud metadata, and review output paths before saving files.

Risk: Generated ecommerce copy can contain unsupported product claims, fake promotions, or absolute wording if inputs are not verified.

Mitigation: Verify product features and promotion terms before generation, avoid absolute claims, and review generated copy before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro model flags](references/model-flags.md)
- [dLazy provider information](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands; executed helpers can save image files or return JSON status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses product images and optional layout references; default item-selling-point generation uses seedream-5.0-pro at 1:1 and 2k resolution, with batch output saved to user-selected paths.]

## Skill Version(s):

1.0.9 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
