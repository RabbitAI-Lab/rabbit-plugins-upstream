## Description:

Guides extraction of clean, white-background flat-lay product images from photos of worn or displayed clothing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and content creators use this skill to prepare flat-lay garment images from model photos, street photos, or customer images for product listings and visual workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos, prompts, and generated images are sent to the configured image provider.

Mitigation: Review provider terms before sending private or sensitive photos, and use --dry-run to inspect requests first.

Risk: The shared runner supports additional ecommerce workflows beyond clothing extraction.

Mitigation: Invoke the documented clothing-extraction task unless other workflows are intentionally needed.

Risk: Hidden garment details are inferred and may not match the source product.

Mitigation: Inspect generated details against the original photo and manually confirm or correct obscured areas before use.

## Reference(s):

- [Clothing Extraction on ClawHub](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider and CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and output image paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated flat-lay images locally; obscured garment details require visual review.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
