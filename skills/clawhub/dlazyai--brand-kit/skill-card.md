## Description:

店铺品牌视觉锁定。一份 brand.yaml 定义模特、色温、构图、留白与文案语气，所有生图技能读它，保证跨 SKU 视觉统一。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and developers use this skill to create and apply a reusable brand.yaml that keeps model identity, lighting, composition, margins, color treatment, and copy tone consistent across product image generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand, product, model, or reference images may be uploaded to the selected generation provider during generation.

Mitigation: Only use images that are approved for that provider, and run with --dry-run and --provider first to confirm destination and request shape.

Risk: Default brand.yaml values may unintentionally define the wrong model identity or visual style for a store.

Mitigation: Review and customize brand.yaml before running batch jobs, then test one SKU with and without the brand file before scaling.

Risk: Provider API keys can grant access to paid generation services.

Mitigation: Use scoped, revocable keys and rotate or revoke them if exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/brand-kit)
- [brand.yaml Field Reference](references/brand-schema.md)
- [Provider CLI Reference](references/provider-cli.md)
- [dLazy CLI Source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML configuration examples, shell commands, and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can append brand constraints to prompts, add model reference images when present, and route generation through the selected provider.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
