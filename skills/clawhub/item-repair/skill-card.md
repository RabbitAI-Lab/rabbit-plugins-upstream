## Description:

Retouches casual product photos into listing-ready images by reducing wrinkles, straightening composition, evening lighting, and cleaning backgrounds while preserving product style and color.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, merchandisers, and agents use this skill to prepare product photos for catalog listings by generating retouching prompts and commands that preserve product identity while improving layout, lighting, wrinkles, and background cleanliness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product photos and prompts may be sent to the configured image provider.

Mitigation: Use only trusted local image files or trusted image URLs, avoid sensitive product imagery unless provider handling is acceptable, and review dry-run payloads before execution.

Risk: Unrestricted image paths, image URLs, or a custom Ark endpoint could expose local data, API keys, or image content if misused.

Mitigation: Do not run the skill on untrusted requests that supply file paths or URLs, and set ARK_BASE_URL only when the endpoint is intentionally trusted.

Risk: Retouching may accidentally obscure product defects or alter product structure, color, or styling.

Mitigation: Compare source and output images before use, preserve real defects that must remain visible, and include explicit prompts to keep structure, color, hardware, and intentional folds unchanged.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Parameter Reference](references/model-flags.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/item-repair)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and saved image-file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run previews, configurable image providers, batch generation, and saved JPEG image outputs.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
