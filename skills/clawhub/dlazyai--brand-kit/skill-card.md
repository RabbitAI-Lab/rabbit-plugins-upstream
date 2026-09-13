## Description:

店铺视觉统一 Brand Kit helps ecommerce agents apply a reusable brand.yaml specification for model identity, color temperature, composition, spacing, copy tone, and forbidden elements so image generation stays visually consistent across SKUs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and agent developers use this skill to create or apply a shared brand.yaml visual standard before generating product imagery in batches. It helps keep model identity, lighting, layout, tone, and forbidden visual elements consistent across many SKUs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A provider endpoint setting can redirect API keys and private image inputs.

Mitigation: Install only in a trusted runtime, use dedicated low-scope provider keys, and set ARK_BASE_URL only to a controlled HTTPS endpoint.

Risk: Local reference images may contain sensitive content and can be sent to the configured image provider.

Mitigation: Avoid passing sensitive files through --images or model.reference, and confirm the configured provider is appropriate for the data.

Risk: Watermark-removal behavior can be misused on images the user is not authorized to edit.

Mitigation: Use removal tasks only for images the user owns or has permission to modify.

## Reference(s):

- [brand.yaml field reference](references/brand-schema.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/brand-kit)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands; optional JSON dry-run/status output and saved generated media files when the helper script is executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use configured image providers and local reference images; output paths and generated media depend on provider response and --save options.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
