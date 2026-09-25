## Description:

店铺品牌视觉锁定。一份 brand.yaml 定义模特、色温、构图、留白与文案语气，所有生图技能读它，保证跨 SKU 视觉统一。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agent builders use this skill to create and reuse a brand.yaml visual style guide so product image generation remains consistent across many SKUs. Agents can use it to generate the brand template, append style constraints to image prompts, and route generation through supported providers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running generation scripts can send prompts and selected local images to the configured external provider.

Mitigation: Use --dry-run first, confirm the selected provider and credentials, and only supply prompts or images that are appropriate to share with that provider.

Risk: Default brand examples include model identity and representation choices that may not match the user's brand or consent requirements.

Mitigation: Edit brand.yaml before batch generation, especially model.reference, model.description, and forbid entries, and review one SKU before applying the style to a full batch.

Risk: Generation calls may consume paid provider credits or fail because credentials are missing or insufficient.

Mitigation: Use the doctor and dry-run modes to verify credentials, provider selection, estimated credits, and request shape before running paid generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/brand-kit)
- [brand.yaml field guide](references/brand-schema.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML examples and inline shell commands; scripts can emit JSON status or save generated media files when invoked.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a brand.yaml file to append prompt constraints and, when configured, an additional model reference image; dry-run mode previews provider requests before external calls.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
