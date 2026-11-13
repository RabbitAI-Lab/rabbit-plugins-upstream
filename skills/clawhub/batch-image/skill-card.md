## Description:

多商品批量生图流水线。商品清单 CSV → 整批统一视觉的商拍图，带并发、重试、断点续跑、成本熔断与挑图联系表。当用户说「批量生图」「一批商品」「跑整个 SKU 表」「几百个商品出图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员和开发者可用它按商品清单批量生成视觉统一的商品图片，并管理运行进度、失败重试和结果挑选。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the advertised image-generation workflow and some implemented behavior, and its analysis is partial.

Mitigation: Review the relevant commands and scripts, then run a small test batch and inspect its outputs before scaling up.

Risk: The security review flags cost-control concerns and possible unexpected charges.

Mitigation: Use dry-run estimates, confirm the selected provider/model and batch settings, and set a maximum credit budget before starting a large run.

Risk: Prompts and images may be processed by an external image-generation provider.

Mitigation: Check the selected provider's data handling and submit only prompts and images you are authorized to send.

## Reference(s):

- [Provider CLI reference](artifact/references/provider-cli.md)
- [Model flags reference](artifact/references/model-flags.md)
- [Platform specifications](artifact/references/platform-specs.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Markdown workflow guidance and shell command examples; generated product images, CSV run reports, and optional contact sheets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch results are organized by SKU; a contact sheet can support manual image selection.]

## Skill Version(s):

1.0.32 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
