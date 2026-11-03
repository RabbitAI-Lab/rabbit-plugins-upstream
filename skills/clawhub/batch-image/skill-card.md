## Description:

从商品清单批量生成视觉统一的商拍图，并提供并发、重试、断点续跑、成本熔断与挑图联系表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商运营者和商品内容制作人员，用商品清单批量生成视觉统一的商拍图片，并汇总生成状态以便挑选和复核。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Imported product-list text can execute local commands through the documented workflow.

Mitigation: Fix and review CSV-to-shell dispatch before using imported lists, and begin with a small batch.

Risk: Advertised spending safeguards are incomplete, and the external CLI and live services were not validated.

Mitigation: Enforce spending limits at the provider, use a separate output directory, validate the selected backend and quality-check path with a small batch, treat checker errors as failures, and upload only approved materials.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [Platform specifications](references/platform-specs.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Product images, JSON batch manifest, HTML contact sheet, Shell commands]

**Output Format:** [Generated image files, a JSON batch report, optional HTML contact sheet, and Markdown guidance with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One image per SKU; optional resumable batch state and contact sheet.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
