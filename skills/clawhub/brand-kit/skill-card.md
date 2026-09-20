## Description:

店铺品牌视觉锁定。一份 brand.yaml 定义模特、色温、构图、留白与文案语气，所有生图技能读它，保证跨 SKU 视觉统一。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ecommerce operators use this skill to create and reuse a brand.yaml visual standard so product image generation keeps a consistent model, lighting, composition, layout, and store tone across many SKUs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product images, and face reference images may be sent to the configured generation provider.

Mitigation: Treat those inputs as sensitive, choose the provider and credentials deliberately, and keep face reference files out of shared repositories unless consent and retention expectations are clear.

Risk: Generation requests can spend provider credits or use the wrong backend if credentials are configured unexpectedly.

Mitigation: Run --dry-run or --doctor before paid generation to review the selected provider, request shape, referenced images, and estimated credits.

Risk: Brand constraints can conflict with a task prompt or use an unavailable face reference, reducing visual consistency.

Mitigation: Preview the appended brand prompt for one SKU first, resolve conflicting style fields, and confirm referenced face images exist before batch generation.

## Reference(s):

- [brand.yaml field reference](references/brand-schema.md)
- [Provider CLI reference](references/provider-cli.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/brand-kit)

## Skill Output:

**Output Type(s):** [configuration, shell commands, code, guidance]

**Output Format:** [Markdown guidance with YAML configuration and shell command examples; optional JSON from helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can generate a brand.yaml template, append brand constraints to prompts, add model reference images when present, and save generated outputs through the selected provider.]

## Skill Version(s):

1.0.9 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
