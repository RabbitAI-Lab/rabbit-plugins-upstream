## Description:

一张商品图裂变成整套素材。商品图 + 卖点 → 多角度多场景成套图，够铺满一屏。当用户说「裂变套图」「一张变一屏」「凑够详情页」「出一套图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce teams use this skill to turn one product image plus selling points into a consistent set of product, lifestyle, detail, and comparison images for listings or detail pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and optional brand reference images are uploaded to dLazy or the selected third-party generation provider.

Mitigation: Install only when this data sharing is acceptable, review configured provider credentials, and use dry runs to inspect requests before paid generation.

Risk: Generated ecommerce images can drift from the real product or imply unsupported product qualities.

Mitigation: Review the full output set before publication, keep the product-faithfulness prompt segment consistent, and avoid inventing selling points not present in the source evidence.

Risk: Paid generation can consume provider credits and write image files to local paths.

Mitigation: Use explicit save paths and dry-run cost checks before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with bash commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are saved JPEG image files when generation is executed; dry runs report request details and estimated credits.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
