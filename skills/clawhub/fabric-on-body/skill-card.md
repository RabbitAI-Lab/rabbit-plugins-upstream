## Description:

一键替换服装面料 Fabric on Body helps an agent turn a garment style or pattern reference plus a fabric swatch into a visual preview of the same garment rendered in the new material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce apparel teams, designers, and production users use this skill to preview how a fixed garment silhouette, construction, and camera angle would look after replacing only the fabric. It supports faster fabric selection before physical sampling while documenting that the output is a visual preview, not a real material sample.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private garment images, fabric swatches, and prompts may be sent to the selected image-generation provider.

Mitigation: Use only images and prompts that are acceptable to upload to the selected provider, and review the provider data flow before execution.

Risk: ARK_BASE_URL can route prompts, images, and an Ark API key to an environment-configured endpoint.

Mitigation: Set ARK_BASE_URL only to a trusted HTTPS Ark-compatible endpoint you control, and prefer scoped, revocable API keys.

Risk: External or local CLI installation paths may be involved when running provider commands.

Mitigation: Review any npx or local CLI installation path before use, and use --dry-run to inspect requests when checking behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI Reference](artifact/references/provider-cli.md)
- [gpt-image-2 Model Flags](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples and saved image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typical generated assets are JPEG visual previews; dry-run mode can show request details before provider execution.]

## Skill Version(s):

1.0.9 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
