## Description:

Helps agents retouch product photos into listing-ready images by reducing random wrinkles, improving symmetry and lighting, preserving product attributes, and producing clean catalog-style outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams and developers use this skill to guide product-photo retouching workflows for catalog listings. It provides prompts, command patterns, and configuration guidance for editing one to four same-product images while preserving style, color, structure, and visible defects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to dLazy or configured third-party AI providers.

Mitigation: Use the skill only with images and prompts appropriate for those providers, and review provider terms and data-handling requirements before execution.

Risk: The bundled generator can fetch image inputs from arbitrary URLs.

Mitigation: Use vetted local files or trusted image URLs, and avoid untrusted or attacker-controlled URLs.

Risk: Provider credentials may be exposed in shared or attacker-controlled environments.

Mitigation: Keep API keys in trusted local configuration or environment variables, avoid shared shells, and rotate or revoke keys if exposure is suspected.

Risk: Changing provider endpoints can route requests to unintended services.

Mitigation: Do not override ARK_BASE_URL unless the endpoint is trusted and expected for the deployment.

Risk: Paid image generation can consume credits unexpectedly.

Mitigation: Run dry-run checks before paid generation and review estimated cost, provider, model, and batch count.

Risk: Retouching can misrepresent a product by removing real defects or changing structure.

Mitigation: Preserve style, color, hardware, structure, and visible damage in prompts, then compare outputs against source images before listing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples and generated image files when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost checks, JSON-capable CLI output, local save paths, and batch generation.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
