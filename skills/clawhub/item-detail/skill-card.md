## Description:

生成带中文排版的详情页模块。商品图 + 卖点 → 可直接上架的详情页图文模块。当用户说「详情页」「做详情图」「商品描述图」「详情页模块」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and agents use this skill to turn a product image and short selling points into Chinese product detail page modules, including banners, feature icon rows, material blocks, detail closeups, and parameter blocks. It is intended for controlled product marketing workflows where claims and generated Chinese text are reviewed before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Non-dry-run generation sends prompts and selected product images to the configured image provider.

Mitigation: Use --dry-run to inspect the request first, avoid confidential or unapproved product photos, and use only approved provider credentials for the workflow.

Risk: Generated Chinese text, product appearance, or marketing claims may be inaccurate or unsupported.

Mitigation: Keep copy short, include only verified selling points, preserve product fidelity in prompts, and review every generated module before publishing.

Risk: Generated assets are saved locally and may be misplaced if paths are not controlled.

Mitigation: Set --save explicitly to a reviewed output location and inspect saved files before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands and generated image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses product images and short Chinese copy to produce local e-commerce detail image modules; output paths are controlled with --save.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
