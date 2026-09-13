## Description:

Helps agents turn clothing photos, street shots, buyer photos, or competitor screenshots into clean white-background e-commerce flat-lay product images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, merchandising teams, and developers use this skill to draft prompts and commands that extract individual garments or accessories from source photos into clean flat-lay product assets for catalog workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos and prompts may be sent to a selected cloud provider.

Mitigation: Use the skill only with photos and prompts you are permitted to upload, and use revocable API keys with limited account scope.

Risk: Untrusted image URLs or custom provider endpoints can expand data-flow and endpoint trust risk.

Mitigation: Prefer trusted local images or trusted URLs, and set ARK_BASE_URL only for endpoints you fully control and trust.

Risk: Occluded garment areas are reconstructed by inference and may not exactly match the original product.

Mitigation: Review generated flat-lay images against the source photo before using them in commercial listings or downstream catalog workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [Related flat-lay skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/flat-lay/skill.md)
- [Related to-3d skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/to-3d/skill.md)
- [Related fabric-on-body skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/fabric-on-body/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, image files]

**Output Format:** [Markdown guidance with prompt templates and shell command examples; generated artifacts are saved image files from the selected provider or CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default task settings use a 1024x1024 image size with high quality, usually saving JPEG or PNG outputs; batch generation can be used when occlusion reconstruction needs review choices.]

## Skill Version(s):

1.0.8 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
