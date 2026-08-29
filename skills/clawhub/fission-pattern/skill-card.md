## Description:

Creates a coordinated set of ecommerce product images from one product photo and selling points, covering multiple angles, scenes, and detail shots while preserving product identity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and developers use this skill to turn a single product photo plus selling points into a consistent set of product, lifestyle, macro, and comparison images for listings or detail pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, brand files, and model references may be sent to the selected cloud image-generation provider.

Mitigation: Use --dry-run or --doctor to confirm routing, set an explicit provider when needed, and avoid private URLs or sensitive local image inputs.

Risk: The example brand profile may not match the user's actual store identity or privacy expectations.

Mitigation: Customize brand.yaml before use and avoid reusing default model references or brand constraints unchanged.

Risk: Generated ecommerce imagery can drift from the real product or imply unsupported product claims.

Mitigation: Keep the product-fidelity prompt segment consistent across the set, avoid inventing features or promotional text, and review the complete image set before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples and JSON-capable CLI output; generated assets are saved as image files through the selected provider.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typical generated files are ecommerce product images, commonly JPEG, with provider, model, size, quality, and save-path options.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
